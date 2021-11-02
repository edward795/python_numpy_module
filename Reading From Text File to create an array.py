'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
from io import StringIO
import numpy as np

x = StringIO('''88.25 93.45 72.60 90.90
72.3 78.85 92.15 65.75
90.5 92.45 89.25 94.50
''')

d = np.loadtxt(x,delimiter=' ')

print(d)

