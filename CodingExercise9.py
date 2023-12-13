# Dictionary mapping English words to their German translations
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

# Loop to continuously prompt the user for input
while True:
    # Get user input
    user_input = input('Enter a word in English or EXIT: ')

    # Check if the user wants to exit the loop
    if user_input == 'EXIT':
        break

    # Check if the entered word is in the dictionary
    if user_input in sample_dict:
        # If yes, print the translation
        print('Translation:', sample_dict[user_input])
    else:
        # If no match is found, print an error message
        print('No match!')

# Print a farewell message when the loop is exited
print('Bye!')
