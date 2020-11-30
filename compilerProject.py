import re
from lark import Lark
import sys, getopt
from sys import argv

# Ids: dict = {"T_ID": "T_ID", "T_HEX": "T_INTLITERAL", "T_INT": "T_INTLITERAL", "T_STRINGLITERAL": "T_STRINGLITERAL",
#              "T_TRUE_BOOLEAN": "T_BOOLEANLITERAL", "T_CHARLITERAL": "T_CHARLITERAL",
#              "T_FALSE_BOOLEAN": "T_BOOLEANLITERAL", "T_DOUBLELITERAL": "T_DOUBLELITERAL"}


def myparser(grammar, inputfile):

    try:
        parser = Lark(grammar, parser="lalr", start='start')
        data = parser.parse(inputfile)
        output = "OK"
    except:
        output = "Syntax Error"

    print(output)
    file = open("outputs/output.txt", "w+")
    file.write(output)
    file.close()

def main(argv):
    f = open("python/tests/t10.in", "r")
    f2 = open("grammar2.lark", "r")
    inputfile = f.read()
    grammar = f2.read()
    myparser(grammar=grammar, inputfile=inputfile)
    f.close()
    f2.close()

if __name__ == "__main__":
    main(sys.argv[1:])
