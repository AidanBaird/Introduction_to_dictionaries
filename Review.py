songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:count for song, count in zip(songs, playcounts)}

plays.update({"Purple Haze": 1})

plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}



print(plays)
print("")
print(library)
