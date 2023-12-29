
def open_file():
    file = open("data.txt", "r")
    content = file.read()
    print("\n")
    print(content)

def exit():
    file = open("data.txt")
    file.close()

def appending():
    file = open("data.txt", "a")
    text = input("\nEnter the text you want to write:\n")
    file.write("\n")
    file.write(text)
    file.close()

def writing():
    file = open("data.txt", "w")
    text = input("\nEnter the text you want to write:\n")
    file.write("\n")
    file.write(text)
    file.close()
   
print("O  --->  opening the file in read mode ")
print("C  --->  closing the file")
print("E  --->  exiting the menu")
print("W  --->  writing in the file")
print("A  --->  appending in the file")


while (1):
    a=input("\nEnter the action you want to peform: ")

    if(a == 'O'):
        open_file()

    elif(a == 'C'):
        exit()

    elif(a == 'W'):
        writing()
        ans = input("Do you want to see the edited file? (y/n): ")
        if(ans == 'y'):
            print("\nAfter writing the file is:")
            open_file()

    elif(a == 'A'):
        appending()
        ans = input("Do you want to see the edited file? (y/n): ")
        if(ans == 'y'):
            print("\nAfter appending the file is:")
            open_file()
 
    elif(a == 'E'):
        break


        
        
# hellllooooo!!!
# Siddhi here
# Peforming file handling in python
#python is the easiest programming language to learn.