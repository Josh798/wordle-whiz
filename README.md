# Wordle Whiz

This Wordle solver requires Python 3. Run it like this:

```
python main.py
```

After telling you the guess, the solver will prompt you for input. You should enter 5 characters, then press enter. Each character you type is either a 'x', '*', or '!' character.

**'x'** means the character is not in the word (GRAY in Wordle).

**'*'** means the character is in the word, but is in the wrong spot (YELLOW in Wordle).

**'!'** means the character is in the word and is in the correct spot (GREEN in Wordle).

If at any point the solver gives you a word that Wordle (or your Wordle app) rejects, simply press CTRL+D to skip this word and get the next word.

Here is an example of the solver trying to guess the word 'dream':

```
 1  $ python3 main.py 
 2  best guess: aeros
 3  result: 
 4  best guess: soare
 5  result: 
 6  best guess: arose
 7  result: *!xx*
 8  best guess: tread
 9  result: x!!!*
10  best guess: dream
11  result: !!!!!
12  Yay! You found the word in 3 guesses.
```

Notice that in lines 3 and 5, the user did not type anything. This is because their Wordle app rejected both of the words 'aeros' and 'soare', so the user did not type anything and instead pressed CTRL+D to move on to the next guess.