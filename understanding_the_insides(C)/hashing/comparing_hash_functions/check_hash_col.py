#This contains a analysis of the different hash functions possible 
#should seed for fixed hash() but i havent


with open ("names.txt","r") as names:
    input_list = names.read().split("\n")
from collections import Counter
def check_hash(hash_func,arg_list,input_list):
    c = Counter(list(map(lambda x: hash_func(x,*arg_list), input_list)))
    return c



def hash1(c,N):
    n = len(c)
    v = 0 
    for i in c:
        v^=ord(i)+N
    return v%N


def hash2(c,N):
    n = len(c)
    v = 0 
    for i in c:
        v+=ord(i)
    return v%N

def hash3(c,N):
    n = len(c)
    v = 0 
    for i in c:
        v+=ord(i)^N
    return v%N
def hash4(c,N):
    return hash(c)%N


N_input = len(input_list)

r1 = check_hash(hash1,[10],input_list)
r2 = check_hash(hash2,[10],input_list)
r3 = check_hash(hash3,[10],input_list)
r4 = check_hash(hash4,[10],input_list)
print("Index\tHash1\tHash2\tHash3\tHash4")
tot = [0]*4
for i in range(10):
    v1 = r1[i]/N_input
    v2 = r2[i]/N_input
    v3 = r3[i]/N_input
    v4 = r4[i]/N_input
    tot[0]+=v1
    tot[1]+=v2
    tot[2]+=v3
    tot[3]+=v4
    print(f"{i}\t{v1:.2f}\t{v2:.2f}\t{v3:.2f}\t{v4:.2f}")
print(f"Tot:\t{tot[0]:.2f}\t{tot[1]:.2f}\t{tot[2]:.2f}\t{tot[3]:.2f}")


from matplotlib import pyplot
import numpy as np
vr1 = np.array([r1[i] for i in range(10)])/N_input
vr2 = np.array([r2[i] for i in range(10)])/N_input
vr3 = np.array([r3[i] for i in range(10)])/N_input
vr4 = np.array([r4[i] for i in range(10)])/N_input
meanr = np.array([0.1]*10)
#deviations from the mean result
sd1 = np.sum((meanr-vr1)**2)*10
sd2 = np.sum((meanr-vr2)**2)*10
sd3 = np.sum((meanr-vr3)**2)*10
sd4 = np.sum((meanr-vr4)**2)*10

#plotting
pyplot.figure(figsize=(8,6))
pyplot.plot(range(10),vr1, alpha=0.75,        label="Simple_Xor:    std = {:.5f}".format(sd1))
pyplot.plot(range(10),vr2, alpha=0.75,        label="Simple_Add:    std = {:.5f}".format(sd2))
pyplot.plot(range(10),vr3, alpha=0.75,        label="Add_Fin_Xor:   std = {:.5f}".format(sd3))
pyplot.plot(range(10),vr4, alpha=0.75,        label="Built_in_Hash: std = {:.5f}".format(sd4))
pyplot.plot(range(10),meanr,"-p", alpha=0.75, label="Ideal Hash:      std = 0.0")
pyplot.xlabel("Data", size=14)
pyplot.ylabel("Count", size=14)
pyplot.title("Multiple Histograms with Matplotlib")
pyplot.legend(loc='upper right')

pyplot.show()
