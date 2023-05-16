import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import seaborn as sns
red = sns.color_palette("hls", 10)[0]
blue = sns.color_palette("hls", 10)[-4]
fig = plt.figure(1, figsize=(12, 6), dpi=1000)  # 初始化一张画布


font = {  # 'family': 'serif',
    # 'serif': 'Times New Roman',
    'weight': 'normal',
    'size': 20}
plt.rc('font', **font)
n = 200

np.random.seed(2)
random.seed(10)
t = np.random.random(size=n) * 2 * np.pi - np.pi
x1 = np.cos(t)
x2 = np.sin(t)
for i in range(n):
    len = np.sqrt(np.random.random())
    x1[i] = x1[i] * len/2.1-random.uniform(0, 1)
    x2[i] = x2[i] * len/2.1-random.uniform(0, 1)

m = 10
s = np.random.random(size=m) * 2 * np.pi - np.pi
x3 = np.cos(s)
x4 = np.sin(s)
for j in range(m):
    len = np.sqrt(0.1)
    x3[j] = x3[j] * len/20 - random.uniform(0.5, 1)+1.4
    x4[j] = x4[j] * len/20 - random.uniform(0.5, 1)+1.4
random.seed(50)
m = 5
s = np.random.random(size=m)
x5 = np.cos(s)
x6 = np.sin(s)
for j in range(m):
    len = np.sqrt(1)
    x5[j] = x5[j] * len*2 - random.uniform(0, 0.5)-3.2
    x6[j] = x6[j] * len*1.8 - random.uniform(0, 0.5)


random.seed(60)
m = 5
s = np.random.random(size=m)
x7 = np.cos(s)
x8 = np.sin(s)
for j in range(m):
    len = np.sqrt(1)
    x7[j] = x7[j] * len*1.8 - random.uniform(0, 0.5)-3
    x8[j] = x8[j] * len*1.8 - random.uniform(0, 0.5)-1.4
plt.subplot(121)
# fig, axes=plt.subplots(,figsize=(18, 10))
# fig, ax = plt.subplots((1,2,1), figsize=(8, 8))
plt.scatter(x1/2, x2/2, marker='o', color=blue, label='clean local gradient')
plt.scatter(x3/2, x4/2, marker='o', color=red, label='poisoned local graident')
plt.scatter(x5/2, x6/2, marker='o', color=red)
plt.scatter(x7/2, x8/2, marker='o', color=red)
plt.xlim(-1.0, 0.8)
plt.ylim(-1.0, 0.8)
# plt.xlabel('x')
# plt.ylabel('y')
plt.axis('off')
plt.title("(a) Gradient distribution \n in conventional federated learning. ",
          y=0, loc='center', fontsize=15)

plt.xticks([])  # 不显示x轴
plt.yticks([])  # 不显示y轴


n = 200
m = 20
np.random.seed(2)
random.seed(30)
t = np.random.random(size=n) * 2 * np.pi - np.pi
x1 = np.cos(t)
x2 = np.sin(t)

for i in range(n):
    len = np.sqrt(np.random.random())
    x1[i] = x1[i] * len/2-random.uniform(0, 1)
    x2[i] = x2[i] * len/2-random.uniform(0, 1)


s = np.random.random(size=m) * 2 * np.pi - np.pi
x3 = np.cos(s)
x4 = np.sin(s)
for j in range(m):
    len = np.sqrt(0.4)
    x3[j] = x3[j] * len/3-random.uniform(0, 0.5)-0.2
    x4[j] = x4[j] * len/3 - random.uniform(0, 0.5)-0.2


plt.subplot(122)
plt.scatter(x1/2, x2/2, marker='o', color=blue,)
plt.scatter(x3/2, x4/2, marker='o', color=red,)
plt.title('(b) Gradient distribution \n in conventional differential private federated learning.',
          y=0, loc='center', fontsize=15)
# plt.title("(a) Gradient distribution in conventional federated learning. ",y=0,loc='center')
plt.axis('off')


plt.xlim(-1.0, 0.8)
plt.ylim(-1.0, 0.8)
# plt.xlabel('x')
# plt.ylabel('y')
plt.axis('off')

plt.xticks([])  # 不显示x轴
plt.yticks([])  # 不显示y轴

# plt.legend(loc='upper center')
# plt.title('Random Scatter',)
# plt.grid(True)
fig.legend(ncol=2, loc='upper center', fontsize=15)
plt.savefig('imag.png', dpi=1000)


plt.show()


'''
import numpy as np
import matplotlib.pyplot as plt
 
# Fixing random state for reproducibility
np.random.seed(19680801)
 
 
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
 
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
'''
