











# enumerate function
# grocery = ['bread', 'butter', 'beef']

# enumerateGrocery = enumerate(grocery)
# print(list(enumerateGrocery))

# the output:
#[(0, 'bread'), (1, 'butter'), (2, 'beef')]

# for item in enumerate(grocery):
#   print(item)
# the output:
# (0, 'bread')
# (1, 'butter')
# (2, 'beef')


# for idx, item in enumerate(grocery):
#   print(idx, item)
# the output:
# 0 bread
# 1 butter
# 2 beef

# for idx, item in enumerate(grocery,100):
#    print(idx, item)
# the output:
# 100 bread
# 101 butter
# 102 beef













# inheritence
# from chef import chef
# from ChineseChef import ChineseChef

# print("this is the parent class:  ")
# my_chef = chef()
# my_chef.make_chicken()
# my_chef.make_special_dish()

# print("\nthis is inheritance class: ")
# my_Chinese_Chef = ChineseChef()
# my_Chinese_Chef.make_fried_rice()
# my_Chinese_Chef.make_special_dish()




#its give the memory for the list
# a = [10 for _ in range(10)]
# for x in range(len(a)):
#   print(x)









# Class
# from school import Student
# student1 = Student("nate", 20, 7.17, "computer science")
# print(student1.gpa,student1.name)


# Class function 
# from school import Student
# student1 = Student("nate", 20, 7.17, "computer science")
# print("the GPA is reach the command of graduation? " + str(student1.graduateGPA()))



# this is how to import a extenial file 
# import guessGame
# print(guessGame.main())


# if statement eg.
  # x=10
  # y=100
  # print("the difference is : " + str(abs(x-y)))
  # # print("the greater one: " + str(y)) if x < y else print("the greater one is : " + str(x)) if x > y else print("they were equal. ")
  # if x < y or x == y:
  #   # print("the greater one is: " + str(y))
  #   pass
  # else:
  #   print("the greater one is: " + str(x))


# While loop eg.
  # i = 0
  # while i < 10:
  #   print("cout: " + str(i))
  #   i += 1
  #   if i == 3:
  #     continue
  #   if i == 4:
  #     break
  # else:
  #   print("the count is no longer less than 10")


#square func
# def square_shape(leng): # no need to use 3 variables
        
#   for x in range(leng):
#     if x == 0 or x == leng - 1:
#       print(". " * leng)
#       continue
#     print (". " + "  " * (leng-2) + ".")
        
# square_shape(8)

#the next com is about get input from user

# hello user proj
# def prac():
#   name = input("Enter your name: ")
#   age = input("Enter your age: ")
#   print("Hello " + name + "! " + "Your are " + age + ". ")

# prac()



#caculator proj
# def prac():
#   num1 = input("Enter num1: ")
#   num2 = input("Enter num2: ")
#   print("The answer: " + str(float(num1)+float(num2)))
# prac()



# mad libs game proj
# def prac():
#   adj = input("Enter adj: ")
#   noun = input("Enter noun: ")
#   taste = input("Enter taste: ")
#
#   print("This is a " + adj + " day.")
#   print("I love " + noun)
#   print("This coke is " + taste)
# prac()


# list basics
# def prac():
#   friend = ["john", "nate", "nate", "kevin", "karen"]
#   age = [4, 112, 21, 22, 26, 12]
#   friend.extend(age) # it means add the age list after friend list
#   friend.append("jane") #it just add a element after the list
#   friend.insert(2, "jane") # it just insert a element in the index and other element move right
#   friend.remove("kevin") # it remove one element
#   friend.clear() # it clear the list
#   friend.pop() # it just remove the last element
#   friend.index("nate") # it get the element's index
#   friend.count("nate") # it count the # of the element
#   age.reverse() # it reverse the list
#   print(friend.index("nate"))
#   friend2 = friend.copy()
#   friend.sort()
#   print(friend)
# prac()



# cube num proj
# def cube(num):
#   return pow(num,3)
# num1 = cube(int(input("Enter a number: ")))
# print("The cube of this number is : " + str(num1))
# def cube(num):
#   return pow(num,3)
#
# inpNum = int(input("Enter a number: "))
# num1 = cube(inpNum)
# print("The cube of this number is : " + str(num1))


# calculator program
# def caculator(num1, num2, op):
#   if op == "+":
#     print(num1 + num2)
#   elif op == "-":
#     print(num1 - num2)
#   elif op == "/":
#     print(num1 / num2)
#   elif op == "*":
#     print(num1 * num2)
#   else:
#     print("Invalid operator! ")
# num1 = float(input("Enter first number: "))
# op = input("Enter the operator: ")
# num2 = float(input("Enter second number: "))
# caculator(num1, num2, op)


# guess game proj
# def main():
#     wordBase = ["nate", "shit", "god", "what", "day"]
#     playAgain = True
#     while playAgain == True:
#         guessGame(wordBase)
#         tryAgain = input("Do u want try again? (Y/N) :")
#         if tryAgain == "N":
#             playAgain = False
#
# def guessGame(wordBase):
#   guessInp = ""
#   guessCount = 0
#   guessLimit = 3
#   randNum = random.randint(0, 4)
#   guessWord = wordBase[randNum]
#   while guessInp != guessWord and guessCount < guessLimit:
#     guessInp = input("Enter the guess word: ")
#     guessCount += 1
#   if guessCount == guessLimit:
#     print("Out of Guesses, YOU LOSE")
#   else:
#     print("You Win!!!! :)")
#
# main()


# power function
# def power(baseN, powN):
#   num = 1
#   for x in range(powN):
#     num *= baseN
#   print(num)
# power(2, 3)


# 2D list && nested for loop
# numGrid = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9],
#   [0]
# ]
# print(numGrid[0][2])
# for row in numGrid:
#   for col in row:
#     print(col)


# translate the vowel to g
# def translate(phrase):
#   trans = ""
#   for letter in phrase:
#     if letter.lower() in "aeiou":
#       if letter.isupper(): trans += "G"
#       else: trans += "g"
#     else: trans += letter
#   return trans
# print(translate(input("Enter the sentence: \n")))



# try except
# try:
#   answer = 10 / 0
#   number = int(input("Enter a number: "))
#   print(number)
# except ZeroDivisionError as err:
#   print(err)
# except ValueError:
#   print("invalid input! ")




# extential file
# file = open("name.txt", "r") # open the text file and set it to a variable which is readable
# # print(file.readable())
# # print(file.read()) # read the variable file
# # print(file.readline() #read the first line we have
# #print(file.readlines()) # store all lines of string into a list
# print(file.readlines()[0]) # get which index in the list
# file.close()  # if open the file, it should be closed as well

# file = open("name.txt", "a") # this "a" is append, which is add some content after at that text file
# file.write("\nthis is what i appending to that text file") # and it was using write to adding
# file.close()

# file = open("name.txt", "w") # it will overwrite the file 
# file.write("this will be overwriting the text file")
# file.close()

# file = open("name1.txt", "w") # it will also create a new file 
# file.write("it will be what i write in the new text file")
# file.close()

# file = open("writeFile.html", "w")
# file.write("<p>This is what i write by using python3 :) </p>")
# file.close()