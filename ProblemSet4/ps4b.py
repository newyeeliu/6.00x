from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(word, HAND_SIZE)
            # If the score for that word is higher than your best score
            if score > maxScore:
                # Update your best score, and best word accordingly
                maxScore = score
                bestWord = word

    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    # Keep track of two numbers: the number of letters left in your hand and the total score
    remainingLetters = calculateHandlen(hand)
    totalScore = 0

    # As long as there are still letters left in the hand:
    while remainingLetters > 0:
        # Display the hand
        print 'Current hand:', 
        displayHand(hand)
        # Ask user for input
        selectedWord = compChooseWord(hand, wordList)
        if selectedWord == None:
            break

        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
        score = getWordScore(selectedWord, HAND_SIZE)
        totalScore += score
        print selectedWord, 'earned', str(score), 'points. Total:', totalScore, 'points'
        # Update the hand
        hand = updateHand(hand, selectedWord)
        remainingLetters = calculateHandlen(hand)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if remainingLetters == 0:
        print 'Run out of letters. Total score:', totalScore, 'points.'
    else:
        print 'Goodbye! Total score:', totalScore, 'points.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    selection = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

    hand = {}
    while selection != 'e':
        comp = raw_input('Enter u to play yourself or c to let the computer play: ')
        while comp != 'c' and comp != 'u':
            print 'Invalid command.'
            comp = raw_input('Enter u to play yourself or c to let the computer play: ')

        if selection == 'n':
            hand = dealHand(HAND_SIZE)

            if comp == 'c':
                compPlayHand(hand.copy(), wordList)
            elif comp == 'u':
                playHand(hand.copy(), wordList, HAND_SIZE)
        elif selection == 'r':
            if len(hand) == 0:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                if comp == 'c':
                    compPlayHand(hand.copy(), wordList)
                elif comp == 'u':
                    playHand(hand.copy(), wordList, HAND_SIZE)
        else:
            print 'Invalid command.'
        selection = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


