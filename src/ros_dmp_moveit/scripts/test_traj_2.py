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
    """MoveGroupPythonInterfaceTutorial"""

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

    def go_to_joint_state(self):
        global joint_goal
        move_group = self.move_group
        # get joint angle from traj file
        df = pd.read_csv('/home/chionn/fyp_ws/src/ros_dmp_moveit/pydmps-test/examples/traj_files/draw_2.traj',header=None)
        df = df.loc[0:1249,0:5]

        joint_goal = move_group.get_current_joint_values()
        joint_goal[0],joint_goal[1],joint_goal[2],joint_goal[3],joint_goal[4],joint_goal[5] = df.iloc[0]

        move_group.go(joint_goal, wait=True)
        print('read final pos')
        for i in range(0,len(df),5):
            print('qwe')
            joint_goal[0],joint_goal[1],joint_goal[2],joint_goal[3],joint_goal[4],joint_goal[5] = df.iloc[i]
            move_group.go(joint_goal, wait=True)

        # joint_goal[0],joint_goal[1],joint_goal[2],joint_goal[3],joint_goal[4],joint_goal[5] = 0.551098,0.010168,-1.136722,-0.026116,0.862260,0.420633
        # move_group.go(joint_goal, wait=True)
        # joint_goal[0],joint_goal[1],joint_goal[2],joint_goal[3],joint_goal[4],joint_goal[5] = -0.416215,-1.028408,-0.340022,-0.487066,1.032515,0.420468
        # move_group.go(joint_goal, wait=True)

        move_group.stop()

        ## END_SUB_TUTORIAL

        # For testing:
        current_joints = move_group.get_current_joint_values()
        return all_close(joint_goal, current_joints, 0.01)

    def go_to_pose_goal(self,px,py,pz):
        move_group = self.move_group

        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.orientation.x = -0.9388040580269565
        pose_goal.orientation.y = -0.23971834990313626
        pose_goal.orientation.z = -0.23966499133622135
        pose_goal.orientation.w = 0.06117798034951591
        pose_goal.position.x = px
        pose_goal.position.y = py
        pose_goal.position.z = pz

        move_group.set_pose_target(pose_goal)
        success = move_group.go(wait=True)
        move_group.stop()
        move_group.clear_pose_targets()

        # For testing:
        # Note that since this section of code will not be included in the tutorials
        # we use the class variable rather than the copied state variable
        current_pose = self.move_group.get_current_pose().pose
        return all_close(pose_goal, current_pose, 0.01)  

def main():
    try:
        # Setting up MoveitCommander
        myrobot = initiate_robot()
        input("============ Press `Enter` to execute a movement using a pose goal ...")
        # myrobot.go_to_pose_goal(0.2969906358809285,0.16222601608747705,0.07924469529761477)  
        myrobot.go_to_joint_state()

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()