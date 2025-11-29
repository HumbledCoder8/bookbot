import sys

from stats import get_word_count, count_book_characters,sort_dictionaries

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def report_creation(book_path,num_words,sorted_list):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")  
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        char = i["char"] 
        num = i["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    
    print("============= END ===============")
    



def main():

    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_as_string = get_book_text(book_path)

    #print(book_as_string)

    num_words = get_word_count(book_as_string)
    

    word_dict = count_book_characters(book_as_string)
    #print(word_dict)

    sorted_list = sort_dictionaries(word_dict)

    report_creation(book_path,num_words,sorted_list)

if __name__ == "__main__":
    main()