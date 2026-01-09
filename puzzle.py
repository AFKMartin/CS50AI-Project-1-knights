from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a knight or a knave, never both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # If A is a knight then A statement is true
    # If A is a Knave then A statement is false
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Each one is either a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # If A is a knight then "we are both knaves" is true
    # If A is a knave then "we are both knaves" is false
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Each one is either a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # If A is a knight, then they are the same 
    # If A is a knave, then they are NOT the same
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    # If B is a knight, then they are different
    # If B is a knave, then they are NOT different
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))   
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Each one is either a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # If A is a knight, "I am a knight" is true
    # If A is a knave, "I am a knight" is false
    # Implication(AKnight, AKnight),  # Always true
    # Implication(AKnave, Not(AKnight)), # Also always true

    # If B is knight, then A is knave (creates contradiction - forces B to be knave)
    Implication(BKnight, And(AKnight, AKnave)),
    Implication(BKnave, AKnight),

    # If B is a knight, then C is a knave
    # If B is a knave, then C is NOT a knave (C should be a knight)
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    # If C is a knight, then A is a knight
    # If C is a knave, then A is NOT a knight (A should be a knave)
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
