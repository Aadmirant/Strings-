# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1

Ruud_Gullit = 'Scorer 1'
Marco_van_Basten = 'Scorer 2'
goal_0= 32
goal_1= 54
goal_time_1= f'Ruud Gullit scored in the {goal_0}nd minute '
goal_time_2= f'\nMarco van Basten scored in the {goal_1}th minute'
scorers = goal_time_1 + goal_time_2
report=(goal_time_1 + goal_time_2)
print(report)

# Part 2

player = 'Ronald Koeman'
first_name = player[0:6]
last_name_len = len(player[7:13])
name_short = 'R. Koeman'
chant = len(first_name) * (first_name + '! ')
print(chant.lstrip())
good_chant = 'Ronald! Ronald! Ronald! Ronald! Ronald! Ronald! '
good_chant != chant
print(good_chant != chant) is False