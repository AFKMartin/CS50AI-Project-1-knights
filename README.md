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