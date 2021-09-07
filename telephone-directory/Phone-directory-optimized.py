directory = {
  1111111111:"Amal",
  2222222222:"Mohammed",
  3333333333:"Khadijah",
  4444444444:"Abdullah",
  5555555555:"Rawan",
  6666666666:"Faisal",
  7777777777:"Layla"
}

def getkey(nm):
  for key, value in directory.items():
    if nm == value:
      return key

end = False
while not end:
    print("To search using a phone number, type '1'")
    print("To search using a name, type '2'")
    print("To add an entry, type '3'")
    print("Or to quit, type '4'\n\n")
    choice = input("Please choose the required service: ")

    if choice == "4":
      end = True
      print("Thank you for using the phone directory")

    elif choice == "1":
      phone_num = int(input("Please enter a phone number: "))
      if len(str(phone_num)) == 10 and phone_num in directory:
          print(f"This phone number belongs to: {directory[phone_num]}\n\n")
      elif len(str(phone_num)) == 10 and phone_num not in directory:
          print("Sorry, the number is not found\n\n")
      else:
          print("This is an invalid number\n\n")

    elif choice == "2":
      name = input("Please enter a name: ").capitalize()
      if getkey(name) in directory:
        print(f"The phone number is {getkey(name)}\n\n")
      else:
        print("Sorry, this user is not in the phone directory")

    elif choice == "3":
      name_entry = input("Please enter a name: ").capitalize()
      number_entry = int(input("Please enter a phone number: "))
      directory[number_entry] = name_entry
      print(f"Directory updated: {directory}\n\n")
