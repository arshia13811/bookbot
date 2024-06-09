def main():
    path = "books/frankenstein.txt"
    text = get_book_content(path)    
    num_words = words_counter(text)
    num_chars = char_counter(text)
    print(f"{num_chars} chars found in the document")
    

def get_book_content(path):
    with open(path) as f:
        return f.read()
        

def words_counter(text):
    words = text.strip()
    print(len(words))
    

def char_counter(text):
    dic = {}
    words = text.lower()

    for i in words:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
        
    
if __name__ == "__main__":
    main()