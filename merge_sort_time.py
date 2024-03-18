from merge_sort import merge_sort
from timeit import default_timer as timer
from get_words import get_words_from_file
from matplotlib import pyplot as plt, use

use("agg")


def count_time_merge_sort():
    x_axis = []
    y_axis = []
    for i in range(10):
        words_to_sort = get_words_from_file((i + 1) * 1000)
        start = timer()
        merge_sort(words_to_sort)
        end = timer()
        x_axis.append((i + 1) * 1000)
        y_axis.append(end - start)
    return x_axis, y_axis


def plot_time_merge_sort():
    x_axis, y_axis = count_time_merge_sort()
    plt.plot(x_axis, y_axis)
    plt.title("Merge sort")
    plt.ylabel("Time[s]")
    plt.xlabel("Number of words")
    plt.savefig("merge_sort.png", format="png")


if __name__ == "__main__":
    plot_time_merge_sort()
