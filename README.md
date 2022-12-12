# Anki-CSV-To-Cards

This is a program I wrote to convert a list of the 12k most frequent words found on Japanese netflix, into Anki cards that I can study. Im not very experienced with python so this has been an interesting challenge.

This script uses an API for Jisho.com which allows for appending a search term at the end of an HTML string and it returns a JSON file with the dictionary info on the given word. This script then parses that JSON file into usable text which can be pased into cards.

## Running from VS Code
![](https://github.com/NoahBraasch/Anki-CSV-To-Cards/blob/main/img/ezgif.com-gif-maker(2).gif)

When running, this code simulate keyboard inputs by the `pyautogui` library and manually fills the fields of the flashcards

## Running in Anki
![](https://github.com/NoahBraasch/Anki-CSV-To-Cards/blob/main/img/2022-12-11%2017-24-59.gif)

There is certainly a faster way to do this. But I have only written very limited amounts of python in the past so this was sufficient for myself.
