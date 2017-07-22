num = float(raw_input('Enter your number:'))
right = 'Your number is right !'
wrong = 'Wrong number !'
while False == (100 > num and num > 1):
    print wrong
    num = float(raw_input('Enter your number:'))
print right

