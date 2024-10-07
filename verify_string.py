text = input('Type your text: ')

a_in_text = text.count('a')

if a_in_text == 0:
    print('There is no "A" in your text.')

elif a_in_text == 1:
    print(f'There is {a_in_text} A in your text.')

else:
    print(f"There is {a_in_text} A's in your text.")