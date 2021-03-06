import sys
from c_ast import *
from c_parser import CParser

"""
for testing print added in 
c_ast.c
	line : 695 and 937

"""

# returns all variable names from the quation binaryOpObj
def getIDsFromBinaryOp(binaryOpObj):
	ret = []
	for i in binaryOpObj:
		if type(i) is ID:
			ret.append(i.getName())
		if type(i) is BinaryOp:
			ret.extend(getIDsFromBinaryOp(i))
	return ret
	
# handles 'a=b*d/c*10'
def handleBinaryOp(leftNode, BinaryOpObj):
	
	ids = getIDsFromBinaryOp(BinaryOpObj)
	
	for i in leftNode:
		print('assign', i, end=" ")
	
		for id in ids:
			print(id, end=" ")
		print()
	pass

# handles 'a=b=c=...'
def handleMultiAssign(leftNodes, assignmentObj):

	leftChild = assignmentObj.children()[0][1]
	rightChild = assignmentObj.children()[1][1]

	if type(rightChild) is Assignment:
		leftNodes.append(leftChild.getName())
		handleMultiAssign(leftNodes, rightChild)

	elif type(rightChild) is Constant:
		for id in leftNodes:
			print('assign',id)
		print('assign',leftChild.getName())

	elif type(rightChild) is ID:
		for id in leftNodes:
			print('assign', id, rightChild.getName())
		print('assign', leftChild.getName(), rightChild.getName())
	
	elif type(rightChild) is BinaryOp:	# a = b*c	
		leftNodes.append(leftChild.getName())
		handleBinaryOp(leftNodes, rightChild)

	pass

# handling (l = r) stmts
def handleAssignmentOp(assignmentObj):

	leftChild = assignmentObj.children()[0][1]
	rightChild = assignmentObj.children()[1][1]

	if type(rightChild) is ID:	# Eg., a = b
		print('assign', leftChild.getName(), rightChild.getName())
	
	elif type(rightChild) is Constant:	# Eg., a = 10
		print('assign', leftChild.getName())
	
	elif type(rightChild) is Assignment:	# a = b = c
		handleMultiAssign([leftChild.getName()], rightChild)
	
	elif type(rightChild) is BinaryOp:	# a = b*c		
		handleBinaryOp([leftChild.getName()], rightChild)


def handleWhileLoops(nodeObj):
	ids = getIDsFromBinaryOp(nodeObj.children()[0])
	print('loop', end=' ')
	for id in ids:
		print(id, end=' ')
	print(len(nodeObj.children()[1][1].children()))

	dfs(nodeObj.children()[1][1])
	pass


def handleScanf(scanfObj):
	print('input', end=' ')
	for expr in scanfObj.children()[1][1].children():
		if type(expr[1]) is UnaryOp:
			print(expr[1].children()[0][1].getName(), end=' ')
	print()

	pass

def handlePrintf(printfObj):

	print("output", end=' ')
	# print(printfObj.children()[1][1].children())
	for expr in printfObj.children()[1][1].children():
		
		if type(expr[1]) is ID:
			print(expr[1].getName())
		
		elif type(expr[1]) is BinaryOp:
			ids = getIDsFromBinaryOp(expr)
			for id in ids:
				print(id,end=' ')			

	print()


# printf, scanf, anyother fn call
def handleFunctionCalls(fnCallObj):
	if fnCallObj.children()[0][1].getName() == 'scanf':
		handleScanf(fnCallObj)

	elif fnCallObj.children()[0][1].getName() == 'printf':
		handlePrintf(fnCallObj)

	pass

def handleIfElse(nodeObj):

	ids = getIDsFromBinaryOp(nodeObj.children()[0])
	print('if', end=' ')
	for id in ids:
		print(id,end=' ')
	print(len(nodeObj.children()[1][1].children()))
	
	# recur on stmts inside 'if' block
	dfs(nodeObj.children()[1][1])
	
	print('else',len(nodeObj.children()[2][1].children()))

	# recur on stmts inside 'else' block
	dfs(nodeObj.children()[2][1])
	
	pass



def dfs(nodeObj):

	if(nodeObj):
		if type(nodeObj) is Assignment:
			handleAssignmentOp(nodeObj)
			pass
		
		elif type(nodeObj) is While or type(nodeObj) is DoWhile:
			handleWhileLoops(nodeObj)

		elif type(nodeObj) is FuncCall:
			handleFunctionCalls(nodeObj)
	
		elif type(nodeObj) is If:
			handleIfElse(nodeObj)
			
		else:
			for child in nodeObj:
				dfs(child)


parser = CParser()
with open("testing_c_file.c", 'rU') as f:
	text = f.read()
syntaxTree=parser.parse(text, "testing_c_file.c")


dfs(syntaxTree)
