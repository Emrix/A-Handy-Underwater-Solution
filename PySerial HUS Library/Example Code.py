'''
A Handy Underwanter Solution (HUS) Arduino Serial Communication Library Example

Created on 2016-8-27

@author: Matt Ricks
'''

# Import HUS Library.
from HUS import HUS
Hand = HUS("COM4",9600)
print(Hand.move(7,True)) #Move Forward
print(Hand.move(3,False)) #Move Backward
Hand.stop()
