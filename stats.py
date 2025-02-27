def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    text =text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] +=1
        else: 
            char_counts[char] =1
    return char_counts

def sort_by_count(char_dict):
    return list(char_dict.values())[0]

def chars_to_sorted_list(char_counts):
    chars_list = [{char:count} for char, count in char_counts.items()]
    chars_list.sort(reverse=True, key=sort_by_count)
    return chars_list