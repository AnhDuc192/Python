n = int(input("nhap n: "))
sum = 0
if n%2==1:
    for i in range(1,n,2):
      print(i)
      sum = sum +i
    print(sum)      
else :
    print(" đéo tính")
