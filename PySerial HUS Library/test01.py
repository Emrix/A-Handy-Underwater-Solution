from HUS import HUS
import time


Hand = HUS("/dev/ttyACM1",9600)

print("Com port established")


Hand.move_by(1,False,100) #Move Forward
time.sleep(1)
Hand.move_by(1,True,100)
time.sleep(1)

Hand.move_by(1,False,100) #Move Forward
time.sleep(1)
Hand.move_by(1,True,100)
time.sleep(1)
'''
print("move 1 to 250")
Hand.move_to(1,250)

print("move 1 to 240")
Hand.move_to(1,240)


print("move 1 to 250")
Hand.move_to(1,250)
'''

Hand.move_by(2,False,100) #Move Forward
time.sleep(1)
Hand.move_by(2,True,100)
time.sleep(1)

Hand.move_by(2,False,100) #Move Forward
time.sleep(1)
Hand.move_by(2,True,100)
time.sleep(1)

