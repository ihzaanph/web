l=list(map(int,input('enter a list of number : ').split()))
p=int(input('enter no : '))
k=[]
for i in l:
    if p%i!=0 and i%p!=0:
        k.append(i)

print(k)
