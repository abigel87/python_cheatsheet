import pandas as pd
import re

datepattern = re.compile("\d{4}.\d{2}.\d{2} \d{2}:\d{2}")

df = pd.read_excel('D:/Downloads/logminta.xlsx')
df_processed = pd.DataFrame(columns=['rowID', 'timestamp', 'logtext'])
rowID = 0

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""        

def is_nan(x):
    return (x != x)

for i in df['ALLAPOT_LOG']:
    if is_nan(i)==False:
        
        matcher = datepattern.search(i)
        if matcher is None:
            pass
        else:
            foundList = re.findall(datepattern, i)
            for index, j in enumerate(foundList):
                if index == len(foundList)-1:
                    logText = (i[i.index( foundList[index] ) + len( foundList[index] ):])
                else:
                    logText = (find_between(i, foundList[index], foundList[index+1]))
                
                df_processed = df_processed.append({"rowID":rowID, "timestamp": j, "logtext": logText},ignore_index=True)
        rowID +=1
