# Anirudh Gupta

# 11/26/23

# This is the started code for the Picobot Final Project

# The goal of this project is to write a genetic algorithm 
# that writes a program that can solve a picobot maze

import random

HEIGHT = 25
WIDTH = 25
NUMSTATES = 5

POSSIBLE_SURROUNDINGS = ['xxxx','Nxxx','NExx','NxWx','xxxS','xExS','xxWS','xExx','xxWx']

class Program:
    def __init__(self):
        """Constructor for Program Objects
           Does not take any arguments
           Programs only have a rules attribute which is a dictionary
        """ 
        self.rules = {}

    def __repr__(self):
        """Represents the rules in a program object in a sorted order
        """
        unsortedKeys = list(self.rules.keys()) 
        sortedKeys = sorted(unsortedKeys)

        sortedRules = ""
        for x in range(len(self.rules)):
            if(len(sortedRules) > 0 and sortedRules[-14] != str(sortedKeys[x][0])):
                sortedRules += "\n"
            sortedRules += str(sortedKeys[x][0]) + " " + sortedKeys[x][1] + " -> " + self.rules[sortedKeys[x]][0] + " " + str(self.rules[sortedKeys[x]][1]) + "\n"

        return sortedRules

    def randomize(self):
        """Generates a random, full set of rules for the rules dictionary
        """
        for x in range(NUMSTATES):
            for y in POSSIBLE_SURROUNDINGS:
                possible_steps = []
                for step in 'NEWS':
                    if step not in y:
                        possible_steps += [step]
                self.rules[(x, y)] = (random.choice(possible_steps), random.randint(0, NUMSTATES - 1))

