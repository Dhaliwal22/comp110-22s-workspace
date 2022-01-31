"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730467923"

secret: str = "python"
wordle: str = input("What is your 6-letter guess? ")

while len(wordle) != 6: 
    wordle = input("That was not 6 letters! Try again: ")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
count: int = 0
second_count: int = 0

output: str = ""
while count < len(wordle):
    second_count = 0
    if wordle[count] is secret[count]:
        output += GREEN_BOX
    else:
        exists: bool = False
        while second_count < len(wordle):
            if wordle[second_count] is secret[count]:
                output += YELLOW_BOX
                exists = True
                second_count = len(wordle) + 5
            second_count += 1
            
        if exists is False:
            output += WHITE_BOX
    count += 1

print(output)
if wordle == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")