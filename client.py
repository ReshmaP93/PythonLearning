import sys
sys.path.append("C:/Users/hi/PycharmProjects/PythonTraining/Day 9/pack1")
#Approach1
import module1
import module2

module1.display()
module2.show()

#Approach 2

from module1 import *
from module2 import *
display()
show()

