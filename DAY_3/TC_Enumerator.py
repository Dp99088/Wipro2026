#Enumerator
fruits=['Apple','Orange',"Banana"]
for index, value in enumerate(fruits):
    print(index,value)

#enum- assigning fixed values
from enum import Enum
class color(Enum):
    Red=1
    Green=2
    Blue=3
print(color.Red.value)
print(color.Red.name)
