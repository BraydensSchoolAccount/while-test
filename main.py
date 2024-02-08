# While Loop test
# Brayden Towner
# 02/08/2024

# FIX previous number value was 12, making the while invalid
number = 1
while number <=10:
    print(number)
    number += 1

# DON'T RUN
# number = 0
# while number <=10:
#     print(number)
#     number -= 1

# Output: Decrementing negative numbers
# The number, continually going down, never met the condition
# It doesn't end because it never meets the condition of the while loop, running forever

number = 1
while number <=10:
    if number % 2 == 0:
        print(number, end=" ")
    number += 1

# Output: 2 4 6 8 10
# The end being " " causes each item to be separated by a space
# Line 3 checks to see if the number is a multiple of 2

while valid_input:
    user_number = int(input("Enter a number between 1 and 10 >  "))
    valid_input = 1 <= user_number <= 10
    if not valid_input:
        print("Invalid input, please try again")
print("Valid input, you're clear")
