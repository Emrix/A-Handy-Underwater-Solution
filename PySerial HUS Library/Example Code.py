'''
A Handy Underwanter Solution (HUS) Arduino Serial Communication Library Example

Created on 2016-8-27

Updated on 2016-11-18

@author: Matt Ricks
'''

# Import HUS Library.
from HUS import HUS
Hand = HUS("COM4",9600)
print(Hand.move(3,400)) #Move Forward
print(Hand.move(3,300)) #Move Backward
print(Hand.move(3,300)) #Move to original spot
Hand.stop()