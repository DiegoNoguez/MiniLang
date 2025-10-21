grammar MiniLang;

program : (statement (NEWLINE)*)* EOF;

statement : assign | print;

assign: ID '=' expr;

print: 'print' '('expr')';

expr: expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | INT | ID
    | '(' expr ')';

ID: [A-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
NEWLINE: [\r\n]+;
WS: [ \t]+ -> skip;

