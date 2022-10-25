from mystack import ListStack

def in2post(expr):
    prec={'*':2,'/':2,'+':1,'-':1}  # calculate level
    s=ListStack()       # stack is used to store operator and assist the expression in postfix order
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
        else:   # operators
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

print(in2post('V*W*(X+Y)-Z'))
print(in2post('X-(Y+W*(Z/V))'))
print(in2post('A-B*(C+D/E)'))
print(in2post('A/(B*C)-(D+E)'))
