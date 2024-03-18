STRING_FILTER = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZęóąśłżźćńĘÓĄŚŁŻŹĆŃ "


def get_words_from_file(number_of_words):
    words_list = []
    with open("pan-tadeusz-unix.txt", "r") as file_handle:
        for line in file_handle:
            filtered_string = filter(lambda x: x in STRING_FILTER, line)
            filtered_string = ("".join(filtered_string)).split()
            filtered_string = [word for word in filtered_string if word.strip()]
            if filtered_string:
                for element in filtered_string:
                    if number_of_words > 0:
                        words_list.append(element)
                        number_of_words -= 1
            if number_of_words <= 0:
                break
    return words_list
