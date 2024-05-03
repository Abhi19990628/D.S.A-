


def count_smaller_element(array,x):
    k=[]
    count=0
    for i in array:
        if i<=x:
            count+=1
            k.append(i) 
    print(k)
    return  count

x=10
array=[1,2,3,4,5,7,8,9,10,20]
print(count_smaller_element(array,x))

