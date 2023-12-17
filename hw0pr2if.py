# coding: utf-8
#
# hw0pr2if.py
#

""" 
Title for your adventure: Animal Adventure.

Notes on how to "win" or "lose" this adventure:
  Any Animal Wins.
  If you don't like animals you lose :(.
"""

def adventure():
    print()

    print("Hello Adventurer! Today you will be taken on a Journey through the Animal Kingdom")

    print()

    choice1 = input("Do you like animals(yes/no), if you say no then your adventure ends. ")

    # An if control structure (with no trailing elif nor trailing else at all)
    if(choice1 == "yes"):
        print()
        
        print("I like animals too!")

        print()

        choice2 = input("Do prefer creatures of the land, air, or sea(land, air, sea) ")

        # An if, elif, and else control structure (with exactly one elif)
        if(choice2 == "land"):
            print()

            print("Great choice the land has many intresting animals!")

            print()

            choice3 = input("Do you like mammals,bugs,reptiles, or amphibians(mammals,bugs,reptiles,amphibians) ")

            print()

            # An if, elif, elif, ... and else control structure (with at least two elifs and a trailing else)
            if(choice3 == "mammals"):
                print("Mammals are my favorite too!")

                print()

                print("Your animal of choice is the Red Panda")

            elif(choice3 == "bugs"):
                print("I hate bugs, but each to their own")

                print()

                print("Your animal of choice is the Bullet Ant")

            elif(choice3 == "reptiles"):
                print("Reptiles are cool but scary!")

                print()

                print("Your animal of choice is the Black Mamba")

            else:
                print("Amphibians are super intresting!")

                print()

                print("Your animal of choice is the Axolotl")


        elif(choice2 == "air"):
            print()

            print("Great choice the air has many intresting animals!")

            print()

            choice3 = input("Do you like birds(yes/no) ")

            print()

            # An if, else control structure (with zero elifs)
            if(choice3 == "yes"):
                print("Birds are cool!")

                print()

                print("Your animal of choice is the Peregrine Falcon")

            else:
                print("That's unfortunate, but there are other creatures that fly!")

                print()

                print("Your animal of choice is the Dragonfly")

        else:
            print()

            print("Great choice the sea has many intresting animals!")

            print()

            choice3 = input("Do you like fish(yes/no) ")

            print()

            # An if, elif, ... control structure (with one or more elifs but no trailing else at all)
            if(choice3 == "yes"):
                print("I also like fish, and they taste good too!")

                print()

                print("Your animal of choice is the Great White Shark")

            elif(choice3 == "no"):
                print("It's okay, fish are not for everyone")

                print()

                print("Your animal of choice is the Octopus")




