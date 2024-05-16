# Write a Python function to check if a given string is a palindrome or not.
# Palindrome strings are those that read the same backward as forward, ignoring spaces, punctuation, and
# capitalization. For example, "A man, a plan, a canal, Panama!" is a palindrome.


# my_str1 = "miami"
# my_str2 = "malayalam"
#
# rev_str1 = reversed(my_str1)
# rev_str2 = reversed(my_str2)
#
# if list(my_str1) == list(rev_str1):
#     print("The string is palindrome")
# else:
#     print("The string is not a palindrome")
#
# if list(my_str2) == list(rev_str2):
#     print("The string is palindrome")
# else:
#     print("The string is not a palindrome")


# def is_palindrome(s):
#     # Convert the string to lowercase and remove spaces and punctuation
#     s = s.lower()
#     s = ''.join(char for char in s if char.isalnum())
#
#     # Check if the string is equal to its reverse
#     return s == s[::-1]
#
#
# # Example usage
# input_string = "A man, a plan, a canal, Panama!"
# print(is_palindrome(input_string))  # Output: True


# Write a Python function to find the maximum occurring character in a given string.
# If there are multiple characters with the same maximum occurrence, return any one of them.

# string = "kranthikrishnayadlapati"
# emp = {}
# for i in string:
# 	if i in emp:
# 		emp[i] = emp[i]+1
# 	else:
# 		emp[i] =1
# result = max(emp, key = emp.get)
# print(result)


# string = "kranthikrishiniayadlapati"
# emp = {}
# for i in string:
#     if i in emp:
#         emp[i] = emp[i] + 1
#     else:
#         emp[i] = 1
# max_occ = 0
# for count in emp.values():
# 	if count > max_occ:
# 		max_occ = count
# max_chars = []
# for char, count in emp.items():
# 	if count == max_occ:
# 		max_chars.append(char)
#
# print(max_chars)

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)



class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

account1 = BankAccount("12345")
account1.deposit(100)


print("Account Number:", account1.account_number)
print("Balance:", account1.balance)














