# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
plt.figure(figsize=(8, 5))
font = {'family': 'serif',
        'serif': 'Times New Roman',
        'weight': 'normal',
        'size': 15}
plt.rc('font', **font)
y1 = [81.90, 	85.90, 	84.53, 	83.33]
x1 = ["0", "0.1", "0.3", "0.5"]
y2 = [81.29, 	85.17, 	82.29, 	82.65]
x2 = ["0", "0.1", "0.3", "0.5"]
# x3=[30,50,70,90,105,114,128,137,147,159,170,180,190,200,210,230,243,259,284,297,311]
# y3=[48,48,48,48,66,173,351,472,586,712,804,899,994,1094,1198,1360,1458,1578,1734,1797,1892]
x = np.arange(0, 60)
y = np.arange(40, 100)
ax = plt.gca()
y_major_locator = MultipleLocator(10)
ax.yaxis.set_major_locator(y_major_locator)
plt.ylim((70, 100))
l1 = plt.plot(x1, y1, 'ro-', label='Accuracy')
l2 = plt.plot(x2, y2, 'g+-', label='F1 score')
# l3=plt.plot(x3,y3,'b--',label='type3')
plt.plot(x1, y1, 'ro-', x2, y2, 'g+-')
# plt.title('The Lasers in Three Conditions')
plt.ylabel('Accuracy/F1 score')
xlabel = r"${\alpha}$"
plt.xlabel('The value of different sample stability weights coefficient ' + xlabel)
# plt.xlabel(xlabel)
plt.legend()

plt.show()
plt.savefig("./lineplot_alpha.pdf", bbox_inches="tight")
