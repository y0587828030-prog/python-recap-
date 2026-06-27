# ##vers
# agent_name = str("yehosh")
# mission_code = int(1234)
# distance_to_target = float(35.7)
# mission_active_status = True

# print(agent_name,mission_code,distance_to_target,mission_active_status)

# ##logical operators:
# status = False
# print(status)

# age = 18
# has_id = True

# if age >= 18 and has_id == True:
#     print("entar")
# else:
#     print("no entar")

# ##conditions
# give_age = int(input("How old are you?"))
# if give_age >= 18:
#     print(give_age,"Can enter")
# else:
#     print("Cannot enter")

# temperature = 38.2
# if temperature > 37.5:
#     print("High temperature")
# else:
#     print("Normal temperature")

# given_numbar = int(input("Enter a number"))
# if given_numbar % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# battery = 15
# is_charging = True  
# if battery < 20 and is_charging == True:
#     print("Low battery, charging now")
# elif battery < 20  and is_charging != True:
#     print("Low battery, connect charger")
# else:
#     print("battery ok")


###list
##הצגת הרשימה
my_list =["Milk", "eggs", "cheese", "bread", "vegetables"]
# #הצגה לי מיקום
# print(my_list[0])
# print(my_list[1])

# #מיקום האחרון
# print(my_list[-1])

# #הצגת אורך הרשימה
# print(len(my_list))

# ##הוספת ערכים
# #הוספת ערך לסוף הרשימה
# my_list.append("apple")
# print(my_list)

# #הוספת ערך במיקום ספציפי
# my_list.insert(2, "chree")
# print(my_list)

# ##עריכת ערכים
# my_list[0] = "drink"
# print(my_list)

# ##מחיקת ערכים
# #מחיקה לפי שם הערך
# my_list.remove("drink")
# print(my_list)

#מחיקה לפי מיקום
deleted_my_list = my_list.pop(0)
print(my_list)
print(deleted_my_list)

#מחיקת הערך האחרון
deleted_my_list2 = my_list.pop() 
print(my_list)
print(deleted_my_list2)

#מחיקת הערכים
my_list.clear()
print(my_list)


