#Create a new variable to check for palindromes and print to verify.

palindrome = str(input("Please enter a word or name here: \n"))
#print(palindrome)

rpalindrome = palindrome [::-1]
print(rpalindrome)

#comparative if statement

if palindrome == rpalindrome:
    print("this is a palindrome")
else:
    print("this is not a palindrome")


