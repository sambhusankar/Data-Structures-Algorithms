def DistinctNumber(arr):
  output=[]
  for element in arr:
    if element not in output:
      output.append(element)
  print(output)
DistinctNumber([2,1,2,1,2,5,4,6,5,5])