print("\n\tWELCOME TO THE LETTER COUNT APP")

def usr_input():
    try:
        usr_name=input("\n\tEnter your username: ")
        print("\n\tHello {}!\n\tI will count the number of times that a specific letter occurs in a message.".format(usr_name))
        usr_mssg = input("\n\tPlease enter a message: ")
        letter_count = input("\tWhich letter would you like to count the occurrences of: ")
        letter_count = letter_count.lower()
        usr_mssg = usr_mssg.lower()
        return letter_count,usr_mssg,usr_name
    except ValueError:
        print("\n\tPlease enter correct information!!")

def letter_count(usr_mssg,letter_count,name):
    count = 0
    usr_mssg = usr_mssg.split()
    for i in usr_mssg:
        for j in i:
            if j == letter_count:
                count = count+1
    print("\n\t{}, your message has {} h's in it".format(name,count))

#MAIN PROGRAM
usr_data = usr_input()
letter_count(usr_data[1],usr_data[0],usr_data[2])

while True:
    condn = input("\n\tDo you want to continue with the application? (y/n): ")
    if condn.lower() == "y":
        usr_data = usr_input()
        letter_count(usr_data[1],usr_data[0],usr_data[2])
    else:
        print("\n\tTHANK YOU")
        break