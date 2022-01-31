"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730467923"

secret: str = "python"
word: str = input("What is your 6-letter guess? ")

while len(word) != 6: 
    word = input("That was not 6 letters! Try again: ")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
count: int = 0
second_count: int = 0

output: str = ""
while count < len(word):
    second_count = 0
    if word[count] is secret[count]:
        output += GREEN_BOX
    else:
        exists: bool = False
        while second_count < len(word):
            if word[second_count] is secret[count]:
                output += YELLOW_BOX
                exists = True
                second_count = len(word) + 5
            second_count += 1
            
        if exists is False:
            output += WHITE_BOX
    count += 1

print(output)
if word == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")