import csv
import matplotlib.pyplot as plt
import numpy as np
import os

#
# 1. tab:blue
#
# 2. tab:orange
#
# 3. tab:green
#
# 4. tab:red
#
# 5. tab:purple
#
# 6. tab:brown
#
# 7. tab:pink
#
# 8. tab:gray
#
# 9. tab:olive
#
# 10. tab:cyan


def process():
    with open("tmp.txt", "r", encoding="utf8") as f_in:
        reader = csv.reader(f_in)
        with open("tmp2.csv", "w", encoding="utf-8") as f_out:
            writer = csv.writer(f_out)
            for item in reader:
                item = item[0].split("\t")
                print(item)
                writer.writerow([item_.split("+")[0] for item_ in item])
                # writer.writerow(["$"+"_{".join(item_.split("+"))+"}$" for item_ in item])


def process2():
    with open("data.txt", "r", encoding="utf8") as f_in:
        reader = csv.reader(f_in)
        out_str = "["
        for item in reader:
            item = item[0].split("\t")
            try:
                item = [float(i.split("+")[0]) for i in item]
            except:
                print(item)
                continue
            out_str_row = "["
            for item_ in item:
                out_str_row += "{:.2f},".format(item_)
            out_str_row += "],\n"
            out_str += out_str_row
        out_str += "]"
        print(out_str)


def plot1():
    # baselines plot

    fig = plt.figure(figsize=(9, 6))
    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    labels = ["TS-FCN", "TS-RNN", "TS-CSW", "TS-ATT", "TS-GNN"]
    colors = ["tab:green", "tab:cyan", "tab:blue", "tab:pink", "tab:purple"]
    # colors = ["green", "tab:green", "tab:blue", "blue", "tab:purple"]

    plt.subplot(2, 3, 1)
    n_components_range = range(1, 6)
    f1_means = [
        [36.14, 22.79, 18.29, 12.45, 0.83],
        [73.27, 68.19, 59.82, 46.99, 32.71],
        [75.37, 67.46, 60.62, 49.36, 33.05],
        [74.11, 67.63, 60.15, 48.19, 29.73],
        [72.22, 65.98, 56.43, 42.78, 26.09]
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        plt.bar(
            xpos,
            f1_means[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    plt.ylim(0, 110)
    plt.xticks(n_components_range, ["50%", "40%", "30%", "20%", "10%"],)
    # plt.legend(["TS-FCN", "TS-RNN","TS-CSW", "LSTMATT", "GNN"], loc=9,prop={'size': 8}, ncol=3)
    plt.xlabel("SRS")
    plt.ylabel("$F_1$ score")
    plt.title("Tweet AC")
    fig.legend(labels, loc="upper center", ncol=5, prop={'size': 12})
    plt.hlines(50, 0.5, 5.5, color="red", ls="--")
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines["right"].set_visible(False)
    # plt.text(0.4, 55, "50 $F_1$", fontsize=14)

    plt.subplot(2, 3, 4)
    n_components_range = range(1, 6)
    f1_means = [
        [43.31, 30.47, 7.95, 4.77, 0.21],
        [56.99, 49.87, 40.78, 21.25, 9.62],
        [64.22, 55.76, 45.42, 28.95, 13.30],
        [50.85, 41.31, 27.81, 16.58, 7.85],
        [62.41, 42.49, 31.35, 25.06, 4.81]
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        plt.bar(
            xpos,
            f1_means[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    plt.ylim(0, 110)
    plt.xticks(n_components_range, ["50%", "40%", "30%", "20%", "10%"],)
    # plt.legend(["TS-FCN", "TS-RNN","TS-CSW", "LSTMATT", "GNN"], loc=9,prop={'size': 8}, ncol=3)
    plt.xlabel("SRS")
    plt.ylabel("$F_1$ score")
    plt.title("Tweet ADG")
    plt.hlines(50, 0.5, 5.5, color="red", ls="--")
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines["right"].set_visible(False)
    # plt.text(0.4, 55, "50 $F_1$", fontsize=14)

    plt.subplot(2, 3, 2)
    n_components_range = range(1, 6)
    f1_means = [
        [36.35, 30.43, 19.96, 12.42, 0.00],
        [65.55, 60.52, 53.30, 43.11, 24.23],
        [72.30, 62.47, 54.43, 36.91, 27.33],
        [64.16, 60.30, 52.29, 39.92, 26.11],
        [69.01, 60.46, 52.45, 39.57, 23.84]
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        plt.bar(
            xpos,
            f1_means[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    plt.ylim(0, 110)
    plt.xticks(n_components_range, ["50%", "40%", "30%", "20%", "10%"],)
    # plt.legend(["TS-FCN", "TS-RNN","TS-CSW", "LSTMATT", "GNN"], loc=9,prop={'size': 8}, ncol=3)
    plt.xlabel("SRS")
    plt.ylabel("$F_1$ score")
    plt.title("Reddit AC")
    plt.hlines(50, 0.5, 5.5, color="red", ls="--")
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines["right"].set_visible(False)
    # plt.text(0.4, 55, "50 $F_1$", fontsize=14)

    plt.subplot(2, 3, 5)
    n_components_range = range(1, 6)
    f1_means = [
        [33.10, 14.22, 5.96, 4.38, 0.09],
        [41.27, 34.32, 25.29, 13.73, 5.08],
        [49.36, 45.50, 19.90, 12.46, 15.13],
        [41.01, 31.39, 22.59, 13.74, 4.70],
        [45.43, 42.88, 33.34, 24.88, 7.00]
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        plt.bar(
            xpos,
            f1_means[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    plt.ylim(0, 110)
    plt.xticks(n_components_range, ["50%", "40%", "30%", "20%", "10%"],)
    # plt.legend(["TS-FCN", "TS-RNN","TS-CSW", "LSTMATT", "GNN"], loc=9,prop={'size': 8}, ncol=3)
    plt.xlabel("SRS")
    plt.ylabel("$F_1$ score")
    plt.title("Reddit ADG")
    plt.hlines(50, 0.5, 5.5, color="red", ls="--")
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines["right"].set_visible(False)
    # plt.text(0.4, 55, "50 $F_1$", fontsize=14)

    plt.subplot(2, 3, 3)
    n_components_range = range(1, 6)
    f1_means = [
        [0.80, 0.40,  0.80, 0, 0.00],
        [16.92, 12.60, 11.43, 4.39, 2.41],
        [13.16, 7.98, 6.19, 6.51, 5.97],
        [17.47, 12.01, 8.28, 5.78, 1.14],
        [23.42, 17.45, 15.62, 9.82, 0.98]
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        plt.bar(
            xpos,
            f1_means[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    plt.ylim(0, 110)
    plt.xticks(n_components_range, ["50%", "40%", "30%", "20%", "10%"], )
    # plt.legend(["TS-FCN", "TS-RNN","TS-CSW", "LSTMATT", "GNN"], loc=9,prop={'size': 8}, ncol=3)
    plt.xlabel("SRS")
    plt.ylabel("$F_1$ score")
    plt.title("Weibo AC")
    plt.hlines(50, 0.5, 5.5, color="red", ls="--")
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines["right"].set_visible(False)
    # plt.text(0.4, 55, "50 $F_1$", fontsize=14)

    plt.subplot(2, 3, 6)
    n_components_range = range(1, 6)
    f1_means = [
        [2.84, 0.72, 0.87, 0.00, 0.00],
        [12.58, 10.21, 6.42, 1.58, 2.77],
        [17.55, 5.41, 4.92, 4.87, 8.14],
        [11.14, 9.84, 6.21, 2.62, 2.25],
        [33.41, 27.59, 13.38, 6.72, 1.12]
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        plt.bar(
            xpos,
            f1_means[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    plt.ylim(0, 110)
    plt.xticks(n_components_range, ["50%", "40%", "30%", "20%", "10%"], )
    # plt.legend(["TS-FCN", "TS-RNN","TS-CSW", "LSTMATT", "GNN"], loc=9,prop={'size': 8}, ncol=3)
    plt.xlabel("SRS")
    plt.ylabel("$F_1$ score")
    plt.title("Weibo ADG")
    plt.hlines(50, 0.5, 5.5, color="red", ls="--")
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines["right"].set_visible(False)
    # plt.text(0.4, 55, "50 $F_1$", fontsize=14)
    # fig.legend(labels, loc="upper center", ncol=5)
    plt.savefig("fig4-1.pdf", bbox_inches="tight")
    plt.show()


def plot2():
    plt.figure(figsize=(9, 5))
    plt.subplots_adjust(hspace=0.5, wspace=0.3)
    colors = ["tab:green", "tab:cyan", "tab:blue", "tab:pink", "tab:purple"]

    ax1 = plt.subplot(2, 2, 1)
    ax2 = ax1.twinx()
    n_components_range = range(0, 5)
    f1_means = [
        [1.06, 0.01, 0.81, 0.68, 0.29],
        [0.22, 0.63, 0.65, 0.53, 0.37],
        [2.92, 0.76, 1.21, 0.29, 0.79],
        [0.48, 0.86, 0.81, 0.55, 0.13],
        [0.33, 1.60, 0.85, 2.42, 0.05]
    ]
    # f1_relatives = [
    #     [1.57,0.01,0.99,0.22,0.95],
    #     [0.28,0.78,0.76,1.22,0.93],
    #     [3.84,0.94,1.41,0.72,0.91],
    #     [0.63,1.06,0.94,0.69,1.23],
    #     [0.46,2.09,1.02,3.00,0.81]
    # ]
    # for i, f1_mean in enumerate(f1_means):
    #     ax1.plot(f1_mean, c=colors[i])

    # for i, f1_relative in enumerate(f1_relatives):
    #     ax2.plot(f1_relative,"o-", c=colors[i], )
    # plt.ylim(0, 110)
    # ax1.set_ylim(0,4)
    # ax2.set_ylim(0,4)
    plt.xticks(n_components_range, ["50%", "40%", "30%", "20%", "10%"][::-1], )
    plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"],
               loc=9, prop={'size': 8}, ncol=3)
    plt.xlabel("SRS")
    plt.ylabel("$F_1$ score")
    plt.title("Reddit VLC BPW=4.17")

    # plt.hlines(50, 0.5, 5.5, color="red", ls="--")
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.savefig("fig3-5.pdf", bbox_inches="tight")
    plt.show()


def plot3():
    fig = plt.figure(figsize=(18, 8))
    plt.subplots_adjust(hspace=0.5, wspace=0.2)
    colors = ["tab:green", "tab:cyan", "tab:blue", "tab:pink", "tab:purple"]
    labels = ["TS-FCN", "TS-RNN", "TS-CSW", "TS-ATT", "TS-GNN"]
    n_components_range = range(0, 10)

    ax1 = plt.subplot(3, 2, 1)
    plt.xticks(n_components_range, ["0.45", "1.46", "2.38", "3.23",
                                    "4.00", "4.69", "5.30", "5.82", "5.28", "6.71"], rotation=45)
    f1_gains = [
        [1.4, 1.58, 2.15, -0.29, 2.13, 5.62, 16.4, 34.61, 20.54, 8.54],
        [0.54, 0.1, 0.18, 0.6, 0.49, 0.22, 2.85, 1.86, 0.77, 1.96],
        [1.55, 0.06, 0.34, 0.18, 1.23, 1.34, 2.85, 3.58, 1.77, 1.75, ],
        [1.6, 0.02, 0.5, 0.14, 0.76, 0.78, 1.32, 5.19, 1.33, 0.81],
        [1.36, 0.95, 1.3, 1.3, 1.57, 1.12, 4.98, 4.21, 12.41, 6.75]
    ]
    f1_means = [
        [86.21, 84.93, 79.33, 77.74, 69.13, 59.13, 37.70, 12.97, 3.36, 0.00],
        [89.21, 89.00, 84.19, 82.02, 75.67, 74.03, 64.13, 54.77, 35.02, 24.23],
        [88.88, 89.51, 84.86, 81.49, 74.89, 72.58, 61.63, 55.01, 38.87, 27.33],
        [88.88, 88.92, 84.42, 81.58, 65.59, 72.88, 64.02, 52.35, 34.53, 26.11],
        [87.72, 86.86, 81.87, 77.84, 70.74, 64.17, 52.78, 45.73, 26.82, 23.84],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i],
                 c=colors[i], linewidth=2.5, alpha=0.8)
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 10)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)

    ax1.set_xlabel("BPW", loc="right", fontsize=12)
    plt.title("Reddit AC SRS=10%")

    ax1 = plt.subplot(3, 2, 2)
    plt.xticks(n_components_range, ["0.45", "1.46", "2.38", "3.23",
                                    "4.00", "4.69", "5.30", "5.82", "5.28", "6.71"], rotation=45)
    f1_gains = [
        [2.9, 1.76, 1.19, 0.73, 0.54, 0.63, 1.85, 5.35, 8.37, 16.49],
        [0.21, 0.19, 0.24, 0.17, 0.5, 0.75, 0.97, 1.42, 2.8, 0.72, ],
        [0.09, 0.11, 0.24, 0.06, 0.43, 1.07, 1.46, 0.05, 0.24, 0.83],
        [0.06, 0.27, 0.23, 0.31, 0.59, 1.12, 1.43, 1.78, 1.81, 1.65],
        [0.07, 0.25, 0.16, 0.11, 0.38, 0.84, 0.97, 1.95, 1.43, -0.1]
    ]
    f1_means = [
        [90.29, 90.55, 88.70, 87.74, 85.60, 83.70, 79.44, 70.56, 58.70, 36.35],
        [95.33, 94.70, 93.12, 91.79, 89.70, 87.80, 85.70, 81.29, 74.63, 65.55],
        [95.50, 95.12, 93.63, 91.55, 89.25, 88.02, 85.19, 83.19, 77.62, 72.30],
        [95.31, 94.62, 93.28, 92.00, 89.90, 88.15, 85.44, 80.77, 74.75, 64.16],
        [95.01, 93.84, 92.12, 90.86, 88.23, 85.79, 83.26, 79.10, 74.61, 68.81],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i],
                 c=colors[i], linewidth=2.5, alpha=0.8)
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 10)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)
    plt.xlabel("BPW")
    plt.title("Reddit AC SRS=50%")

    ax1 = plt.subplot(3, 2, 3)
    plt.xticks(n_components_range, ["0.37", "1.39", "2.40", "3.23",
                                    "4.18", "4.96", "5.68", "6.33", "6.94", "7.54"], rotation=45)
    f1_gains = [
        [3.94, 3.97, 0.3, 0.18, 4.14, 5.07, 12.7, 32, 25.81, 16.19],
        [7.07, 3.56, 5.28, -0.06, 0.19, 0.08, -1.62, 0.09, 2.53, 3.22],
        [7.08, 5.48, 5.79, 0.43, 4.65, 1.7, 0.59, 0.69, 2.2, 1.59, ],
        [6.97, 5.94, 6, -0.54, 0.98, 1.32, 0.89, 2.26, 6.65, 4.6],
        [5.32, 4.53, 4.49, 0.68, 2.97, 1.02, 2.75, 5.69, 5.06, 8.51]
    ]
    f1_means = [
        [58.34, 59.77, 61.49, 63.34, 50.08, 54.15, 32.51, 4.98, 2.21, 0.83],
        [62.71, 66.08, 64.68, 69.74, 63.60, 71.43, 65.38, 53.63, 47.29, 32.71],
        [63.42, 65.55, 64.19, 71.44, 61.32, 70.85, 65.61, 54.18, 51.19, 33.05],
        [62.98, 64.18, 62.44, 70.42, 61.07, 70.07, 63.80, 52.56, 44.02, 29.73],
        [60.43, 61.99, 62.11, 66.55, 56.67, 65.26, 57.56, 44.48, 39.69, 26.09],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i],
                 c=colors[i], linewidth=2.5, alpha=0.8)
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 10)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)
    plt.xlabel("BPW")
    plt.title("Tweet AC SRS=10%")

    ax1 = plt.subplot(3, 2, 4)
    plt.xticks(n_components_range, ["0.37", "1.39", "2.40", "3.23",
                                    "4.18", "4.96", "5.68", "6.33", "6.94", "7.54"], rotation=45)
    f1_gains = [
        [-0.32, -0.14, 0.17, 0.02, 5.75, 4.64, 3.26, 8.23, 20.85, 23.95],
        [0.36, 0.05, 0.6, 0.04, -0.09, 0.31, 0.07, 0.24, 0.29, 2.97],
        [0.16, -0.29, -0.06, -0.57, -0.35, 0.54, 0.07, -0.07, 2.03, 2.44],
        [0.04, 0.16, 0.56, 0.16, 0.39, 0.02, -0.13, 0.13, 0.06, 1.14],
        [0.52, 0.64, 0.07, -0.45, 0.09, -0.21, 0.53, 0.13, 3.25, 1.24]
    ]
    f1_means = [
        [89.83, 88.57, 86.07, 85.31, 77.51, 77.39, 74.26, 63.52, 46.30, 36.14],
        [93.74, 92.90, 91.41, 91.26, 90.62, 89.11, 87.99, 85.18, 80.29, 73.29],
        [94.72, 94.33, 92.91, 91.97, 91.23, 88.85, 88.25, 86.19, 80.40, 75.37],
        [93.88, 92.73, 91.44, 91.30, 90.46, 88.67, 87.88, 85.34, 81.04, 74.11],
        [92.63, 91.98, 90.19, 90.27, 88.82, 87.84, 85.20, 82.90, 76.03, 72.22],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i],
                 c=colors[i], linewidth=2.5, alpha=0.8)
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 10)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)
    plt.xlabel("BPW")
    plt.title("Tweet AC SRS=50%")

    ax1 = plt.subplot(3, 2, 5)
    plt.xticks(n_components_range, ["0.24", "1.17", "2.00", "2.66", "3.27", "3.76", "4.20", "4.52", "4.88", "5.09"],
               rotation=45)
    f1_gains = [
        [20.7, 16.36, 33.69, 30.48, 29.57, 20.51, 8.36, 11.09, 6.72, 8.46],
        [6.18, 5.68, 14.96, 16.06, 11.13, 11.95, 11.21, 6.98, 11.18, 7.28],
        [13.3, 9.66, 15.19, 16.58, 11.26, 7.75, 11.15, 9.21, 6.64, 1.82],
        [8.43, 3.61, 13.63, 13.39, 10.17, 11.59, 7.14, 6.92, 5.07, 3.34],
        [9.95, 8.97, 16.24, 22.82, 17.46, 18.85, 17.92, 12.74, 10.42, 11.18]
    ]
    f1_means = [
        [49.21, 38.29, 11.48, 0, 0, 0, 0, 0, 0, 0],
        [66.58, 52.31, 35.89, 17.47, 14.08, 6.34, 3.55, 3.75, 1.32, 2.41],
        [65.12, 52.25, 36.00, 15.87, 12.44, 7.69, 2.13, 5.12, 5.26, 5.97],
        [64.87, 53.77, 36.46, 18.41, 14.86, 6.36, 2.77, 4.05, 3.11, 1.14],
        [61.86, 46.09, 28.40, 6.17, 7.49, 2.61, 1.02, 1.07, 1.16, 0.98],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i],
                 c=colors[i], linewidth=2.5, alpha=0.8)
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 30)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)
    plt.xlabel("BPW")
    plt.title("Weibo AC SRS=10%")

    ax1 = plt.subplot(3, 2, 6)
    plt.xticks(n_components_range, ["0.24", "1.17", "2.00", "2.66", "3.27", "3.76", "4.20", "4.52", "4.88", "5.09"],
               rotation=45)
    f1_gains = [
        [7.41, 19.48, 28.66, 36.14, 47.45, 55.61, 50.63, 51.72, 48.67, 51.15],
        [2.83, 5.8, 12.94, 17.66, 22.5, 23.56, 26.13, 29.77, 29.42, 30.49],
        [3.82, 7.42, 13.61, 18.17, 28.82, 28.71, 39.23, 40.12, 33.58, 34.15],
        [3.36, 6.63, 11.44, 15.6, 23.28, 26.19, 24.19, 29.23, 24.55, 22.45],
        [3.01, 8.92, 19.2, 20.92, 28.36, 27.15, 27.15, 39.92, 27.16, 40.31]
    ]
    f1_means = [
        [82.28, 66.34, 52.07, 41.46, 24.86, 10.37, 10.58, 2.44, 3.42, 0.80],
        [89.32, 80.84, 68.86, 60.14, 44.87, 36.57, 28.99, 23.20, 19.64, 16.92],
        [89.23, 80.14, 69.45, 59.11, 40.44, 32.82, 21.86, 15.12, 19.39, 13.16],
        [89.17, 80.38, 69.97, 60.65, 44.08, 35.19, 27.79, 21.17, 16.93, 17.47],
        [88.00, 76.30, 60.34, 53.07, 44.39, 43.39, 39.48, 27.16, 37.52, 23.42],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i],
                 c=colors[i], linewidth=2.5, alpha=0.8)
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 30)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)
    plt.xlabel("BPW")
    plt.title("Weibo AC SRS=50%")

    fig.legend(labels, loc="upper center", ncol=5, prop={'size': 15})
    plt.savefig("fig3-5.pdf", bbox_inches="tight")
    plt.show()


def plot4():
    fig = plt.figure(figsize=(18, 8))
    plt.subplots_adjust(hspace=0.5, wspace=0.2)
    colors = ["tab:green", "tab:cyan", "tab:blue", "tab:pink", "tab:purple"]
    labels = ["TS-FCN", "TS-RNN", "TS-CSW", "TS-ATT", "TS-GNN"]
    n_components_range = range(0, 10)

    ax1 = plt.subplot(3, 2, 1)
    plt.xticks(n_components_range, ["0.45", "1.46", "2.38", "3.23",
                                    "4.00", "4.69", "5.30", "5.82", "5.28", "6.71"], rotation=45)
    f1_gains = [
        [1.4, 1.58, 2.15, -0.29, 2.13, 5.62, 16.4, 34.61, 20.54, 8.54],
        [0.54, 0.1, 0.18, 0.6, 0.49, 0.22, 2.85, 1.86, 0.77, 1.96],
        [1.55, 0.06, 0.34, 0.18, 1.23, 1.34, 2.85, 3.58, 1.77, 1.75, ],
        [1.6, 0.02, 0.5, 0.14, 0.76, 0.78, 1.32, 5.19, 1.33, 0.81],
        [1.36, 0.95, 1.3, 1.3, 1.57, 1.12, 4.98, 4.21, 12.41, 6.75]
    ]
    f1_means = [
        [86.21, 84.93, 79.33, 77.74, 69.13, 59.13, 37.70, 12.97, 3.36, 0.00],
        [89.21, 89.00, 84.19, 82.02, 75.67, 74.03, 64.13, 54.77, 35.02, 24.23],
        [88.88, 89.51, 84.86, 81.49, 74.89, 72.58, 61.63, 55.01, 38.87, 27.33],
        [88.88, 88.92, 84.42, 81.58, 65.59, 72.88, 64.02, 52.35, 34.53, 26.11],
        [87.72, 86.86, 81.87, 77.84, 70.74, 64.17, 52.78, 45.73, 26.82, 23.84],
    ]
    f1_gains = np.array(f1_gains)
    f1_means = np.array(f1_means)
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_means[i],
            width=0.15,
            color=colors[i],
            label=labels[i], alpha=0.

        )

    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            bottom=f1_means[i],
            height=f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i],
        )

    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    # ax2 = ax1.twinx()
    # for i, f1_mean in enumerate(f1_means):
    #     ax2.plot(f1_mean, label=labels[i], c=colors[i])
    ax1.set_ylabel("$F_1$ scores")
    # ax1.set_ylim(0, 10)
    # ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)

    plt.xlabel("BPW")
    plt.title("Reddit AC SRS=10%")

    ax1 = plt.subplot(3, 2, 2)
    plt.xticks(n_components_range, ["0.45", "1.46", "2.38", "3.23",
                                    "4.00", "4.69", "5.30", "5.82", "5.28", "6.71"], rotation=45)
    f1_gains = [
        [2.9, 1.76, 1.19, 0.73, 0.54, 0.63, 1.85, 5.35, 8.37, 16.49],
        [0.21, 0.19, 0.24, 0.17, 0.5, 0.75, 0.97, 1.42, 2.8, 0.72, ],
        [0.09, 0.11, 0.24, 0.06, 0.43, 1.07, 1.46, 0.05, 0.24, 0.83],
        [0.06, 0.27, 0.23, 0.31, 0.59, 1.12, 1.43, 1.78, 1.81, 1.65],
        [0.07, 0.25, 0.16, 0.11, 0.38, 0.84, 0.97, 1.95, 1.43, -0.1]
    ]
    f1_means = [
        [90.29, 90.55, 88.70, 87.74, 85.60, 83.70, 79.44, 70.56, 58.70, 36.35],
        [95.33, 94.70, 93.12, 91.79, 89.70, 87.80, 85.70, 81.29, 74.63, 65.55],
        [95.50, 95.12, 93.63, 91.55, 89.25, 88.02, 85.19, 83.19, 77.62, 72.30],
        [95.31, 94.62, 93.28, 92.00, 89.90, 88.15, 85.44, 80.77, 74.75, 64.16],
        [95.01, 93.84, 92.12, 90.86, 88.23, 85.79, 83.26, 79.10, 74.61, 68.81],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i], c=colors[i])
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 10)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)
    plt.xlabel("BPW")
    plt.title("Reddit AC SRS=50%")

    ax1 = plt.subplot(3, 2, 3)
    plt.xticks(n_components_range, ["0.37", "1.39", "2.40", "3.23",
                                    "4.18", "4.96", "5.68", "6.33", "6.94", "7.54"], rotation=45)
    f1_gains = [
        [3.94, 3.97, 0.3, 0.18, 4.14, 5.07, 12.7, 32, 25.81, 16.19],
        [7.07, 3.56, 5.28, -0.06, 0.19, 0.08, -1.62, 0.09, 2.53, 3.22],
        [7.08, 5.48, 5.79, 0.43, 4.65, 1.7, 0.59, 0.69, 2.2, 1.59, ],
        [6.97, 5.94, 6, -0.54, 0.98, 1.32, 0.89, 2.26, 6.65, 4.6],
        [5.32, 4.53, 4.49, 0.68, 2.97, 1.02, 2.75, 5.69, 5.06, 8.51]
    ]
    f1_means = [
        [58.34, 59.77, 61.49, 63.34, 50.08, 54.15, 32.51, 4.98, 2.21, 0.83],
        [62.71, 66.08, 64.68, 69.74, 63.60, 71.43, 65.38, 53.63, 47.29, 32.71],
        [63.42, 65.55, 64.19, 71.44, 61.32, 70.85, 65.61, 54.18, 51.19, 33.05],
        [62.98, 64.18, 62.44, 70.42, 61.07, 70.07, 63.80, 52.56, 44.02, 29.73],
        [60.43, 61.99, 62.11, 66.55, 56.67, 65.26, 57.56, 44.48, 39.69, 26.09],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i], c=colors[i])
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 10)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)
    plt.xlabel("BPW")
    plt.title("Tweet AC SRS=10%")

    ax1 = plt.subplot(3, 2, 4)
    plt.xticks(n_components_range, ["0.37", "1.39", "2.40", "3.23",
                                    "4.18", "4.96", "5.68", "6.33", "6.94", "7.54"], rotation=45)
    f1_gains = [
        [-0.32, -0.14, 0.17, 0.02, 5.75, 4.64, 3.26, 8.23, 20.85, 23.95],
        [0.36, 0.05, 0.6, 0.04, -0.09, 0.31, 0.07, 0.24, 0.29, 2.97],
        [0.16, -0.29, -0.06, -0.57, -0.35, 0.54, 0.07, -0.07, 2.03, 2.44],
        [0.04, 0.16, 0.56, 0.16, 0.39, 0.02, -0.13, 0.13, 0.06, 1.14],
        [0.52, 0.64, 0.07, -0.45, 0.09, -0.21, 0.53, 0.13, 3.25, 1.24]
    ]
    f1_means = [
        [89.83, 88.57, 86.07, 85.31, 77.51, 77.39, 74.26, 63.52, 46.30, 36.14],
        [93.74, 92.90, 91.41, 91.26, 90.62, 89.11, 87.99, 85.18, 80.29, 73.29],
        [94.72, 94.33, 92.91, 91.97, 91.23, 88.85, 88.25, 86.19, 80.40, 75.37],
        [93.88, 92.73, 91.44, 91.30, 90.46, 88.67, 87.88, 85.34, 81.04, 74.11],
        [92.63, 91.98, 90.19, 90.27, 88.82, 87.84, 85.20, 82.90, 76.03, 72.22],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i], c=colors[i])
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 10)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)
    plt.xlabel("BPW")
    plt.title("Tweet AC SRS=50%")

    ax1 = plt.subplot(3, 2, 5)
    plt.xticks(n_components_range, ["0.24", "1.17", "2.00", "2.66", "3.27", "3.76", "4.20", "4.52", "4.88", "5.09"],
               rotation=45)
    f1_gains = [
        [20.7, 16.36, 33.69, 30.48, 29.57, 20.51, 8.36, 11.09, 6.72, 8.46],
        [6.18, 5.68, 14.96, 16.06, 11.13, 11.95, 11.21, 6.98, 11.18, 7.28],
        [13.3, 9.66, 15.19, 16.58, 11.26, 7.75, 11.15, 9.21, 6.64, 1.82],
        [8.43, 3.61, 13.63, 13.39, 10.17, 11.59, 7.14, 6.92, 5.07, 3.34],
        [9.95, 8.97, 16.24, 22.82, 17.46, 18.85, 17.92, 12.74, 10.42, 11.18]
    ]
    f1_means = [
        [49.21, 38.29, 11.48, 0, 0, 0, 0, 0, 0, 0],
        [66.58, 52.31, 35.89, 17.47, 14.08, 6.34, 3.55, 3.75, 1.32, 2.41],
        [65.12, 52.25, 36.00, 15.87, 12.44, 7.69, 2.13, 5.12, 5.26, 5.97],
        [64.87, 53.77, 36.46, 18.41, 14.86, 6.36, 2.77, 4.05, 3.11, 1.14],
        [61.86, 46.09, 28.40, 6.17, 7.49, 2.61, 1.02, 1.07, 1.16, 0.98],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i], c=colors[i])
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 30)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)
    plt.xlabel("BPW")
    plt.title("Weibo AC SRS=10%")

    ax1 = plt.subplot(3, 2, 6)
    plt.xticks(n_components_range, ["0.24", "1.17", "2.00", "2.66", "3.27", "3.76", "4.20", "4.52", "4.88", "5.09"],
               rotation=45)
    f1_gains = [
        [7.41, 19.48, 28.66, 36.14, 47.45, 55.61, 50.63, 51.72, 48.67, 51.15],
        [2.83, 5.8, 12.94, 17.66, 22.5, 23.56, 26.13, 29.77, 29.42, 30.49],
        [3.82, 7.42, 13.61, 18.17, 28.82, 28.71, 39.23, 40.12, 33.58, 34.15],
        [3.36, 6.63, 11.44, 15.6, 23.28, 26.19, 24.19, 29.23, 24.55, 22.45],
        [3.01, 8.92, 19.2, 20.92, 28.36, 27.15, 27.15, 39.92, 27.16, 40.31]
    ]
    f1_means = [
        [82.28, 66.34, 52.07, 41.46, 24.86, 10.37, 10.58, 2.44, 3.42, 0.80],
        [89.32, 80.84, 68.86, 60.14, 44.87, 36.57, 28.99, 23.20, 19.64, 16.92],
        [89.23, 80.14, 69.45, 59.11, 40.44, 32.82, 21.86, 15.12, 19.39, 13.16],
        [89.17, 80.38, 69.97, 60.65, 44.08, 35.19, 27.79, 21.17, 16.93, 17.47],
        [88.00, 76.30, 60.34, 53.07, 44.39, 43.39, 39.48, 27.16, 37.52, 23.42],
    ]
    for i in range(5):
        xpos = np.array(n_components_range) + 0.15 * (i - 2)
        ax1.bar(
            xpos,
            f1_gains[i],
            width=0.15,
            color=colors[i],
            label=labels[i]
        )
    # plt.legend(["TS-FCN", "TS-RNN", "TS-CSW", "LSTMATT", "GNN"], loc=2, prop={'size': 9}, ncol=3)
    ax2 = ax1.twinx()
    for i, f1_mean in enumerate(f1_means):
        ax2.plot(f1_mean, label=labels[i], c=colors[i])
    ax1.set_ylabel("$F_1$ gains")
    ax1.set_ylim(0, 30)
    ax2.set_ylabel("$F_1$ of baselines")
    # ax2.set_ylim(0, 140)
    plt.xlabel("BPW")
    plt.title("Weibo AC SRS=50%")

    fig.legend(labels, loc="upper center", ncol=5, prop={'size': 15})
    plt.savefig("fig3-6.pdf", bbox_inches="tight")
    plt.show()


def plot5():
    fig = plt.figure(figsize=(10, 7.2))
    plt.subplots_adjust(hspace=0.1, wspace=0.2)
    colors = ["tab:cyan",  "tab:purple", "tab:blue", "tab:pink", "tab:green", ]
    titles = ["TS-FCN", "TS-RNN", "TS-CSW", "TS-ATT", "TS-GNN"]
    labels = ["baselines", "ours", "Mod"]
    n_components_range = range(0, 9)

    f1_only_content = [
        [67.73, 77.25, 75.99, 76.74, 71.28],
        [0.00, 24.23, 27.33, 26.11, 23.84],
        [0.29, 5.08, 15.13, 4.70, 7.00],
        [0.00, 7.02, 9.12, 7.60, 5.54],
        [0.00, 2.41, 5.97, 1.14, 0.98],
        [0.00, 2.77, 8.14, 2.25, 1.12],
        [60.98, 70.40, 70.77, 70.89, 66.25],
        [0.83, 32.71, 33.05, 29.73, 26.09],
        [0.21, 9.62, 13.30, 7.85, 9.88]
    ]
    ours = [
        [68.79, 77.47, 78.91, 77.22, 71.61],
        [8.54, 26.19, 29.08, 26.92, 30.59],
        [1.92, 6.58, 14.92, 5.33, 12.02],
        [33.45, 23.94, 19.25, 25.64, 26.50],
        [8.46, 9.69, 7.79, 4.48, 12.16],
        [6.50, 8.60, 12.61, 8.88, 10.90],
        [62.40, 69.62, 71.17, 70.51, 66.43],
        [17.02, 35.93, 34.64, 34.44, 34.60],
        [4.90, 12.94, 14.07, 11.82, 15.38]
    ]
    f1_only_context = [
        [68.54, 76.53, 75.72, 75.07, 69.58],
        [8.71, 33.86, 36.03, 24.20, 17.35],
        [2.99, 6.82, 6.51, 0.00, 2.37],
        [9.86, 10.02, 20.85, 0.00, 9.35],
        [0.75, 1.26, 5.94, 0.00, 1.27],
        [0.28, 2.68, 4.63, 0.00, 1.50],
        [61.42, 68.35, 69.51, 67.82, 64.07],
        [10.83, 30.46, 37.66, 20.83, 29.61],
        [1.07, 7.37, 9.77, 3.91, 1.90]
    ]
    f1_only_content = np.array(f1_only_content).transpose()
    f1_only_context = np.array(f1_only_context).transpose()
    ours = np.array(ours).transpose()

    for index in range(5):
        plt.subplot(5, 1, index+1)
        plt.xticks([])
        # plt.xticks(n_components_range, ["Reddit VLC", "Reddit AC","Reddit ADG", "Weibo VLC", "Weibo AC","Weibo ADG",
        #                             "Tweet VLC", "Tweet AC","Tweet ADG"],rotation=45 )
        # xpos = np.array(n_components_range) + 0.15 * (- 1)
        plt.bar(
            np.array(n_components_range) + 0.2 * (- 1),
            f1_only_content[index],
            width=0.2,
            color=colors[0],
            label=labels[0]
        )
        plt.bar(
            np.array(n_components_range) + 0.2 * 0,
            ours[index],
            width=0.2,
            color=colors[1],
            label=labels[1]
        )
        plt.bar(
            np.array(n_components_range) + 0.2 * 1,
            f1_only_context[index],
            width=0.2,
            color=colors[2],
            label=labels[2]
        )
        # plt.ylabel("$F_1$ score")
        plt.ylabel(titles[index], fontsize=11)
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines["right"].set_visible(False)
    plt.xticks(n_components_range, ["Reddit VLC", "Reddit AC", "Reddit ADG", "Weibo VLC", "Weibo AC", "Weibo ADG",
                                    "Tweet VLC", "Tweet AC", "Tweet ADG"], rotation=45, fontsize=11)

    fig.legend(labels, loc="upper center", ncol=3, prop={'size': 15})
    plt.savefig("fig7.pdf", bbox_inches="tight")
    plt.show()


def plot6():
    # SRS=10
    # Tweet = [[63.77,63.16,62.63,62.40,62.97,62.82,],
    #     [69.61,70.40,70.98,69.62,70.20,70.54,],
    #     [70.62,70.63,70.76,71.17,72.09,70.56,],
    #     [69.80,70.18,70.61,70.51,70.70,69.85,],
    #     [66.29,66.39,65.72,66.43,67.54,67.41,],
    #     [13.83,15.14,16.16,17.02,18.13,14.97,],
    #     [34.27,34.12,35.99,35.93,34.97,36.54,],
    #     [36.08,35.52,34.09,34.64,35.95,33.08,],
    #     [35.01,35.24,34.85,34.33,34.60,34.59,],
    #     [34.44,32.29,34.47,34.60,36.69,33.89,],
    #     [2.37,4.04,7.58,4.90,9.31,6.56,],
    #     [12.38,14.32,13.35,12.94,14.83,14.11,],
    #     [16.12,16.18,14.49,14.07,16.94,14.22,],
    #     [12.52,9.31,10.29,11.82,12.91,10.87,],
    #     [10.52,12.90,13.83,15.38,14.92,13.74,],
    #     ]
    # Reddit =[[68.89, 70.07, 68.83, 68.79, 68.35, 68.42, ],
    #     [77.08, 77.23, 77.75, 77.47, 77.54, 76.24, ],
    #     [77.31, 77.43, 77.37, 78.91, 77.37, 78.43, ],
    #     [76.30, 77.08, 77.46, 77.22, 77.73, 77.32, ],
    #     [70.57, 71.21, 70.69, 71.61, 72.26, 72.02, ],
    #     [7.92, 9.01, 10.48, 8.54, 12.58, 13.69, ],
    #     [28.66, 27.82, 26.14, 26.19, 29.15, 28.71, ],
    #     [30.69, 31.90, 28.88, 29.08, 35.73, 32.53, ],
    #     [27.13, 26.45, 29.18, 26.92, 29.57, 28.50, ],
    #     [25.21, 30.25, 33.48, 30.59, 30.31, 31.40, ],
    #     [1.69, 1.14, 0.96, 1.92, 3.19, 3.71, ],
    #     [6.52, 6.38, 8.62, 6.58, 5.88, 7.33, ],
    #     [11.55, 12.71, 11.63, 14.94, 9.92, 8.23, ],
    #     [5.16, 5.20, 5.59, 5.33, 4.97, 4.67, ],
    #     [10.10, 9.81, 12.28, 12.02, 13.88, 13.56, ],
    #     ]
    # Weibo =[[21.63,34.37,27.48,33.45,30.76,29.07,],
    #     [20.44,25.10,26.46,23.94,23.80,24.22,],
    #     [19.21,20.23,19.98,19.25,23.61,23.79,],
    #     [20.66,25.40,24.24,25.64,21.29,27.35,],
    #     [25.49,29.54,28.53,26.50,29.02,29.50,],
    #     [1.66,4.99,6.29,8.46,7.27,11.88,],
    #     [4.61,6.33,6.43,9.69,8.04,8.94,],
    #     [6.73,3.73,11.60,7.79,12.51,8.43,],
    #     [2.74,6.18,5.88,4.48,4.93,4.50,],
    #     [12.04,8.94,13.15,12.16,11.11,12.96,],
    #     [0.00,1.41,7.00,6.50,8.33,12.40,],
    #     [8.37,7.65,9.24,8.60,10.89,10.09,],
    #     [10.01,8.07,13.39,12.61,7.11,8.25,],
    #     [6.96,7.16,6.64,8.88,8.66,7.52,],
    #     [10.62,10.36,12.29,10.90,9.64,10.65,],
    #     ]
    # SRS=50%
    Tweet = [
        [82.56, 82.50, 82.58, 82.64, 82.11, 82.29, ],
        [89.11, 89.37, 89.00, 89.29, 89.00, 89.31, ],
        [89.22, 89.26, 89.17, 89.24, 89.20, 89.03, ],
        [89.25, 89.16, 89.18, 89.31, 89.30, 89.22, ],
        [87.81, 87.24, 88.07, 87.96, 87.69, 87.34, ],
        [60.24, 60.51, 61.52, 60.09, 62.32, 61.27, ],
        [75.92, 76.01, 75.83, 76.24, 75.55, 76.03, ],
        [77.19, 76.98, 76.45, 77.81, 78.06, 77.31, ],
        [75.65, 76.03, 75.73, 75.25, 76.17, 75.82, ],
        [71.29, 75.05, 74.68, 73.46, 75.76, 75.41, ],
        [52.89, 50.39, 56.07, 52.70, 54.39, 54.07, ],
        [61.58, 57.92, 60.22, 56.15, 55.62, 55.26, ],
        [61.48, 67.96, 62.19, 67.41, 62.19, 64.54, ],
        [52.24, 52.01, 55.56, 52.63, 51.12, 49.80, ],
        [62.25, 60.75, 64.56, 65.35, 65.46, 64.67, ],
    ]
    Reddit = [
        [84.80, 85.04, 85.43, 85.04, 84.95, 85.29, ],
        [88.87, 88.85, 88.96, 88.86, 88.98, 88.88, ],
        [89.07, 88.97, 89.04, 88.73, 89.29, 89.41, ],
        [88.92, 88.94, 88.70, 88.53, 88.62, 89.12, ],
        [85.81, 86.67, 86.43, 86.37, 86.64, 86.43, ],
        [52.07, 54.31, 51.53, 52.84, 55.51, 54.94, ],
        [68.65, 67.81, 68.27, 66.27, 67.75, 66.53, ],
        [75.92, 71.88, 73.69, 73.13, 72.29, 71.41, ],
        [65.31, 67.39, 66.13, 65.81, 66.70, 66.64, ],
        [69.68, 69.22, 68.64, 68.71, 70.17, 68.02, ],
        [37.43, 40.38, 35.02, 41.12, 44.98, 43.87, ],
        [48.31, 46.22, 46.06, 46.43, 46.52, 47.08, ],
        [63.52, 59.34, 59.43, 54.52, 53.34, 56.41, ],
        [44.26, 44.22, 43.42, 45.90, 45.23, 44.37, ],
        [59.80, 56.17, 49.42, 56.80, 62.45, 54.90, ],
    ]
    Weibo = [
        [72.71, 73.53, 72.95, 73.75, 73.33, 73.03, ],
        [68.24, 70.25, 70.57, 69.57, 71.56, 70.49, ],
        [69.65, 68.86, 68.62, 70.25, 69.49, 68.86, ],
        [68.78, 69.90, 69.78, 70.06, 68.91, 70.34, ],
        [73.58, 73.50, 72.23, 71.13, 72.57, 71.91, ],
        [44.63, 43.84, 50.17, 51.95, 52.53, 52.83, ],
        [41.97, 44.78, 46.18, 47.41, 47.12, 48.69, ],
        [37.48, 47.86, 44.89, 47.31, 52.81, 52.57, ],
        [37.31, 43.18, 42.74, 39.92, 44.67, 44.18, ],
        [64.20, 63.72, 64.98, 63.73, 63.03, 61.89, ],
        [39.51, 44.47, 48.10, 44.19, 48.03, 48.30, ],
        [38.62, 40.62, 44.17, 40.69, 44.60, 43.90, ],
        [46.26, 46.13, 44.08, 43.61, 40.10, 47.25, ],
        [34.90, 41.73, 41.24, 42.20, 41.59, 36.47, ],
        [61.14, 58.47, 61.99, 63.14, 60.47, 62.06, ],
    ]
    Tweet = np.array(Tweet)
    Reddit = np.array(Reddit)
    Weibo = np.array(Weibo)
    fig = plt.figure(figsize=(8, 6))
    plt.subplots_adjust(hspace=0.2, wspace=0.2)
    colors = ["tab:cyan",  "tab:purple", "tab:blue",
              "black", "tab:green", "tab:pink"]
    methods = ["TS-FCN", "TS-RNN", "TS-CSW", "TS-ATT", "TS-GNN"]
    labels = ["2 heads", "4 heads", "6 heads",
              "8 heads", "10 heads", "12 heads"]
    dataset_names = ["Reddit", "Tweet", "Weibo"]
    n_components_range = range(0, 5)

    for index in range(9):
        plt.subplot(3, 3, index+1)
        plt.xticks([])
        if index <= 2:
            dataset = Reddit
        elif index <= 5:
            dataset = Tweet
        else:
            dataset = Weibo
        for k, _ in enumerate(labels):
            plt.bar(
                np.array(n_components_range) + 0.12 * (k - 2),
                dataset[5*(index % 3):5*(index % 3+1)].transpose()[k],
                width=0.12,
                color=colors[k],
                label=labels[k]
            )
        min = dataset[5*(index % 3):5*(index % 3+1)].min()
        max = dataset[5*(index % 3):5*(index % 3+1)].max()
        plt.ylim(min*0.95, max*1)
        # plt.ylabel(titles[index])
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines["right"].set_visible(False)
        if index >= 6:
            plt.xticks(n_components_range, methods, rotation=45)
        if index % 3 == 0:
            plt.ylabel(dataset_names[index//3], fontsize=12)
        if index == 0:
            plt.title("VLC")
        if index == 1:
            plt.title("AC")
        if index == 2:
            plt.title("ADG")

    fig.legend(labels, loc="upper center", ncol=6, prop={'size': 10})
    plt.savefig("fig8-1.pdf", bbox_inches="tight")
    plt.show()


def plot7():
    # SRS=10
    # Tweet = [[63.42,62.40,62.99,61.73,],
    #     [70.85,69.62,71.39,70.33,],
    #     [70.55,71.17,71.32,70.46,],
    #     [70.73,70.51,69.65,69.11,],
    #     [67.18,66.43,67.04,66.39,],
    #     [7.66,17.02,15.49,16.85,],
    #     [36.67,35.93,36.90,35.32,],
    #     [33.26,34.64,32.89,33.82,],
    #     [34.16,34.33,34.60,32.49,],
    #     [33.69,34.60,32.63,34.65,],
    #     [3.40,4.90,9.72,8.18,],
    #     [10.42,12.94,13.67,14.45,],
    #     [15.94,14.07,13.84,16.50,],
    #     [11.75,11.82,13.11,13.25,],
    #     [10.88,15.38,14.86,15.63,],
    #     ]
    # Reddit =[[69.67,68.79,68.63,69.42,],
    #     [77.11,77.47,77.29,77.66,],
    #     [78.45,78.91,77.38,78.74,],
    #     [76.84,77.22,77.35,76.77,],
    #     [70.19,71.61,71.65,72.53,],
    #     [9.99,8.54,9.97,12.59,],
    #     [29.52,26.19,26.51,27.61,],
    #     [30.53,29.08,31.50,31.27,],
    #     [26.35,26.92,28.51,27.27,],
    #     [32.51,30.59,28.87,29.13,],
    #     [3.25,1.92,3.06,5.47,],
    #     [6.04,6.58,6.22,5.53,],
    #     [13.05,14.94,8.37,14.00,],
    #     [6.69,5.33,4.26,4.96,],
    #     [13.22,12.02,15.08,14.69,],
    #     ]
    # Weibo =[[63.42,62.40,62.99,61.73,],
    #     [70.85,69.62,71.39,70.33,],
    #     [70.55,71.17,71.32,70.46,],
    #     [70.73,70.51,69.65,69.11,],
    #     [67.18,66.43,67.04,66.39,],
    #     [7.66,17.02,15.49,16.85,],
    #     [36.67,35.93,36.90,35.32,],
    #     [33.26,34.64,32.89,33.82,],
    #     [34.16,34.33,34.60,32.49,],
    #     [33.69,34.60,32.63,34.65,],
    #     [3.40,4.90,9.72,8.18,],
    #     [10.42,12.94,13.67,14.45,],
    #     [15.94,14.07,13.84,16.50,],
    #     [11.75,11.82,13.11,13.25,],
    #     [10.88,15.38,14.86,15.63,],
    #     ]
    # SRS = 50
    HC = [

        [97.01, 95.12, 98.05, 83.32, 74.27],  # 每个颜色(label)的三个数【改】
        [96.93, 94.69, 97.87, 80.81, 68.01],
        [97.33, 95.56, 98.87, 93.27, 89.62],
        [97.27, 94.91, 98.71, 93.17, 89.27],
    ]
    AC = [
         [97.52, 95.56, 97.69, 86.98, 83.03],  # 每个颜色(label)的三个数【改】
         [97.43, 95.2, 97.47, 86.9, 82.36],
         [97.69, 96.28, 97.96, 89.45, 84.59],
         [97.55, 95.75, 97.68, 89.21, 84.25],

    ]
    ADG = [
        [96.79, 93.54, 97.01, 75.47, 75.45],  # 每个颜色(label)的三个数【改】
        [96.68, 93.01, 96.69, 70.7, 76.01],
        [96.79, 94.78, 96.53, 92.02, 88],
        [96.54, 94.09, 95.96, 91.94, 87.74],
    ]

    HC = np.array(HC)
    AC = np.array(AC)
    ADG = np.array(ADG)
    fig = plt.figure(figsize=(9, 4))
    plt.subplots_adjust(hspace=0.2, wspace=0.2)
    colors = ["tab:cyan",  "black", "tab:blue",
              "tab:pink", "tab:green", "tab:orange"]
    methods = ["TS-FCN", "TS-RNN", "TS-CSW", "TS-ATT", "TS-GNN"]
    labels = ["Acc of CNN", "F1 of CNN",
              "Acc of SeSy", "F1 of SeSy"]
    dataset_names = ["HC", "AC", "ADG"]
    dataset = [HC, AC, ADG]
    n_components_range = range(0, 5)

    for index in range(3):
        plt.subplot(1, 3, index+1)

        for k, _ in enumerate(labels):
            plt.bar(
                np.array(n_components_range) + 0.2 * (k - 1.5),
                HC[k],
                width=0.2,
                color=colors[k],
                label=labels[k]
            )

        # plt.ylabel(titles[index])
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.legend(labels, loc="upper center", ncol=4, prop={'size': 11}, )
    plt.savefig("fig9-1.pdf", bbox_inches="tight")
    plt.show()


def plot8():
    Reddit = [
        [68.14, 68.79, 27.68, 0.00, 0.00, 0.00, 0.00, 0.00, 1.22, 0.00, ],
        [76.62, 77.47, 75.70, 53.52, 7.56, 0.00, 0.00, 2.17, 0.00, 0.00, ],
        [76.20, 78.91, 75.90, 75.68, 44.02, 14.30, 1.88, 3.75, 0.00, 0.28, ],
        [76.99, 77.22, 60.84, 7.81, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [12.69, 8.54, 0.10, 0.59, 0.00, 0.00, 0.00, 0.00, 0.00, 0.33, ],
        [33.79, 26.19, 16.81, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [32.71, 29.08, 29.97, 10.09, 0.00, 0.00, 1.11, 0.00, 0.00, 0.00, ],
        [28.65, 26.92, 0.00, 0.00, 0.00, 0.00, 0.00, 0.48, 0.00, 0.00, ],
        [5.78, 1.92, 0.62, 0.00, 0.19, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [13.51, 6.58, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [7.07, 14.94, 0.50, 0.00, 0.27, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [2.99, 5.33, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
    ]
    Tweet = [
        [61.94, 62.40, 49.23, 18.41, 6.27, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [67.82, 69.62, 55.09, 20.09, 0.00, 0.00, 0.00, 0.00, 0.22, 0.00, ],
        [69.56, 71.17, 68.80, 61.81, 13.45, 6.45, 0.00, 0.21, 4.93, 0.00, ],
        [69.49, 70.51, 33.82, 0.00, 6.16, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [16.78, 17.02, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [33.63, 35.93, 4.41, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [39.92, 34.64, 29.84, 9.99, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [34.89, 34.33, 7.16, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [6.09, 4.90, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [14.95, 12.94, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [12.56, 14.07, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [0.00, 11.82, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
    ]
    Tweet = np.array(Tweet)
    Reddit = np.array(Reddit)
    fig = plt.figure(figsize=(8, 6))
    plt.subplots_adjust(hspace=0.2, wspace=0.2)
    colors = ["tab:cyan", "black", "tab:blue",
              "tab:pink", "tab:green", "tab:orange"]
    methods = ["TS-FCN", "TS-RNN", "TS-CSW", "TS-ATT", "TS-GNN"]
    algs = ["VLC", "AC", "ADG"]
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    from scipy.interpolate import make_interp_spline
    for i in range(6):
        plt.subplot(3, 2, i+1)
        dataset = Tweet if i % 2 == 1 else Reddit
        for j in range(4):
            model = make_interp_spline(x, dataset[(i//2)*4+j])
            xs = np.linspace(1, 10, 100)
            ys = model(xs)
            plt.plot(xs, ys, label=methods[j], color=colors[j])
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines["right"].set_visible(False)
        print(i)
        if i == 0:
            plt.title("Reddit", fontsize=12)
        if i == 1:
            plt.title("Tweet", fontsize=12)
        if i == 4 or i == 5:
            plt.xlabel("number of layers", loc="right")
        if i % 2 == 0:
            plt.ylabel(algs[i % 3], fontsize=12)

    fig.legend(methods[:4], loc="upper center", ncol=4, prop={'size': 12})
    plt.savefig("fig10.png", bbox_inches="tight")
    plt.show()


def plot9():
    Weibo = [
        [14.67, 23.94, 0.00, 0.00, 0.00, 0.00, 1.82, 0.00, 0.00, 0.00, ],
        [1.47, 25.64, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [7.29, 9.69, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [0.00, 4.48, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [7.22, 8.60, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ],
        [0.00, 8.88, 0.00, 0.00, 0.00, 0.00, 2.04, 0.00, 0.00, 0.00, ],
    ]
    Weibo = np.array(Weibo)
    fig = plt.figure(figsize=(8, 4))
    plt.subplots_adjust(hspace=0.2, wspace=0.2)
    colors = ["tab:blue", "tab:pink", "tab:green", "tab:orange", "tab:cyan", ]
    methods = ["TS-FCN", "TS-RNN", "TS-CSW", "TS-ATT", "TS-GNN"]
    algs = ["VLC", "AC", "ADG"]
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    from scipy.interpolate import make_interp_spline
    for i in range(3):
        plt.subplot(3, 1, i+1)
        dataset = Weibo
        for j in range(2):
            # plt.plot(x, dataset[i*2+j], label=methods[j*2+1], color=colors[j])
            model = make_interp_spline(x, dataset[i*2+j])
            xs = np.linspace(1, 10, 100)
            ys = model(xs)
            plt.plot(xs, ys, label=methods[j*2+1], color=colors[j])
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.ylabel(algs[i], fontsize=12)
        if i == 2:
            plt.xlabel("number of layers", loc="right", fontsize=12)
        if i == 0:
            plt.title("Weibo", fontsize=15)

    fig.legend(["TS-RNN", "TS-ATT"], loc="upper right",
               ncol=1, prop={'size': 12})
    plt.savefig("fig11.png", bbox_inches="tight")
    plt.show()


def plot10():
    # SRS = 10
    Reddit = [
        [70.64, 71.61, 48.11, 6.97, 0.00, ],
        [21.29, 30.59, 4.01, 0.00, 0.00],
        [4.52, 12.02, 0.00, 0.00, 0.00]
    ]
    Tweet = [
        [60.61, 66.43, 38.37, 6.79, 0.00],
        [29.12, 34.60, 12.66, 0.00, 0.00],
        [6.02, 15.28, 0.00, 0.00, 0.00]
    ]
    Weibo = [
        [8.95, 26.50, 0.00, 0.00, 0.00],
        [1.91, 12.16, 0.00, 0.00, 0.00],
        [0.33, 10.90, 0.00, 0.00, 0.00]
    ]
    # SRS = 50
    # Reddit = [
    #     [86.43, 86.37, 87.63, 87.76, 67.93],
    #     [59.51, 68.71, 61.49, 54.06, 18.71],
    #     [37.63, 56.80, 28.26, 0.02, 0.00]
    # ]
    # Tweet = [
    #     [87.46, 87.96, 87.68, 80.68, 77.44],
    #     [72.93, 73.46, 71.10, 65.86, 39.22],
    #     [50.66, 65.35, 23.61, 12.95, 11.70]
    # ]
    # Weibo = [
    #     [52.44, 71.13, 45.22, 24.06, 4.45],
    #     [30.08, 63.73, 29.35, 12.97, 10.58],
    #     [28.94, 63.14, 33.56, 11.11, 5.15]
    # ]
    Tweet = np.array(Tweet)
    Reddit = np.array(Reddit)
    Weibo = np.array(Weibo)
    # dataset = np.array(Reddit+Tweet+Weibo)
    fig = plt.figure(figsize=(12, 5.5))
    plt.subplots_adjust(hspace=0.2, wspace=0.2)
    colors = ["tab:cyan", "tab:blue", "tab:pink", "tab:green", "tab:orange"]
    methods = ["TS-FCN", "TS-RNN", "TS-CSW", "TS-ATT", "TS-GNN"]
    labels = ["L=1", "L=2", "L=3", "L=4", "L=5"]
    dataset_names = ["Reddit", "Tweet", "Weibo"]
    n_components_range = range(0, 9)
    from scipy.interpolate import make_interp_spline
    # for k, _ in enumerate(labels):
    #     plt.bar(
    #         np.array(n_components_range) + 0.15 * (k - 2),
    #         dataset.transpose()[k]+5,
    #         width=0.15,
    #         color=colors[k],
    #         label=labels[k],
    #     )

    # plt.ylim((-10, 90))
    # plt.xticks(n_components_range, ["Reddit VLC","Reddit AC","Reddit ADG", "Tweet VLC", "Tweet AC", "Tweet ADG", "Weibo VLC", "Weibo AC", "Weibo ADG"], rotation=30)
    x = [1, 2, 3, 4, 5]
    for index in range(3):
        plt.subplot(3, 1, index+1)
        plt.plot(x, Reddit[index], label=dataset_names[0],
                 linewidth=3, color=colors[0])
        plt.plot(x, Tweet[index], label=dataset_names[1],
                 linewidth=3, color=colors[1])
        plt.plot(x, Weibo[index], label=dataset_names[2],
                 linewidth=3, color=colors[2])
        plt.xticks([1, 2, 3, 4, 5])
        plt.xlabel("L", fontsize=12, loc="right")
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines["right"].set_visible(False)
        if index == 0:
            plt.ylabel("VLC", fontsize=12)
        if index == 1:
            plt.ylabel("AC", fontsize=12)
        if index == 2:
            plt.ylabel("ADG", fontsize=12)

    fig.legend(dataset_names, loc="upper center", ncol=3, prop={'size': 14})
    plt.savefig("fig12.pdf", bbox_inches="tight")
    plt.show()


if __name__ == '__main__':
    # plot1()
    # plot3()
    # process()
    # process2()
    # plot6()
    plot7()
    # plot5()
    # plot8()
    # plot9()
    # plot10()
