contacts={}

def add_contact():
    name=input("enter name:")
    phone=input("enter phone number:")
    contacts[name]=phone
    print("contact added! ")

def view_contacts():
    if contacts:
      for name, phone in contacts.items():
         print(f"{name}: {phone}")
    else:
       print("contact not found")

def search_contact():
   name=input("enter name to search:")
   if name in contacts:
      print(f"{name}:{contacts[name]}")
   else:
      print("contact not found")

def update_contact():
   name=input("enter name to update:")
   if name in contacts:
      phone=input("enter new phone number:")
      contacts[name]=phone
      print("contact updated!")
   else:
      print("contact not found")

def delete_contact():
   name=input("enter name to delete:")
   if name in contacts:
      del contacts[name]
      print("contact deleted!")
   else:
      print("contact not found")

while True:
   print("---contact Book Menu---")
   print("1.Add Contact")
   print("2.View Contact")
   print("3.Search Contact")
   print("4.Update Contact")
   print("5.Delete Contact")
   print("6.Exit") 

   choice= input("enter choice:")

   if choice=="1":
      add_contact()
   elif choice=="2":
      view_contacts()  
   elif choice=="3":
      search_contact()
   elif choice=="4":
      update_contact()
   elif choice=="5":
      delete_contact()
   elif choice=="6":
    print("exiting...Goodbye!")
    break
   else:
      print("Invalid choice,please try again")                                 