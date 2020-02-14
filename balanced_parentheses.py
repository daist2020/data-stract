class Stack(object):
    def __init__(self,limit=10):
        self.stack=[]
        self.limit=limit

    def push(self,data):
        if len(self.stack)>=self.limit:
            raise IndexError('chao chu rongliang')
        else:
            self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from kongzhan')

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def if_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)

def balanced_parenthese(parenteses):
    stack =Stack(len(parenteses))
    for parentesis in parenteses:
        if parentesis =='(':
            stack.push(parentesis)
        elif parentesis == ')':
            if stack.if_empty():
                return False
            stack.pop()
    return stack.if_empty()



if __name__=='__main__':
    examples=['((()))','((())',"(()))"]
    print('balanced parentsese demonstriaon:\n')
    for example in examples:
        print(example + ':' +str(balanced_parenthese(example)))
