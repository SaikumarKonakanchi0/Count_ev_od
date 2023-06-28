n=(1,2,3,4,5,6,7,8,9)
ev_count=0
od_count=0
for i in n:
    if i%2==0:
        ev_count+=1
    else:
        od_count+=1
print("Number of even numbers: ",ev_count)
print("Number of odd numbers: ",od_count)
