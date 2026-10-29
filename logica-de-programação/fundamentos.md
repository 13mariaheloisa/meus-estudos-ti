# 🧠 Fundamentos de Lógica de Programação

Resumos e anotações essenciais sobre a base do raciocínio lógico aplicado à programação.

---

## 1. O que é Lógica de Programação?
É a organização estruturada de passos (sequência lógica) para que um computador execute uma tarefa e resolva um problema. É o "como pensar" antes de escrever o código em si.

* **Algoritmo:** É uma sequência finita de instruções claras e ordenadas que levam à solução de um problema. **

---

## 2. Conceitos Básicos

### 🔹 Variáveis e Constantes
São espaços na memória do computador usados para armazenar dados temporariamente:
* **Variável:** Um valor que **pode mudar** (variar) ao longo da execução do programa (ex: `pontuacao`, `nome_usuario`).
* **Constante:** Um valor fixo que **não muda** depois de definido (ex: `PI = 3.14`).

### 🔹 Tipos de Dados
Os tipos mais comuns de informações que manipulamos:
* **Inteiro (`int`):** Números inteiros (ex: `10`, `-5`, `0`).
* **Real / Ponto Flutuante (`float`):** Números com casas decimais (ex: `5.5`, `3.14`).
* **Caractere / String (`str`):** Textos (ex: `"Maria"`, `"Olá, mundo!"`).
* **Booleano (`bool`):** Valores lógicos de verdadeiro ou falso (`true` / `false`).

---

## 3. Estruturas de Controle

São comandos que dizem ao computador qual caminho seguir com base em condições ou repetições.

### 🔹 Condicionais (Decisões)
Permitem que o programa tome decisões:
* **`se` / `senão` (if / else):**
  ```text
  SE (nota >= 6) {
      Imprimir("Aprovado");
  } SENÃO {
      Imprimir("Reprovado");
  }
