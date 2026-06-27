
##VARS:

agent_name = "yehosh"
mission_code =int(1234)
distance = float(35.5)
status_mission = True
print(agent_name, mission_code, distance, status_mission)
print(agent_name)
print(mission_code)
print(distance)
print(status_mission)

#LOGICAL OPERATORS:

status = False
print(not(status))

age = 20
id = True
if age >= 18 and id == True:
    print("enter")
else:
    print("error")

#conditions
#1
# gievn_age = input("Enter your age.") 
# gievn_age = int(gievn_age)
gievn_age = int(input("Enter your age ."))
if gievn_age >= 18:
    print("wellcome")
else:
    print("go away")

#2
temperature = float(38.2)
if temperature >= 37.5:
    print("high temperatur")
else:
    print("normal temperature")

#3
numbar = int(input("give me anumber"))
if numbar % 2 == 0:
    print("even number")
else:
    print("odd number")

#
battery = 15
is_charging = True

if battery < 20 and is_charging == True:
    print("Low battery, charging now")
elif battery <20 and is_charging != True:
    print("Low battery, connect charger")
else:
    print("battry ok")

# battery = int(input("Enter the battery percentage (0 - 100): "))
# is_charging = input("Is the battery rechargeable? (yes/no) ")
# is_charging = is_charging in ["yes"]
# if battery < 20 and is_charging:
#     print("loe battery, chrging now")
#     elif

#list 
agents = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
print(agents)
print(agents[0],agents[-1])
print(agents[1])
print(agents[0:4])

#הוספת ערכים למקום אחרון
agents.append("foxtrot")
print(agents)

#הוספת ערכים לליסט לפי מיקום- 
agents.insert(0, "yehoshua")
print(agents)
agents.insert(1, "josh")
print(agents)

#מחיקת ערכים לפי ערך- .remove("v")
agents.remove("Alpha")
print(agents)

#מחיקה לפי מיקום- 
delet_agents = agents.pop(0)
print(agents)
print(f"Deleted entry: {delet_agents}")

#מחיקה לפי טווח-del משנה- []
del agents[0:1]
print(agents)

#הצגת מהרשימה
print(agents[0])
print(agents[2])

#הצגת מיקום האינדקס
index = agents.index("foxtrot")
print(index)

me_list = ["a", "b", "c", "d" , "a", "a"]
x = me_list.index("a")
print(x)

#ספירת פעמים רשימה
print(me_list.count("a"))

#בדיקה אם קיים ברשימה 
me_list = ["a", "b", "c", "d" , "a", "a"]
if "a" in me_list:
    print("available")
else:
    print("Not found")

##dicts
agent = {'name': 'Alpha', 'level': 3, 'active': True}
print(agent)

#הדפסת הערך לפי מפתח
print(agent["name"])
print(agent["level"])
print(agent["active"])
# print(agent["0"]) יוצר שגיאה
#הדפסת ערך לפי מפתח - .get
agent_name = agent.get("name")
print(agent_name)
agent_level = agent.get("level")
print(agent_level)
agent_active = agent.get("active")
print(agent_active)
agent_zero = agent.get("0") # משיב none
print(agent_zero)

# הוספת ערך\שינוי
agent["score"]=95
print(agent)
agent["level"]=6

#הוספת מפתח \שינוי מפתח .update
agent.update({"height":185 })
print(agent)
agent.update({"level":5})
print(agent)

#מחיקת מפתח והערך שלו
del  agent["active"]
print(agent)

#הדפסת DICT
#לפי מפתח
Keys = agent.keys()
print(Keys)
#לפי ערכים
Values = agent.values()
print(Values)
#כל הדיקס בזוגות
all_key_value = agent.items()
print(all_key_value) 
print("Keys:", list(agent.keys()), "| Values:", list(agent.values()), "| Items:", list(agent.items()))

# # whil loops

#ליצור לולאה מ1-5
i = 1
while i <= 5:
    print(i)
    i += 1

i = 1
while i<= 5:
    print(i)
    i += 1

#ליצור מ1-10 ולהדפיס רק מספרים זוגיים
i =1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

#break עצירה 
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1

# לדלג אם = continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# הדפסה לאחר סיום הריצה
i = 1
while i <6:
    i += 1
else:
    print("i is no longer than 6")

#הדפסה מליסט
agents = ['Alpha', 'Bravo', 'Charlie']
i = 0
while i < len(agents):
    print(agents[i])
    i += 1

# ## loop for 


# #הדפסה של הליסט
list = ["a", "b", "c", "d"]
for x in list:
 print(x)

#הדפסה של תווים של ערך
for x in "banana":
    print(x)

#עצירת breack
list = ["yehosh", "josh", "bob"]
for x in list:
    print(x)
    if x == "josh":
        break

# דילוג על ערך
list = ["1", "2", "3", "4"]
for x in list:
    if x == "3":
        continue
    print(x)

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
   print(x)

x = range(6)
for n in x:
   print(n)

x = range(3,8)
for n in x:
   print(n)

x = range(50, 100, 25)
for n in x:
   print(n)

x = range(0, 10, 2)
for n in x:
   print(n)

# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)
# print(list(y))

# #הדפסת ערך ואינדקס- enumerate
fruits = ['apple', 'banana', 'cherry']
for i , v in enumerate(fruits):
    print(i, v)

list = ["yehoshua", "josh", "zalts"]
for i in enumerate(list):
    print(i)

list1 =("1", "2", "3")
for i in enumerate(list1):
    print(i)



#step 2
x = range(1,6)
for n in x:
 print(n)

 #step 3
 x = range(0, 10, 2)
 for n in x:
    print(n)

#step 4
fruits = ['apple', 'banana', 'cherry']
for i , v in enumerate(fruits):
   print(i , v)


list = ["yehoshua", "josh", "zalts"]
for i in enumerate(list):
    print(i)


list = []
for x in range(1,11):
   list.append(x**2)
print(list)



# ##Part 1 — Basics: while loop, break, continue, looping over lists and dicts

# # stap 1
# i = 1
# while i <= 5:
#     print(i)
#     i = i +1

# #stap 2
# i = 10
# while i >= 1:
#     print(i)
#     i = i -1

# #stap 3
# total = 0
# i = 1
# while i <= 10:
#     total = total + i
#     i = i + 1
# print(total)

# #stap 4
# items = [2, 4, 6, 8]
# index = 0
# while index < len(items):
#     current_number = items[index]
#     if current_number >5:
#         print(current_number)
#         break
#     index = index + 1

# #stap 5
# i = 0
# while i < 10:
#     i = i +1
#     if i % 2 == 1:
#         continue
#     print(i)

# #stap 6
# agents = ['Alpha', 'Bravo', 'Charlie']
# index = 0 
# while index < len(agents):
#     print(agents[index])
#     index += 1

# #stap 7
# scores = {'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
# scores_list = list(scores.items())
# index = 0
# while index < len(scores_list):
#     current_item = scores_list[index]
#     name = current_item[0]
#     score = current_item[1]
#     print(name, score)
#     index = index + 1

# #stap 8
# naber = 1
# while naber <= 100:
#     naber = naber * 2
#     print (naber)

# #stap 9
# data = [3, 7, 2, -1, 5]
# total_sum = 0
# index = 0

# while index < len(data):
#     current_value = data[index]
#     if current_value == -1:
#         break
#     total_sum = total_sum + current_value
#     index = index + 1
# print(total_sum)

# #stap 10
# n = 10
# i = 1
# while i <= 10:
#     result = n * i
#     print(n, "x", i, "=", result)
#     i =i + 1

# ##Part 2 — Optional Advanced Basics
#  #step 1
# items = ['a', 'x', 'b', 'x', 'x']
# i = 0
# while i < len(items):
#     current_item = items[i]
#     if current_item == "x":
#         items.remove(current_item)
#         print(items)
#     else:
#         i = i + 1

# #step 2
# matrix = [[1, 2, 4, 5], [3, 4], [5, 6]]
# x = 0
# y = 0
# while x < len(matrix):
#     while y < len(matrix[x]):
#         current_value = matrix[x][y]
#         print(current_value)
#         y += 1
#     y = 0
#     x += 1  

# #step 3

# my_list = [10, 20, 30, 40, 50]
# current_list = []
# i = len(my_list) - 1
# while i >= 0:
#     current_list.append(my_list[i])
#     i -= 1
# print(current_list)

#step 4
# data = [10, 30, 55, 20, 80]
# i = 0
# while i < len(data) and data[i] <= 50:
#     i += 1
# print(i)

#step 5
secret = 42
guesses = [10, 30, 42]
index = 0
attempts = 1
while index < len(guesses) and guesses[index] != secret:
    attempts += 1
    index += 1
print(attempts)








#part 1 Basics: for loop, 
# step 1

# fruits = ['apple', 'banana', 'cherry']
# for x in fruits:
#     print(x)

# #step 2
# x = range(1,6)
# for n in x:
#  print(n)

#  #step 3
#  x = range(0, 10, 2)
#  for n in x:
#     print(n) 

# #step 4
# fruits = ['apple', 'banana', 'cherry']
# for i , v in enumerate(fruits):
#    print(i , v)

# #step 5
# scores = {'Alpha': 80, 'Bravo': 95}
# for name ,score, in scores.items():
#     print(name , score )

# #step 6
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for number in  numbers:
#    sum +=number
# print(sum)  

#step 7 
#while
# i = 1
# while i <= 5:
#    print(i)
#    i += 1
# for n in range(1,i):
#    print(n)

#for
# x = range(1,6)
# for n in x:
#     print(n)

# #step 8
# matrix = [[1, 2, 3], [4, 5, 6]]
# for x in matrix:
#    for y in x:
#       print(y)

# #step 9
# list = [x ** 2 for x in range(1,11)]
# print(list)

# #step 10
# list = [x for x in range(0, 21, 2)]
# print(list)
# #option
# list = [x for x in range(1,21) if x % 2 == 0 ]
# print(list)

##Part 2 — Optional Advanced Basics
#step 1
# names = ['Alpha', 'Bravo']
# scores = [80, 95]
# x = zip(names, scores)
# print (list(x))

#step 2
list = [( x , x ** 2) for x in range(1, 6)]
print (list)

#step 3

list = ["yehoshua", "josh", "zalts"]
for i,v in enumerate(list):
    print(i,v)

#step 4
matrix = [[1, 2], [3, 4], [5, 6]]
x = [num for row in matrix for num in row]
print(x)

#step 5
words = ['hello', 'world', 'python']
x = [word.upper() for word in words]
print(x)
    