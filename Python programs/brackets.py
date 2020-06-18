# python program to check whether the brackets in given expression is isBalanced
#implemented using stack
def isBalanced(s):
    stack=[]
    def top(stack):
        return stack[len(stack)-1]
    def empty(stack):
        if  len(stack)==0:
            return True
        else:
            return False
    for i in s:
        if(i=='(' or i=='{' or i=='['):
            stack.append(i)
        if(i==')'):
            if(empty(stack) or top(stack)!='('):
                stack.append(i)
            else:
                stack.pop()
        if(i=='}'):
            if(empty(stack) or top(stack)!='{'):
                 stack.append(i)
            else:
                stack.pop()
        if(i==']'):
            if(empty(stack) or top(stack)!='['):
                stack.append(i)
            else:
                stack.pop()
    if(empty(stack)):
        return ("YES")
    else:
        return ("NO")

t=int(input())
for i in range(t):
    s=input()
    result=isBalanced(s)
    print(result)
