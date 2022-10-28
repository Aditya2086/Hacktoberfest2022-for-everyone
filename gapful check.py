#Gapful number check in python

a = input('Enter a number:')
b = a[0] + a[-1]
c = int(a)
d = int(b)
if c % d == 0:
  print('The no.is gapful')
else:
  print('The no.is not gapful')
