import random

my2DList = []

def ran():
    number = random.randint(1,90)
    return number

num = []
for i in range(8):
    num.append(ran())

my2DList = [[num[0], num[1], num[2]],[num[3], "BINGO", num[4]], [num[5], num[6], num[7]]]

def prettyprint():
    for row in my2DList:
        for values in row:
            print(f"{values:^10}", end=" | ")
        print()



print ("David's Nan's Bingo Card Generator")
print()
prettyprint()
