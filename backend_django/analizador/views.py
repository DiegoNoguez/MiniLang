from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from antlr4 import InputStream, CommonTokenStream
from .MiniLangLexer import MiniLangLexer
from .MiniLangParser import MiniLangParser
from .EvalRedvar import EvalRedvar
import json, traceback

@csrf_exempt  # Permitir POST desde tu front
def run_code(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body)
        code = data.get("code", "").rstrip() + "\n"

        # Lexer y parser
        input_stream = InputStream(code)
        lexer = MiniLangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = MiniLangParser(token_stream)
        tree = parser.program()

        # Evaluador
        visitor = EvalRedvar()
        resultado = visitor.visit(tree)

        response = {
            "entrada": code,
            "arbol": tree.toStringTree(recog=parser),
            "resultado": resultado,
            #"memoria": visitor.memory,
            "prints": visitor.output
        }

        if response["resultado"] is None:
            response["resultado"] = visitor.memory

        return JsonResponse(response, safe=False)

    except Exception as e:
        tb = traceback.format_exc()
        return JsonResponse({"error": str(e), "traceback": tb}, status=400)
