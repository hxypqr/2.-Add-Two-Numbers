l1=[2,3,4,5,7,3,5,5,2]
l2=[3,2,7,9,5,4,2]
l3=[0]
k=0
for i in range(0,len(l2)):
    if k==0:
       if l1[i]+l2[i]<10:
        l3.append(l1[i]+l2[i])
        k=0
       else:
        l3.append((l1[i]+l2[i])%10)
        k=1
    else:
       if l1[i] + l2[i]+1 < 10:
          l3.append(l1[i] + l2[i]+1)
          k=0
       else:
          l3.append((l1[i] + l2[i]+1) % 10)
          k = 1
    print k
for j in range(len(l2),len(l1)):
    l3.append(l1[j])
print l3
