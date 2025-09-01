import ply.yacc as yacc
from ExpressionLanguageLex import *
from SintaxeAbstrata import *

# Precedência de operadores
precedence = (
    ('left', 'SOMA', 'SUB'),
    ('left', 'MUL', 'DIV', 'MOD'),
    ('right', 'EXP'),
)

# --- PROGRAM ---
def p_program(p):
    '''program : stm_list'''
    p[0] = p[1]

def p_stm_list_single(p):
    'stm_list : stm'
    p[0] = SingleProgram(p[1])

def p_stm_list_multiple(p):
    'stm_list : stm_list stm'
    p[0] = CompoundProgram(p[1], p[2])

# --- STATEMENTS ---
def p_stm_var(p):
    '''stm : VAR ID end
           | VAR ID DOISPONTOS ID end
           | VAR ID ATRIB exp end
           | VAR ID DOISPONTOS ID ATRIB exp end'''
    if len(p) == 4:  # VAR ID end
        p[0] = VarStm(p[2])
    elif len(p) == 6 and p[3] == ':':  # VAR ID : tipo end
        p[0] = VarStm(p[2], p[4])
    elif len(p) == 6 and p[3] == '=':  # VAR ID = exp end
        p[0] = VarStm(p[2], None, p[4])
    elif len(p) == 8:  # VAR ID : tipo = exp end
        p[0] = VarStm(p[2], p[4], p[6])

def p_stm_proc(p):
    'stm : PROC ID LPAREN sigParams RPAREN DOISPONTOS NEWLINE INDENT stms DEDENT'
    p[0] = ProcStm(p[2], p[4], p[9])

def p_stm_if(p):
    '''stm : IF exp DOISPONTOS NEWLINE INDENT stms DEDENT
           | IF exp DOISPONTOS NEWLINE INDENT stms DEDENT elif_list
           | IF exp DOISPONTOS NEWLINE INDENT stms DEDENT else_stm
           | IF exp DOISPONTOS NEWLINE INDENT stms DEDENT elif_list else_stm'''
    # if simples
    if len(p) == 7:
        p[0] = IfStm(p[2], p[5])
    # if + elif(s)
    elif len(p) == 8 and isinstance(p[7], list):
        p[0] = IfStm(p[2], p[5], p[7])
    # if + else
    elif len(p) == 8:
        p[0] = IfStm(p[2], p[5], None, p[7])
    # if + elif(s) + else
    elif len(p) == 9:
        p[0] = IfStm(p[2], p[5], p[7], p[8])

def p_elif_list(p):
    '''elif_list : ELIF exp DOISPONTOS NEWLINE INDENT stms DEDENT
                 | ELIF exp DOISPONTOS NEWLINE INDENT stms DEDENT elif_list'''
    if len(p) == 7:
        p[0] = [(p[2], p[5])]
    else:
        p[0] = [(p[2], p[5])] + p[7]

def p_else_stm(p):
    'else_stm : ELSE DOISPONTOS NEWLINE INDENT stms DEDENT'
    p[0] = p[5]

def p_stm_while(p):
    'stm : WHILE exp DOISPONTOS NEWLINE INDENT stms DEDENT'
    p[0] = WhileStm(p[2], p[6])

def p_stm_for(p):
    'stm : FOR ID ATRIB exp DOISPONTOS NEWLINE INDENT stms DEDENT'
    p[0] = ForStm(p[2], p[4], p[8])

def p_stm_return(p):
    'stm : RETURN exp end'
    p[0] = ReturnStm(p[2])

def p_stm_import(p):
    'stm : IMPORT id_list end'
    p[0] = ImportStm(p[2])

def p_stm_echo(p):
    'stm : ECHO STRING end'
    p[0] = EchoStm(p[2])

def p_stm_exp(p):
    'stm : exp end'
    p[0] = ExpStm(p[1])

# --- ID LIST (import) ---
def p_id_list_single(p):
    'id_list : ID'
    p[0] = [p[1]]

def p_id_list_compound(p):
    'id_list : ID VIRG id_list'
    p[0] = [p[1]] + p[3]

# --- SIGPARAMS ---
def p_sigParams_empty(p):
    'sigParams : '
    p[0] = EmptySigParams()

def p_sigParams_single(p):
    'sigParams : param'
    p[0] = SingleSigParams(p[1])

def p_sigParams_compound(p):
    'sigParams : param VIRG sigParams'
    p[0] = CompoundSigParams(p[1], p[3])

def p_param(p):
    'param : ID DOISPONTOS ID'
    p[0] = ParamConcrete(p[1], p[3])

# --- STMS ---
def p_stms_single(p):
    'stms : stm'
    p[0] = SingleStms(p[1])

def p_stms_compound(p):
    'stms : stm stms'
    p[0] = CompoundStms(p[1], p[2])

# --- EXPRESSÕES ---
def p_exp_binop(p):
    '''exp : exp SOMA exp
           | exp SUB exp
           | exp MUL exp
           | exp DIV exp
           | exp MOD exp
           | exp EXP exp
           | exp EQ exp
           | exp GT exp
           | exp LT exp
           | exp GE exp
           | exp LE exp'''
    p[0] = BinOpExp(p[1], p[2], p[3])

def p_exp_call(p):
    'exp : call'
    p[0] = CallExp(p[1])

def p_exp_assign(p):
    'exp : assign'
    p[0] = AssignExp(p[1][0], p[1][1])

def p_exp_num(p):
    '''exp : INTNUMBER
           | FLOATNUMBER
           | HEX_INTNUMBER
           | BIN_INTNUMBER
           | OCT_INTNUMBER'''
    p[0] = NumExp(p[1])

def p_exp_id(p):
    'exp : ID'
    p[0] = IdExp(p[1])

# --- CALL ---
def p_call_params(p):
    'call : ID LPAREN params RPAREN'
    p[0] = ParamsCall(p[1], p[3])

def p_call_noparams(p):
    'call : ID LPAREN RPAREN'
    p[0] = NoParamsCall(p[1])

# --- PARAMS ---
def p_params_single(p):
    'params : exp'
    p[0] = SingleParam(p[1])

def p_params_compound(p):
    'params : exp VIRG params'
    p[0] = CompoundParams(p[1], p[3])

# --- ASSIGN ---
def p_assign(p):
    'assign : ID ATRIB exp'
    p[0] = (p[1], p[3])

# --- END OF STATEMENT ---
def p_end(p):
    '''end : PV
           | NEWLINE'''
    pass

# --- ERROR HANDLER ---
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: token {p.type} ({p.value})")
    else:
        print("Erro de sintaxe: fim inesperado do arquivo.")

# --- PARSER ---
def main():
    with open("input.nim", "r") as f:
        entrada = f.read()
    lexer = lex.lex()
    parser = yacc.yacc()
    result = parser.parse(entrada, lexer=lexer, debug=True)
    print(result)

if __name__ == "__main__":
    main()
