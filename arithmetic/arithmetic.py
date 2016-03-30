from arithmeticLexer import arithmeticLexer
from arithmeticListener import arithmeticListener
from arithmeticParser import arithmeticParser
import antlr4
import sys

def handleExpression(expr):
    adding = True
    value = 0
    for child in expr.getChildren():
        if isinstance(child, antlr4.tree.Tree.TerminalNode):
            adding = child.getText() == "+"
        else:
            multValue = handleMultiply(child)
            if adding:
                value += multValue
            else:
                value -= multValue

    print "Parsed expression %s has value %s" % (expr.getText(), value)

def handleMultiply(expr):
    multiplying = True
    value = 1
    for child in expr.getChildren():
        if isinstance(child, antlr4.tree.Tree.TerminalNode):
            multiplying = child.getText() == "*"
        else:
            if multiplying:
                value *= int(child.getText())
            else:
                value /= int(child.getText())

    return value

def main():
    lexer = arithmeticLexer(antlr4.StdinStream())
    stream = antlr4.CommonTokenStream(lexer)
    parser = arithmeticParser(stream)
    tree = parser.expression()
    handleExpression(tree)
if __name__ == '__main__':
    main()

