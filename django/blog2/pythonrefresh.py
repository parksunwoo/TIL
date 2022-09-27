age = 12
name = "Matt"
todayIsCold = True

# print(age)
# print(name)
# print("Hello my name is {} and I am {} years old".format(name, age))

# if age != 14:
#     print("You are older than 18")
#     print("This is another line")
# else:
#     print("you are younger than 18")

# def hello(name="sean", age=0):
#     return "Hello {} you are {} years old".format(name, age)
#
# sentence = hello()
# print(sentence)

# dognames = ["Fido", "Sean", "Sally", "Mark"]
#
# for x in range(5,10):
#     print(x)

class Dog:
    def __init__(self, name="", age=0, furcolor=""):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def bark(self, str):
        print("BARK! " + str)

mydog = Dog("Fido", 13, "Brown")
print(mydog.age)

# mydog.bark("dddddddddddddddddddddddd")
# mydog.name = "Fido"
# mydog.age = 16
# print(mydog.name)
# print(mydog.age)
# print(Dog.dogInfo)
#
# Dog.dogInfo = "Hey there"
# print(Dog.dogInfo)
