sample = {"codingal": 4, 'is':4, 'the':2, 'best':2,"place":4, "for":2, "coding": 4}
count = 0
for i in sample :
    if sample [i] == 4:
        count = count + 1  
print ("the frequency of 4 in sample :", count)
jc = 0
for j in sample:
    if sample [j] == 2:
        jc = jc + 1
print ("the frequency of 2 in sample :", jc)