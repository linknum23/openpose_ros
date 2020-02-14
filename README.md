# TODO: This is completely untested but now it uses way better ros conventions. Come back to this if better openpose ros package doesn't work out.

# openpose-ros
CMU's Openpose for ROS

![posefacehands](pose_face_hands.gif)

## Update Information

I re-implemented cmu's openpose in tensorflow with some modifications.

Especially, using Mobilenet's 'Depthwise Separable Convolution', I improved it to run in realtime even in an low-computation embedded deivce or only-cpu environment.

See : https://github.com/ildoonet/tf-openpose

## Implementation

- [X] Broadcasting Ros Message
- [X] Humans Pose Estimation
- [ ] Face Landmark
- [ ] Hand Pose Estimation

## Installation

### Openpose

See [Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose).

After building openpose, set the environment variable OPENPOSE_HOME.

```
$ export OPENPOSE_HOME='{path/to/your/openpose/home}'
```

### Packages

```
$ sudo apt-get install ros-indigo-image-common ros-indigo-vision-opencv ros-indigo-video-stream-opencv ros-indigo-image-view
```

### Catkin Build 

```
$ cd src
$ git clone https://github.com/linknum23/openpose_ros
$ cd ..
$ catkin_make
```

## Message

### Parameter

+ resolution(string, default: 640x480) : input image resolution
+ net_resolution(string, default: 640x480) : network resolution
+ num_gpu(int, default: -1) : number of gpus to use. -1 indiciates 'all'.
+ num_gpu_start(int, default: 0) : first index of gpu to use.
+ model_pose(string, default: COCO) : pose estimation model name provided by openpose.
+ no_display(bool, default: false) : if true, it will launch opencv image view to show realtime estimation.
+ camera(string, default: /camera/image) 
+ result_image_topic(string, default: '') : if provided, it will broadcast image with estimated pose.

### Broadcast

+ /openpose/pose : [Msg](https://github.com/linknum23/openpose_ros/blob/master/openpose_msgs/msg/Persons.msg)
   + [Persons](https://github.com/linknum23/openpose_ros/blob/master/openpose_msgs/msg/PersonDetection.msg)
     + [BodyPartDetection](https://github.com/linknum23/openpose_ros/blob/master/openpose_msgs/msg/PersonDetection.msg) 

BodyParts are stored as indexed 
    Nose = 0
    Neck = 1
    RShoulder = 2
    RElbow = 3
    RWrist = 4
    LShoulder = 5
    LElbow = 6
    LWrist = 7
    RHip = 8
    RKnee = 9
    RAnkle = 10
    LHip = 11
    LKnee = 12
    LAnkle = 13
    REye = 14
    LEye = 15
    REar = 16
    LEar = 17
    
## Example

### Launch File Example

```
<node name="openpose_node" pkg="openpose_node" type="openpose_node" output="screen" required="true">
        <param name="camera" value="/videofile/image_raw" />
        <param name="result_image_topic" value="/openpose/image_raw" />
        <param name="resolution" value="480x320" />
        <param name="face" value="false" />
    </node>
```


### Test with Camera/Video Files

```
$ roslaunch openpose_node videostream.launch video:=0 video_visualize:=true
$ roslaunch openpose_node videostream.launch video:=${filepath} video_visualize:=true
```

### USB Camera Example

See [/launch/videostream](https://github.com/linknum23/openpose_ros/blob/master/openpose_node/launch/videostream.launch).
