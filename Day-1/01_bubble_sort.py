def bubbleSort(list):
    n = len(list)
    for i in range(0,len(list)):
      for j in range(0,len(list)):  
         if list[i] < list[j]:
            # swap
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    return list

list = [5,6,3,1,2,4]
print(bubbleSort(list))
