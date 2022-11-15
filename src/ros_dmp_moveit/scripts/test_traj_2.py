#!/usr/bin/env python

# Python 2/3 compatibility imports
from __future__ import print_function
from six.moves import input

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from geometry_msgs.msg import Pose, PoseStamped

import pandas as pd

try:
    from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt

    tau = 2.0 * pi

    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))


from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

def all_close(goal, actual, tolerance):
    """
    Convenience method for testing if the values in two lists are within a tolerance of each other.
    For Pose and PoseStamped inputs, the angle between the two quaternions is compared (the angle
    between the identical orientations q and -q is calculated correctly).
    @param: goal       A list of floats, a Pose or a PoseStamped
    @param: actual     A list of floats, a Pose or a PoseStamped
    @param: tolerance  A float
    @returns: bool
    """
    if type(goal) is list:
        for index in range(len(goal)):
            if abs(actual[index] - goal[index]) > tolerance:
                return False

    elif type(goal) is geometry_msgs.msg.PoseStamped:
        return all_close(goal.pose, actual.pose, tolerance)

    elif type(goal) is geometry_msgs.msg.Pose:
        x0, y0, z0, qx0, qy0, qz0, qw0 = pose_to_list(actual)
        x1, y1, z1, qx1, qy1, qz1, qw1 = pose_to_list(goal)
        # Euclidean distance
        d = dist((x1, y1, z1), (x0, y0, z0))
        # phi = angle between orientations
        cos_phi_half = fabs(qx0 * qx1 + qy0 * qy1 + qz0 * qz1 + qw0 * qw1)
        return d <= tolerance and cos_phi_half >= cos(tolerance / 2.0)

    return True


class initiate_robot(object):
    def __init__(self):
        super(initiate_robot, self).__init__()
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node("move_group_python_interface_tutorial", anonymous=True)
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        group_name = "xarm6"
        move_group = moveit_commander.MoveGroupCommander(group_name, wait_for_servers=50.0)
        display_trajectory_publisher = rospy.Publisher(
            "/move_group/display_planned_path",
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=20,)

        planning_frame = move_group.get_planning_frame()
        print("============ Planning frame: %s" % planning_frame)
        eef_link = move_group.get_end_effector_link()
        print("============ End effector link: %s" % eef_link)
        group_names = robot.get_group_names()
        print("============ Available Planning Groups:", robot.get_group_names())
        print("============ Printing robot state")
        print(robot.get_current_state())
        print("")

        # Misc variables
        self.box_name = ""
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names

    def plan_cartesian_path(self):
        move_group = self.move_group
        df = pd.read_csv('/home/chionn/fyp_ws/draw_2_pose.csv',header=None)
        #df = df.iloc[0:3,0:7]
        pose_list = []
        for rows in range(df.shape[0]): 
            pose_temp = Pose()
            pose_temp.position.x,pose_temp.position.y,pose_temp.position.z = df.iloc[rows,0],df.iloc[rows,1],df.iloc[rows,2]
            pose_temp.orientation.x,pose_temp.orientation.y,pose_temp.orientation.z,pose_temp.orientation.w = df.iloc[rows,3],df.iloc[rows,4],df.iloc[rows,5],df.iloc[rows,6]
            pose_list.append(pose_temp)

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0,
        # ignoring the check for infeasible jumps in joint space, which is sufficient
        # for this tutorial.
        (plan, fraction) = move_group.compute_cartesian_path(
            pose_list, 0.01, 0.0  # waypoints to follow  # eef_step
        )  # jump_threshold
        # Note: We are just planning, not asking move_group to actually move the robot yet:
        return plan, fraction

    def execute_plan(self, plan):
        move_group = self.move_group
        move_group.execute(plan, wait=True)

def main():
    try:
        # Setting up MoveitCommander
        myrobot = initiate_robot()
        cartesian_plan, fraction = myrobot.plan_cartesian_path()
        myrobot.execute_plan(cartesian_plan)

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()