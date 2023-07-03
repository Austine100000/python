def mitmorn():
    print("This is MIT Morning class")


mitmorn()


def calculate():
    x = 7
    y = 10
    print(x * y)
    print(x + y)
    print(x - y)
    print(x / y)


calculate()


def majina(myfirstname, mylastname, age):
    print(myfirstname + " " + mylastname, age)


majina("My name is Austine", "Kamama", "my age is 19")
majina("My name is Esther", "Chepki", "my age is 7")
majina("MY name is Marylin", "Samanthe", "my age is 20")
majina("My name is Josiah", "john", "my age is 16")
majina("My name is Ruth", "Cheruu", "my age is 19")

# create a function that will calculate the average of [2.5,6,3,5]
numbers = [2.5, 6, 3, 5]


def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


data = [2.5, 6, 3, 5]
result = average(data)
print(" average ", result)

# create a function that gives you the longest string in a list
