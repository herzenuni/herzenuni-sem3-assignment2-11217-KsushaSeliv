#NOD

A=float(input('Первое число:'))
B=float(input('Второе число:'))

def function(A,B):
    while A!=B:
      if A>B:
        A=A-B
      else:
        B=B-A
    return A
print('НOD: {}'.format(function(A, B)))
