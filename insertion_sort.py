n= int(input("Enter the length of array := "))
arr=[]
for i in range(n):
    element= int(input("Enter the element of array:= "))
    arr.append(element)
print(arr)
def insertion_sort(arr):
    for i in range(1 , len(arr)):
        j= i -1 
        key = arr[i]
        
        while j >= 0 and arr[j]>key:
            arr[j+1]=arr[j]
            j = j - 1
            
            
        arr[j+1]= key
        
    return arr
    

print(insertion_sort(arr))