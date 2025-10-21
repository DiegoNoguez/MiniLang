from .MiniLangVisitor import MiniLangVisitor

class EvalRedvar(MiniLangVisitor):
    def __init__(self):
        self.memory = {}
        self.output = []

    def visitProgram(self, ctx):
        result = None
        for statement in ctx.statement():
            result = self.visit(statement)
        return result

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        self.output.append(str(value))
        return value

    # EXPRESIONES
    def visitExpr(self, ctx):
        # Caso INT
        if ctx.INT():
            return int(ctx.INT().getText())
        # Caso ID
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.memory:
                raise NameError(f"Variable '{var_name}' no definida")
            return self.memory[var_name]
        # Caso parentésis
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expr(0))
        # Caso operación binaria
        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expr(1))
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
        else:
            raise ValueError("Expresión no reconocida")
