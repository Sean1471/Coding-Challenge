inputVariable = 10
partition = []
total_partitions = []
partition_amount = 0

def editPartition(partition): # To remove/ Attempt to use FOR loop
    comparitor = inputVariable/inputVariable
    print
    for i in range(len(partition)):
        if(partition.count(comparitor) > 1):
            partition[i] = comparitor + 1
            partition.pop() # May need to remove pops and instead assess sum of List and remove the difference from the right
            # print(partition)
            # return partition
        else:
            comparitor += 1
            i = 0 # Gets reset to actual I value once line 10 is reached... / Does not reset to 0 as necessary // May have to conver to a WHILE LOOP
            # return partition
        print(partition) ## Remove
    return partition

def editPartition2(partition): # Atempt to use WHILE loop
    comparitor = inputVariable/inputVariable
    i = 0
    while(i < len(partition)):
        if(partition.count(comparitor) > 1):
            partition[i] = comparitor + 1 # +1 here is too definitive and will prevent from cases where +2 etc is necessary. Re-write to be logic based comparitor + 'change(?)' // Potentially check for sum of vals in string = inputVar 
            partition.pop() # May need to remove pops and instead assess sum of List and remove the difference from the right
            # print(partition)
            # return partition
            i += 1
        else:
            comparitor += 1
            i = 0 # Gets reset to actual I value once line 10 is reached...
            # return partition
        print(partition) ## Remove
    return partition

def editPartition3(partition): # Attempt to use first digit in list as pivot..
    comparitor = inputVariable/inputVariable
    i = 0
    while(i < len(partition)):
        if(partition.count(comparitor) > 1):
            if(sum(partition) == inputVariable):
                partition[0] = partition[0] + partition[1]
            # print(partition)
            # return partition
            i += 1
        else:
            comparitor += 1
            i = 0 # Gets reset to actual I value once line 10 is reached...
            # return partition
        print(partition) ## Remove
    return partition

# Used to create initial partition of inputVariable comprised of only val's '1'
for i in range(inputVariable):
    partition.clear()
    for j in range(inputVariable):
        partition.append(1)
    #print(partition)
    total_partitions.append(partition)
partition_amount = 1
print(partition)
# print(total_partitions)
# print(len(total_partitions))

editPartition3(partition)
print(partition_amount)