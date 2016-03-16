from antlr4 import *
from HelloLexer import HelloLexer
from HelloListener import HelloListener
from HelloParser import HelloParser
import sys

class HelloPrintListener(HelloListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    lexer = HelloLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.prog()
    printer = HelloPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()

