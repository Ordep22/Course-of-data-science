import random
from os import system, name

#Function to clear the sreen in the interations
def ClearScreen():

    #print(name)

    #On windows
    if name == 'nt':
        _ = system('cls') ## '_' informs that the returned information will not be used

    #On Mac and linux
    '''
    _ = system('clear')
    '''
def DisplayHangman(chance):

        # Lista de estágios da forca
        stages = [  # estágio 6 (final)
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            # estágio 5
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            # estágio 4
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            # estágio 3
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            # estágio 2
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            # estágio 1
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            # estágio 0
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """
        ]
        return stages[chance]

def Game():

    findLetter = []

    #Clear the acreen
    ClearScreen()

    print("\nWell come to the Hangman game!")
    print("Guess the word bellow")

    #list of words in the game
    words  = ["banana","abacate","uva","morango","laranja"]

    #Choice ramndon word in list words

    word = random.choices(words)

    #List comprehension
    #findLetter = ['_' for i in word]
    for i in word[0]:

        findLetter.append("_")


    #Number of chances
    chance = 6

    #List of wrong words
    wrongLetter = []


    while chance >=0:

        #print(findLetter)

        #print("Wrong letter ".join(wrongLetter))

        print(DisplayHangman(chance))

        print("\nRemaining chances ", chance)

        if (chance == 0):
            break

        print("\n")

        print(findLetter)

        print("\n")




        attempts = input("\nInsert a letter:").lower()


        if attempts in word[0]:
            index = 0

            for letter in word[0]:
                if attempts == letter:
                    findLetter[index] = attempts
                index += 1

        else:
            chance -= 1
            wrongLetter.append(attempts)


        if "_" not in findLetter:
            print(f"You win, the word was: {word[0]}")
            break


    if "_" in findLetter:
        print(f"You louse, the word was: {word[0]}")


#Main bloc

if __name__ == "__main__":

    Game()
    print("\nWell done. You lear code Python!")






