#4.13.3: greetings
#colton hicks
#2.5.19
'''
name = input("what is your name: ")
def greeting():
    print("Hi there " + name +"!")
    print ("nice to meet you ")
greeting()
'''
#4.13.4 Functions and variables
#Colton Hicks
#2.11.19
x=10
def print_something():
    x=3
    print('\n', x)
print (x)
print_something()


4.14.7:print multiple times
#colton hicks
#2.19.19


def print_mult_times(string,times):
    for i in range(times):
        print(string)
print_mult_times('hey there computer scientist',7)
#4.13.6: functions and Variavle, part 3
#Colton Hicks
#2.18.19

def print_number(x):
    print (x)

print_number(13)
print('\n')
print_number(23)

#4.14.5 default parameter values
#Colton Hicks
#2.19.19

def print_two_number(x,y=20):
    print('first number:',x )
    print('second number: '+ str(y))
print_two_number(34, 45)
print_two_number(78)
#4.14.6: print sum
#colton hicks
#2.9.19



def print_sum(x,y):
    print(x + y)
print_sum(46,62)

