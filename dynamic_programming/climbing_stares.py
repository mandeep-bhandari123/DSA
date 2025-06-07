number_of_stairs=int(input("Enter the number of stairs:- "))
stairs_we_can_walk=[1,2]
max_stairs_req=[float("inf") for _ in range(number_of_stairs+1) ]
max_stairs_req[0]=0
for i in range(number_of_stairs):
    for j in max_stairs_req:
        max_stairs_req[i]=max()
        
        
        
