def get_num_words(text):
    return len(text.split())


def get_num_chars(text):
    result = {}
    for char in text:
        char = char.lower()
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


def sort_on(item):
    return item["nums"]


def get_num_chars_report(num_chars_dict):
    result = [
        {"char": key, "nums": value}
        for key, value in num_chars_dict.items()
        if key.isalpha()
    ]
    result.sort(reverse=True, key=sort_on)

    return result
