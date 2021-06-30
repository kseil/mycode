#This script is edited from Challenge01.py
#get the count of numbers in the list
#countcap =int( input ("How many numbers do you have?"))

#take all the numbers for the list and compile them together.
list1 = []

counter = int(0)
while counter < 3:
  carry = int(input("Please list your next number: \n"))
  counter += int(1)
  list1.append(carry)

print(list1)
list1.reverse()
print(list1)
#set variables for first and last list locations
#first=list1[0]
#last= list1[-1]

#test the first and last numbers of the list for 6
#if list[0] == int(6) or list[-1] == int(6):
#   print("list is good")
#else:
#   print("list is not good")


#if first == 6 or last == 6:
#    print("list is good")
#else:
#    print("list is not good")

