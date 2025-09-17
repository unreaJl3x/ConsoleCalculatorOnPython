from src.math import *

def validOper(a : str) -> bool :
    return a[0] in ('+', '-', '*', '/') and len(a) == 1

def listAppend(list:list,pos:int,ithem):
    try:
        list.insert(pos, int(ithem))
    except:
        if validOper(ithem):
            list.insert(pos, (ithem))
        else:
            print("Invalid line " + ithem + '. ')

def Clear(a : list):
    a = list(filter(lambda x: x != ' ', a))

def iltl(a:list,b:list) : #insertListToList
    if(not b):return
    for i in b:
        a.insert(0,i)

def isNum(list : list[str]) -> list:
    if (len(list)==0):return None

    nums = []
    spec_list = []
    spec=False
    for i in list:
         print(nums)
         if ( i in ['(']) : spec = True;spec_list.append([])
         elif ( i in [')']) : spec=False;

         if spec: listAppend(spec_list[len(spec_list)-1],len(spec_list[len(spec_list)-1])-1,i)
         else:
             pos = len(nums)
             if (i in ['*','/']): pos=0
             elif (len(nums)>0 and nums[0] in ['*','/']) : pos=0; nums.insert(1,nums.pop())

             listAppend(nums,pos,i)
    print(spec_list)
    for i in range(len(spec_list)): iltl(nums, isNum(spec_list[i]))
    print(nums)
    return nums

def CheckTypes (a : list,c:type) -> bool:
    for i in a:
        if type(i) != c:
            return False
    return True

def conInt(list:list[str])->list:
        nlist=[]
        num = ""
        print(list)
        while(len(list)>0):
            try:
                int(list[0])
                num+=str(list[0])
                print("remoev ", list[0])
                list.remove(list[0])
                print(list)

            except:
                if (len(str(num))==0): num=list[0];list.remove(list[0])
                else: num=int(num)
                nlist.append(num)
                num=''
        try:
            nlist.append(int(num))
        except:
            nlist.append(num)
        print('nliust ',nlist)
        return nlist



def Schet (nums : list) -> int:
    print("Schet ",nums)
    while (not len(nums)<=1):
        if (type(nums[1]) == str and CheckTypes([nums[0],nums[2]], int) ):
            num = 0
            if (nums[1] == '+'): num = Addactive(nums[0], nums[2])
            elif (nums[1] == '-'): num = Subtraction(nums[0], nums[2])
            elif (nums[1] == '*'): num = Multiplication(nums[0], nums[2])
            elif (nums[1] == '/'): num = Division(nums[0], nums[2])
            nums.remove(nums[0])
            nums.remove(nums[0])
            nums.remove(nums[0])
            nums.insert(0,num)

        elif CheckTypes([nums[0],nums[1]],int) :
            w = nums[0]
            nums.remove(nums[0])
            indx = len(nums)-1
            while (indx>=0):
                if type(nums[len(nums)-1]) == str :
                    nums.insert(len(nums), w)
                    print(nums)
                    break
                elif ((nums[indx-1] in ['+','-','*','/']) and (nums[indx] in ['+','-','*','/'] )) :
                    nums.insert(indx, w)
                    print(nums)
                    break
                indx -= 1
    return nums[0]

def main():
    print("MAth")
    userInput = input()
    Clear(userInput)
    userInput = conInt(list(userInput))
    userInput = isNum((userInput))
    print("result: "+ str(Schet(userInput)))

main()
#2+(4\2)-(2*2)+3-1*(2+2)
