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
      |if exp : INDENT stms DEDENT (elif exp : INDENT stms DEDENT)* (else : INDENT stms DEDENT)?
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


### 1.2.1 Chamadas de Função e Atribuição 




# 2.Exemplos de Código.

