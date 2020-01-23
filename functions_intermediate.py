import random

def randInt(min = 0 , max = 0 ):
    if max < 0:
        return False
    elif min > max:
        return False
        num = random.randint(min, max)
        return num
    elif min == 0:
        num = int(random.random() * max)
        return num
    elif max == 0:
        num = int(random.random()* min * 2)
        return num
    else:
        num = int(random.random() * 100)
        return num

print(randInt()) #should print a random integer between 0 to 100
print(randInt(max = 50)) #should print a random integer between 0 to 50
print(randInt(min = 50)) #should print a random integer between 50 to 100
print(randInt(min = 50, max = 500)) #should print a random integer between 50 to 500

#min = 0
#max = 0
#if min == 0 and max == 0:
#    num = int(random.random()* 10)
#    print(num)
#elif min == 0 and max == 0:
