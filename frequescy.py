sample = {"codingal": 4, 'is':4, 'the':2, 'best':2,"place":4, "for":2, "coding": 4}
count = 0
for i in sample :
    if sample [i] == 4:
        count = count + 1
print ("the frequency of 4 in sample :", count)