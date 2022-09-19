## Flashcards
Created while doing a course 'Python Core' on hyperskill.org, based on general schema and guidelines provided by course author (but solutions designed on my own). It was a lot of fun and possibility to practice using of lists, loops, dictionaries, json files on more advanced level.

Technologies used:
- python
- libraries: random, json, argparse

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
Print the message Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats): each time the user is prompted for their next action. The action is read from the next line, processed, and the message is output again until the user decides to exit the program.

The program's behavior depends on the user's input action:
- log — ask the user where to save the log with the message, save all the lines that have been input in/output to the console to the file, and print the message The log has been saved. Don't clear the log after saving it to the file.
- hardest card — print a string that contains the term of the card with the highest number of wrong answers, for example, If there are several cards with the highest number of wrong answers, print all of the terms.
- reset stats — set the count of mistakes to 0 for all the cards.

Update your import and export actions from the previous stage, so that the error count for each flashcard is also imported and exported.

**Stage 7:**
When provided with command-line arguments, your program should do the following:
- If --import_from=IMPORT is passed, where IMPORT is the file name, read the initial card set from the external file, and print the message n cards have been loaded. as the first line of the output, where n is the number of cards loaded from the external file. If such an argument is not provided, the set of cards should initially be empty and no message about card loading should be output.
- If --export_to=EXPORT is passed, where EXPORT is the file name, write all cards that are in the program memory into this file after the user has entered exit, and the last line of the output should be n cards have been saved., where n is the number of flashcards in the set.
