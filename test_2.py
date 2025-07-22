# test_list = [x + 1 for x in range(5) if x % 2 ==0]
# print(test_list)

# test_2_list = [x for x in range(20) if x % 2 !=0]
# three_list = [x for x in range(20) if x % 3 ==0]
# print(test_2_list)
# print(three_list)

# list = [x for x in range(40) if x % 2 ==0]
# print(list)

# addition_list = [1,2,3,4,5]
# test_list = [x + 10 for x in addition_list]
# print(test_list)

# ages_list = [17,20,46,13,29,30,15,10]
# ages_results = [age for age in ages_list if age > 20]
# # print(ages_results)

# while True: 
#     text = input("Type 'exit' to stop: ")
#     if text == "exit":
#         print("Goodbye!")
#         break
#     else: 
#         print("You typed:", text)

# restaurants = [
#     "Burger Palace",
#     "Sushi World",
#     "Pasta Heaven",
#     "Taco Town",
#     "Curry Express",
#     "Vegan Delight"
# ]

# import random

# def random_restaurant(list):
#     random_integer = random.randint(0, len(list)-1)
#     print(f"Dinner tonight will be from {list[random_integer]}.")

# random_restaurant(restaurants)

# students = [ 
#     ["Alice", 95],
#     ["Bob", 82],
#     ["Charlie", 77],
#     ["Diana", 88],
#     ["Eli", 91],
#     ["Fiona", 67],
#     ["George", 58],
#     ["Hannah", 73],
#     ["Ian", 60],
#     ["Jane", 85]
# ]

# def grading_students(list):
#     a = ""
#     b = ""
#     c = ""
#     d = ""
#     f = ""
#     for grade in range(len(list)):
#         if list[grade][1] <= 100 and list[grade][1] >= 90:
#             a += "*"
#         elif list[grade][1] <= 89 and list[grade][1] >= 80:
#             b += "*"
#         elif list[grade][1] <= 79 and list[grade][1] >=70:
#             c += "*"
#         elif list[grade][1] <= 69 and list[grade][1] >=60:
#             d += "*"
#         else:
#             f += "*"

#     return a,b,c,d,f

# a,b,c,d,f = grading_students(students)

# print("A:", a)
# print("B:", b)
# print("C:", c)
# print("D:", d)
# print("F:", f)

# try:
#     # Code that might cause an error
#     value = int(input("Enter a number: "))
#     print("You entered:", value)
# except ValueError:
#     # Code that runs if an error happens
#     print("Oops! That was not a valid number.")

# inputs = ["10", "20", "", "abc", "30", "40", "xyz"]

# valid_list = []

# for value in inputs: 
#     try:
#         new_value = int(value)
#         if type(new_value) == int:
#             valid_list.append(new_value)
#     except ValueError: 
#         continue

# print(valid_list)

# result = sum(valid_list) / len(valid_list)

# print(result)

# country_capitals = {
#   "United States": "Washington D.C.", 
#   "Italy": "Rome", 
#   "England": "London"
# }

# # Printing the dictionary
# print(country_capitals) 

# my_dict = {
#   1: "Hello", 
#   (1, 2): "Hello Hi", 
#   3: [1, 2, 3]
# }

# print(my_dict)

# country_capitals = {
#   "United States": "Washington D.C.", 
#   "Italy": "Naples", 
#   "England": "London"
# }

# country_capitals["Italy"] = "Rome"
# country_capitals["Mexico"] = "Mexico City"
# print(country_capitals)

# student = {
#     "name": "user",
#     "age": "17"
# }
# print(student["name"])

# student["age"] = "19"
# print(student)

# student["grade"] = "A"
# # student["school"]
# print(student)

# fruits = ["apple", "banana", "cherry", "date"]
# person = {
#     "name": "Bob", 
#     "age": 25,
#     "city": "Chicago"
# }

# print(fruits[2])
# print(person.get("age"))

# dict = {"name": "Alice"}
# print(dict["age"]) 
# print(dict.get("age")) 

# word = "hello"
# type(word)
# print(type(word))
# print(word.upper())

# class Dog:
#     def __init__(self, name):
#         self.name = name
    
#     def bark(self):
#         print(f"{self.name} says woof!")

class Cat:
    def __init__(self,name):
        self.name = name

    def meow(self):
        print(f"{self.name} says meow!")
