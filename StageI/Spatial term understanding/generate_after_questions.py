import random
import itertools
anschoice = {0:"A", 1:"B", 2:"C", 3:"D"}
""" For generating the 'after' multiple choice questions"""


"""
A
1: After personA enter the indoor_space, personA is ___ indoor_space.
A: in
B: above
C: on
D: under
"""
def generate_in(personA, indoor_space, spatial_terms):
    possible_asw = ["in", "inside"]
    for i in possible_asw:
        spatial_terms.remove(i)
    # choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
    text = ""
    for p in personA:
        for space in indoor_space:
            choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
            prep = random.sample(possible_asw, 1)[0]
            answ = [choiceA, choiceB, choiceC, prep]
            # shuffle the answer choice
            random.shuffle(answ)
            # pA = random.choice(personA)
            # insp = random.choice(indoor_space)
            idx_in = answ.index(prep)
            text += (
              f"{anschoice[idx_in]}\n"
              f"After {p} enter the {space}, {p} is ___ {space}.\n"
              f"A: {answ[0]}\n"
              f"B: {answ[1]}\n"
              f"C: {answ[2]}\n"
              f"D: {answ[3]}\n\n"
              )
    return text

"""
C
1: After personA leave the indoor_space, personA is ___ indoor_space.
A: in
B: above
C: outside
D: under
"""
def generate_outside(personA, indoor_space, spatial_terms):
    # remove in and other distracting possible answers
    for i in ["near", "outside"]:
        spatial_terms.remove(i)
    # choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
    text = ""
    for p in personA:
        for space in indoor_space:
            choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
            answ = [choiceA, choiceB, choiceC, "outside"]
            # shuffle the answer choice
            random.shuffle(answ)
            # pA = random.choice(personA)
            # insp = random.choice(indoor_space)
            idx_in = answ.index("outside")
            text += (
              f"{anschoice[idx_in]}\n"
              f"After {p} leave the {space}, {p} is ___ {space}.\n"
              f"A: {answ[0]}\n"
              f"B: {answ[1]}\n"
              f"C: {answ[2]}\n"
              f"D: {answ[3]}\n\n"
              )
    return text

"""
C
1: After personA raises obj1 vertically from the flat_place, obj1 is ___ flat_place.
A: in
B: above
C: on
D: under
"""
def generate_above(personA, flat_things_A, spatial_terms, objects):
    possible_asw = ["above", "over"]
    for i in possible_asw:
        spatial_terms.remove(i)
    # choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
    text = ""
    name = random.sample(personA, 5)
    for p in name:
        for obj in objects:
            for ft in flat_things_A:
              # randomly sampled choices
                choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
                prep = random.sample(possible_asw, 1)[0]
                answ = [choiceA, choiceB, choiceC, prep]
                # shuffle the answer choice
                random.shuffle(answ)
                # pA = random.choice(personA)
                # insp = random.choice(indoor_space)
                idx_in = answ.index(prep)
                text += (
                f"{anschoice[idx_in]}\n"
                f"After {p} raises {obj} vertically from the {ft}, {obj} is ___ {ft}.\n"
                f"A: {answ[0]}\n"
                f"B: {answ[1]}\n"
                f"C: {answ[2]}\n"
                f"D: {answ[3]}\n\n"
                )
    return text

"""
D
1: After personA raises obj1 vertically from the flat_place, flat_place is ___ obj1.
A: in
B: above
C: on
D: under
"""
def generate_under_s(personA, flat_things_A, spatial_terms, objects):
    possible_asw = ["beneath", "under", "near", "underneath"]
    for i in possible_asw:
        spatial_terms.remove(i)
    # choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
    text = ""
    name = random.sample(personA, 5)
    for i in name:
        p = personA[i]
        for obj in objects:
            for ft in flat_things_A:
              # randomly sampled choices
                choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
                prep = random.sample(possible_asw, 1)[0]
                answ = [choiceA, choiceB, choiceC, prep]
                # shuffle the answer choice
                random.shuffle(answ)
                # pA = random.choice(personA)
                # insp = random.choice(indoor_space)
                idx_in = answ.index(prep)
                text += (
                f"{anschoice[idx_in]}\n"
                f"After {p} raises {obj} vertically from the {ft}, {ft} is ___ {obj}.\n"
                f"A: {answ[0]}\n"
                f"B: {answ[1]}\n"
                f"C: {answ[2]}\n"
                f"D: {answ[3]}\n\n"
                )
    return text

"""
    A
    Alice is at school. Alice wants to go to market. market is 1000 miles from school."
    school is ___.\n"
    A: far
    B: near
    C: close
    D: in
"""
def generate_far1(personA, places, spatial_terms):
    possible_asw = ["far", "away", "faraway"]
    for i in possible_asw:
        spatial_terms.remove(i)
    # choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
    text = ""
    # randomly sample 2 names
    name = random.sample(personA, 4)
    # all combination of places 20C2
    combinations = list(itertools.combinations(places, 2))
    for n in name:
        for place1, place2 in combinations:
            choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
            prep = random.sample(possible_asw, 1)[0]
            answ = [choiceA, choiceB, choiceC, prep]
            # shuffle the answer choice
            random.shuffle(answ)
            # pA = random.choice(personA)
            # insp = random.choice(indoor_space)
            idx_in = answ.index(prep)
            miles = random.randint(1000, 2000)
            text += (
            f"{anschoice[idx_in]}\n"
            f"{n} is at {place1}. {n} wants to go to {place2}. {place2} is {miles} miles from {place1}."
            f"{place2} is ___.\n"
            f"A: {answ[0]}\n"
            f"B: {answ[1]}\n"
            f"C: {answ[2]}\n"
            f"D: {answ[3]}\n\n"
            )
    return text

"""
    B
    obj1 is on the left of obj2, obj3 is on the right of obj2. obj2 is ___ obj1 and obj2.
    A: down
    B: between
    C: at
    D: beyond
"""

def generate_between(objects, spatial_terms):
    possible_asw = ["between"]
    for i in possible_asw:
        spatial_terms.remove(i)
    # choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
    text = ""
    # all combination of places 20C2
    combinations = list(itertools.combinations(objects, 3))
    for obj1, obj2, obj3 in combinations:
        choiceA, choiceB, choiceC = tuple(random.sample(spatial_terms, 3))
        prep = "between"
        answ = [choiceA, choiceB, choiceC, prep]
        # shuffle the answer choice
        random.shuffle(answ)
        # pA = random.choice(personA)
        # insp = random.choice(indoor_space)
        idx_in = answ.index(prep)
        text += (
        f"{anschoice[idx_in]}\n"
        f"{obj1} is on the left of {obj2}, {obj3} is on the right of {obj2}. "
        f"{obj2} is ___ {obj1} and {obj3}.\n"
        f"A: {answ[0]}\n"
        f"B: {answ[1]}\n"
        f"C: {answ[2]}\n"
        f"D: {answ[3]}\n\n"
        )
    return text








