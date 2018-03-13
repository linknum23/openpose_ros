cmake_minimum_required(VERSION 2.8.3)
project(openpose_ros_examples)

## Add support for C++11, supported in ROS Kinetic and newer
add_definitions(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  openpose_ros_msgs
  openpose_ros_srvs
)


catkin_package(
  CATKIN_DEPENDS 
)

