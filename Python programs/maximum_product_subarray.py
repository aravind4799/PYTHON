a=[1, -2, -3, 0, 7, -8, -2]
prev_max=[0 for i in range(len(a))]
prev_min=[0 for i in range(len(a))]
curr_max=[0 for i in range(len(a))]
curr_min=[0 for i in range(len(a))]
ref=[0 for i in range(len(a))]

ref[0],prev_max[0],prev_min[0],curr_max[0],curr_min[0]=(a[0],a[0],a[0],a[0],a[0])
#dynamic programming
for i in range(1,len(a)):
    curr_max[i]=max(a[i],prev_max[i-1]*a[i],prev_min[i-1]*a[i])
    curr_min[i]=min(a[i],prev_max[i-1]*a[i],prev_min[i-1]*a[i])
    ref[i]=max(ref[i-1],curr_max[i])
    prev_max[i]=curr_max[i]
    prev_min[i]=curr_min[i]

print(max(ref))
