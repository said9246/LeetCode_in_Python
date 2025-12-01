
# ---------------------------Reverse Arry---------------------------------------01
# a=[1,2,4,5,7]
# a.reverse()
# print(a)

# -----------custome code


# arry=[2,3,4,5,6,7,8]
# rev=[]

# length=len(arry)-1
# print(length)

# for i in range(length,-1,-1):
#     rev.append(arry[i])

# print(rev)

# ---------------------------Find minimum in a Arry---------------------------------------02 
arry =[4,5,6,11,8,12,28,7]
# print("minumum number is ",min(arry))

minimum =arry[0]

for x in arry:
    if x > minimum:
        minimum=x

print("minimum =", minimum)