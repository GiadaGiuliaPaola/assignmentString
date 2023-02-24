# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#UEFA Euro 1988 Final

#variable for each player that score
player10 = 'Ruud Gullit'
player12 = 'Marco van Basten'

#variable minute goal scored
goal_0 = 32
goal_1 = 54

#report who score when
scorers= f'{player10} {str(goal_0)}, {player12} {str(goal_1)}'
print (scorers)

report = f'{player10} scored in the {goal_0}nd minute\n{player12} scored in the {goal_1}th minute'
print(report)

#player name analysis with index
player = 'Berry van Aerle'
first_name = player[:5]
last_name = player[6:]
last_name_len = len(last_name)
name_short = player[0] + '. ' + last_name
print(name_short)
chant = first_name + ('!') + ((' ') + first_name + ('!')) * (len(first_name)-1)
print(chant)

good_chant = chant != (' ')

