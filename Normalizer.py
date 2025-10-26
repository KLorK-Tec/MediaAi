import numpy as np
import json


def normz(fle: str):
    """ Fle will be the file that needs to be normalized"""
    normed = []
    res = []
    with open(f"GesData/{fle}.json", "r") as data:
        da = json.load(data)

    D9 = round(da[9]["x"],4),round(da[9]["y"],4),round(da[9]["z"],4)
    for i in range(len(da)):
        cuco = round(da[i]["x"],4),round(da[i]["y"],4),round(da[i]["z"],4)
        dfact = (((cuco[0]-D9[0])**2)+((cuco[1]-D9[1])**2)+((cuco[2]-D9[2])**2)) ** (1/2)
        dfact = round(dfact,4)
        if dfact == 0:
            dfact = 1
        for j in range(0,21):
            res.append([])
            tred = round(da[j]["x"], 4)-cuco[0], round(da[j]["y"], 4)-cuco[1], round(da[j]["z"], 4)-cuco[2]
            normed = round(tred[0]/dfact,4),round(tred[1]/dfact,4),round(tred[2]/dfact,4)
            for k in range(3):
                res[i].append(normed[k])
    return res[:21]

            


print(normz("Like1"))