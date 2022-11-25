import json

def saveResult(name):
    with open('results/' + result + '.json', 'w') as fp:
        json.dump(sample, fp)