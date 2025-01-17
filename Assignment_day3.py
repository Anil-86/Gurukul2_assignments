# # Write a Python function to find the maximum of three numbers
#
# numbers = (1,2,9)
# print("Maximum of 3 number is :",max(numbers))
#
# # Write a Python function to multiply all the numbers in a list.
# # Sample List : (8, 2, 3, -1, 7)
# # Expected Output : -336
#
# # numbers: List[int] = [8, 2, 3, -1, 7]
# # print('the list is:',given_list)
# # print("the multiply is :")
# # print(multiply_number(given_list))
#
#
#
# #
# # Write a Python program to reverse a string.
# # Sample String : "1234abcd"
# # Expected Output : "dcba4321"
from msilib.schema import ListBox

# a="1234abcd"[::-1]
# print(a)
#
#
# #
# #  Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# n = int(input("Input a number to compute the factorial: "))
# print(factorial(n))


#
# #  Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# # Sample List : [1,2,3,3,3,3,4,5]
# # Unique List : [1, 2, 3, 4, 5]

# def dt(input_list):
#     distinct_elements =list(set(input_list))
#     return distinct_elements
# list = dt(input_list=[1,2,3,3,3,3,4,5])
# print("The distinct element from the list is :",list)

# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# # Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

# def prime(n):
#     if(n==1):
#         return False
#     elif(n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n%x==0):
#                 return False
#         return True
# num=int(input("Enter your number to check it prime or Not:"))
# if prime(num):
#         print(f"{num}  its a prime")
# else:
#         print(f"{num} is Not Prime")



# # Write a Python program to print the even numbers from a given list.
# # Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # Expected Result : [2, 4, 6, 8]

# list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in list:
#     if number % 2 ==0:
#         print(number,end="")
#
#
# # Write a Python function that accepts a string and counts the number of upper and lower case letters.
# # Sample String : 'The quick Brow Fox'
# # Expected Output :
# # No. of Upper case characters : 3
# # No. of Lower case Characters : 12

# string="'The quick Brow Fox'"
# lower=0
# upper=0
# for i in string:
#       if(i.islower()):
#           lower+=1
#       else:
#           upper+=1
# print("The number of lowercase characters is:", lower)
# print("The number of uppercase characters is:", upper)





# # Write a Python function to sum all the numbers in a list.
# # Sample List : (8, 2, 3, 0, 7)
# # Expected Output : 20

# sum_of_list = lambda lst: sum(lst)
# numbers = [1, 2, 3, 4, 5]
# result = sum_of_list(numbers)
# print(result)


#
# #  Write a  Python function that checks whether a passed string is a palindrome or not.
# # Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run

