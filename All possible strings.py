list = ['g', 'a', 'm', 'e']
r =0
list1 = ['g', 'a', 'm', 'e']
list2=[]
list3=[]
list4=[]
for i in list1:
    b=list.index(i)
    list.pop(b)
    for j in list:
        list2.append(i+j)
    list.append(i)
for k in list2:
  c = list.index(k[0])
  list.pop(c)
  d = list.index(k[1])
  list.pop(d)
  for l in list:
    list3.append(k[0]+k[1]+l)
  list.append(k[0])
  list.append(k[1])
for x in list3:
    e = list.index(x[0])
    list.pop(e)
    f = list.index(x[1])
    list.pop(f)
    g = list.index(x[2])
    list.pop(g)
    for y in list:
            list4.append(x[0]+x[1]+x[2]+y)
    list.append(x[0])
    list.append(x[1])
    list.append(x[2])
for z in list4:

    r=r+1
    print(r,z)
