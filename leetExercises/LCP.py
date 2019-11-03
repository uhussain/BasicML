import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--InputArray", "-ls", nargs='*',default=["aa","ac"], help="Must be Roman")
args = vars(parser.parse_args())
print("args offered: ",args)
def LCP(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    result=""
    i=0
    j=0
    while i <= (l1-1) and j <= (l2-1):
        if (str1[i]!=str2[j]):
            break
        result+=str1[i]
        i+=1
        j+=1
    return result
def longestCommonPrefix(strs):
    #Build the commonPrefix of two strings at a time
    #Associative property
    prefix=""
    n=len(strs)
    if n>0:
        prefix=strs[0]
        for i in range(1,n):
            prefix = LCP(prefix,strs[i])
    return prefix
#Can also do a binary search
#find the string with minimum length in array
#minStr=min(strs,key=len)
#low=0, high=len(minStr)
#while(low<=high):
    #mid = low + (high - low) / 2
    #write an allContainsPrefix function
    #if allContainsPrefix(strs,strs[0],len(strs),low,mid):
        #prefix+=strs[0][low:mid]
        #And then go for the right half of the min string
        #low=mid+1
    #else:
        #Divide the left half by 2 again
        #high = mid-1
#return prefix
#def allContainsPrefix(arr,firstStr,n,start,end):
    #for i in range(n):
        #for j in range(start,end+1):
            #if arr[i][j]!=firstStr[j]
                #return false
    #return true
inputVar = args['InputArray']
print ("Array Input: ",inputVar)
print("Longest Common Prefix in ",inputVar,": ",longestCommonPrefix(inputVar))
