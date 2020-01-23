# 1. TASK: print "Hello World"
print('Hello World')
# 2. print "Hello Noelle!" with the name in a variable
name = "Terence"
print('Hello', name ) # with a comma
print( 'Hello ' + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 26
print( 'Hello', name )	# with a comma
print( 'Hello ' + str(name))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "Curry Chicken"
fave_food2 = "Pesto Cavetappi"
print( 'I love to eat {} and {}'.format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string
score = 100
print('The score is ' + str(score));
print('I love to eat {} and {}'.format(fave_food1, fave_food2).upper()) #string.upper
player_one = 'LeBron James'
player_two = 'Brady'
print(player_one.count('e')) #string.count(substring)
print(player_two.find('r')) #string.find(substring)
print(player_one.casefold()) #string.casefold()
print(player_two.endswith('b'))
