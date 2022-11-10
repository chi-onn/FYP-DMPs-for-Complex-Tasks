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
from moveit_msgs.msg import (
    RobotTrajectory,
    Grasp,
    PlaceLocation,
    Constraints,
    RobotState,
)
from moveit_msgs.msg import (
    MoveItErrorCodes,
    TrajectoryConstraints,
    PlannerInterfaceDescription,
    MotionPlanRequest,
)
from sensor_msgs.msg import JointState

try:
    from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt

    tau = 2.0 * pi

    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))


from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

class read_robot_mind(object):
    def __init__(self):
        super(read_robot_mind, self).__init__()
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node("move_group_python_interface_tutorial", anonymous=True)
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        group_name = "xarm6"
        move_group = moveit_commander.MoveGroupCommander(group_name)
        display_trajectory_publisher = rospy.Publisher(
            "/move_group/display_planned_path",
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=20,
        )

        planning_frame = move_group.get_planning_frame()
        print("============ Planning frame: %s" % planning_frame)
        eef_link = move_group.get_end_effector_link()
        print("============ End effector link: %s" % eef_link)
        group_names = robot.get_group_names()
        print("============ Available Planning Groups:", robot.get_group_names())
        print("============ Printing robot state")
        #print(robot.get_current_state())
        #print("")

        # Misc variables
        self.box_name = ""
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names

        state = robot.get_current_state()
        move_group.set_start_state(state)
    
    def give_me_pose(self):
        current_pose = self.move_group.get_current_pose()
        print(current_pose)

    def plan(self, joints=None):
        """Return a tuple of the motion planning results such as
        (success flag : boolean, trajectory message : RobotTrajectory,
         planning time : float, error code : MoveitErrorCodes)"""
        if type(joints) is JointState:
            self.set_joint_value_target(joints)

        elif type(joints) is Pose:
            self.set_pose_target(joints)

        elif joints is not None:
            try:
                self.set_joint_value_target(self.get_remembered_joint_values()[joints])
            except MoveItCommanderException:
                self.set_joint_value_target(joints)

        (error_code_msg, trajectory_msg, planning_time) = self._g.plan()

        error_code = MoveItErrorCodes()
        error_code.deserialize(error_code_msg)
        plan = RobotTrajectory()
        return (
            error_code.val == MoveItErrorCodes.SUCCESS,
            plan.deserialize(trajectory_msg),
            planning_time,
            error_code,
        )

if __name__ == "__main__":
    robot_mind = read_robot_mind()
    robot_pose = robot_mind.give_me_pose()
    daplan = robot_mind.plan(robot_pose)

