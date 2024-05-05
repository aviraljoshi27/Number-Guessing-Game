import random
import math

lower_range= int(input('Enter the lower range'))
upper_range= int(input('Enter the upper range'))

choice= random.randint(lower_range, upper_range)
print('You have to guess the number in that range and you have only ',
       round(math.log(upper_range-lower_range+1)),
         ' chance')

count = 0

while count < round(math.log(upper_range-lower_range+1)):
    count += 1
    users_answer= int(input('Select a number in that range'))
    if users_answer > choice:
        print('You guessed high 😢 Try again!!!')
    elif users_answer < choice:
        print('You guessed low 😢 Try again!!!')
    elif users_answer == choice:
        print('Hurrayy You won🎉🍾🥂')
        break
if count >= round(math.log(upper_range-lower_range+1)):
    print('Exceeds the limit !!! Better Luck Next Time')
    print('correct number was : ', choice)


