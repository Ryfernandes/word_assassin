import random
import requests

apiKey = "MY-API-KEY" #API key from textbelt.com
phoneNumbers = {"NAME1": "PHONE1", "NAME2": "PHONE2"} #names and phone numbers (no dashes) of all participants
names = list(phoneNumbers.keys())
words = "WORD,WORD".split(",") #creates list of all playable words for the game (I had them in a google doc, so was easier to do .split)

#gives each player a different player to be their initial target; organized so that the assignments of players make a "loop" and no two players will ever have each other as targets until the final two
def createPairings(playerNames):
    if len(playerNames) < 2:
        return -1
    
    assignments = {}
    idx = 0
    first = playerNames[idx]
    currentIdx = idx

    #iterates through all names and removes them from names list before assignment; this way, no one gets themselves, and the names will always be assigned in a full "loop"
    for i in range(len(names) - 1):
        nextIdx = random.randint(0, len(playerNames) - 2)
        key = playerNames[currentIdx]
        playerNames.pop(currentIdx)
        assignments[key] = playerNames[nextIdx]
        currentIdx = nextIdx

    assignments[playerNames[currentIdx]] = first

    #returns a dictionary with all of the pairings
    return assignments

#assigns each player a random word to be their word for the first round
def assignNames(playerNames, words):
    assignments = {}

    for name in playerNames:
        idx = random.randint(0, len(words) - 1)
        assignments[name] = words[idx].lower()
        words.pop(idx) #ensures two people do not stat with the same word

    return assignments #returns dictionary with all plaers and their word

#creates a string to be the message for the current name, their target, and their word
def createMessage(name, nameAssignments, wordAssignments):
    msg = f"*From Ryan and Jonny*\nHello {name}, your word assassin target for the next round is {nameAssignments[name]}, and your word is {wordAssignments[name]}"
    return msg

#made with sample code from textbelt; loops through all names and makes a post request to send their text message via textbelt
def sendMessages(playerNames, nameAssignments, wordAssignments, phoneNumbers, apiKey):
    for name in playerNames:
        msg = createMessage(name, nameAssignments, wordAssignments)
        number = phoneNumbers[name]
        resp = requests.post('https://textbelt.com/text', {
            'phone': number,
            'message': msg,
            'key': apiKey,
        })

        print(resp.json()) #prints info on the success status, time, phone number, and remaining texts that can be sent

nameAssignments = createPairings(names[:]) #creates name assignments
wordAssignments = assignNames(names[:], words[:]) #assigns words
sendMessages(names[:], nameAssignments, wordAssignments, phoneNumbers, apiKey) #sends texts
