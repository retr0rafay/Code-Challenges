import json


def isValid(stale, latest, otjson):
    currentString = list(stale)
    # converts json string into array of dictionaries/hash maps
    jsonData = json.loads(otjson)
    startingCursorPosition = 0

    if jsonData == [] and stale == latest:
        return True

    for operations in jsonData:
        if operations["op"] == "skip":
            if operations["count"] > len(currentString) - startingCursorPosition:
                return False
            startingCursorPosition += operations["count"]
        elif operations["op"] == "insert":
            for char in operations["chars"]:
                currentString.insert(startingCursorPosition, char)
                startingCursorPosition += 1
        elif operations["op"] == "delete":
            if operations["count"] > len(currentString) - startingCursorPosition:
                return False
            currentString = currentString[:startingCursorPosition] + list(currentString[
                startingCursorPosition + operations["count"]:])

    return list(currentString) == list(latest)


print(isValid('Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  '[]'))
