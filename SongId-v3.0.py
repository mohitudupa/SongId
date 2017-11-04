import numpy as np
import scipy.misc as smp
import random as rn
import sys
import time


st = time.time()
data = ''
color = {}
n = 5
memo = {}

# Setting command line args
if(len(sys.argv) == 2):
    fname = sys.argv[1]
else:
    print("Provide file name as cmd line argument")
    exit()


# Compare function
def compare(str1, str2):
    sim = 0
    len1 = len(str1)
    len2 = len(str2)
    rep = min(len1, len2, 3)
    for i in range(rep):
        if str1[len1 - i - 1] == str2[len2 - i - 1]:
            sim += 1
    return(sim / 4)


# Color fill function
def fill(colval, i, j):
    if colval == [0, 0, 0]:
        return
    global data
    global n
    for z in range(n):
        for x in range(n):
            data[i * n + z, j * n + x] = colval


# Match function
def match(str1, str2):
    global memo
    global color
    # tup = tuple(sorted([str1, str2]))
    tup = (str1, str2)
    if str1 == str2:
        return(color[str1])
    if tup in memo:
        return(memo[tup])
    x = compare(str1, str2)
    if x > (1 / 2):
        colval = color[str1]
        memo[tup] = [int(colval[0] * .5), int(colval[1] * .5), int(colval[2] * .5)]
        return(memo[tup])
    memo[tup] = [0, 0, 0]
    return([0, 0, 0])


st = time.time()
destname = fname.split('.')[0] + ".bmp"
f = open(destname, 'wb+')
rf = open(fname, 'r')
word = ((rf.read()).lower()).split()
length = len(word)

# Creating the image matrix
data = np.zeros((length * n, length * n, 3), dtype=np.uint8)

# Asigning colors to each word
color = {}

for i in word:
    if i not in color:
        color[i] = [rn.randrange(0, 256), rn.randrange(0, 256), rn.randrange(0, 256)]


for i in range(length):
    for j in range(length):
        fill(match(word[i], word[j]), i, j)

# Creating the image object
img = smp.toimage(data)

# Saving and displaying the image
img.save(f)
f.close()
rf.close()
print("Time taken", time.time() - st)
'''for i in memo:
    if(memo[i] != [0, 0, 0]):   print(i, memo[i])'''
img.show()
