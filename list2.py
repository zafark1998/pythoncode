# a = []

# a.append("Zain")
# a.append("Arsal")
# a.append("Areel")

# print(a)

# b = len(a)
# print(b)

# c = type(a)
# print(c)

# d = type(b)
# print(d)

# name = len("zain")
# print(name)

# a = [1,2,3]
# b = [4,5,6]

# c = a+b
# print(c)

# integers =list(range(0,101,5)) 
# print(integers)

# i = []

# u = input("Enter Name")
# e = input("Enter No.")
# f = input("Enter Age.")

# i.append([u,e,f])
# # i.append(e)
# # i.append(f)

# print(i)

# user =[]
# counter = 0

# while counter < 2:
#     name = input("Enter Your Name: ")
#     age = input("Enter Your Age: ")
#     gender = input("Enter Your Gender: ")

#     user.append(name)
#     user.append(age)
#     user.append(gender)

#     counter = counter + 1

# print(user)

# u = {}
# user =[]
# counter = 0

# while counter < 2:
#     name = input("Enter Your Name: ")
#     age = input("Enter Your Age: ")
#     gender = input("Enter Your Gender: ")

#     u["name"] = name
#     u["age"] = age
#     u["gender"] = gender
    
#     user.append(u)
#     # user.append()
#     # user.append()

#     counter = counter + 1

# print(user)

# loop = [1,2,3,4]

# loop [1] = 200
# print(loop)

# num = (1,2,3,4)

# num [1] = 150
# print(num)


# ins = "aptech metro star gate"

# print(ins[0:6].title())
# print(ins[7:12].title())
# print(ins[13:17].title())
# print(ins[18:23].title())

# ins [1]= "f"

# for inst in ins:
#     print(inst,end="*")

# emptylist = []
# c = 0

# while c <= 3:

#     # emptylist.append(input())

#     num = input("Enter Num  ")
#     c += 1

#     print(emptylist.sort(reverse=True))

# v  = input("Enter Number")

# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# num = int(input("Enter a number: "))

# result = check_even_odd(num)

# print(f"The number {num} is {result}.")

# e = [n for n in range(101) if n % 2==0]
# o = [n for n in range(101) if n % 2!=0]

# for n in range(101):
#     if n % 2 == 0:
#         e.append(n)

#     else:
#         o.append(n)

# print(e)
# print("--------------------------------------------------------------")
# print(o)

# test = "mango"
# fruits = ["apple","mango","pineapple","strawbeerry"]

# for x in range(len(fruits)):
#     if fruits [x] == test:
#           print(x)
    

# print(f"Their is no {test} in the list")

# vovels = ["a","e","i","o","u"]
# get = input("print letter: ")

# if get in vovels:
#     print("its vovels")

# else:
#     print("consonents")

# if 'a' == vovels[0]:
#     print("vovels")

# if 'e' in vovels == get:
#     print("vovels")

# if 'i' in vovels == get:
#     print("vovels")

# if 'o' in vovels == get:
#     print("vovels")

# if 'u' in vovels == get:
#     print("vovels")

# else:
#     print("consonents")


alien = {'a':'zain','b':'faraz','c':'ali','d':'zohaib'}
# print(a)
alien['num']= [123]
alien['str']= ['a','b','c']
alien['dit'] = {'color1':'red','color2':'blue','color3':'green'}


# print(a)
# print(a['b'])
# print(a['num'])
#alien['b']="faiz"

# print(a)

# del a['c']

# print(a)


# state=alien.get('a','not found')

# print(state)

# del alien['str'][:-2]
# print(alien['str'])


# for key,value in alien.items():
#     print(key,value)

# alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}

# print(f"Original Position: {alien_0['x_position']}")


# if alien_0['speed'] == 'slow':
#     x_increment = 1

# elif alien_0['speed'] == 'medium':
#     x_increment = 2

# else:
#     x_increment = 3

# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New Position : {alien_0['x_position']}")

key =[]
value = []

for k,v in alien.items():
    key.append(k)
    value.append(v)

print(key)
print(value)
