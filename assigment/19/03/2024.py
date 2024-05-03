def missing_no(array, n):
    summ=0
    for i in (array):
        summ+=i
    a=n*(n+1)//2-summ
    return a
array=[1,2,3,9,8,7,6,4,10]
n=10
print(missing_no(array,n))


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

# Function to sort a binary list in linear time
def sort(A):
 
    # count number of 0's
    zeros = A.count(0)
 
    # put 0's at the beginning
    k = 0
    while zeros:
        A[k] = 0
        zeros = zeros - 1
        k = k + 1
 
    # fill all remaining elements by 1
    for k in range(k, len(A)):
        A[k] = 1
 
 
if __name__ == '__main__':
 
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
 
    sort(A)
 
    # print the rearranged list
    print(A)
 

