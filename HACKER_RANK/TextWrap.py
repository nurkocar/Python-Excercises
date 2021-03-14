# string = ABCDEFGHIJKLIMNOQRSTUVWXYZ
# max_width = 4

import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))