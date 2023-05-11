#Approach 1
import sys
sys.path.append("C:/Users/hi/PycharmProjects/PythonTraining/Day 9/Package1")
sys.path.append("C:/Users/hi/PycharmProjects/PythonTraining/Day 9/Package1/Package2")

import module1
module1.display()

import module2
module2.show()

#Approach 2
import sys
sys.path.append("C:/Users/hi/PycharmProjects/PythonTraining/Day 9/Package1")
sys.path.append("C:/Users/hi/PycharmProjects/PythonTraining/Day 9/Package1/Package2")

from module1 import *
module1.display()

from module2 import *
module2.show()

display()
show()
