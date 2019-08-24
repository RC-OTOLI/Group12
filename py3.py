""" Function call """
def askName(name, age):
    print("Hi! " + name + ", and you're " + age + " years old")

askName("Pete","30")
askName("Fon","31")
    
def cube(num):
    return num*num*num

result = cube(4)
print(result)
#print(cube(2))

""" if else statements """
is_male = False
is_short = False
if is_male or is_short:
    print("Pete is a male or short or both")
else:
    print("Pete is a superman or tall")

num1 = float(input("Enter the float numbers: "))
op = input("input operator: ")
num2 = float(input("Enter another float numbers: "))
if op == "+" :
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else :
    print("Invalid operators")

""" Month Conversions """
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
#print(monthConversions["Dec"])
print(monthConversions.get("Nov"))
