
def printParenthesis(str, n):
	if(n > 0):
		_printParenthesis(str, 0,n, 0, 0)
	return

def _printParenthesis(str, pos, n,open, close):

	if(close == n):
		print(end='')
		for i in str:
			print(i, end="")
		print(end=',')
		return

	else:
		if(open > close):
			str[pos] = ')'
			_printParenthesis(str, pos + 1, n,open, close + 1)
		if(open < n):
			str[pos] = '('
			_printParenthesis(str, pos + 1, n,open + 1, close)




n=int(input("Enter the n value: "))
print('[',end='')
if n>0:
    str = [""] * 2 * n
    printParenthesis(str, n)
else:
    print("Value can't be negative...!,",end='')

print(']')

