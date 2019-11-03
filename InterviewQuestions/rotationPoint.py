#Clarifying Questions:

#Are there constraints on time or space efficiency?
#No! Any solution will do.
#Does the rotation direction matter?
#This won’t affect the return value.
#What if the input isn’t rotated?
#Return 0.
#def rotation_point(rotated_list):
#  sorted_list=list(sorted(rotated_list))
#  #if no rotations happened, just return 0
#  if (sorted_list==rotated_list):
#    return 0
#  for i in range(len(rotated_list)):
#    if (rotated_list[i]==sorted_list[0]):
#      return i
#
#
#
##### TESTS SHOULD ALL BE TRUE ####
#print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))
#
#print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))
#
#print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 8, 9, 10, 11]), 1, rotation_point([13, 8, 9, 10, 11]) == 1))

#Write a function count_rotations() which has one parameter rotated_list.

#count_rotations() should return the index where the sorted list would begin.

#Your solution should make use of binary search for a O(logN) time complexity!
# find rotation point 
# O(logN) time requirement
# return index of "rotation point" element

def rotation_point(rotated_list):
  sorted_list=list(sorted(rotated_list))
  #if no rotations happened, just return 0
  if (sorted_list==rotated_list):
    return 0
  low=0 #beginning of list
  high=len(rotated_list)-1 #last index
  while low<=high:
    print("low: ",low)
    print("high: ",high)
    mid=int((low+high)/2)
    print ("mid: ",mid)
    mid_next = (mid+1) % len(rotated_list)
    print("mid_next: ",mid_next)
    mid_previous = (mid-1) % len(rotated_list)
    print("mid_previous: ",mid_previous)
    if ((rotated_list[mid]<rotated_list[mid_previous]) and (rotated_list[mid]<rotated_list[mid_next])):
        print ("cant be here")
        return mid
    if (rotated_list[mid] < rotated_list[high]):
        high=mid-1
    else:
        low=mid+1
        print("printing new low")
        print(low)
      


#### TESTS SHOULD ALL BE TRUE ####
#print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

#print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 8, 9, 10, 11]), 1, rotation_point([13, 8, 9, 10, 11]) == 1))
