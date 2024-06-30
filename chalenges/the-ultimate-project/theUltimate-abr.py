import words
import random
import pyfiglet

def aiReturn(sentences):
    sentence = words.conversation

    for listsItem in sentence:
        if sentences in listsItem:
            if len(sentence) >= 5:
                    print(sentence)
            else:
                print(f"mhhhh.... Tell me more about {sentences}")

    
    
    return words.conversation

def sortedWord(sentences):
    
    pass
    




def abbreviation(word):
    abbreviate = (words.abbreviations)
    matching_word1 = []
    matching_word2 = []
    for lst in abbreviate:
        
        if word in lst[0].lower():
            matching_word1.append(lst[1])
        elif word in lst[1].lower():
            matching_word2.append(lst[0])


    if matching_word2:
        abbreviated = random.choice(matching_word2)
        print(f"{word}, '{abbreviated}'")
    elif matching_word1:
        abbreviated = random.choice(matching_word1)
        print(f"{word}, '{abbreviated}'")

def fillerWord():
    greetStatus = words.conversation_sentences
    firstGreet = random.choice(greetStatus)
    returnGreet = random.choice(firstGreet)

    print(returnGreet)

def getWord():
    pass

def main(): 
    sentences = input("\nWhat do you Want to talk about today? ")         
    aiReturn(sentences)
main()