# rotate list
# no time/space requirements
# return "rotated" version of input list

def rotate(my_list, num_rotations):
  rotated_list=my_list[-num_rotations:]+my_list[:-num_rotations]
  return rotated_list

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['f', 'a', 'b', 'c', 'd', 'e'], 
                                                rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['f', 'a', 'b', 'c', 'd', 'e']))

#Given a list and a positive integer, return the same list “rotated” a number of times that match
#the input integer. This time, we’ll rotate the list backward and use O(1) space.

def rotate_backwards(my_list,num_rotations):
    for i in range(num_rotations):
        c=my_list.pop(0)
        my_list.append(c)
    return my_list
#### TESTS SHOULD ALL BE TRUE ####
print ("Executing the rotate_backwards function with O(1) space")

print("{0}\n should equal \n{1}\n {2}\n".format(rotate_backwards(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['b', 'c', 'd', 'e', 'f', 'a'], rotate_backwards(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['b', 'c', 'd', 'e', 'f', 'a']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate_backwards(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['c', 'd', 'e', 'f', 'a', 'b'], rotate_backwards(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['c', 'd', 'e', 'f', 'a', 'b']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate_backwards(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'], rotate_backwards(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b', 'c']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate_backwards(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['e', 'f', 'a', 'b', 'c', 'd'], rotate_backwards(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['e', 'f', 'a', 'b', 'c', 'd']))
