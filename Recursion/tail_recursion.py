# tail recursion, which occurs when a function includes a
# single recursive call as the last statement of the function. In this case, a stack is
# not needed to store values to be used upon the return of the recursive call and thus
# a solution can be implemented using an iterative loop instead.
def printInorder( node ):
    if node is not None :
        print( node.data )
        printInorder( node.next )
