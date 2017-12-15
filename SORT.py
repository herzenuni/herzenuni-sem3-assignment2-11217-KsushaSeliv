def pusirek(a):
  list=[]
  for i in a:
      i=str(i)
      summa=0
      for k in i:
          summa=summa+int(k)**2
      if 0==summa%17:
          list.append(i)
  return list

def main():
    print('=', pusirek(range(10,1000)))

if __name__ == '__main__':
    main()
