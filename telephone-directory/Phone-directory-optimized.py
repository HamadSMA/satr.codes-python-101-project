#Creating a deictionary and filling it with keys and values
directory ={"Amal":1111111111, 
    "Mohammed":2222222222,
    "Khadijah":3333333333, 
    "Abdullah":4444444444, 
    "Rawan":5555555555, 
    "Faisal":6666666666, 
    "Layla":7777777777}

#Defining a function that locate the key based on the value
def getkey(num):
  for key, value in directory.items():
    if num == value:
      return key

#As long as the asthe user inputs "Y", the program will continue to run
answer = "Y"
print(" ********** Welcome to the telephone directory **********\n ")
while answer == "Y":
  
  choice = input("Type 1 to search using a name\nor\nType 2 to search using a phone number\nor\nType 3 to add an entry\n")

#Case 1: The user is trying to find a phone number based on the user's name
  if choice == "1":
    direct_name = input("Please enter a name:\n").capitalize()
    if direct_name in directory:
      print(f"The phone number is: {directory[direct_name]}")
    else:
      print("Sorry, the user is not found")

#Case 2: The user is looking to find the name who's the phone number belongs to
  elif choice == "2":
    direct_num = int(input("Please enter the a phone number:\n"))
    if direct_num in directory:
      print(f"This phone number belongs to: {getkey(direct_num)}")
    elif len(str(direct_num)) > 10 or len(str(direct_num)) < 10:
      print("This is an ivalid number")
    else: 
      print("Sorry, the user is not found")

#Case 3: The user Will add an enrty to the phone directory
  elif choice == "3":
    name = input("Please enter the name of the user: ").capitalize()
    phone = int(input ("Please enter the phone number: "))
    directory[name]=phone
    print (f"Updated directory:\n{directory}\n")

#typing "N" will end the programm. "Y" will run it again
  answer = input(" ********** Type 'Y' to run again or 'N' to quit ********** ").upper()
  if answer == "N":
   break 
 
