# m,n = input().split()
# vals=[]
# vals1=[]
# for i in range(int(m)):
#   vals.append(input())
# for i in range(int(n)):
#   vals1.append(input())
# ssps=''
# for k in vals1:
#     temp=''
#     while(k in vals):
#         temp+=str(vals.index(k)+1)+' '
#         vals[vals.index(k)]='unnnnn'
#     if temp=='':
#       temp = '-1'
#     ssps+=temp+'\n'
# print(ssps)


from collections import defaultdict
d = defaultdict(list)
list1 = []

n, m = map(int, input().split())

for i in range(0, n):
    d[input()].append(i+1)

for i in range(0, m):
    list1 = list1+[input()]

for i in list1:
    if i in d:
        print(" ".join(map(str, d[i])))
    else:
        print(-1)
