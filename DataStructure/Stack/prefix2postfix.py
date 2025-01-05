from pythonds.basic import Stack
import string
def infix2postfix(infix:str):
    infix_list=infix.split()
    # print(infix_list)

    postfix_list=[]
    prec={}
    prec['(']=3
    prec['*']=2
    prec['/']=2
    prec['+']=1
    prec['-']=1

    s=Stack()
    for item in infix_list:
        # print(s.items)
        if item=='(':
            s.push(item)
        elif item==')':
            postfix_list.append(s.pop())
            s.pop()
        elif item in string.ascii_uppercase:
            postfix_list.append(item)
        else:
            if not s.isEmpty() and prec[s.peek()]>=prec[item]:
                if s.peek()!='(':
                    postfix_list.append(s.pop())
                s.push(item)
    while not s.isEmpty():
        postfix_list.append(s.pop())

    return ''.join(postfix_list)
if __name__=='__main__':
    infix='( ( A + B ) * ( C + D ) )'
    print(infix2postfix(infix))
