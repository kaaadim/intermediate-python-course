def main():
  import random
 
  dice_rolls=int(input('How many rolls baby?'))
  dice_sides=int(input('How many sides would you like in a dice?'))
  dice_sum=0
  
  for i in range(0,dice_rolls):
   roll=random.randint(1,dice_sides)
   if roll==1:
    print(f'You rolled a {roll}! CRITICAL FAIL!')
   
   elif roll==dice_sides:
   	print(f'You rolled a {roll}! CRITICAL SUCESS!')
  
   else:
    print(f'You rolled a {roll}')
   dice_sum=dice_sum+roll
  
  print(f'Sum of dices is {dice_sum}')

if __name__== "__main__":
  main()