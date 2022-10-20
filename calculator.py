def input_num():
    return int(input("Enter a number "))

def input_operator():
    return input("Enter an operation (Add, Sub, Mul, Div) ")

def add(a, b):
    return a+b

def div(a, b):
    return a/b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

# num1 = input_num()
# num2 = input_num()

input_ranges = 2

input_list = []
for iter in range(input_ranges):
    input_list.append(input_num())

# input_list = [input_num() for iter in range(input_ranges)]

operator = input_operator()
operator = operator.lower()

if operator == "add":
    output = add(input_list[0], input_list[1])
elif operator == "sub":
    output = sub(input_list[0], input_list[1])
elif operator == "mul":
    output = mul(input_list[0], input_list[1])
elif operator == "div":
    output = div(input_list[0], input_list[1])
else:
    print("Operation not available")

print("The output for {} and {} with operation {} is {}".format(input_list[0], input_list[1], operator, output))