#/usr/bin/env python3


#Welcome statement, always run

print("Kitchen conversions made easy!\n\nI can handle tsp, tbsp, cups, pints, quarts, gallons, floz, ml")

#create conversion table in nested dictionary

conversions = { 'tsp': {'tbsp': 1.0/3.0 , 'cups': 1.0/40.0 , 'pints': 1.0/96.0 , 'quarts': 1.0/192.0 , 'gallons': 1.0/768.0 , 'ml': 4.929 , 'floz': 1.0/6.0},
                'tbsp': {'tsp': 3.0 , 'cups':1.0/16.231 , 'pints': 1.0/32.0 , 'quarts': 1.0/64.0 , 'gallons': 1.0/256.0 , 'ml': 14.878, 'floz': 1.0/2.0},
                'cups': {'tsp': 48.692 , 'tbps': 16.231 , 'pints': 1.0/1.972 , 'quarts': 1.0/3.943 , 'gallons': 1.0/15.773 , 'ml': 240 , 'floz': 8.115},
                'pints': {'tsp': 96.0 , 'tbsp': 32.0 , 'cups': 1.972 , 'quarts': 1.0/2.0 , 'gallons':1.0/8.0 , 'ml': 473.0 , 'floz': 16.0},
                'quarts': {'tsp': 192.0 , 'tbsp': 64.0 , 'cups':3.943 , 'pints': 2.0 , 'gallons': 1.0/4.0 , 'ml': 946.353 , 'floz': 32.0},
                'gallons': {'tsp': 768.0 , 'tbsp': 256.0 , 'cups': 15.773 , 'pints': 8.0  , 'quarts': 4.0 , 'ml': 3785.41 , 'floz': 128.0},
                'ml':{'tsp': 1.0/4.929 , 'tbsp': 1.0/14.787 , 'cups': 1.0/240.0 , 'pints': 1.0/473.0 , 'quarts': 1.0/946.0 , 'gallons': 1.0/3785.0 , 'floz': 1.0/29.574},
                'floz':{'tsp': 6.0 , 'tbsp': 2.0 , 'cups': 1.0/8.115 , 'pints': 1.0/16.0 , 'quarts': 1.0/32.0 , 'gallons':1.0/128.0 , 'ml':29.574}
                }



#main function
def main():
    #attempt to make continuous loop
    #create function variables through user input

    key = input("What measurement do you have?")
    howmuch = float(input("How much do you have?"))
    value = input("What measurement do you want?")

        #check if the values are the same
    if key == value:
        print("These are the same measures, did you make a mistake?")
    #if the values are not the same, continue with conversion
    else:
        #use user inputs to pull conversion values from the dictionary
        result = howmuch * (conversions[key][value])

        #print the results to users
        print(result)

        #ask to do another
        #contcheck = input("Would you like to do another? Y/N \n")

        #thank the user for use upon exit
    print("Thank you for using my conversion table!")

main()
