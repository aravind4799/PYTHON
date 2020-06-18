sally = "sally sells sea shells by the sea shore and by the road"

from collections import Counter
characters=Counter(sally)
keys=[]
for key in characters.keys():
    keys.append(key)
minn=keys[0]
#else you can iterate using .items()--which returns list of tuples

for key in keys:
    if characters[key]<minn:
        minn=characters[key]
        worst_char=key
