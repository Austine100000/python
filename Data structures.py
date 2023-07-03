# list data structure
# a list enable you to change data : can change position, can remove, can add data.
myclassmate = ["Eric", "Joan", "Susan", "Purity", "Daniel"]
mynos = [4, 5, 6, 20, 50, -9]
myclassmate[0] = "Austine"
mynos.sort()
myclassmate.append("Christine")
myclassmate.insert(2, "Esther")
myclassmate.pop(5)
print(myclassmate)
print(mynos)

# for loop
for students in myclassmate:
    print(students)

# this is a tuple :cannot change its position
countries = ("Kenya", "Uganda", "Tanzania", "Burundi")
print(countries)
for nchi in countries:
    print(nchi)

# sets :starts with {}, changes, cannot have identical data
cars = {"Toyota", "Nissan", "Mercedes", "Subaru", "Rangerover"}
print(cars)

for magari in cars:
    print(magari)

# dictionaries data structure: starts with{}
matunda= {
    "price": 50,
    "color": "Green",
    "Name": "Banana"
}
matunda["shape"]="oval"
matunda["Name"]="Orange"

print(matunda)
x=matunda["price"]
print(x)
x=matunda["color"]
print(x)
x=matunda["Name"]
print(x)


car= {
    "price": 500000,
    "color": "Blue",
    "Name": "Toyota"
}
print(car)
