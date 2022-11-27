'''Write a program that takes as input a sorted array of numbers.
 The objective is to return the array arranged in an alternate order such that
 max value is followed by min value in a descending fashion, so that the 1st element
 is the max value, 2nd element is the min value, 3rd element is the second max value,
 4th element is the second min value & so on.
 Example: For an input array [2, 4, 6, 8, 10],
 the expected result would be [10, 2, 8, 4, 6]
 Note: The solution should modify the original array itself.
 '''

arr= list(map(int,input().split()))
l=len(arr)
c=0
x=0
if l%2==1:
    x=1
for i in range (0, l//2+x):
    arr.append(arr[l-(1+i+c)])
    arr.pop(l-(1+i+c))
    c=c+1
    if (c<l//2 or c==l//2):
        arr.append(arr[0])
        arr.pop(0)
print(arr)
