#!usr/bin/env python3

#Starting variables

#farenheit = 36
#celsius = (farenheit - 32)* 5/9

#celsius conversion function
def to_celsius():
    farenheit = input("What\'s the temperature outside?")
    farenheit = float(farenheit)
    celsius = (farenheit - 32) * 5/9
    print("It is", celsius, "degrees celsius outside.")
    return

#farenheit conversion function
def to_farenheit():
    celsius = input("What\'s the temperature outside?")
    celsius = float(celsius)
    farenheit = (celsius * 9/5) + 32
    print("It is", farenheit, "degrees farenheit outside.")
    return

#main function
#def main():
#    usrin = input("What are we converting F or C? To quit press Q.\n")
#    while usrin.lower() == "q":
#        break
#    while usrin.lower() != "q":
#        if usrin.lower() == "f":
#            temp = input("What is the temperature outside? \n")
#            temp = float(temp)
#            to_celsius(temp)
#            return
#        elif usrin.lower() == "c":
#            temp = input("What is the temperature outside? \n")
#            temp = float(temp)
#            to_farneheit(temp)
#            return
#        else:
#            print("Please choose C or F")
#            return



def main():
    answer=input("Are you converting from:\n 1) Celsius to Farenheit \n or \n 2) Farenheit to Celsius \n Press Q to quit at any time \n")
    while answer == 'q':
        break
    while answer == '1':
        to_farenheit()
    while answer == '2':
        to_celsius()

main()
