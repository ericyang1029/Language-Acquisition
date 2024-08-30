import random
import itertools
anschoice = {0:"A", 1:"B", 2:"C", 3:"D"}
""" For generating the 'after' multiple choice questions"""


"""
A
1: After personA entered the indoor_space, personA is ___ indoor_space.
A: in
B: above
C: on
D: under

wrote in the file in permute_in_inside
"""
def permute_1(personA, indoor_space, spatial_terms):
    prep = "in"
    spatial_terms.remove("in")
    # choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
    choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
    answ = [choiceA, choiceB, choiceC, "in"]
    text = ""
    for p in personA:
        for space in indoor_space:
            # shuffle the answer choice
            random.shuffle(answ)
            # pA = random.choice(personA)
            # insp = random.choice(indoor_space)
            idx_in = answ.index("in")
            text += (
              f"{anschoice[idx_in]}\n"
              f"After {p} entered the {space}, {p} is ___ {space}.\n"
              f"A: {answ[0]}\n"
              f"B: {answ[1]}\n"
              f"C: {answ[2]}\n"
              f"D: {answ[3]}\n\n"
              )
    return text





"""2: Obj A is on flat_things_A, ObjB is under flat_things_A
   Question: Obj A is ___ Obj B. And Obj B is ___ Obj A.

   A: under
   B: above
   C: beside
   D: in
"""


