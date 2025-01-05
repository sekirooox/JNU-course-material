from pythonds.basic import Stack

def Deci2Binary(n:int):
    st = Stack()
    while n>0:
        remainer=n%2
        quotient=n//2
        n=n//2
        st.push(remainer)
    output_number=''
    while st.size()>0:
        output_number=output_number+str(st.pop())
    print(f'十进制{n}转换为二进制为{output_number}')
    return output_number
if __name__ == "__main__":
    deci_n=984
    bina_n=Deci2Binary(deci_n)


