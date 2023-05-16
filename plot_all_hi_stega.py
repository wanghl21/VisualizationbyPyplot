# -*- coding:utf-8 -*-
# https://matplotlib.org/gallery/index.html
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot
import seaborn as sns
palette = sns.color_palette("pastel")

color = [
    'lightcoral',
    'coral',
    'darkorange',
    'gold',
    'palegreen',
    'paleturquoise',
    'skyblue',
    'plum',
    'hotpink',
    'pink',
    'Mistyrose']
font = {'family': 'serif',
        'serif': 'Times New Roman',
        'weight': 'normal',
        'size': 10}
plt.rc('font', **font)
color = ['#cff09e', '#a8dba8', '#79bd9a', '#3b8686']
color0 = ['#FFFF7C', '#B1D372', '#6AA96A', '#377D65']
color1 = ['#cff09e', '#a8dba8', '#6AA96A', '#377D65']
color2 = ['#E2EFDA', '#DDEBF7', '#FFF2CC', '#FCE4D6']
# ylabels = ['0',' 10 ', ' 20 ', ' 30 ',' 40 ',' 50 ',' 60 ',' 70 ','80','90','100']
labels = ['gpt', ' model_1 ', ' model_2 ', ' model_3 ', ' model_4 ']  # 【改】

# for HC
h1 = [97.01, 95.12, 98.05, 83.32, 74.27]  # 每个颜色(label)的三个数【改】
h2 = [96.93, 94.69, 97.87, 80.81, 68.01]
h3 = [97.33, 95.56, 98.87, 93.27, 89.62]
h4 = [97.27, 94.91, 98.71, 93.17, 89.27]

# for AC
y1 = [97.52, 95.56, 97.69, 86.98, 83.03]  # 每个颜色(label)的三个数【改】
y2 = [97.43, 95.2, 97.47, 86.9, 82.36]
y3 = [97.69, 96.28, 97.96, 89.45, 84.59]
y4 = [97.55, 95.75, 97.68, 89.21, 84.25]

# for ADG_v2

z1 = [96.79, 93.54, 97.01, 75.47, 75.45]  # 每个颜色(label)的三个数【改】
z2 = [96.68, 93.01, 96.69, 70.7, 76.01]
z3 = [96.79, 94.78, 96.53, 92.02, 88]
z4 = [96.54, 94.09, 95.96, 91.94, 87.74]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars
plt.figure(figsize=(30, 16))
ax = plt.subplots(1, 3, sharex=True, sharey=True)

rects1 = ax[0].bar(x - width/2-0.1, h1,
                   width=width*0.8, label='Acc of CNN', color=color2[0], edgecolor='black', linewidth='0.1')  # 算法1颜色)#label标题【改】
rects2 = ax[0].bar(x + width/2-0.15, h2,
                   width=width*0.8, label='F1 of CNN', color=color2[1], edgecolor='black', linewidth='0.1')  # label标题【改】
rects3 = ax[0].bar(x + width*3/2-0.2, h3,
                   width=width*0.8, label='Acc of SeSy', color=color2[2], edgecolor='black', linewidth='0.1')  # label标题【改】
rects4 = ax[0].bar(x + width*5/2-0.25, h4,
                   width=width*0.8, label='F1 of SeSy', color=color2[3], edgecolor='black', linewidth='0.1')  # label标题【改】
#
# Add some text for labels, title and custom x-axis tick labels, etc.
ax[0].set_ylabel('Accuracy / F1(%)', fontsize=10)  # x标题【改】
ax[0].set_ylim([50, 105])
ax[0].set_xticks(x)
ax[0].set_xticklabels(labels, fontsize=8)
ax[0].set_title('HC')
# ax.set_yticklabels(ylabels,fontsize=15)
# ax.legend(ncol=2,fontsize=15,loc=3)
# upper center
# ax[0].legend(ncol=1, loc='lower left', fontsize=10)


# fig, ax = plt.subplot(1,2,2)
rects1 = ax[1].bar(x - width/2-0.1, y1,
                   width=width*0.8, label='Acc of CNN', color=color2[0], edgecolor='black', linewidth='0.1')  # 算法1颜色)#label标题【改】
rects2 = ax[1].bar(x + width/2-0.15, y2,
                   width=width*0.8, label='F1 of CNN', color=color2[1], edgecolor='black', linewidth='0.1')  # label标题【改】
rects3 = ax[1].bar(x + width*3/2-0.2, y3,
                   width=width*0.8, label='Acc of SeSy', color=color2[2], edgecolor='black', linewidth='0.1')  # label标题【改】
rects4 = ax[1].bar(x + width*5/2-0.25, y4,
                   width=width*0.8, label='F1 of SeSy', color=color2[3], edgecolor='black', linewidth='0.1')  # label标题【改】
#
# Add some text for labels, title and custom x-axis tick labels, etc.
# ax[1].set_ylabel('Accuracy / F1(%)', fontsize=10)  # x标题【改】
ax[1].set_ylim([60, 105])
ax[1].set_xticks(x)
ax[1].set_xticklabels(labels, fontsize=10)
ax[1].set_title('AC')

rects1 = ax[2].bar(x - width/2-0.1, z1,
                   width=width*0.8, label='Acc of CNN', color=color2[0], edgecolor='black', linewidth='0.1')  # 算法1颜色)#label标题【改】
rects2 = ax[2].bar(x + width/2-0.15, z2,
                   width=width*0.8, label='F1 of CNN', color=color2[1], edgecolor='black', linewidth='0.1')  # label标题【改】
rects3 = ax[2].bar(x + width*3/2-0.2, z3,
                   width=width*0.8, label='Acc of SeSy', color=color2[2], edgecolor='black', linewidth='0.1')  # label标题【改】
rects4 = ax[2].bar(x + width*5/2-0.25, z4,
                   width=width*0.8, label='F1 of SeSy', color=color2[3], edgecolor='black', linewidth='0.1')  # label标题【改】
#
# Add some text for labels, title and custom x-axis tick labels, etc.
# ax[2].set_ylabel('Accuracy / F1(%)', fontsize=10)  # x标题【改】
ax[2].set_ylim([50, 105])
ax[2].set_xticks(x)
ax[2].set_xticklabels(labels, fontsize=8)
# ax.set_yticklabels(ylabels,fontsize=15)
# ax.legend(ncol=2,fontsize=15,loc=3)
# upper center
num1 = 1.01
num2 = 0.5
num3 = 3
num4 = 0
# ax[0].legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4)
ax[0].legend(bbox_to_anchor=(0, -0.15), loc='lower left',
             ncol=4)  # , borderaxespad=0

# ax[0].legend(ncol=1, loc='lower left', fontsize=10)
ax[2].set_title('ADG')
plt.subplots_adjust(bottom=0.13)

# ax.set_yticklabels(ylabels,fontsize=15)
# ax.legend(ncol=2,fontsize=15,loc=3)
# upper center
# ax[1].legend(ncol=2, loc='lower left', fontsize=10)
# plt.subplots_adjust(bottom=0.13)
# plt.tight_layout()
# plt.show()
plt.savefig("All_steganalysis.pdf")
