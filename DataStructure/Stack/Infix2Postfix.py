import string

from pythonds.basic import Stack
def infix2Postfix(infix_expression:str):
    dict={}
    dict[')']=4
    dict['*']=3
    dict['/']=3
    dict['+']=2
    dict['-']=2
    dict['(']=1
    def compare_prior(opa:str,opb:str):# 返回优先级的比较
        return dict[opa]>dict[opb]

    opstack=Stack()
    res=[]
    token_list=infix_expression.split()
    for token in token_list:
        """
        三种情况：
        1.正常的数字或者字母
        2.优先级低：出栈
        3.优先级高：入栈
        """
        if token in string.ascii_uppercase:
            res.append(token)
        elif token in string.digits:
            res.append(token)
        else:
            # if opstack.isEmpty() or compare_prior(token,opstack.peek()):
            #     # 栈为空且优先级高:加入

            while not opstack.isEmpty() and compare_prior(token,opstack.peek()):# 如果栈顶元素优先级更大
                 # 栈不为空且优先级低:
                 pop_item=opstack.pop()
                 if pop_item not in ['(',')']:# (*)-
                    res.append(pop_item)
            opstack.push(token)
        # print(res)
        # print(opstack.peek())
    return res

if __name__ == "__main__":
    infix_expression="( A + B ) * ( C + D )"
    print(infix2Postfix(infix_expression))