"""
CS 562 - Assignment 3 - Hero Villain
Author: Kellie Clark
Date: 2026-03-25
"""
from logic import *
# Source: Python docs - permutations() for generating all possible orderings - https://docs.python.org/3/library/itertools.html#itertools.permutations
from itertools import permutations

# Create propositional variables for each character matched with each political system.
# Character initials used to shorten unnecessarily long code
JH_Belters, JH_OPA, JH_MCRN, JH_UN = vars('JH_Belters', 'JH_OPA', 'JH_MCRN', 'JH_UN')
NN_Belters, NN_OPA, NN_MCRN, NN_UN = vars('NN_Belters', 'NN_OPA', 'NN_MCRN', 'NN_UN')
AK_Belters, AK_OPA, AK_MCRN, AK_UN = vars('AK_Belters', 'AK_OPA', 'AK_MCRN', 'AK_UN')
JM_Belters, JM_OPA, JM_MCRN, JM_UN = vars('JM_Belters', 'JM_OPA', 'JM_MCRN', 'JM_UN')

# Facts from the assignment spec that need to be in the KB
fact1 = JH_UN
fact2 = NN_Belters | NN_OPA
fact3 = ~JM_MCRN
hero_villain_kb = (fact1 & fact2 & fact3)

characters = ['JH', 'NN', 'AK', 'JM']
pol_system = ['Belters', 'OPA', 'MCRN', 'UN']

count = 1
# Use Permutations to create every possible combination of the political systems and loop through them
# Source: Python docs - permutations() for generating all possible orderings - https://docs.python.org/3/library/itertools.html#itertools.permutations
for perm in permutations(pol_system):
    char_pol_tv = {}
    # Use enumerate to assign an index to each character that can be match to a political system
    # Source: Python docs - enumerate() for getting index and value in a loop - https://docs.python.org/3/library/functions.html#enumerate
    for i, char in enumerate(characters):
        for system in pol_system:
            char_pol_tv[char + '_' + system] = (system == perm[i])
    # Constraints - check alongside the KB during evaluation - done this way for efficiency so we only build valid worlds
    if (exactly_one([char_pol_tv['JH_Belters'], char_pol_tv['JH_OPA'], char_pol_tv['JH_MCRN'], char_pol_tv['JH_UN']]) and
    exactly_one([char_pol_tv['NN_Belters'], char_pol_tv['NN_OPA'], char_pol_tv['NN_MCRN'], char_pol_tv['NN_UN']]) and
    exactly_one([char_pol_tv['AK_Belters'], char_pol_tv['AK_OPA'], char_pol_tv['AK_MCRN'], char_pol_tv['AK_UN']]) and
    exactly_one([char_pol_tv['JM_Belters'], char_pol_tv['JM_OPA'], char_pol_tv['JM_MCRN'], char_pol_tv['JM_UN']]) and
    exactly_one([char_pol_tv['JH_Belters'], char_pol_tv['NN_Belters'], char_pol_tv['AK_Belters'],
                 char_pol_tv['JM_Belters']]) and
    exactly_one([char_pol_tv['JH_OPA'], char_pol_tv['NN_OPA'], char_pol_tv['AK_OPA'], char_pol_tv['JM_OPA']]) and
    exactly_one([char_pol_tv['JH_MCRN'], char_pol_tv['NN_MCRN'], char_pol_tv['AK_MCRN'], char_pol_tv['JM_MCRN']]) and
    exactly_one([char_pol_tv['JH_UN'], char_pol_tv['NN_UN'], char_pol_tv['AK_UN'], char_pol_tv['JM_UN']])
    and hero_villain_kb.evaluate(**char_pol_tv)):
        # Verify valid pairs by printing results. - Two tables will print due to the different options for JM and NN
        # Source: CS 562 Assignment 2 - main.py, lines 72-75
        print(f"{'Results Table: Option ' + str(count) :^30}")
        print(f"{'Character' :<15} {'Political System' :<15}")
        print(f"{'James Holden' :<15} {perm[0]}")
        print(f"{'Alex Kamal' :<15} {perm[2]}")
        print(f"{'Joe Miller' :<15} {perm[3]}")
        print(f"{'Naomi Nagata' :<15} {perm[1]}")
        print()
        count += 1