import json
import numpy as np


#Numpy to json encoder
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


#Write data to file
def saveResult(dat, name):
    with open('results/' + name, 'w') as fp:
        json.dump(dat, fp, cls=NpEncoder)