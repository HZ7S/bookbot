from stats import get_num_words, get_char_count, chars_to_sorted_list
import sys 
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_books>")
    sys.exit(1)
path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read() 
    
def count_words(text):
    return len(text.split())
    
def main():
    book_text = get_book_text(path)
    num_words = count_words(book_text)  

    char_counts = get_char_count(book_text)

    sorted_chars = chars_to_sorted_list(char_counts)
   

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")

    print("============= END ===============")

main()
