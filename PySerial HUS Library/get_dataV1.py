#1 launch a ros server
# ifconfig
#$ ping 192.168.0.15
#$ roslaunch cortex_ros launchfile.launch
#$ roslaunch cortex_ros basic.launch 



#other commands 
#$ rostopic lic
#$ rostopic list
#$ rostopic echo /handy_base/handy_base /
#$ 



import random
import rospy
import time
from geometry_msgs.msg import PoseStamped

from HUS import HUS
import cPickle


finger_start_data = []
base_start_data = []
finger_result_data = []
base_result_data = []
servo_data = []


def callback_finger_start(msg):
    finger_start_data.append(msg.pose)

def callback_base_start(msg):
    base_start_data.append(msg.pose)    

def callback_finger_result(msg):
    finger_result_data.append(msg.pose)

def callback_base_result(msg):
    base_result_data.append(msg.pose)    


rospy.init_node('handy_data_getter')


'''
rospy.init_node('handy_data_getter')
rospy.Subscriber('/handy_finger/handy_finger', PoseStamped, callback_finger)
rospy.Subscriber('/handy_base/handy_base', PoseStamped, callback_base)


while not rospy.is_shutdown():
    rospy.sleep(0.001)
'''


Hand = HUS("/dev/ttyACM1",9600)


def f(x):
    return int(  ((x)/255.0) * (100.0 - 255.0) + 255.0  )

def move_servo2(pos):    
    if pos > 255 or pos < 0:
        pos = 0  
    Hand.move(3,pos)
    Hand.move(4,f(pos))


def get_start():
    rospy.Subscriber('/handy_finger/handy_finger', PoseStamped, callback_finger_start)
    rospy.Subscriber('/handy_base/handy_base', PoseStamped, callback_base_start)

def get_result():
    rospy.Subscriber('/handy_finger/handy_finger', PoseStamped, callback_finger_result)
    rospy.Subscriber('/handy_base/handy_base', PoseStamped, callback_base_result)


def get_random_pos():
	
	pos = random.randint(0,255)
	servo_data.append(pos)

	move_servo2(pos)
	
	
def system_reset():
	move_servo2(255)


for i in range(1000):
    print(i)
    system_reset()	
    time.sleep(2) 
    get_start()   
    get_random_pos()
    time.sleep(2)
    get_result()
	

data_dict = {}


for i in range(len(servo_data)):
	data_dict[i] = finger_start_data[i], base_start_data[i], servo_data[i], finger_result_data[i], base_result_data[i]


print("Pickeling the data")
output = open('pickled_data.plk','wb')
cPickle.dump(data_dict,output)
output.close()

	

'''
figer_file  = open("fingerData.txt", 'w')
base_file   = open("baseData.txt", 'w')
servo_file = open("servoPosDats",'w')

for i in finger_data:
	finger_file.write("%s\n" % i)
for j in base_data:
	base_file.write("%s\n" % j)
for w in servo_data:
	servo_file.write("%s\n" % w)
'''

#print finger_data
