n=int(input("enter the value of n:"))
if(n==-1):
  print("invalid entry")
else:
 def integral(a, b, n):
   integrate=(b**(n+1))/(n+1) - (a**(n+1))/(n+1)
   print(f"The value of integral of x to the power of {n} = {integrate}")
 a=int(input("enter lower limit:"))
 b=int(input("enter upper limit:"))
 integral(a, b, n)
