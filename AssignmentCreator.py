import random
import requests

apiKey = "fcba19dd2093ec3bb84c44244921a054da714252qoXEFm9KJJXb7YlBJo9QJ07LO"
phoneNumbers = {"Ryan F": "5083973554", "Jonny": "5089756850", "Jacob": "8575002749", "Jonah": "5086547781", "Max": "5089303452", "Gabe": "5088105373", "Reed": "7817076703", "Dan Z": "8574259259", "Ryan A": "5087828826", "Nadav": "7742792635", "Rick": "6179131681", "Dan B": "3392210312", "Matt": "5087822634"}
names = list(phoneNumbers.keys())
words = "Crab,Water Bottle,Stoichiometry,Wild Krats,Pigskin,Microphone,Envelope,Butter Knife,Frisbee,Dentist,Xbox,Portal,Fox,Skull,Hammer,LED Lights,Swiss Army Knife,Twitch,Cactus,Overnight Camp,Earbud,Coin Toss,Anticipation,Artist,Red Panda,Communication,Textbook,Double Decker Bus,Frisbee,Jealousy,Maroon,KN95,Sculpture,Clay,Rocket,Shovel,Pickaxe,Oak,Juniper,Pear,Mango,Recycling,Lettuce,Suitcase,Paintbrush,Molar,Braces,Retainer,Aglet,Highlighter,Badminton,Pickleball,Cricket,Eagle,Jaguar,Puma,Panther,Lion,Tiger,Pie,Meta,Pikachu,Charmander,Squirtle,Piccolo,Clarinet,Stopwatch,Mustard,Mayo,Substitute,Mario,Toad,Sideline,Truck,Remote,Kiwi,Unity,Binder,Sharpener,Fire Extinguisher,Locomotive,Setter,Spork,Dragon,Telegram,Duplicate,German,Japanese,Portuguese,Pajamas,Crafting Table,Italicize,Conductor,Safari,Taxi,Skyscraper,Hand Sanitizer,Vaccine,Trampoline,Joe Biden,Bernie Sanders,Trump,Anaconda,Python,Hot Chocolate,Apple Cider,Keyboard,Violin,Global Awareness,Trophy,Document,Salsa,Dream,Bishop,Pawn,Dwight,Vance Refrigeration,Hole Puncher,Stapler,Stocking,Sheets,Carpet,Lightbulb,Hammer,Screwdriver,Battery,Electoral College,Harvard,Yale,MIT,Stanford,Maroon,Mockingbird,Potato".split(",")

def createPairings(playerNames):
    if len(playerNames) < 2:
        return -1
    
    assignments = {}
    idx = 0
    first = playerNames[idx]
    currentIdx = idx

    for i in range(len(names) - 1):
        nextIdx = random.randint(0, len(playerNames) - 2)
        key = playerNames[currentIdx]
        playerNames.pop(currentIdx)
        assignments[key] = playerNames[nextIdx]
        currentIdx = nextIdx

    assignments[playerNames[currentIdx]] = first

    return assignments

def assignNames(playerNames, words):
    assignments = {}

    for name in playerNames:
        idx = random.randint(0, len(words) - 1)
        assignments[name] = words[idx].lower()
        words.pop(idx)

    return assignments

def createMessage(name, nameAssignments, wordAssignments):
    msg = f"*From Ryan and Jonny*\nHello {name}, your word assassin target for the next round is {nameAssignments[name]}, and your word is {wordAssignments[name]}"
    return msg

def sendMessages(playerNames, nameAssignments, wordAssignments, phoneNumbers, apiKey):
    for name in playerNames:
        msg = createMessage(name, nameAssignments, wordAssignments)
        number = phoneNumbers[name]
        resp = requests.post('https://textbelt.com/text', {
            'phone': number,
            'message': msg,
            'key': apiKey,
        })

        print(resp.json())

nameAssignments = createPairings(names[:])
wordAssignments = assignNames(names[:], words[:])
sendMessages(names[:], nameAssignments, wordAssignments, phoneNumbers, apiKey)