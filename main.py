"""
Given n as input, check which of the numbers from 2 to 5 divide n.
input: n=15
Output: 
2: no 
3: yes 
4: no 
5: yes
"""

n = int(input("Enter Number: "))

for i in range(2,6):
  if (n%i==0):
    print(f"{i}:Yes")
  else:
    print(f"{i}:No")
    