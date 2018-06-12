cmake_minimum_required(VERSION 2.8.3)
project(openpose_ros_srvs)

## Add support for C++11, supported in ROS Kinetic and newer
add_definitions(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  openpose_ros_msgs
  message_generation
)

#Generate services in the 'srv' folder
 add_service_files(
   FILES
   DetectPeoplePoseFromImg.srv
 )


generate_messages(
  DEPENDENCIES std_msgs openpose_ros_msgs sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS message_generation message_runtime
)

