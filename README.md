## Flashcards
??


**Stages:**
**Stage 1:**
- Print term and definition for one card.

**Stage 2:**
- Get term and definition for user, then ask user about it and check if answer is correct.

**Stage 3:**
- Get the number of flashcards the user would like to create. 
- Create the defined amount of cards. 
- Test the user on their knowledge of the definitions of all terms in the order they were added.

**Stage 4:**
- When the user tries to add a duplicate term of definition, forbid it. 
- When the user enters the wrong definition for the requested term, but this definition is correct for another term, print the appropriate message:' Wrong. The right answer is "correct answer", but your definition is correct for "term for user's answer".'

**Stage 5:**
- Print the message Input the action (add, remove, import, export, ask, exit): each time the user is prompted for their next action. The action is read from the next line, processed, and the message is output again until the user decides to exit the program.

The program's behavior depends on the action the user inputs:
- add — create a new flashcard with a unique term and definition.  If a term or a definition already exists, output the line The <term/definition> already exists. Try again: and accept a new term or definition.
- remove — ask the user for the term of the card they want to remove. If a matching flashcard exists, remove it from the set and output the message. If there is no such flashcard in the set, inform the user.
- import — ask user for file, and import all the flashcards written to this file. If there is no file with such name, print the message File not found.. The imported cards should be added to the ones that already exist in the memory of the program. However, the imported cards have priority: if you import a card with the name that already exists in the memory, the card from the file should overwrite the one in memory.
- export — request the file name with the line and write all currently available flashcards into this file.
- ask — ask the user about the number of cards they want and then prompt them for definitions, like in the previous stage.
- exit — print Bye bye! and finish the program.


**Stage 6:**
**Stage 7:**
