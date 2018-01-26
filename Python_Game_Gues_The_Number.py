import random
number = random.randint(1,20)

print ("Whats is your Name?")

username = input()

print ("Hello " + str(username) + ", I'm thinkig about number between 1-20, try and guest it. You gave only 6 try" )
# u_number = input()
def getAnswer():

    i = 0
    global number

    while i < 3:
        u_number = input()

        try:
            if int(u_number) > int(number):
                print("more")
            elif int(u_number) < int(number):
                print("less")
            else:
                print("You are correct")
                break
            i = i + 1

        except ValueError:
            
            print ('You did not enter a number')
            # continue


getAnswer()

