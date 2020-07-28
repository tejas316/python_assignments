def match_ends(words):
  count=0
  for i in words:
      if len(i)>1 and (i[0]==i[-1]):
          count+=1
  return (count)
#match_ends(['abd', 'fyx', 'ga', 'dx', 'dbb'])


# B. front_x
def front_x(words):
    l1=[]
    l2=[]
    words.sort()
    for i in words:
        if i[0]=='x':
            l1.append(i)
        else:
            l2.append(i)
    return (l1+l2)
#front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])

# C. sort_last

def func(items):
    return (items[-1])

def sort_last(tuples):
    tuples.sort(key=func)
    return (tuples)

#sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print
    'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']),3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    #print
    print
    'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    #print
    print
    'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
