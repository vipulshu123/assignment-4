
try:
    x=open('sample.txt','r')
    y=x.read()
    print(y)
except FileNotFoundError:
    print('The file \'sample .txt\' was not found ')




