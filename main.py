import networkx as nx
import numpy as np


# Start of the program
def main():
    # Creating a digraph for each of the decisions
    decisions_digraph = create_decisions_digraph()

    # Each index of the array will correlate with the decision in the digraph
    # Each decision can have up to 2 narratives
    narrative = create_narrative()

    # create an array with all of the decisions
    decisions = create_decisions()

    # Start of the program
    current_node = 0
    print("How to Play:")
    print("-----------------------------------------------------")
    print("1. Type either \"1\" or \"2\" to select your decision")
    print("2. Hit enter to move past the dialog")
    print("-----------------------------------------------------")
    print_dialog("Enjoy the game!")
    print("-----------------------------------------------------")

    is_last_node = False

    while (is_last_node == False):
        if (len(list(decisions_digraph.successors(current_node))) == 0):
            is_last_node = True

        print_dialog(narrative[current_node][0]) # there will always be at least 1 narrative.

        if(narrative[current_node][1] != None):
            print_dialog(narrative[current_node][1])

        print()
        print(decisions[current_node])

        choice = 0 # resets the choice

        while not (choice == 1 or choice == 2):
            try:
             choice = int(input())

             if ((choice == 1 or choice == 2) and is_last_node == False): # Reassigns the current node to the node from the decision
                 current_node = list(decisions_digraph.successors(current_node))[choice - 1]
             elif (is_last_node == True):  # User reaches the end of the game
                 print()
                 endings = create_ending()
                 print(endings[current_node][choice-1])
                 print("-----------------------------------------------------")
                 print("Please purchase the full game to continue playing...")
             else:  # User enters wrong number.
                 print("You must enter 1 or 2:")
            except: # int cast makes it so it has to be in a try catch for different data types
                print("You must enter 1 or 2:")

# Creates a hashmap where the key is the node and the value is an array of the two outcomes.
# Follows the last node in each path
def create_ending():
    return {
        7: ["*The slime is quicker than anticipated*\n"
            "*Your sword hardly misses. The slime slams into you with all of its might*\n"
            "*Your vision slowly starts to fade*",
            "*The slime wizzes by your ear, narrowly missing*\n"
            "*You quickly turn around, following the slime out of the corner of your eye*"],
        8: ["*You walk down the left path. Hearing a rustle in the bush, you quickly turn*\n"
            "*A group of bandits walk out of the trees...*",
            "*Walking down the right path you see a black lotus just a few feet off of the path*\n"
            "*Luck is on your side today!!*"],
        4: ["*You walk around town, exploring the market*\n"
            "*As you walk down the alley you hear a sound behind you*\n"
            "*Suddenly a bag appears over your head and everything goes dark...*",
            "*You eat at the Inn and promptly fall asleep*"],
        9: ["*You proceed to fill up everyone's water*\n"
            "*Setting off in the direction of the dungeon, you think about what went wrong*",
            "*Everyone busts out laughing*\n"
            "You've got guts *someone exclaims!*\n"
            "*You are welcomed to the party*"],
        10: ["*As you cast a spell, your magic is amplified to a degree you didn't know was possible*",
             "*As you cast a spell, nothing happens... Suddenly your vision goes black*"],
        6: ["*Running around the corner, you see the figure jump back into a dark alley way...*",
            "It's him *one of the gaurds yells at you...*\n"]
    }

# Comes before each decision/node
def create_narrative():
    # Max of 2 possible narratives. Left as None if you only want one narrative
    return np.array([
        ["Welcome, brave adventurer! We're thrilled to have you \n"
         "interested in joining the Adventure Guild.\n"
         "Our organization is always seeking new members to join \n"
         "us in our quest for discovery and excitement.",
         "To get started, we just need to know what class you are!"]
        ["Oh a warrior I see! Would you like to sign up for a quest at this time?", None],
        ["A Sorcerer?!?!?! We don't see many of your specialty \n"
         "around here these days.\n\n"
         "*You waive off the excitement and hurry to complete the paperwork* ",
         "*An Adventurer approaches you from across the room as you turn away from the desk*\n"
         "I heard you're a Sorcerer, we could really use one in our party..."],
        ["Awesome! We have a few different options. Which looks the best to you?", None],
        ["Understandable, have a good day!\n"
         "*You exit the guild building*", None],
        ["Great! We are meeting tomorrow morning in front of the guild... We will see you then!\n"
         "*Night passes*",
         "*The following morning you meet out front of the guild...*\n"
         "*As you introduce yourself to the party, someone asks what your affinity is*"],
        ["That's a bummer! If you ever change your mind dont hesitate to reach out.\n"
         "*You leave the guild*",
         "*Outside, you suddenly get shoved to the side as a hooded figure runs past*\n"
         "*Looking back, you see a party of city gaurds running in your direction*"], 
        ["*You venture out to the countryside...*\n"
         "*Seeing a slime you slowly start to approach...*",
         "*Raising your sword ready to attack, it suddenly bounces towards you...*"],
        ["*You venture out to the countryside..*",
         "*Seeing a split in the path you have to options...*"],
        ["*You are given the role of water boy in the party*",
         "Fill up my water waterboy *orders one of the members*"],
        ["*You're re given the role of rear support in the party*",
         "Is that all of the gear you have *One of the party members says to you*\n"
         "Lets go buy you some new gear in the town\n"
         "*You show up to the blacksmiths*\n"
         "Go and pick out a new wand"]
    ])

# Prompt that gives the user the option for their decisions.
def create_decisions():
    return np.array([
        "Choose Class:\n1: Warrior \n2: Sorcerer",
        "Sign up for a quest:\n1: Yes \n2: No",
        "Join the adventurers party:\n1: Yes \n2: No",
        "Choose a quest:\n1: Hunt slimes \n2: Look for rare herbs",
        "What would you like to do:\n1: Explore the market \n2: Go back to the Inn",
        "Choose your affinity:\n1: Water \n2: Wind",
        "What would you like to do:\n1: Chase the figure \n2: Stay in place and let the gaurds pass",
        "What would you like to do:\n1: Swing your sword \n2: Doge the slime",
        "Which path would you like to go down:\n1: Left \n2: Right",
        "What would you like to do:\n1: Fill up his water\n2: Spray him with water",
        "Which wand would you like to purchase: \n1: A gorgeous wand cover with various gems and jewels \n2: A precarious wand with strange engravings",
    ])
def create_decisions_digraph():
    digraph = nx.DiGraph()
    # Add 10 nodes
    digraph.add_node(0)
    digraph.add_node(1)
    digraph.add_node(2)
    digraph.add_node(3)
    digraph.add_node(4)
    digraph.add_node(5)
    digraph.add_node(6)
    digraph.add_node(7)
    digraph.add_node(8)
    digraph.add_node(9)
    digraph.add_node(10)

    # Add edges
    digraph.add_edge(0, 1)
    digraph.add_edge(0, 2)

    digraph.add_edge(1, 3)
    digraph.add_edge(1, 4)

    digraph.add_edge(2, 5)
    digraph.add_edge(2, 6)

    digraph.add_edge(3, 7)
    digraph.add_edge(3, 8)

    digraph.add_edge(5, 9)
    digraph.add_edge(5, 10)

    return digraph

def print_dialog(dialog):
    print()
    print(dialog)
    input("Press enter to continue... ")

main()
