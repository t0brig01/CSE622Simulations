import math
import random
import matplotlib.pyplot as plt


#There are only 5 paths this graph can take
lengths12347 = []
lengths1247 = []
lengths15347 = []
lengths1547 = []
lengths1567 = [] 

epochs = 500

for epoch in range(epochs):
    lengths12347.append((random.uniform(4,6) + 6 + random.triangular(4,8,10) + 4))
    lengths1247.append((random.uniform(4,6) + random.uniform(6,8) + 4))
    lengths15347.append((6 + 8 + random.triangular(4,8,10) + 4))
    lengths1547.append((6 + 11 + 4))
    lengths1567.append((6 + random.uniform(8,10) + random.uniform(9,10)))

avg12347 = sum(lengths12347)/len(lengths12347)
avg1247 = sum(lengths1247)/len(lengths1247)
avg15347 = sum(lengths15347)/len(lengths15347)
avg1547 = sum(lengths1547)/len(lengths1547)
avg1567 = sum(lengths1567)/len(lengths1567) 

print("Overall \t Avg: {0}".format((avg12347+avg1247+avg15347+avg1547+avg1567)))
print("Path 1,2,3,4,7 \t Avg: {0} \t Min: {1} \t Max: {2}".format(avg12347,min(lengths12347),max(lengths12347)))
print("Path 1,2,4,7 \t Avg: {0} \t Min: {1} \t Max: {2}".format(avg1247,min(lengths1247),max(lengths1247)))
print("Path 1,5,3,4,7 \t Avg: {0} \t Min: {1} \t Max: {2}".format(avg15347,min(lengths15347),max(lengths15347)))
print("Path 1,5,4,7 \t Avg: {0} \t Min: {1} \t Max: {2}".format(avg1547,min(lengths1547),max(lengths1547)))
print("Path 1,5,6,7 \t Avg: {0} \t Min: {1} \t Max: {2}".format(avg1567,min(lengths1567),max(lengths1567)))

plt.title("Path 1,2,3,4,7")
plt.plot(lengths12347)
plt.xlabel("Epoch")
plt.ylabel("Length")
plt.ylim(0,30)
plt.show()

plt.title("Path 1,2,4,7")
plt.plot(lengths1247)
plt.xlabel("Epoch")
plt.ylabel("Length")
plt.ylim(0,30)
plt.show()

plt.title("Path 1,5,3,4,7")
plt.plot(lengths15347)
plt.xlabel("Epoch")
plt.ylabel("Length")
plt.ylim(0,30)
plt.show()

plt.title("Path 1,5,4,7")
plt.plot(lengths1547)
plt.xlabel("Epoch")
plt.ylabel("Length")
plt.ylim(0,30)
plt.show()

plt.title("Path 1,5,6,7")
plt.plot(lengths1567)
plt.xlabel("Epoch")
plt.ylabel("Length")
plt.ylim(0,30)
plt.show()