import random 
name = input("What is your name? ")
print("Good Luck !", name)


words = [
    "apple", "river", "mountain", "sky", "ocean", "forest", "tree", "flower", "sun", "moon",
    "star", "cloud", "wind", "rain", "storm", "snow", "ice", "fire", "stone", "sand",
    "field", "valley", "hill", "island", "beach", "lake", "stream", "water", "earth", "world",
    "city", "village", "road", "bridge", "tower", "house", "garden", "window", "door", "table",
    "chair", "book", "paper", "pen", "pencil", "letter", "story", "music", "song", "voice",
    "sound", "light", "shadow", "color", "shape", "circle", "square", "line", "point", "space",
    "time", "moment", "hour", "day", "night", "morning", "evening", "season", "winter", "summer",
    "spring", "autumn", "energy", "power", "force", "motion", "speed", "path", "track", "trail",
    "dream", "thought", "idea", "mind", "heart", "spirit", "hope", "peace", "joy", "love",
    "friend", "family", "child", "parent", "teacher", "student", "leader", "worker", "artist", "writer"
]
word = random.choice(words)
print("Guess the characters: ")

guesses = ''
turns = 9

while turns > 0:
    failed = 0 
    for char in word:
       
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1 

    print("")
    if failed == 0:
        print("You Win ")
        print("The word is: ", word)
        break

    guess = input("guess a character: ")
    guesses += guess 

    if guess not in word:
        turns -= 1 
        print("wrong")
        print("You have", + turns, 'more guesses')

    if turns == 0:
        print("You LOOSEEEEEEEEE")
        answer = input("Wanna play again ? ")
        if answer == "Yes":
            turns = 9
            word = random.choice(words)
            guesses = []
        elif answer == "No":
            print("Fawk You then ")
        else:
            print("BYEE")
    
    





