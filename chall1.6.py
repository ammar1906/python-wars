def chch(arr):
        
        dir1 = " ".join(arr)
   
        dir2 = dir1.replace("EAST WEST", "").replace("WEST EAST", "").replace("NORTH SOUTH", "").replace("SOUTH NORTH", "")
        dir3 = dir2.split()
        return chch(dir3) if len(dir3) < len(arr) else dir3


arr = ['EAST','NORTH','WEST','SOUTH',"NORTH"]
print(arr)
print(" ".join(arr))
print(chch(arr))