# parentheses checker.
"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
    Balanced Example: {[]}
    Non-Balanced Example: (()
    Non-Balanced Example: ))
"""
from stack import Stack

def is_match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "{" and p2 == "}":
        return True
    if p1 == "[" and p2 == "]":
        return True
    else:
        return False

def parentheses_checker(paren_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(paren_string) and balanced:
        paren = paren_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False

print(parentheses_checker("(((({}))))"))

print(parentheses_checker("[][]]]"))
print(parentheses_checker("[][]"))
