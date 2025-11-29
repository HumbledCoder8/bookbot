def sort_num(dict_chars):
    return dict_chars["num"]


def get_word_count(text_from_book):

    split_book = text_from_book.split()
    return len(split_book)

def count_book_characters(book_text):
    #first convert to lower for simplification
    book_text = (book_text.lower())

    word_dict = {}

    for i in book_text:
        
        if i not in word_dict:
            word_dict[i] = 1
        
        else:
            word_dict[i]+=1

    return word_dict
    

def sort_dictionaries(dict_chars):

    dict_list = []

    for i in dict_chars:
        dict_list.append({"char": i,"num": dict_chars[i]})

    #print(dict_list)

    dict_list.sort(reverse=True,key=sort_num)

    return dict_list 

    




def num_key_helper():
    pass



