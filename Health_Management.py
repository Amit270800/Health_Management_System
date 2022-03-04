# Health Management System
"""
Manage you health by monitoring daily exercise and diet with help of files
Log and retrieve the data as per different client
"""

def getdate(): # To get live date and time while updating data
    import datetime
    return datetime.datetime.now()

def put_exercise(client,exercise): # To log in the exercise of client
    a = open(client + "_exercise.txt","a")
    a.write('[' + str(getdate()) + '] - ' + exercise + "\n")
    a.close()
    print("You successfully logged the Data")
    print()

def put_diet(client,diet): # To log in the diet of client
    a = open(client + "_diet.txt","a")
    a.write('[' + str(getdate()) + '] - ' + diet + "\n")
    a.close()
    print("You successfully logged the Data")
    print()

def get_exercise(client): # To retrieve the exercise of client
    a = open(client + "_exercise.txt")
    print(a.read())
    a.close()

def get_diet(client): # To retrieve the diet of client
    a = open(client + "_diet.txt")
    print(a.read())
    a.close()


print("Enter Client Name: ", end="")
client = input()
print()

k = 'y'
while(k == 'y' and k != 'n'):
    print("What would you like to do?")
    print("Enter your choice: \n1. Log \n2. Retrieve")
    ac = int(input())
    print()

    print("What data?")
    print("Enter your choice: \n1. Exercise \n2. Diet")
    ch = int(input())
    print()

    if ac == 1: # Log the data
        if ch == 1: # Log exercise data
            print("Enter the exercise you want to enter: ", end="")
            exercise = input()
            put_exercise(client, exercise)
            print("Would you like to add more or retrieve the data(y/n): ")
            k = input()
            k.lower()
            print()
            continue
        elif ch == 2: # Log diet data
            print("Enter the diet you want to enter: ", end="")
            diet = input()
            put_diet(client, diet)
            print("Would you like to add more or retrieve the data (y/n): ")
            k = input()
            k.lower()
            print()
            continue
        else:
            print("Enter correct choice")

    elif ac == 2: # Retrieve the data
        if ch == 1: # Retrieve exercise data
            get_exercise(client)
            break
        elif ch == 2: # Retrieve diet data
            get_diet(client)
            break
        else:
            print("Enter correct choice")

    else:
        print("Enter correct choice")