def main():
  arr = []
  return_arr = []
  n = int(input("Enter the number of elements in the array: "))

  if(n<=0):
    print("Array cannot be less then or equal to zero")
  else:
    for i in range(0,n):
      value = int(input("Enter number: "))

      arr.append(value)

  while len(arr)!=0:
    if len(arr) == 1:
      return_arr.append(min(arr))
      arr.remove(min(arr))
    else:
      return_arr.append(max(arr))
      arr.remove(max(arr))
      return_arr.append(min(arr))
      arr.remove(min(arr))
  print(return_arr)
if __name__ == main():
  main()
"""Given an array of integers, print the array in alternating min/max order. The first element should be the first maximum, second element should be the first minimum, third element should be second maximum, etc.
For example:
#Given the following array:
arr[] = [10, 2, 11, 3, 7, 4, 1]
#Your function should return:
11, 1, 10, 2, 7, 3, 4
"""