__author__ = 'ssamanth'

reply = 1
while reply != 0:
    try:
        # Get the input from the user
        reply = int(input("Enter a positive integer, enter zero when complete:"))
        # Entering an integer that is less than 0
        if reply < 0:
            print("Your input is negative, try again")
        # Entering an integer that is greater than 0
        else:
            print("Your input is positive, your input doubled is", reply * 2)
    # entering anything other than an integer,including enter.
    except:
        print("You must enter an integer, try again")
