from selection_sort import selection_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


def test_selection_sort_basic_number_sort():
    array = [6, 4, 3, 1, 9, 11, 23, 764, 12, 132, 16, 2]
    assert selection_sort(array) == sorted(array)


def test_selection_sort_characters_sort():
    array = ["Q", "w", "E", "r", "T", "y", "U", "i", "O", "p"]
    assert selection_sort(array) == sorted(array)


def test_selection_sort_basic_number_sort_visible():
    array = [7, 4, 7, 1, 11]
    assert selection_sort(array) == [1, 4, 7, 7, 11]


def test_selection_sort_characters_sort_visible():
    array = ["c", "b", "a", "f"]
    assert selection_sort(array) == ["a", "b", "c", "f"]


def test_selection_sort_empty_list():
    array = []
    assert selection_sort(array) == []


def test_selection_sort_words():
    array = ["rak", "krowa", "radek", "Radek", "KUCHNIA", "Kuchnia", "zlew"]
    assert selection_sort(array) == sorted(array)


def test_selection_sort_words_polish_letters():
    array = ["Żółw", "Żyrafa", "Radosław", "Dzięcioł"]
    assert selection_sort(array) == sorted(array)


def test_selection_sort_empty_strings():
    array = ["", "", "abc", "", "def", ""]
    assert selection_sort(array) == ["", "", "", "", "abc", "def"]


def test_selection_sort_words_2():
    array = ["Jak", "to", "jest", "być", "skrybą", "dobrze"]
    assert selection_sort(array) == ["Jak", "być", "dobrze",
                                     "jest", "skrybą", "to"]


def test_quick_sort_basic_number_sort():
    array = [6, 4, 3, 1, 9, 11, 23, 764, 12, 132, 16, 2]
    assert quick_sort(array) == sorted(array)


def test_quick_sort_characters_sort():
    array = ["Q", "w", "E", "r", "T", "y", "U", "i", "O", "p"]
    assert quick_sort(array) == sorted(array)


def test_quick_sort_basic_number_sort_visible():
    array = [7, 4, 7, 1, 11]
    assert quick_sort(array) == [1, 4, 7, 7, 11]


def test_quick_sort_characters_sort_visible():
    array = ["c", "b", "a", "f"]
    assert quick_sort(array) == ["a", "b", "c", "f"]


def test_quick_sort_empty_list():
    array = []
    assert quick_sort(array) == []


def test_quick_sort_words():
    array = ["rak", "krowa", "radek", "Radek", "KUCHNIA", "Kuchnia", "zlew"]
    assert quick_sort(array) == sorted(array)


def test_quick_sort_words_polish_letters():
    array = ["Żółw", "Żyrafa", "Radosław", "Dzięcioł"]
    assert quick_sort(array) == sorted(array)


def test_quick_sort_empty_strings():
    array = ["", "", "abc", "", "def", ""]
    assert quick_sort(array) == ["", "", "", "", "abc", "def"]


def test_quick_sort_words_2():
    array = ["Jak", "to", "jest", "być", "skrybą", "dobrze"]
    assert quick_sort(array) == ["Jak", "być", "dobrze",
                                 "jest", "skrybą", "to"]


def test_bubble_sort_numeric():
    arr = [3, 1, 5]
    assert bubble_sort(arr) == [1, 3, 5]
    arr2 = [7, 4, 7, 1, 11]
    assert bubble_sort(arr2) == [1, 4, 7, 7, 11]


def test_bubble_sort_characters_sort_visible():
    array = ["c", "b", "a", "f"]
    assert bubble_sort(array) == ["a", "b", "c", "f"]


def test_bubble_sort_alphabetic():
    word = "tadeusz"
    assert "".join(bubble_sort(list(word))) == "adestuz"


def test_bubble_sort_words():
    array = ["rak", "krowa", "radek", "Radek", "KUCHNIA", "Kuchnia", "zlew"]
    assert bubble_sort(array) == sorted(array)


def test_merge_sort_numeric():
    arr = [3, 1, 5]
    assert merge_sort(arr) == [1, 3, 5]
    arr2 = [7, 4, 7, 1, 11]
    assert merge_sort(arr2) == [1, 4, 7, 7, 11]


def test_merge_sort_characters_sort_visible():
    array = ["c", "b", "a", "f"]
    assert merge_sort(array) == ["a", "b", "c", "f"]


def test_merge_sort_alphabetic():
    word = "Tadeusz"
    assert "".join(merge_sort(list(word.casefold()))) == "adestuz"


def test_merge_sort_words():
    array = ["rak", "krowa", "radek", "Radek", "KUCHNIA", "Kuchnia", "zlew"]
    assert merge_sort(array) == sorted(array)
