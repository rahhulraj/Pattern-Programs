"""

for i in range(6):
    print("* "*i)

"""
"""

for i in range(5,0,-1):
    print("* "*i)

"""

"""
for i in range(7):
    if i%2==0:
        print("* "*i)
        
    else:
        print(("* "*i)*2)
"""
"""
num=int(input("ENTER THE NUMBER :"))
for i in range(1,11):
    multi=num*i
    print(num,"*",i,"=",multi)

"""
for i in range(1, 11):
    factor=0
    for n in range(1,i+1):
        if i%n==0:
            factor=factor+1
    if factor==2:
        print("* "*(i + 1))
    else:
        print("* "*i)