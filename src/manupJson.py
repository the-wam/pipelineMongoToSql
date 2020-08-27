import json

def openJson(filePath):
    with open(filePath, "r") as f:
        data = json.load(f)

    return data

def saveJson(filePath, data):
    with open(filePath, 'w') as f:
        json.dump(data,f)

