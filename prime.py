def prime1(n):
  flag=0
  for i in range(2,n):
    if n%i==0:
      flag=1
      break
  if flag==1:
    print("notprime number")
  else:
    print("prime")
    