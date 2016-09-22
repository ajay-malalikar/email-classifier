import os
import random
import subprocess

def randomNumber(path):
    spamList = []
    hamList = []
    randomHash = {}
    i=0
    j=0
    for d,s,f in os.walk(path):
        if len(f) is not 0:
            for file in f:
                if "spam" in d:
                    spamList.append(d + "/" + file)
                    i+=1
                else:
                    hamList.append(d + "/" + file)
                    j+=1
    ran = int(j/10)+36
    for x in range(1, ran):
        r = random.randint(1, j)
        if r not in randomHash:
            file = hamList[r]
            subprocess.call('cp ' + file + ' /home/ajay/Documents/email-classifier/train-auto/ham/', shell=True)
            randomHash[r] = True
    randomHash.clear()
    ran = int(i/10)+36
    for x in range(1, ran):
        r = random.randint(1, i)
        if r not in randomHash:
            file = spamList[r]
            subprocess.call('cp ' + file + ' /home/ajay/Documents/email-classifier/train-auto/spam/', shell=True)
            randomHash[r] = True


randomNumber("/home/ajay/Documents/email-classifier/train")