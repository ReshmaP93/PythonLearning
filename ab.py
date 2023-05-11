#Approach 1

import a
import b

obj=a.Animal()
obj.display()

obj1=b.Bird()
obj1.display()

#Approach 2

from a import Animal
from b import Bird

obj1=Animal()
obj1.display()

obj2=Bird()
obj2.display()

