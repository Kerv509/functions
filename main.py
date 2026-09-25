#Function to calculate the area of a circle
def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area
radius = float(input("please enter radius: "))
answer = circle_area(radius)
print("Cricle area of the circle is: ",answer)

#function to calculate tax return
def total_due(money,tax):
    total_due = (money) + (money * tax)
    return total_due
money = float(input("please enter amout of money: "))
tax = float(input("please enter tax rate: "))

answer = total_due(money,tax)
print("The total due is: ",answer)

#Function to calculate temperature
def celcius_value(farenheit):
    celcius_value = (farenheit - 32) * (5/9)
    return celcius_value
farenheit = float(input("Please enter temperature: "))
answer = celcius_value(farenheit)
print("The celcius value is: ",answer)

#The end!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!