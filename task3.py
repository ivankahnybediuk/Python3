"""
Task 3
The name check.
Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. The program should check if your input is equal to the stored name even if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”, it should return True.
"""
myName = 'ivanka'
enteredName = input('Please, enter the name  ')
if enteredName.lower().strip() == myName:
    print('It`s right name!')
else:
    print('PLease, enter right name!')