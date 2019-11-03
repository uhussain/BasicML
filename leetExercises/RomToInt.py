import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--RomanNumber", "-r", type=str,default="IX", help="Must be Roman")
args = vars(parser.parse_args())
print("args offered: ",args)
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    value=0
    roman_int={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    for i in range(len(s)):
        if i>0 and roman_int[s[i]] > roman_int[s[i-1]]:
            value+=(roman_int[s[i]] - 2*roman_int[s[i-1]])
        else:
            value+=roman_int[s[i]]
    #i=0
    #tot=len(s)
    #print ("tot:",tot)
    #while i < tot:
    #    print ("idx: ",i)
    #    print ("s[",i,"] :",s[i])
    #    if s[i]=="M":
    #        value+=1000
    #        i+=1
    #        print ("value: ",value)
    #    elif s[i]=="D":
    #        value+=500
    #        i+=1
    #    elif s[i]=="C":
    #        if i!=len(s)-1:
    #            if s[i+1]=="D":
    #                value+=400
    #                i+=2
    #            elif s[i+1]=="M":
    #                value+=900
    #                i+=2
    #            else:
    #                value+=100
    #                i+=1
    #        else:
    #            value+=100
    #            i+=1
    #    elif s[i]=="L":
    #        value+=50
    #        i+=1
    #    elif s[i]=="X":
    #        if i!=len(s)-1:
    #            if s[i+1]=="L":
    #                value+=40
    #                i+=2
    #            elif s[i+1]=="C":
    #                value+=90
    #                i+=2
    #            else:
    #                value+=10
    #                i+=1
    #        else:
    #            value+=10
    #            i+=1
    #    elif s[i]=="V":
    #        value+=5
    #        i+=1
    #    elif s[i]=="I":
    #        if i!=len(s)-1:
    #            if s[i+1]=="V":
    #                value+=4
    #                i+=2
    #            elif s[i+1]=="X":
    #                value+=9
    #                i+=2
    #                print ("value: ",value)
    #                print ("i:",i)
    #            else:
    #                value+=1
    #                i+=1
    #        else:
    #            value+=1
    #            i+=1
    #    else:
    #        print("Not Roman")
    return value
inputVar = args['RomanNumber']
print ("Roman Input: ",inputVar)
print("Integer Equivalent to ",inputVar,": ",romanToInt(inputVar))
