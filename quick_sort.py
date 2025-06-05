import random

#setting a list to sort
arr=[10,9,8,7,6,5,4,3,2,1]


def quick_sort(arr):
    #Base case
    if len(arr)<=1:
        return arr
    #creating a random pivot
    pivot= random.choice(arr)
    #Removing the pivot from list
    
    arr.remove(pivot)
    
    # left_arr will have the elements that ase smaller then pivot
    left_arr =[]
    #right_arr will have the elements that are bigger then pivot
    right_arr=[]
    
    #loop to find element that are lower then or greater then pivot 
    for i in arr:
        
        if i < pivot:
            left_arr.append(i)
        else :
            right_arr.append(i)
    
     
    return quick_sort(left_arr)+ [pivot] + quick_sort(right_arr)
 
#printing the sorted list   
print(quick_sort(arr))