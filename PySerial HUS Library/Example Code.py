'''
A Handy Underwanter Solution (HUS) Arduino Serial Communication Library Example

Created on 2016-8-27

Updated on 2016-11-18

@author: Matt Ricks


http://stackoverflow.com/questions/345187/math-mapping-numbers
'''

# Import HUS Library.
from HUS import HUS
Hand = HUS("/dev/ttyACM0",9600)
print(Hand.move(3,255)) #Move Forward
print(Hand.move(3,100)) #Move Backward
print(Hand.move(3,200)) #Move to original spot
Hand.stop()


#roslaunch cortex_ros basic.launch 


Hand = HUS("/dev/ttyACM1",9600)

import math

def f(x):
    return int(  ((x)/255.0) * (100.0 - 255.0) + 255.0  )

def move_servo2(pos):    
    if pos > 255 or pos < 0:
        pos = 0  
    Hand.move(3,pos)
    Hand.move(4,f(pos))


def mov(pos):
	Hand.move(3,pos)
	Hand.move(4,255-pos)





'''
import rospy
import time
from geometry_msgs.msg import PoseStamped

finger_data = []
base_data = []


def callback_finger(msg):
    finger_data.append(msg.pose)

def callback_base(msg):
    base_data.append(msg.pose)


rospy.init_node('handy_data_getter')
rospy.Subscriber('/handy_finger/handy_finger', PoseStamped, callback_finger)
rospy.Subscriber('/handy_base/handy_base', PoseStamped, callback_base)

while not rospy.is_shutdown():
    rospy.sleep(0.001)

print finger_data


'''
