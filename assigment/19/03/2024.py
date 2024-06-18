


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
 
# Function to find the largest sublist having an equal number of 0's and 1's
def findLargestSublist(nums):
 
    # create an empty dictionary to store the ending index of the first
    # sublist having some sum
    d = {}
 
    # insert (0, -1) pair into the set to handle the case when a
    # sublist with zero-sum starts from index 0
    d[0] = -1
 
    # `length` stores the maximum length of sublist with zero-sum
    length = 0
 
    # stores ending index of the largest sublist having zero-sum
    ending_index = -1
 
    total = 0
 
    # Traverse through the given list
    for i in range(len(nums)):
 
        # sum of elements so far (replace 0 with -1)
        total += -1 if (nums[i] == 0) else 1
 
        # if the sum is seen before
        if total in d:
 
            # update length and ending index of largest sublist having zero-sum
            if length < i - d.get(total):
                length = i - d.get(total)
                ending_index = i
 
        # if the sum is seen for the first time, insert the sum with its
        # index into the dictionary
        else:
            d[total] = i
 
    # print the sublist if present
    if ending_index != -1:
        print((ending_index - length + 1, ending_index))
    else:
        print('No sublist exists')
 
 
if __name__ == '__main__':
 
    nums = [0, 0, 1, 0, 1, 0, 0]
    findLargestSublist(nums)
    
def missing_no(array, n):
    summ=0
    for i in (array):
        summ+=i
    a=n*(n+1)//2-summ
    return a
array=[1,2,3,9,8,7,6,4,10]
n=10
print(missing_no(array,n))