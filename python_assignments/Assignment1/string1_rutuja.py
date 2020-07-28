# A. Donuts
import sys
def donuts(count):
  if count < 10:
    return ( 'Number of donuts: '+str(count))
  else:
    return ('Number of donuts: many')

# B. both_ends

def both_ends(s):
  if len(s)<= 2:
    return('')
  else:
    return (s[0:2]+s[-2:])

# C. fix_start

def fix_start(s):
  first_char=s[0]
  replaced_string=s[1:].replace(first_char,'*')
  return (first_char+replaced_string)

# D. MixUp

def mix_up(a, b):
  first=a[0:2]
  second=b[0:2]
  return (a.replace(a[0:2],second)+' '+ b.replace(b[0:2],first))

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
  print
  'donuts'
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  #print
  print
  'both_ends'
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  # #print
  print
  'fix_start'
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  # # print
  print
  'mix_up'
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main() 