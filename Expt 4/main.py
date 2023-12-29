import re

#regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

contact_application = {}

print("Guidelines:")
print("Type I to enter the details of new contact\nType S to search for details of a person\nType D to delete existing contact")
print("Type U to update a contact\nType P to print the details of existing contact\nType E to exit the application")

def home():
    print("HOME\nWelcome to contact_application")

def insert():
        print("Enter your details")
        name=input("name: ")
        contact_no=int(input("contact_no.: "))
        email_id=input("Email-id: ")
        
        if re.match(r"[^@]+@[^@]+\.[^@]+", email_id):  
            age=int(input("Age: "))
            birth_day=input("D.O.B: ")
            contact_application[name] = {
            "Contact no.:" : contact_no,
            "Email-Id:" : email_id,
            "Age:" : age, 
            "Birth-Day": birth_day
             }
        
        else:
            email_id1=input("Wrong email address, please enter the correct one: ")
            age=int(input("Age: "))
            birth_day=input("D.O.B: ")
            contact_application[name] = {
            "Contact no.:" : contact_no,
            "Email-Id:" : email_id1,
            "Age:" : age, 
            "Birth-Day": birth_day
            }
    
def search():
    search = input("Enter the name of the person: ")
    print(contact_application[search])

def print_dict():
    if(not contact_application):
        print("Sorry!! can't display anything since the dictionary is empty ")
    else:
        print(contact_application)

def delete():
    if(not contact_application):
        print("Sorry!! can't delete anything since the dictionary is empty ")
    else:
        detail=input("Enter contact you want to delete detail of: ")
        del contact_application[detail]
        a=input("Do you want to see the revised contact_application (y/n) ")
        if(a=='y'):
            print(contact_application)
        else:
            home()

def update():
    if(not contact_application):
        print("Sorry!! can't update anything since the dictionary is empty ")
    else:
        detail = input("Enter the details of contact you want to update: ")
        del contact_application[detail]
        print("Now Again")
        insert()
        a=input("Do you want to see the revised contact_application (y/n) ")
        if(a=='y'):
            print(contact_application)
        else:
            home()

while(True): 
    
    user = input("Enter the action you want to perform according to the guidelines: " )
    
    if(user == 'I'):
        insert()

    elif(user == 'S'):
        search()
    
    elif(user == 'P'):
        print_dict()
        
    elif(user == 'D'):
        delete()

    elif(user == 'E'):
        break
    
    elif(user == 'U'):
        update()
        
        










