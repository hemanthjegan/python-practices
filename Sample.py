def SumOfN(k):
  s = 0
  for i in range(1, k+1):
    s += i
  return s

print("Enter the Value of n: ", end="")
try:
  n = int(input())
  if n<0:
    print("\nInvalid Input!")
  else:
    sum = SumOfN(n)
    print("\nSum =", sum)
except ValueError:
  print("\nInvalid Input!")