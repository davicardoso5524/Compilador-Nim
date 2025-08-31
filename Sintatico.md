# Documentação Sintática da Linguagem Nim

# 1. Elementos Sintáticos.
Um programa em Nim é composto por uma ou mais declarações e blocos de código. A estrutura básica de uma procedura (proc) é definida pela seguinte regra:

```
proc -> ID ID "(" sigParams ")" ":" stms
```

Onde:
- `Primeiro ID` -> tipo de retorno da função (int, bool, float, string, void)
- `Segundo ID` -> nome da função
- `sigParams` -> parâmetros da função (pode ser vazio)
- `stms` -> sequência de comandos ou instruções da função

## 1.1 Comandos Da Linguagem Nim
Nim suporta os seguintes comandos:

```
stm -> exp;
      | while exp : INDENT stms DEDENT
      | for ID = exp : INDENT stms DEDENT
      | var ID (: type)? (= exp)? ;
      | proc ID (params)? (: type)? : INDENT stms DEDENT
      | return exp ;
      | import ID (, ID)* ;
      | if exp : INDENT stms DEDENT (elif exp : INDENT stms DEDENT)* (else : INDENT stms DEDENT)?
```
- Comando de expressão:
 Qualquer expressão seguida de ponto e vírgula (;).

- Comando condicional (`if / elif / else`):
 Começa com if, seguido de uma expressão e dois pontos (:).
 Um bloco de comandos indentado (INDENT ... DEDENT) segue o if.
 Permite zero ou mais blocos elif e um bloco opcional else.

- Comando de repetição (`while`):
 Começa com while seguido de expressão e dois pontos.
 Um bloco indentado de comandos segue.

- Comando de repetição (`for`):
 Começa com for, seguido de identificador (ID) e atribuição (=) de um valor.
 Um bloco indentado de comandos segue.

- Declaração de variável (`var`):
 Inicia com var, seguido do nome da variável.
 Pode ter tipo especificado (: tipo) e/ou valor inicial (= exp).
 Finaliza com ponto e vírgula.

- Declaração de procedimento (`proc`):
 Inicia com proc, seguido do nome do procedimento e parâmetros entre parênteses.
 Pode ter tipo de retorno (: tipo).
 O bloco de comandos é delimitado por indentação.

- Comando de retorno (`return`):
 Inicia com return seguido de expressão.
 Finaliza com ponto e vírgula (;).

- Importação de módulos (`import`):
 Inicia com import, seguido de um ou mais nomes de módulos separados por vírgula.
 Finaliza com ponto e vírgula.


## 1.2 Expressões em Nim
A linguagem NIM dá suporte a expressões aritméticas com soma (`+`), subtração (`-`), multiplicação (`*`), divisão (`/`), módulo (`mod`) e exponenciação (`^`).

Além disso, NIM permite:
Atribuição de valores a variáveis (`assign`) 
Chamadas de função (`call`)
Números literais (`INTNUMBER, FLOATNUMBER, HEX_INTNUMBER, BIN_INTNUMBER, OCT_INTNUMBER`)
Strings e caracteres (`STRING, CHAR`)
Variáveis (`ID`).

```
exp → exp "+" exp
      | exp "-" exp
      | exp "*" exp
      | exp "/" exp
      | exp "mod" exp
      | exp "^" exp
      | call
      | assign
      | INTNUMBER
      | FLOATNUMBER
      | HEX_INTNUMBER
      | BIN_INTNUMBER
      | OCT_INTNUMBER
      | STRING
      | CHAR
      | ID
```

### 1.2.1 Chamadas de Função e Atribuição 

A linguagem NIM dá suporte a chamadas de função com ou sem parâmetros. Um parâmetro de função pode ser qualquer expressão da linguagem. Além disso, NIM permite atribuir valores a variáveis usando o operador `=`.

A sintaxe dessas construções pode ser representada pelas seguintes regras:

```
call → ID "(" params ")" 
       | ID "(" ")"

params → exp "," params
         | exp

assign → ID "=" exp
```

# 2.Exemplos de Código.
A seguir alguns exemplos da linguagem Nim: 

```
proc soma(a: int, b: int): int
    return a + b;

var resultado: int;
resultado = soma(5, 10);
echo resultado;
```

```
proc gerarNumero(): int
    return 42;

var numero: int;
numero = gerarNumero();
echo "O número gerado é: ", numero;
```

```
import math, strutils;

proc calcularQuadrado(n: int): int
    return n ^ 2;

var numeros: array[5, int];
var i: int;

for i = 0 : 
    INDENT
    numeros[i] = i * 2;
DEDENT

var somaTotal: int = 0;
i = 0;
while i < 5 :
    INDENT
    if numeros[i] mod 2 == 0 :
        INDENT
        somaTotal = somaTotal + calcularQuadrado(numeros[i]);
    DEDENT
    i = i + 1;
DEDENT

echo "Soma dos quadrados dos números pares: ", somaTotal;
```
