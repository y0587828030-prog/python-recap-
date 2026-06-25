
#VARS:

# agent_name = "yehosh"
# mission_code =int(1234)
# distance = float(35.5)
# status_mission = True
# print(agent_name, mission_code, distance, status_mission)
# print(agent_name)
# print(mission_code)
# print(distance)
# print(status_mission)

# #LOGICAL OPERATORS:

# status = False
# print(not(status))

# age = 20
# id = True
# if age >= 18 and id == True:
#     print("enter")
# else:
#     print("error")

# #conditions
# #1
# # gievn_age = input("Enter your age.") 
# # gievn_age = int(gievn_age)
# gievn_age = int(input("Enter your age ."))
# if gievn_age >= 18:
#     print("wellcome")
# else:
#     print("go away")

# #2
# temperature = float(38.2)
# if temperature >= 37.5:
#     print("high temperatur")
# else:
#     print("normal temperature")

# #3
# numbar = int(input("give me anumber"))
# if numbar % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# #
# battery = 15
# is_charging = True

# if battery < 20 and is_charging == True:
#     print("Low battery, charging now")
# elif battery <20 and is_charging != True:
#     print("Low battery, connect charger")
# else:
#     print("battry ok")

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
agents.append("foxtrot")
print(agents)