"""EX01 - Chardle - A cute step towards wordle."""

__author__ = "730467923"
 

word: str = str(input("Enter a 5-character word: "))
length = len(word)

isfive: bool = True
if length != 5:
    print("Error: Word must contain 5-characters")
    isfive = False
    
if isfive is True:
    letter: str = str(input("Enter a single character: "))
    l_length = len(letter)
    if l_length > 1:
        print("Error: Character must be a single character.")
    else:
        print("Searching for " + letter + " in " + word)  

    index: int = 0
    instances = int(index)

    count: int = 0

    if letter is word[0]:
        print(letter + " found at index " + str(index))
        count = count + 1
        index = index + 1     
    else:
        index = index + 1

    if letter is word[1]:
        print(letter + " found at index " + str(index))
        count = count + 1
        index = index + 1     
    else:
        index = index + 1

    if letter is word[2]:
        print(letter + " found at index " + str(index))
        count = count + 1
        index = index + 1     
    else:
        index = index + 1

    if letter is word[3]:
        print(letter + " found at index " + str(index))
        count = count + 1
        index = index + 1     
    else:
        index = index + 1

    if letter is word[4]:
        print(letter + " found at index " + str(index))
        count = count + 1
        index = index + 1     
    else:
        index = index + 1

    if (count == 1):
        print(str(count) + " instance of " + letter + " in " + word)
        
    if (count > 1):
        print(str(count) + " instances of " + letter + " in " + word)
    else:
        print("No instances of " + letter + " found in " + word)
