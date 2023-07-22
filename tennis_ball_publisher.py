#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def video_reader_node():
    rospy.init_node('video_reader_node', anonymous= True)
    pub = rospy.Publisher('video_read',Image,queue_size=10)
    br = CvBridge()
    rate = rospy.Rate(1)
    video_capture = cv2.VideoCapture('/home/arunvenkat/catkin_ws_ros/src/ros_essentials_cpp/src/topic03_perception/video/tennis-ball-video.mp4')
    while not rospy.is_shutdown():
        _,frame = video_capture.read()
        if frame is not None:
            try:
                img_frame = br.cv2_to_imgmsg(frame,'bgr8')
            except CvBridgeError as e:
                    print(e)
            pub.publish(img_frame)
            rate.sleep()
            
        else:
            video_capture = cv2.VideoCapture('/home/arunvenkat/catkin_ws_ros/src/ros_essentials_cpp/src/topic03_perception/video/tennis-ball-video.mp4')
    video_capture.release()

if __name__ == '__main__':
        try:
            video_reader_node()
        except rospy.ROSInterruptException:
            pass