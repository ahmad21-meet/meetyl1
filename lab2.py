list1 = [2,3,4,5,6,7,8,9,22,76]
list2 = [22,3,76,6,8]
def creat_fun(l1,l2):
	x=[]
	for num in l1:
		if  num in l2:
			x.append(num)
	return (x)
x = creat_fun(list1,list2)





print(x)
b=0
sum=0
k=len(x)
for b in range(k):
	sum=sum+x[b]
	b=+1
	print(sum)
	