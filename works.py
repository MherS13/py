#point 1
'''
company = "Digitain"
myCountry = "Armenia"
name = "Mher"
age = 29
mySurname = "Sahakyan"
value = 500
USD = AMD = EURO = 5000
colour = "Green"
work_Space = "IT company"
status = "free"
height,width,size = 90,50,70
_result_point = 100


#point 2

a = int(input("Enter the first angle of a triangle"))
b = int(input("Enter the second angle of a triangle"))
c = 180-(a+b)
print("Third angle of a triangle ", c)

#point 3

Minutes = int(input("Enter the Minutes"))
seconds = (Minutes*60)
print("result into seconds", seconds)

#point 4 

Celsius = int(input("Enter degree"))
Fahrenheit = (Celsius * 9/5) + 32
print(Fahrenheit)



# point.5

number = int(input("Enter number to check it is even or odd"))
formula = number % 2
if (formula == 0):
    print(number,"is an even number")
else:
    print(number,"is an odd number")


# point 6 

Fahrenheit = int(input("Enter degree"))
Celsius = (Fahrenheit-32)/1.8000
print(Celsius)


# point 7

high_1 = int(input("The height of the fisrt mountain! "))
high_2 = int(input("Enter the height of the second mountain! "))
high_3 = int(input("Enter the height of the third mountain! "))

if (high_1 >= high_2) and (high_1 >= high_3):
	biggest = high_1
elif (high_2>=high_1) and (high_2 >= high_3):
	biggest = high_2
else:
	biggest = high_3
print("The biggest mountain", biggest)


# point 8

print("enter the rectangle's length size")
length = int(input())
print("enter the rectangle's width size")
width = int(input())
area = (length*width)

print(area)

# point 9


side = int(input("enter the side to compute the area of square" ))
area = int(side**2)
print(area)



side = int(input("enter the side to compute the area of square" ))
area = int(side**2)
print(" The area of the square is" ,area)



# point 10

print("What is your name?")
name = input()
print("What is your surname!")
surname = input()
print("How old are you?")
age = input()
print ("where are you from?")
myCountry = input()
print("It's nice to meet you")

'''
'''
print("what is your name," + " what is your surname, " + "how old are you and " + "where are you from?")
name = input()
surname = input() 
age = input() 
myCountry = input()

print("It's nice to meet you")


#####

# def read_file():
#     file = open("poem.txt","r")
#     for line in file:
#         print(line, end="")
#     file.close()
#
# read_file()

#2
# def read_data():
#     f = open("text.txt", 'r')
#     s = f.read()
#     x = s.split()
#     print(str(len(x)) +" "+"Words")
# 
# read_data()

1

# file = open("C:\data.txt", "rt")
# data = file.read()
# words = data.split()
#
# print('Number of words in text file :', len(words))

2

# file = open('file.txt', 'r')
# read_data = file.read()
# per_word = read_data.split()
#
# print('Total Words:', len(per_word))

5#
# L = ["Geeks\n", "for\n", "Geeks\n"]
# 
# # writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()
# 
# # Using readlines()
# file1 = open('myfile.txt', 'r')
# Lines = file1.readlines()
# 
# count = 0
# # Strips the newline character
# for line in Lines:
#     count += 1
#     print("Line{}: {}".format(count, line.strip()))