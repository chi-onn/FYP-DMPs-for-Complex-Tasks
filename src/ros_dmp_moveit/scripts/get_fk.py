#!/usr/bin/env python

import rospy
from moveit_msgs.srv import GetPositionFK
from moveit_msgs.srv import GetPositionFKRequest
from moveit_msgs.srv import GetPositionFKResponse
from sensor_msgs.msg import JointState

class GetFK(object):
    def __init__(self, fk_link, frame_id):
        """
        A class to do FK calls thru the MoveIt!'s /compute_ik service.
        :param str fk_link: link to compute the forward kinematics
        :param str frame_id: frame_id to compute the forward kinematics
        into account collisions
        """
        rospy.loginfo("Initalizing GetFK...")
        self.fk_link = fk_link
        self.frame_id = frame_id
        rospy.loginfo("Asking forward kinematics for link: " + self.fk_link)
        rospy.loginfo("PoseStamped answers will be on frame: " + self.frame_id)
        self.fk_srv = rospy.ServiceProxy('/compute_fk',
                                         GetPositionFK)
        rospy.loginfo("Waiting for /compute_fk service...")
        self.fk_srv.wait_for_service()
        rospy.loginfo("Connected!")
        self.last_js = None
        self.js_sub = rospy.Subscriber('/joint_states',
                                       JointState,
                                       self.js_cb,
                                       queue_size=1)

    def js_cb(self, data):
        self.last_js = data

    def get_current_fk_pose(self):
        resp = self.get_current_fk()
        if len(resp.pose_stamped) >= 1:
            return resp.pose_stamped[0]
        return None

    def get_current_fk(self):
        while not rospy.is_shutdown() and self.last_js is None:
            rospy.logwarn("Waiting for a /joint_states message...")
            rospy.sleep(0.1)
        return self.get_fk(self.last_js)

    def get_fk(self, joint_state, fk_link=None, frame_id=None):
        """
        Do an FK call to with.
        :param sensor_msgs/JointState joint_state: JointState message
            containing the full state of the robot.
        :param str or None fk_link: link to compute the forward kinematics for.
        """
        if fk_link is None:
            fk_link = self.fk_link

        req = GetPositionFKRequest()
        req.header.frame_id = 'world'
        req.fk_link_names = [self.fk_link]
        req.robot_state.joint_state = joint_state
        try:
            resp = self.fk_srv.call(req)
            return resp
        except rospy.ServiceException as e:
            rospy.logerr("Service exception: " + str(e))
            resp = GetPositionFKResponse()
            resp.error_code = 99999  # Failure
            return resp

    def get_fk_list(self,joint_angles):
        self.last_js.position = joint_angles
        #print(self.last_js)
        return self.get_fk(self.last_js)


if __name__ == '__main__':
    rospy.init_node('test_fk')
    rospy.loginfo("Querying for FK")
    gfk = GetFK('link_tcp', 'world')
    rospy.sleep(3)
    joint_angles1 = (0.551098,0.010168,-1.136722,-0.026116,0.862260,0.420633,0.000000, 0.0, 0.0, 0.0, 0.0, 0.0)
    joint_angles2 = (0.549959,0.010176,-1.136722,-0.026116,0.862260,0.420633,0.000000, 0.0, 0.0, 0.0, 0.0, 0.0)

    resp = gfk.get_fk_list(joint_angles1)
    #from moveit_python_tools.friendly_error_codes import moveit_error_dict
    #rospy.loginfo(moveit_error_dict[resp.error_code.val])
    posestamped = resp.pose_stamped[0]
    position = (posestamped.pose.position.x, posestamped.pose.position.y, posestamped.pose.position.z)
    orientation = (posestamped.pose.orientation.x,
               posestamped.pose.orientation.y,
               posestamped.pose.orientation.z,
               posestamped.pose.orientation.w)
    print(position)
    print(orientation)

    resp = gfk.get_fk_list(joint_angles2)
    posestamped = resp.pose_stamped[0]
    position = (posestamped.pose.position.x, posestamped.pose.position.y, posestamped.pose.position.z)
    orientation = (posestamped.pose.orientation.x,
               posestamped.pose.orientation.y,
               posestamped.pose.orientation.z,
               posestamped.pose.orientation.w)
    print(position)
    print(orientation)





# all joint = 0
# pose: 
#   position: 
#     x: 0.20700000000000002
#     y: -1.832929346706894e-06
#     z: -0.0599999999943131
#   orientation: 
#     x: 0.9999999999932537
#     y: 0.0
#     z: 0.0
#     w: 3.673205103638112e-06

# new
# pose: 
#   position: 
#     x: 0.2069851186115573
#     y: -0.34460915840135126
#     z: -0.060033632558241304
#   orientation: 
#     x: -0.9999999993443056
#     y: -2.06498359824289e-05
#     z: 1.69097855144651e-05
#     w: 2.447514191547756e-05
# -1.0299039747990566, 0.3648179396204452, -0.6624267554427007, 1.213102753857908e-05, 0.2976681921119253, -1.0299568721178611, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0