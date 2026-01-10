# CS50W Project 1 - Knights Checklist

Add knowledge to knowledge bases knowledge0, knowledge1, knowledge2, and knowledge3 to solve the following puzzles.

- [x] Puzzle 0 is the puzzle from the Background. It contains a single character, A.
    - [x] A says “I am both a knight and a knave.”

- [x] Puzzle 1 has two characters: A and B.
    - [x] A says “We are both knaves.”
    - [x] B says nothing.

- [x] Puzzle 2 has two characters: A and B.
    - [x] A says “We are the same kind.”
    - [x] B says “We are of different kinds.”

- [x] Puzzle 3 has three characters: A, B, and C.
    - [x] A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
    - [x] B says “A said ‘I am a knave.’”
    - [x] B then says “C is a knave.”
    - [x] C says “A is a knight.”

In each of the above puzzles, each character is either a knight or a knave. Every sentence spoken by a knight is true, and every sentence spoken by a knave is false.

Once you’ve completed the knowledge base for a problem, you should be able to run python puzzle.py to see the solution to the puzzle.

## Output:

Puzzle 0

- A is a Knave

Puzzle 1

- A is a Knave
- B is a Knight

Puzzle 2

- A is a Knave
- B is a Knight

Puzzle 3
- A is a Knight
- B is a Knave
- C is a Knight

## Explanation

- Puzzle 0: 

A says, “I am both a knight and a knave.” 

That statement is logically impossible. Therefore it must be false, and A must be a knave.

- Puzzle 1:

A says “We are both knaves.”
B says nothing.

If A were a knight, the statement would be true, implying A is a knave - contradiction. 

Therefore A is a knave, the statement is false, and B must be a knight.

- Puzzle 2:

A says “We are the same kind.”
B says “We are of different kinds.”

These two statements are logical negations of each other. Exactly one must be true.

If A were a knight, then “same kind” would be true, making B’s statement false - which would require B to be a knave. But if B is a knave, then “different kinds” is false, meaning they are the same kind - contradiction.

Therefore A must be a knave and B a knight.

- Puzzle 3:

A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
B says “A said ‘I am a knave.’”
B then says “C is a knave.”
C says “A is a knight.”

Assuming that A is a knave leads to a contradiction: if A were a knave, then B’s claim that A said “I am a knave” would have to be false (since a knave cannot truthfully say they are a knave), making B a knave; this in turn makes B’s statement “C is a knave” false, so C must be a knight, but then C’s statement “A is a knight” would be true, contradicting the assumption that A is a knave. Therefore, A must be a knight; once this is established, C’s statement is true and C is a knight, while B’s statement about C is false, making B a knave, which satisfies all conditions of the puzzle consistently.