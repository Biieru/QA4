# Atividade de Validação – Calculadora (QA)

Este repositório contém a implementação das funções de uma **calculadora simples** e seus respectivos **testes unitários**, desenvolvidos como parte da atividade da disciplina de **Qualidade de Software / Teste de Software**.

O objetivo da atividade é demonstrar a construção de **casos de teste**, a implementação das funções a serem testadas e a execução de **testes automatizados** usando o módulo `unittest` do Python.

---

## Estrutura do Projeto

```text
/atividade-calculadora
├── calculadora.py          # Implementação das funções
├── test_calculadora.py     # Testes unitários com unittest
├── README.md               # Este arquivo
└── Atividade 4.pdf         # Arquivo original com as instruções (professor)
```

## Testes Unitários

Os testes foram desenvolvidos utilizando a biblioteca padrão unittest.
Cada operação possui cenários cobrindo:

- Entradas positivas

- Entradas negativas

- Multiplicação por zero

- Tratamento de divisão por zero

- Resultados esperados conforme os casos de teste especificados


---


## Como executar os testes

1. Certifique-se de estar na pasta do projeto.

2. Execute o comando:

```text
python -m unittest test_calculadora.py
```
Ou simplesmente:

```text
python test_calculadora.py
```

### Saída esperada:
```text
Erro: Divisão por zero.
....
----------------------------------------------------------------------
Ran 4 tests in X.XXXs

OK
```
## Casos de Teste (Resumo)

| ID    | Operação         | Entrada | Resultado Esperado |
| ----- | ---------------- | ------- | ------------------ |
| CT-01 | Soma             | (10, 5) | 15                 |
| CT-02 | Soma             | (-3, 7) | 4                  |
| CT-03 | Subtração        | (10, 4) | 6                  |
| CT-04 | Subtração        | (3, 9)  | -6                 |
| CT-05 | Multiplicação    | (7, 6)  | 42                 |
| CT-06 | Multiplicação    | (15, 0) | 0                  |
| CT-07 | Divisão          | (20, 4) | 5                  |
| CT-08 | Divisão por zero | (10, 0) | None               |


---


### Tecnologias Utilizadas

Python 3.x

unittest (biblioteca padrão)

VSCode / Terminal / GitHub
