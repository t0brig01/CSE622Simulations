import matplotlib.pyplot as plt
# from scipy.stats import chi2_contingency, chisquare,chi2
from sklearn.feature_selection import chi2
import numpy as np 

nums1 = [0.21,0.88,0.37,0.06,0.98,0.61,0.89,0.28,0.7,0.94,0.46,0.92,0.34,0.08,0.79,0.82,0.36,0.62,0.27,0.1]
nums1split = [[.06,.08,.1],[],[.21,.27,.28],[.34,.36,.37],[.46],[],[.61,.62,.7],[.79],[.82,.88,.89],[.92,.94,.98]]

#Histogram 
count = []
for x in nums1split:
    count.append(int(len(x)))

y_pos = np.arange(len(nums1split))
labels = ['0.0-0.1', '0.1-0.2', '0.2-0.3', '0.3-0.4', '0.4-0.5','0.5-0.6', '0.6-0.7', '0.7-0.8', '0.8-0.9', '0.9-1.0']

plt.style.use('ggplot')

plt.bar(y_pos, count, align='center', alpha=0.5)
plt.xticks(y_pos, labels)
plt.ylabel('Count')

plt.show()

for x in nums1split:
    while len(x) < 3:
        x.append(0)
#Chi-Squared Test
stat, p = chi2(nums1split,labels)

print("p values are " + str(p)) 




nums2 = [[20,22,13,2,2],[10,19,25,4,1]]

stat, p = chi2(nums2,["This Year","Last Year"])

print("p values are " + str(p)) 
