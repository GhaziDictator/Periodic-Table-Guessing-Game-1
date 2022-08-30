import random

#to define the function for the game 

def main():
    """Start a element guessing game."""
    print("Guess the element!")

#to tell the function the elements to keep

    element = [
        "Hydrogen",
        "Iron",
        "Lithium",
        "Beryllium",
        "Boron",
        "Carbon",
        "Nitrogen",
        "Oxygen",
        
        ]

#to ask the function to choose a random elements

    x = random.choice(element)
    guess = None

#to give the player another chances if their answers are wrong

    while x != guess:

        guess = str(input("What element am I thinking of? "))
        
#to tel the player that they got it right
        
        if x == guess:
            print("You guessed it right. Congratulations you got it right!".format(guess))
            break

#to tell the player clues if they got it wrong

        elif x == "Hydrogen":
            print("The atomic radius for this element is 120 pm.")
        elif x == "Iron":
            print("The atomic radius for this element is 194 pm.")
        elif x == "Lithium":
            print("The atomic radius for this element is 182 pm.")
        elif x == "Beryllium":
            print("The atomic radius for this element is 153 pm.")
        elif x == "Boron":
            print("The atomic radius for this element is 192 pm.")
        elif x == "Carbon":
            print("The atomic radius for this element is 170 pm.")
        elif x == "Nitrogen":
            print("The atomic radius for this element is 155 pm.")
        elif x == "Oxygen":
            print("The atomic radius for this element is 152 pm.")
        

main()

