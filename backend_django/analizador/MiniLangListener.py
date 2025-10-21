# Generated from MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#program.
    def enterProgram(self, ctx:MiniLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLangParser#program.
    def exitProgram(self, ctx:MiniLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLangParser#statement.
    def enterStatement(self, ctx:MiniLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#statement.
    def exitStatement(self, ctx:MiniLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#assign.
    def enterAssign(self, ctx:MiniLangParser.AssignContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assign.
    def exitAssign(self, ctx:MiniLangParser.AssignContext):
        pass


    # Enter a parse tree produced by MiniLangParser#print.
    def enterPrint(self, ctx:MiniLangParser.PrintContext):
        pass

    # Exit a parse tree produced by MiniLangParser#print.
    def exitPrint(self, ctx:MiniLangParser.PrintContext):
        pass


    # Enter a parse tree produced by MiniLangParser#expr.
    def enterExpr(self, ctx:MiniLangParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#expr.
    def exitExpr(self, ctx:MiniLangParser.ExprContext):
        pass



del MiniLangParser