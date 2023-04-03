Muzaffarhusain Turak mturak@stevens.edu

Url:https://github.com/tmuzu98/CS515Project

Estimate time spent: 10 hours

# a description of how you tested your code
Starting with the basic functionality of the code I tested it making sure that all the basline functionalities are running on the map provided in the project description such as go, get, inventory and quit verbs. Then making sure all the extention are working properly like the help verb is providing the list of all the possible commands in the game and since I could not name help as the name of the function I used show_help as the name of the function I used a conditional statement to print help. Finally coming towards the winning and losing condition testing this functionality took a lot of time testing all the possible conditions reaching to all the rooms and making sure reaching to the final room ie., Chamber of Secrets is possible through all the rooms in the map and the game prints the required output when the winning condition is reached and not otherwise. Meaning the user does not win if the winning condition is not reached.

# any bugs or issues you could not resolve
No

# an example of a difficult issue or bug and how you resolved
While ruuning the program using the terminal inside the project folder using the command "python3 adventure.py [map filename]" when running using this command and providing the game map in the command I was not able to invoke the game map in the code where I took the help of "ArgumentParser" imported from library "argparse" and then I was able to invoke the game map in the code and load the map in the game.
Next is the help function where I took the help of decorator called register to save the name of all the action verbs used. The register function in the code is a decorator that adds the decorated function to the valid_verbs dictionary, which is used to generate the help message for the game.
The significance of the register function is that it provides a clean and reusable way to add new commands to the game. By decorating functions with @register, we can add them to the valid_verbs dictionary without having to manually modify the dictionary every time a new command is added. This makes the code more modular and easier to maintain, since we can simply decorate a new function with @register to add it as a valid command. Additionally, the register function makes the code more readable, since it explicitly states that the function is being registered as a valid command for the game.So basically, show_help() dynamically generates a list of valid commands based on the functions that have been decorated with @register, and displays that list to the user. This makes it easy for the user to learn how to interact with the game.

# a list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them (i.e., what are the new verbs/features, how do you exercise them, where are they in the map)
Following is the list of three extentions that I have implemented in the code:
1. help verb -  The show_help() function is used to display a list of all the valid commands that the user can input in the game. Here's what it does:
    a. It creates an empty list called valid_verbs to store the names of all the valid commands.
    b. It then iterates through all the functions that have been decorated with @register (i.e., the go(), look(), get(), drop(), show_inventory(), and show_help() functions), and uses the inspect.getfullargspec() function to check if each function takes any arguments.
    c. If a function takes arguments, show_help() adds a ' ...' string to the end of its name to indicate that the user needs to provide additional input after the command. Otherwise, it just adds the function's name to valid_verbs.
    d. After all the functions have been processed, show_help() iterates through the valid_verbs list and prints each command name to the console, with some minor formatting.
    So show_help() basically compiles a list of valid instructions from the @register-decorated functions and presents it to the user. This facilitates a quick and painless introduction to the game's controls.
2. drop verb - The drop function is used to drop an item from the player's 
    inventory  and place it in the current room. It takes an item argument that specifies the name of the item to be dropped. If the item is in the player's inventory, it is removed from the inventory and added to the list of items in the current room. If the item is not in the player's inventory, a message is printed indicating that the item cannot be dropped because it is not in the inventory. If the item is successfully dropped, a message is printed indicating that the item has been dropped.
3. Winning and losing conditions - For the winning conditions the player has to  
    have  key in his inventory to reach the Chamber of Secrets which the primary objective of the game so if and only if the player has the key in his inventory then only he can get to the Chamber of Secrets and if the player does not have a key in his inventory the final Room ie., the Chamber of Secrets is locked and the player cannot enter the if not the game does not allow the user to enter the Chamber of Secrets. If yes Congratulations you have won the Game!!. Also I have included a small objective in the game where you need to get the love potion for Romilda to help her get the love potion and when you reach Chamber of Secrets along with the love potion. You have helped Romilda as well.

    For the losing condition if the player exceeds more than 20 moves using the go verb the engine prompts "No of attempts used {count}. You have used all of your attempts. Better Luck next time!!

Talking about the extentions it does not affect the core gamplay ie., when you run the game with the basic commands ie., go, look, get and help command it runs with the map provided in the project description. The EOFError is also handled in the code where the engine prompts the player to use quit to exit out of the game and everytime a new player starts the game it starts from the beginning of the game.
