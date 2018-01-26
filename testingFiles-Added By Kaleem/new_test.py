import sys
from c_ast import *
from c_parser import CParser

"""
for testing print added in 
c_ast.c
	line : 695 and 937

"""
def printOutput(assignmentObj):
	print 'assign', assignmentObj.children()[0][1].getName()
	if type(assignmentObj.children()[1][1]) is Assignment:
		printOutput(assignmentObj.children()[1][1])

def dfs(nodeObj, space):
	if(nodeObj):
		if type(nodeObj) is Assignment:
			printOutput(nodeObj)
		else:
			print space*'=', nodeObj.children()	
			for child in nodeObj:
				dfs(child, space+1)


parser = CParser()
with open("testing_c_file.c", 'rU') as f:
	text = f.read()
syntaxTree=parser.parse(text, "testing_c_file.c")


# print sytaxTree.children()

print(syntaxTree)
if type(syntaxTree) is FileAST:
	print "yes"
dfs(syntaxTree, 0)


# print "\nfirst child"
# temp1= sytaxTree.children()[0][1]
# print temp1
# temp2= temp1.children()[0][1]
# print temp2
# temp3= temp2.children()[0][1]
# print temp3
# print temp3.children()

# print "\nsecond child"
# temp0 =sytaxTree.children()[1][1]
# print temp0
# print temp0.children()
# temp1= temp0.children()[0][1]
# print "\nsecond-first child"
# print temp1
# temp2= temp1.children()[0][1]
# print temp2
# temp3= temp2.children()[0][1]
# print temp3
# temp4= temp3.children()[0][1]
# print temp4
# temp5 = temp4.children()
# print temp5

# print "\nsecond-second child"
# temp6 =temp0.children()[1][1]
# print temp6
# temp7 =temp6.children()
# print temp7
