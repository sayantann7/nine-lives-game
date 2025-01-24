import requests, random
wordURL = "https://random-word-api.herokuapp.com/word"
print("LET THE GAME BEGIN.....")
print("HERE IS THE WORD")
wordRES = requests.get(wordURL)
word = wordRES.json()[0]
try :
    meaningURL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    meaningRES = requests.get(meaningURL)
    meaning = meaningRES.json()
    definition = meaning[0]['meanings'][0]['definitions'][0]['definition']
    length = len(word)
    for i in range(0,length):
        if i%2!=0:
            print("_",end="")
        else:
            print(word[i],end="")
    print()
    capitalized_definition = definition.upper()
    print("MEANING OF THE WORD : ")
    print(capitalized_definition)
    str = ""
    for j in range(0,9):
        print("GUESS THE WORDsss...")
        print(f"LIVES LEFT : {9-j}")
        str = input("ENTER THE WORD : ")
        if(str==word):
            print("HURRAY!!! YOU WON!!!!!")
            break
        else:
            print("TRY AGAIN :(")
    if str!=word:
        print(f"ALL LIVES ARE OVER :( THE WORD WAS {word.upper()}")


except:
    print("OOPS! GAME NOT FUNCTIONAL RN :( TRY AGAIN LATTER")