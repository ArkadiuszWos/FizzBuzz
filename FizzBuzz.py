# -*- coding: utf-8 -*-
__author__ = "Arkadiusz Wos"
__copyright__ = "Arkadiusz Wos"
__version__ = "1.0"
__email__ = "arkadiusz.wos@gmail.com"

"""
Script to loop through 2 numbers(n,m) set by User and print accoring rules:
● for multiples of three, print Fizz (instead of the number)
● for multiples of five, print Buzz (instead of the number)
● for multiples of both three and five, print FizzBuzz (instead of the number)
● 1 <= n < m <= 10000
"""

def FuzzBuzz():

    #rules for input first number
    n_input = 0
    while True:
        try:
            n_input = int(input("Enter first number from 1 to 10000: "))
            
            if (n_input < 1 or n_input > 10000):
                print ("You number isn't from 1 to 10000!")
                continue
        except ValueError:
            print("Not an integer! Try again!")
            continue
        else:
            break
        
    #rules for input second number
    m_input = 0
    while True:
        try:
            m_input = int(input('Enter second number higer than %s less to 10000: ' %n_input))
            if (m_input <= n_input or m_input > 10000):
                print ('You number is not higer than %s less to 10000: '%n_input)
                continue
        except ValueError:
            print("Not an integer! Try again!")
            continue
        else:
            break
    
     #loop for range first to second number  
    num_list = [num for num in range(n_input, m_input+1)]
    print ("\n"*2) #to look better
    for num in num_list:
        if num%5 == 0 and num%3==0:
            print ("FizzBuzz")
        elif num%5 == 0:
            print("Fizz")
        elif num%3 == 0:
            print ("Buzz")
        else:
            print (num)
                
FuzzBuzz()















