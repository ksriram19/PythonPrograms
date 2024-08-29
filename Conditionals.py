# If statements
x = 3
if x > 0:
    pass

if x > 0:
    print(x)

inp = input('Enter Fahrenheit temperature: ')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')

    
# Short circuiting and Guard Evaluation

x = 4
y = 0

if x > 5 and (x/y) > 0:
    print(x)

if x > 2 and y != 0 and (x/y)>0:
    print(True)

# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

try:
    hour = input("Enter the hours: ")
    hours = float(hour)
    rates = input("Enter the rate: ")
    rate = float(rates)

    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours-40) * (rate * 1.5)

    print(pay)
except:
    print("Print a number")

# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error      message. If the score is between 0.0 and 1.0, print a grade using the following table:

try:
    inp = input("Enter score")
    score = float(inp)

    if score < 0.6:
        grade = 'F'
    elif score >= 0.6 and score <= 0.7:
        grade = 'D'
    elif score >= 0.7 and score <= 0.8:
        grade = 'C'
    elif score >= 0.8 and score <= 0.9:
        grade = 'B'
    elif score >= 0.9 and score <= 1.0:
        grade = 'A'
    else:
        grade = 'Bad Score'

    print(grade)
except:
    print("Error")
