from mystack import ListStack

data={'V':1,'W':3,'X':7,'Y':9,'Z':10,'A':12,'B':4,'C':3,'D':8,'E':2}

def in2post(expr):
    prec={'*':2,'/':2,'+':1,'-':1}
    s=ListStack()
    postFix=''
    for c in expr:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            postFix=postFix+c
        elif c=='(':
            s.push(c)
        elif c==')':
            t=s.pop()
            while t != '(':
                postFix=postFix+t
                t=s.pop()
        else:
            while not s.is_empty():
                if s.top()=='(':
                    break
                elif prec[s.top()] < prec[c]:
                    break
                else:
                    postFix=postFix+s.pop()
            s.push(c)
    while not s.is_empty():
        postFix=postFix+s.pop()
    return postFix

def evaluate(expr):
    postFix=in2post(expr)
    s=ListStack()
    for c in postFix:
        if c in '+-*/':
            up=s.pop()
            down=s.pop()
            if c=='+':
                result=down+up
            elif c=='-':
                result=down-up
            elif c=='*':
                result=down*up
            else:
                result=down/up
            s.push(result)
        else:
            s.push(data[c])
    return result

print(evaluate('V*W*(X+Y)-Z'))
print(evaluate('X-(Y+W*(Z/V))'))
print(evaluate('A-B*(C+D/E)'))
print(evaluate('A/(B*C)-(D+E)'))
    

        
