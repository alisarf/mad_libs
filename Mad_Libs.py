'''Ali's Mad Libs'''

'''
It was a {adjective}, cold November day. I woke up to the {adjective2} smell of {bird} 
roasting in the {room} downstairs. I {verb_past_tense} down the stairs to see if I could 
help {verb} the dinner. My mom said, "See if {needs a fresh {noun}." So I carried a tray 
of glasses full of {liquid} into the {verb_ing} room. When I got there, I couldn't believe
 my {body_part}! There were {plural_noun} {verb_ing2} on the {noun2}!
'''


import time
time.sleep(2)

player_name = input('Hello Player! What is your name?')
time.sleep(2)
print(f'Welcome {player_name}!')
time.sleep(2)
intro = 'Would you like to play a round of mad libs?(yes/no)'
time.sleep(2)
introduction = input(intro)

if introduction != 'no':
	print("Wonderful! I will need you to provide a few words for me.")
	print('Okay. Here we go...')
else:
	print('Okay... Maybe another time. Bye now!')

adjective= input('please give me an adjective.')
adjective2= input('Another one...')
bird = input("Now I'll need a type of bird.")
room = input("Great. Can I please have a room to a house?")
verb_past_tense = input("Ok. Ok. Now please provide a verb but it must be past tense. Thanks.")
verb = input("Another verb please.")
noun = input("And a noun.")
liquid = input("Thanks. Next I'll need a liquid")
verb_ing = input("Another verb ending in 'ing'.")
body_part = input("Okay how about a body part.")
plural_noun = input("I'll need another noun but a plural one! We're almost done.")
verb_ing2 = input("Thank you. One more verb ending in 'ing'")
noun2 = input("Okay. Finally, I'll need a noun.")

'''
time.sleep(2)
print(f'Okay, thank you {player_name} for playing my Mad Libs.')
time.sleep(2)
print('Please give me a moment while I scribble in your words.')
time.sleep(2)
print('...scribble...')
time.sleep(2)
print('...scribble...')
time.sleep(2)
print('Okay, all done!')
'''

print(f'It was a {adjective}, cold November day.')
print(f'I woke up to the {adjective2} smell of {bird} ')
print(f'roasting in the {room} downstairs. I {verb_past_tense}')
print(f'down the stairs to see if I could ')
print(f'help {verb} the dinner. My mom said, See if it needs a fresh {noun}.')
print(f'So I carried a tray of glasses full of {liquid}')
print(f'into the {verb_ing} room. When I got there, I could not')
print(f'believe my {body_part}! There were {plural_noun} {verb_ing2} on the {noun2}!')



