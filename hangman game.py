
print("\n\n")
print("\t\t\tWelcome to the hangman game :D ")
print("\t\t\t\t\tCoded By D4az")
name= str(input("Enter Your Name : "))
print("\n\n")

print("\t\t\t\t\tWelcome "+name)
print("-----------------------------------------------------------------------------------------------\n")

word ="hello"

guess = ''
times = 0

while times < 10:
    main = ""
    missed = 0

    for letter in word:
            if letter in guess:
                main = main + letter
            else:
                main = main + "_" + " "
    if(main == word):
        print("\t\tYou won the game!\n\n")
        break

    print("\n\n")
    print("Guess the word \n\n", main)
    print("\n")
    guess=input()


    if guess not in word:
            times = times+1
    
    if(times == 1):
        print("\n")
        print("\n_______________\n\n")

    if(times ==2 ):
        print("\n")
        print("\n_______________")
        print("       0        \n\n")

    if(times ==3 ):
        print("\n")
        print("\n_______________")
        print("       0        ")
        print("       |        \n\n")

    if(times ==4 ):
        print("\n")
        print("\n_______________")
        print("       0        ")
        print("       |        ")       
        print("       |       \n\n")
    
    if(times ==5 ):
        print("\n")
        print("\n_______________")
        print("       0        ")
        print("       |        ")       
        print("       |        ")
        print("      /         \n\n")
    if(times ==6 ):
        print("\n")
        print("\n_______________")
        print("       0        ")
        print("       |        ")       
        print("       |        ")
        print("      / \        \n\n")  

    if(times ==7):
        print("\n_______________")
        print("       0        ")
        print("      /|        ")       
        print("       |        ")
        print("      / \        \n\n")          


    if(times ==8 ):
        print("\n")
        print("\n_______________")
        print("       0        ")
        print("      /|\        ")       
        print("       |        ")
        print("      / \        \n\n")          

    if(times ==9 ):
        print("\n")
        print("\n_______________")
        print("       0----     ")
        print("      /|\        ")       
        print("       |        ")
        print("      / \        \n\n")   

    if(times ==10 ):
        print("\n")
        print("\n_______________")
        print("       0_____     ")
        print("      /|\   |   'You Loose' ")       
        print("       |    |   ")
        print("      / \   |    \n\n")          


