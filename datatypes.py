# Built in Data Types: are data types that are predefined by a programming language and can
# be used directly in a program without the need to create them.
from collections.abc import Mapping

# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Types: dict
# Set Types: set, frozenset
# Boolean Types: bool
# Binary Types: byes, bytearray, memoryview
# None Type: NoneType

#Getting the Data Type type()
#print a data type of variable x:
x = 5
print(type(x))
print(type(x))
x_complex = 34j
print(type(x_complex))
print(type(x_complex))
x_float = 3.14
print(type(x_float))
print(type(x_float))
y = "Ernest"
print(type(y))
print(type(y))
z = True
print(type(z))
print(type(z))
t = 208.453
print(type(t))
print(type(t))
w = ["maembe", "avocado", "mapera", "parachichi"]
print(type(w))
print(w)
r = ("maembe", "avocado", "mapera", "parachichi")
print(type(r))
print(r)
u_range = (6)
print(type(u_range))
print(u_range)
x_dict = {"name" : "John", "age" : 36}
print(type(x_dict))
print(x_dict)
x_set = {"apple", "banana", "cherry"}
print(type(x_set))
print(x_set)
x_frozen = frozenset({"apple", "banana", "cherry"})
print(type(x_frozen))
print(x_frozen)
x_bytearray = bytearray(5)
print(type(x_bytearray))
print(x_bytearray)
x_memoryview = memoryview(x_bytearray)
print(type(x_memoryview))
print(x_memoryview)
x_none = None
print(type(x_none))
print(x_none)

# Setting specific datatype
x_int = int(23)
print(x_int)
x_float = float(2.14)
print(x_float)
x_complex = complex(2.14, 3.14)
print(x_complex)
x = 5
print(type(x))
