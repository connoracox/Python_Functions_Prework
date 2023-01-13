#Connor Cox
#January 23rd Cohort
# Coding Question Responses: Python 102



# Question 1:
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name("USERNAME")



# Question 2:
# Write a python function, first_odds that prints the odd numbers 
# from 1-100 and returns nothing

def first_odds(start, end):

    for num in range(start, end + 1):
     
        if num % 2 != 0:
            print(num, end = " ")

first_odds(1,100)



# Question 3:
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):

    maxValue = max(a_list) 
    print(maxValue)

a_list = [1, 23, 98, 62, 12, 342, 7]
max_num_in_list(a_list)



# Question 4:
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
  # Checking if the given year is leap year  
    if((a_year % 400 == 0) or  
    (a_year % 100 != 0) and  
    (a_year % 4 == 0)):   
        print(True)  
  # Else it is not a leap year  
    else:  
        print (False)  

is_leap_year(1993) 
# Above is False
#Input a year like 2020 to get True



# Question 5:
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list1):
    return sorted(a_list1) == list(range(min(a_list1), max(a_list1)+1))
     
# Driver Code
a_list1 = [3, 4, 1, 5, 2, 7, 6]
print(is_consecutive(a_list1))
#example above returns True, they are consecutive
#input a list such as [2, 45, 6, 51, 33] to get False