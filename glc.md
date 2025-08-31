# GLC da Linguagem de Programação NIM (Somente um Exemplo)
Na gramática, os terminais correspondem a símbolos literais (entre aspas duplas, por exemplo "+", "=", ";") 
e a categorias básicas da linguagem (como ID para identificadores e NUM para números).
```
program → stm
        | stm program

stm → proc ID "(" sigParams ")" ":" stms
     | var ID ";"
     | var ID ":" type ";"
     | var ID "=" exp ";"
     | var ID ":" type "=" exp ";"
     | if exp ":" INDENT stms DEDENT
     | while exp ":" INDENT stms DEDENT
     | for ID "=" exp ":" INDENT stms DEDENT
     | return exp ";"
     | import ID ("," ID)* ";"
     | exp ";"

sigParams → param
          | param "," sigParams
          | ε

param → ID ":" type
type → "int" | "float" | "bool" | "string" | "void"

stms → stm
      | stm stms

exp → exp "+" exp
     | exp "-" exp
     | exp "*" exp
     | exp "/" exp
     | exp "mod" exp
     | exp "^" exp
     | call
     | assign
     | NUM
     | ID

call → ID "(" params ")" 
      | ID "(" ")"

params → exp
        | exp "," params

assign → ID "=" exp
        | exp "," params

assign → ID "=" exp
```
