
def Request_two_numbers (): #בקשת 2 מספרים
    try:
        num_1 = input("Conference number 1  ")
        num_1 = int(num_1)
          
        num_2 = input("Conference number 2  ")
        num_2 = int(num_2)
        return num_1 , num_2
    except ValueError:
              print("Only a number must be entered.")


Saving_number = Request_two_numbers()
print(Saving_number)


n1=Saving_number[0]
n2 = Saving_number[1]


# Connection 
def add_num1_num2(num1 , num2):
        return n1+n2
# add_num1_num2(n1,n2)
# # Connection_calculation = add_num1_num2()
# # print(Connection_calculation)

def Subtraction_num1_num2(num1 , num2):
        return n1-n2
# Subtraction_num1_num2(n1,n2)

def multiplication_num1_num2(num1 , num2):
        return n1*n2
# multiplication_num1_num2(n1,n2)

def Division_num1_num2(num1 , num2):
        return n1/n2
# Division_num1_num2(n1,n2)


def Operations_and_Calculation_Menu(): #תפריט פעולות וחישוב
      print("\n ---Actions menu---")
      print("1. Connection (+)  ")
      print("2. Subtraction (-)  ")
      print("3. multiplication (*)  ")
      print("4. Division (/)  ")
      choice = input(" (1-4) Select an action : ")
      if choice == "1":
            result = add_num1_num2(n1, n2)
            print(f" result : {result}")
      elif choice == "2":
            result = Subtraction_num1_num2(n1, n2)
            print(f" result : {result}")
      elif choice == "3":
            result = multiplication_num1_num2(n1, n2)
            print(f" result : {result}")
      elif choice == "4":
            if n2 == 0:
                   print("erro zerc")
            else:
              result = Division_num1_num2(n1, n2)
              print(f" result : {result}")

Operations_and_Calculation_Menu()
        
              
           
              

