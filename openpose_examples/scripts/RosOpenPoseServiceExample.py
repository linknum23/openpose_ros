#! /usr/bin/env python
__author__ ='Jacques Saraydaryan'
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from openpose_srvs.srv import DetectPeoplePoseFromImg

import rospkg



def LoadImgAndPublish():
    # get an instance of RosPack with the default search paths
    rospack = rospkg.RosPack()

    # get the file path for rospy_tutorials
    package_path=rospack.get_path('openpose_examples')
    
    _bridge = CvBridge()
    
    media_folder=package_path+'/media';
    rospy.loginfo("media_folder:"+str(media_folder))
    #print ("media_folder:"+str(media_folder))
    

    
    rospy.init_node('LoadAndPublishImg', anonymous=True)
    
    #Load Image
    #img_loaded1 = cv2.imread(media_folder+'/pexels-photo-109919.jpeg')
    #msg_im1 = _bridge.cv2_to_imgmsg(img_loaded1, encoding="bgr8")

    #img_loaded2 = cv2.imread(media_folder+'/pexels-photo.jpg')
    #msg_im2 = _bridge.cv2_to_imgmsg(img_loaded2, encoding="bgr8")

    img_loaded3 = cv2.imread(media_folder+'/COCO_val2014_000000000544.jpg')
    msg_im3 = _bridge.cv2_to_imgmsg(img_loaded3, encoding="bgr8")


    #call service to learn people
    rospy.wait_for_service('people_pose_from_img')

    #try:
    #    detect_from_img_srv = rospy.ServiceProxy('people_pose_from_img', DetectPeoplePoseFromImg)
    #    resp1 = detect_from_img_srv(msg_im1)
    #    print "nb people"
    #    print "service:"+str(resp1.personList)
    #except rospy.ServiceException, e:
    #    print "Service call failed: %s"%e
    
    #try:
    #    resp2 = detect_from_img_srv(msg_im2)
    #    print "nb people"
    #    print "service:"+str(resp2.personList)
    #except rospy.ServiceException, e:
    #    print "Service call failed: %s"%e

    try:
        detect_from_img_srv = rospy.ServiceProxy('people_pose_from_img', DetectPeoplePoseFromImg)
        resp3 = detect_from_img_srv(msg_im3)
        print "nb people"
        print "service:"+str(resp3.personList)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    

    # spin
    rospy.spin()

if __name__ == '__main__':
    try:
        LoadImgAndPublish()
    except rospy.ROSInterruptException:
        pass