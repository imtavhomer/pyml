import pandas as pd
import re
import json
from pandas.io.json import json_normalize

def featurizestrVal(strVal):
    strVal = strVal.lower()
    strVal = re.sub("\s+", " ", strVal)  # normalize whitespace
    vec = [0] * 38
    for c in strVal:
        if(c >= 'a' and c <= 'z'):
            vec[c-'a'] += 1
        elif(c >= '0' and c <= '9'):
            vec[c-'0'] += 1
        elif(c == ' '):
            vec[36] += 1
    vec[37] = len(strVal)
    return vec

with open('0000000', 'r', encoding='utf-8') as file:
    lines = file.readlines

df = pd.DataFrame.from_records(map(json.loads, lines))
locs = df['Location'].apply(json.loads)
df2 = pd.DataFrame(locs.tolist())
df2['Vector'] = df2['DisplayName'].apply(featurizer)
df3 = pd.concat([df2['Vector'].apply(pd.Series), df3['DisplayName']], axis=1)
df3.to_csv('d:/temp/features.csv')