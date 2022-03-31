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

    high = ''
    maxprob = 0
    for w in wordset:
        s = set()
        for c in w:
            s.add(c)
        
        prob = 0
        for c in s:
            prob += freq[letter2num[c]]
        
        if prob > maxprob:
            maxprob = prob
            high = w

    guess = high
    print('best guess: ' + guess)

    # enter: x for wrong letter
    #        * for correct letter wrong spot
    #        ! for correct letter correct spot
    #        CTRL+D if the word was rejected.
    try:
        result = input('result: ')
        guesses += 1
    except EOFError:
        wordset.remove(guess)
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
    for c in result:
        if c == 'x':
            notcontains += guess[i]
        elif c == '*':
            knownwrongpos[i] += guess[i]
        elif c == '!':
            known[i] = guess[i]
        
        i += 1

    removeme = set()
    for w in wordset:
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
