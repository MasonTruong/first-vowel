#Compares a string with vowels and displays up the first vowel found
print("Enter in anything: ")
word = input()  #string to modify
uptoFirstVowel = ""
vowels = "aeiouAEIOU"
foundVowel = False

#compares character in word to vowels. Stops when the first instance of a vowel is found
for x in word:
    for y in vowels:
        if x == y:  #add character first, then end loop
            uptoFirstVowel += x
            foundVowel = True
            break
        if y == vowels[-1]: #add character at end of loop
            uptoFirstVowel += x    

    if foundVowel == True:
        break

print("")
print("Original: " + word)
print("Stops at vowel: " + uptoFirstVowel)