import sys
def file_word(filename):
    wordcount={}
    with open(filename,'r') as file_obj:
        for line in file_obj:
            low=line.lower()
            lines = low.split()
            for word in lines:
                if word in wordcount:
                    wordcount[word]=wordcount[word]+1
                else:
                    wordcount[word]=1
        file_obj.close()    
        return wordcount

def print_words(filename):
    wordcount=file_word(filename)
    all_words=sorted(wordcount)
    for word in all_words:
        print (word,wordcount[word])

def common_count(words):
    return words[1]

def print_top(filename):
    wordcount=file_word(filename)
    all_words=sorted(wordcount.items(),key=common_count,reverse=True)
    for word in all_words[:20]:
        print (word[0],word[1])

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()