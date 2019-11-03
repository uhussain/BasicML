# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(int(n/2), -1, -1): 
        heapify(arr, n, i)
        #print("Building a maxheap",i)
        #print (arr)
    # One by one extract elements
    sortedArray=[]
    for i in range(n-1, 0, -1):
        print ("maxelement: ",arr[0])
        arr[i], arr[0] = arr[0], arr[i] # swap the root with last element
        ##the following implementation avoids creating another array.
        #print("Swapping in maxheap",i)
        #print (arr)
        #heapify(arr, i, 0)
        #print("Extracting elements",i)
        #print (arr)
        sortedArray.append(arr[i])
        print ("array before poping: ",arr)
        arr.pop(i)
        if i>1:
            #new root may violate maxHeap but children are max-heap so only need at root
            heapify(arr,i,0)
        else:
            #last element left
            sortedArray.append(arr[0])
        print("Extracting elements",i)
        print (arr)


    return sortedArray
        
# Driver code to test above 
arr = [ 12, 11, 13, 5, 6,7,1,0,-1,34,53,20] 
SortedArr = heapSort(arr)
#print(arr)
n = len(SortedArr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %SortedArr[i]), 
