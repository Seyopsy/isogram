# def is_isogram(word):
    # your code here
        #validation
    #An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
    # Implement a function that determines whether a string that contains only letters is an isogram.
    #  Assume the empty string is an isogram. Ignore letter case.
    
while True:
    # accepts input
    iso_word = str(input("Enter the Word to Check for Isogram ").lower().strip())
    if iso_word == "" :
        print("Yes, an empty word is also an anagram")
        continue

    # checks if input is valid (strictly letterss)    
    elif iso_word.isalpha() == True:
        print("You have entered " + "'" + iso_word + "'")
    else:
        print("Please enter a valid word")
        continue 

    #checks length of word and groups in sets 
    if len(iso_word) == len(set(iso_word)):
        print(iso_word, "is an isogram")
    else :
        print(iso_word, "is not an isogram")
    continue