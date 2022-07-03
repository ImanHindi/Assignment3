





def winner(num_of_pair_blocks):
    x=num_of_pair_blocks%2
    print(x)
    if x:
        print('ps1')
    else:
        print('ps2')

winner(1223)



list1=['blue','red','red','blue','blue']

list1.sort()
uniquevalues=set(list1)
x1=list.count(list1,'red')
x2=list.count(list1,'blue')

if x1>x2:
    print('red')
else:
    print('blue')




