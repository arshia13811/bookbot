def main():
    path = "/home/arshiadev/workspace/github.com/arshia13811/bookbot/books/frankenstein.txt"
    text = get_book_content(path)    
    num_words = words_counter(text)
    num_chars = char_counter(text)
    x = char_counter(text)
    for i in x:
        print(i+"\n")
    
    
    
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
        if i.isalpha():
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
                
    sorted_items = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    lis = [f"the character {k} has {v} occurrences" for k, v in sorted_items]
    
    return lis
          

if __name__ == "__main__":
    main()