__author__ = 'knp069'

import math

numToWord = {'1': 'One ','2': 'Two ','3': 'Three ','4': 'Four ','5': 'Five ',
             '6': 'Six ','7': 'Seven ','8': 'Eight ','9': 'Nine ','10': 'Ten ',
             '11': 'Eleven ','12': 'Twelve ','13': 'Thirteen ','14': 'Fourteen ',
             '15': 'Fifteen ','16': 'Sixteen ','17': 'Seventeen ','18': 'Eighteen ','19': 'Nineteen ',
             '20': 'Twenty ','30': 'Thirty ','40': 'Forty ','50': 'Fifty ','60': 'Sixty ',
             '70': 'Seventy ','80': 'Eighty ','90': 'Ninety ',}

def stringSplit(s,l):
    return [s[::-1][i:i+l][::-1] for i in range(0,len(s),l)]

def stringsplitwrapper(s,l):
    strs = stringSplit(s,l)
    strs.reverse()
    rets = []
    for s in strs:
        k = [s[::-1][i:i+2][::-1] for i in range(0,len(s),2)]
        k.reverse()
        for i in k:
            rets.append(i)
    return rets


testcases = int(input())

i=0

def nTow(x):
    if numToWord.__contains__(str(int(x))):
        return numToWord[str(int(x))]
    elif int(x)!=0:
        tx = str(int(x)%10)
        ty = str(int(int(x)/10)*10)
        return numToWord[ty]+numToWord[tx]
    return ''


while i<testcases:
    word=[]
    n = str(input())
    split3 = stringsplitwrapper(n,3)
    highCurrency = len(split3)
    tval='undef'
    for x in split3:
        print(nTow(x),end='')
        if highCurrency%2==1 and (tval=='undef' or tval=='set'):
            if(int(highCurrency))==9:
                print('Trillion',end=' ')
            elif(int(highCurrency))==7:
                print('Billion',end=' ')
            elif(int(highCurrency))==5:
                print('Million',end=' ')
            elif(int(highCurrency))==3:
                print('Thousand',end=' ')
        if highCurrency%2==0 and int(x)!=0:
            print('Hundred',end=' ')
            tval='set'
        else:
            tval='unset'
        highCurrency=highCurrency-1
    print('')
    i=i+1