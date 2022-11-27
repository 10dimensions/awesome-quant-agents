import json
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

def saveResult(dat, name):
    with open('results/' + name, 'w') as fp:
        #json.dumps({k: v.tolist() for k, v in dat.items()})
        json.dump(dat, fp, cls=NpEncoder)