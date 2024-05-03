def missing_no(array, n):
    summ=0
    for i in (array):
        summ+=i
    a=n*(n+1)//2-summ
    return a
array=[1,2,3,9,8,7,6,4,10]
n=10
print(missing_no(array,n))

x=10
array=[1,2,3,4,5,7,8,9,10,20]
print(count_smaller_element(array,x))

def count_smaller_element(array,x):
    k=[]
    count=0
    for i in array:
        if i<=x:
            count+=1
            k.append(i) 
    print(k)
    return  count


