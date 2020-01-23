class MathDojo:
    def __init__(self):
    	self.result = 0
    #add a for loop to loop through the data
    def add(self, num, *nums):
        for a in nums:
            num += a
        self.result += num
        return self

    def subtract(self, num, *nums):
        for s in nums:
            num -= s
        self.result -= num
        return self

# create an instance:
md = MathDojo()
ts = MathDojo()
# to test:
y = md.add(3).add(1,2,3).result
print(f'md result: {y}')
y = md.add(10).add(5,9,1).add(7,4,6).result
print(f'md result_2: {y}')
y = md.add(8).add(2,4,6).result
print(f'md result_3: {y}')
#test to subtract
x = ts.subtract(10).result
print(f'ts result: {x}')
x = ts.subtract(14).subtract(7,5,1).result
print(f'ts result_2: {x}')
x = ts.add(5).add(3,4,3).subtract(4,3,21).result
print(f'ts result_3: {x}')
x = md.add(2).add(2,5,1).subtract(3,2).result
print(f'md result_4: {x}')	# should print 5
# run each of the methods a few more times and check the result!
