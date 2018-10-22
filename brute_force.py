def union(a,b):
    c=[]
    for i in a:
        c.append(i)
    for i in b:
        if (i not in c):
            c.append(i)
    c.sort()
    return c

    
def support(itemset):
    total_tran=992
    cs=open('filename.txt', "r")
    count_num=0
    for line in iter(cs):
        rline=line.split()
        tem=[]
        for i in rline:
            tem.append(int(i))
        t=1
        for i in itemset:
            if (i not in tem):
                t=0
        count_num+=t
    cs.close()
    return (count_num/total_tran)

def confidence(itemset_a,itemset_b):
    count_a = support(itemset_a)
    count_ab = support(union(itemset_a,itemset_b) )
    if (count_a==0):
        return (-1)
    return(count_ab/count_a)



#def L(i):
    #for k in range()


    
####### _main_   ########
    
        
count_item=[]
for i in range(1000):
    count_item.append(0)
fp = open('filename.txt', "r")
for line in iter(fp):
    a=line.split()
    for i in a:
        tem=int(i)
        count_item[tem-1]+=1
fp.close()
    
#print('count_item',count_item)
    
frequent_1item=[]
min_support=300
for item in range(len(count_item)):
    tem=item
    if (count_item[tem]>min_support):
        frequent_1item.append(tem+1)
print("frequent_1item",frequent_1item)

    

for i in frequent_1item:
    tem=i-1
    print ("itemset{%.f}: support= %.3f " % (i,support([i])))
for i in frequent_1item:
    for j in frequent_1item:
        if (i!=j):
            print ("itemsetA{%s} itemsetB{%s}: support= %.3f  confidence= %.3f" % (i,j,support(union([i],[j])), confidence ([i],union([i],[j]))    ))




