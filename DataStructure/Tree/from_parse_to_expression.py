from pythonds.trees import BinaryTree
def f(tree):
    if not tree.getLeftChild() and not tree.getRightChild():
        return tree.getRootVal()
    return '('+f(tree.getLeftChild())+tree.getRootVal()+f(tree.getRightChild())+')'
# 构造解析树
def buildExampleTree():
    root = BinaryTree('*')  # 根节点是 '*'
    
    left_subtree = BinaryTree('+')
    left_subtree.insertLeft('3')
    left_subtree.insertRight('5')
    
    right_subtree = BinaryTree('-')
    right_subtree.insertLeft('4')
    right_subtree.insertRight('2')
    
    root.insertLeft(left_subtree)
    root.insertRight(right_subtree)
    
    return root

# 测试
tree = buildExampleTree()
result = f(tree)
print("中缀表达式为：", result)