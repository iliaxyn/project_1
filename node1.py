#!/usr/bin/env python
import rospy
 
from std_msgs.msg import Int32
from random import randint
 
#a function to generate the random number
def generate_random_number():
    rnd1= randint(0,1000)
    return rnd
 
if __name__=='__main__':
    rospy.init_node('random_number1')
    pub=rospy.Publisher('rand_no1', Int32, queue_size=10)
    rate= rospy.Rate(5)
 
    while not rospy.is_shutdown():
        rnd_gen=generate_random_number()
       
       
 
rate.sleep()
