from words import wordset, letter2num, num2letter

# letters in here are letters that are known to NOT be in the word.
notcontains = ''

# letters in here are letters that are known to be in the word, but
# are known to NOT be in the position they are in inside this list.
knownwrongpos = [
    '',
    '',
    '',
    '',
    ''
]

# letters in here are known to be in the word at the position they
# are in this list.
known = [
    '',
    '',
    '',
    '',
    ''
]

# Duplicate the wordset, but we will not modify this one. (Except if
# the user tells us a word was rejected, then we will take it out of
# this set.)
staticwordset = set(wordset)

guesses = 0

while True:
    freq = [0.0] * 26
    total = len(wordset)

    if total == 0:
        print('Uh-oh! Looks like this word isn\'t in our dictionary. :(')
        print('You\'re on your own. Good luck!')
        break

    for w in wordset:
        s = set()
        for c in w:
            s.add(c)
        
        for c in s:
            freq[letter2num[c]] += 1

    for i in range(0, 26):
        freq[i] /= total

    guess = ''
    if (len(wordset) <= 2):
        # If there are only 1 or 2 possible solutions, you are better off to
        # guess at random than to pick a word from the set of non-solutions
        # in order to eliminate a word from the set of possible solutions.
        guess = wordset.pop()
    else:
        if guesses >= 6:
            # If we are on the last guess, we want to make sure
            # we guess from the set of possible solutions. Idealy,
            # by the 6th guess, there is only one solution, which
            # we would have picked above.
            guessset = wordset
        else:
            # Otherwise, we can pick from every word.
            guessset = staticwordset
        
        maxprob = 0
        for w in guessset:
            s = set()
            for c in w:
                s.add(c)
            
            prob = 0
            for c in s:
                if c not in known or guesses >= 6:
                    prob += freq[letter2num[c]]
            
            if prob > maxprob:
                maxprob = prob
                guess = w

    print('best guess: ' + guess)

    # enter: x for wrong letter
    #        * for correct letter wrong spot
    #        ! for correct letter correct spot
    #        CTRL+D if the word was rejected.
    try:
        result = input('result: ')
        guesses += 1
    except EOFError:
        if wordset.__contains__(guess):
            wordset.remove(guess)
        staticwordset.remove(guess)
        print()
        continue

    if result == '!!!!!':
        if guesses == 1:
            es = ''
        else:
            es = 'es'
        print(f'Yay! You found the word in {guesses} guess{es}.')
        break

    i = 0
    addtonotcontains = ''
    addtoknownwrongpos = [ '', '', '', '', '' ]
    addtoknown = [ '', '', '', '', '' ]
    for c in result:
        if c == 'x' and guess[i] not in known:
            addtonotcontains += guess[i]
        elif c == '*':
            addtoknownwrongpos[i] += guess[i]
        elif c == '!':
            addtoknown[i] = guess[i]
        
        i += 1

    # If the user guesses something like 'ahead' and it commes back like '!xx*x',
    # then we know there must be at least two 'a' characters in the word.
    inferredlettercounts = dict()
    notcontains += addtonotcontains
    for i in range(0, 5):
        knownwrongpos[i] += addtoknownwrongpos[i]
        known[i] = addtoknown[i]
        if addtoknownwrongpos.__contains__(addtoknown[i]):
            inferredlettercounts[addtoknown[i]] = 1 + addtoknownwrongpos.count(addtoknown[i])

    removeme = set()
    for w in wordset:
        for k in inferredlettercounts.keys():
            num = inferredlettercounts[k]
            if w.count(k) < num:
                removeme.add(w)
    
        for c in notcontains:
            if w.__contains__(c):
                removeme.add(w)

        for i in range(0, 5):
            for c in knownwrongpos[i]:
                if w[i] == c or not w.__contains__(c):
                    removeme.add(w)
        
            if known[i] != '' and known[i] != w[i]:
                removeme.add(w)

    for w in removeme:
        wordset.remove(w)

    # If every word in the set of possible solutions has a letter in the same
    # spot, add that to the 'known' letters.
    newknowns = list(wordset.pop())
    wordset.add(''.join(newknowns))
    for w in wordset:
        for i in range(0, 5):
            if newknowns[i] != w[i]:
                newknowns[i] = ''
    
    for i in range(0, 5):
        if newknowns[i] != '':
            known[i] = newknowns[i]

    # Loop through the words in a second pass to remove words that have
    # 'inferred' knowns.
    removeme = set()
    for w in wordset:
        for i in range(0, 5):
            if known[i] != '' and known[i] != w[i]:
                removeme.add(w)

    for w in removeme:
        wordset.remove(w)

    # print(wordset)
