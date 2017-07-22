print "1.SUM"
print "2.AVG"
print "X.EXIT"
cho = str(raw_input('Which one did you what choice ?'))
def fun_sum():
    'sum function'
    num1 = float(raw_input('Enter your number:'))
    num2 = float(raw_input('Enter your number:'))
    num3 = float(raw_input('Enter your number:'))
    num4 = float(raw_input('Enter your number:'))
    num5 = float(raw_input('Enter your number:'))
    print int(num1+num2+num3+num4+num5)
def fun_ave():
    'ave_funciton'
    num1 = float(raw_input('Enter your number:'))
    num2 = float(raw_input('Enter your number:'))
    num3 = float(raw_input('Enter your number:'))
    num4 = float(raw_input('Enter your number:'))
    num5 = float(raw_input('Enter your number:'))
    print float(((num1+num2+num3+num4+num5) / 5))
if cho == str(1):
    fun_sum()   
elif cho == str(2):
    fun_ave()
elif cho == str("X"):
    exit
else:
    print 'None !'
