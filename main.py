from merge_sort_time import count_time_merge_sort
from bubble_sort_time import count_time_bubble_sort
from quick_sort_time import count_time_quick_sort
from selection_sort_time import count_time_selection_sort
from matplotlib import pyplot as plt, use

use("agg")


def main():
    merge_sort_times = count_time_merge_sort()
    bubble_sort_times = count_time_bubble_sort()
    selection_sort_times = count_time_selection_sort()
    quick_sort_times = count_time_quick_sort()

    plt.close("all")
    plt.plot(merge_sort_times[0], merge_sort_times[1], color="r", label="Merge sort")
    plt.plot(bubble_sort_times[0], bubble_sort_times[1], color="g", label="Bubble sort")
    plt.plot(quick_sort_times[0], quick_sort_times[1], color="b", label="Quick sort")
    plt.plot(
        selection_sort_times[0],
        selection_sort_times[1],
        color="y",
        label="Selection sort",
    )

    plt.title("Comparison of sorting algorithms")
    plt.ylabel("Time[s]")
    plt.xlabel("Number of words")
    plt.legend()
    plt.savefig("sorting_comparison.png", format="png")

    plt.yscale("log")
    plt.savefig("sorting_comparison_logarithmic.png", format="png")
    plt.close("all")


if __name__ == "__main__":
    main()
