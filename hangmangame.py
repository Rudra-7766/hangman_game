import random
words=['KITE','APPLE','BANANA','UNIVERSE']
word=random.choice(words)
word=word.upper()
total_chance=7
guessed_word="-"*len(word)
while total_chance!=0:
    print(guessed_word)
    letter=input("guess a letter:").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guessed_word=guessed_word[:index]+letter+guessed_word[index+1:]
        if guessed_word==word:
            print("congratulation you won")
            break
    else:
        total_chance=total_chance-1
        print("incorrect guess")
        print("remaining chances:",total_chance)

else:
    print("game over")
    print("you loose")
    print("all chances are used")
print("correct word is ",word)
    
