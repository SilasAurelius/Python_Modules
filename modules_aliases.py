# # Task 1: Custom Module with Aliases 
# Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.
from text_utils import reverse_string as reverse
from text_utils import captialize_string as captialize

s = "I am Silas Aurelius Leone and I like coding, turtles, and mocha frappe's!"
print(s)

print(reverse(s))
print(captialize(s))

# I used print(reverse.s) and got an attribute error. Tried reverse(s) and it worked.