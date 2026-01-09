x=int(input("Number of rows "))
n=x
ast='*'
while ast<='*'*n:
    print(ast)
    ast=ast+'*'
for i in range(x+1):
    ast='*'*x
    print(ast)
    x=x-1