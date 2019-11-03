#How would you write a function that checks if a string is a palindrome?

#What are some assumptions you had? Did you have any questions?

#Here are some questions which clarify exactly what the function should return.

#Should you consider spaces? For example, is "taco cat" a palindrome?

#Is punctuation ignored or considered part of the string?

#What are the edge cases? Those unconsidered scenarios which break your program. Would an empty string be considered a palindrome?

#Basic inefficient recursive function

class Solution:
    def palindrome_rec(self,string):
        #'a' is a palindrome?
        if len(string) <= 1:
            return True
        if (string[0]!=string[-1]):
            return False
        return self.palindrome_rec(string[1:-1])
    def palindrome_nocase(self,string):
        #get rid of punctuation/space?
        extras=[',', '!', '?', '.',' ']
        #print(string)
        for e in extras:
            string=string.replace(e,'')
        lowstring=string.lower()
        #print(lowstring)
        for i in range(len(string)//2):
            if(lowstring[i]!=lowstring[-i-1]):
                return False
        return True
    def palindrome_python(self,string):
        extras=[',', '!', '?', '.',' ']
        print(string)
        for e in extras:
            string=string.replace(e,'')
        #casefold is an aggresive version of lower()
        lowstring=string.casefold()
        #reversed() method returns an iterator that accesses the given sequence in the reverse order.
        rev_string=reversed(lowstring)
        if list(lowstring)==list(rev_string):
            return True
        return False

def main():
    x=Solution()
    palindrome="taco cat!"
    print(x.palindrome_rec(palindrome))
    print(x.palindrome_nocase(palindrome))
    print(x.palindrome_python(palindrome))
    #print(palindrome_rec(palindrome))

if __name__ == "__main__":
          main()
