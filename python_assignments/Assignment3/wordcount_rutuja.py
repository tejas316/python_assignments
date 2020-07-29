import sys

# WORD COUNT

wordCount={}
def word_count_dict(filename):
    file=open(filename,'r')
    for str in file:
        str = str.lower()
        words_list=str.split()
        for words in words_list:
            if words in wordCount:
                wordCount[words]=wordCount[words]+1
            else:
                wordCount[words]=1
    for key in sorted(wordCount.keys()):
        print (key,":",wordCount[key])
    return (wordCount)
    file.close()

#word_count_dict('alice.txt')

##TOP COUNT
def  print_top(filename):
    words_count=word_count_dict(filename)
    sorted_orders=sorted(words_count.items(),key=lambda x:x[1],reverse=True)
    for i in sorted_orders:
        print (i[0],":",i[1])
#print_top('alice.txt')

def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    word_count_dict(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
   main()
