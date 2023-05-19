n,x=map(int,input().split())
a=list(map(int,input().split()))
 
def ryou(ti,a,n):
  p=0
  for i in range(n):
    k=ti//a[i]
    p+=k
  return p
 
l=1
r=10**9
while True:
  mid=(l+r)//2
  if mid==l:
    rr=r
    break
  kk=ryou(mid,a,n)
  #print(l,mid,r,kk)
  if kk>=x:
    r=mid
  else:
    l=mid
print(rr)