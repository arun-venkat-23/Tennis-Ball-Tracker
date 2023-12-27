# Tennis-Ball-Tracker using ROS Noetic and OpenCV

## Dependencies:

ROS-Noetic <br>
Python <br>
OpenCV <br>

## Goal
It is an example of a ROS publisher and listener. Here the publisher reads a video file and publishes each frame. The listener in turn reads each frame and tries to detect the tennis ball (if any) in it.

## Remarks

Since this is primarily an example of a publisher and listener interacting, the detector section is very basic. The detection can be improved by applying erosion and dilution. The color calbration is also presently done for the lighting conditions in the video. The ball detector code was tested with a USB camera as well but expectedly is very sensitive to conditions different from that in the video.

## How to Run
```
git clone https://github.com/arun-venkat-23/Tennis-Ball-Tracker

cd <path>/<ros_workspace>
# eg. cd ~/catkin_ws
catkin_make
## The following two commands need to be run in two different terminal sequentially
./tennis_ball_publisher.py
./tennis_ball_publisher.py
```
