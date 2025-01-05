from pythonds.basic import Stack
from pythonds.trees import BinaryTree

def buildParseTree(string:str):
    string=string.split()
    s=Stack()
    eTree=BinaryTree('')
    s.push(eTree)
    for item in string:
        p=s.peek()
        if item=='(':
            p.insertLeft('')
            left=p.getLeftChild()
            s.push(left)
        elif item not in ['+', '-', '*', '/']:
            p.setRootVal(item)
            s.pop()
        elif item in ['+', '-', '*', '/']:
            p.setRootVal(item)
            p.insertRight('')        
            right=p.getRightChild()
            s.push(right)
        else:
            s.pop()

    return eTree

def inorderTraversal(tree):
    if tree:
        inorderTraversal(tree.getLeftChild())
        print(tree.getRootVal(), end=' ')
        inorderTraversal(tree.getRightChild())

expr = "( ( 3 + 5 ) * ( 4 - 2 ) )"
parse_tree = buildParseTree(expr)

# 打印解析树的中序遍历（应输出 3 + 5 * 4 - 2）
inorderTraversal(parse_tree)

