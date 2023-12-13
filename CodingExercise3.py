#Practising input()
#Ask the user to provide their login and native language. Use the following prompts:

#Enter your login: << remember to add a space at the end of this prompt!
#Enter your native language: << remember to add a space at the end of this prompt!

#Then, show the user the following message:

#Your login is {login provided} and you speak {language provided}

#For example, if the user provides the login h_potter and language British English, show:

#Your login is h_potter and you speak British English

#Watch out for typos: you must show the output in this particular format!

# Get input from the user for login and native language
login = input('Enter your login: ')
language = input('Enter your native language: ')

# Print a message with the entered login and native language
print('Your login is', login, 'and you speak', language)
