/**
 * Projeto: Calculadora de Média Escolar Básica
 * Descrição: Script simples em JavaScript para praticar lógica, 
 * variáveis, operadores e condicionais (if/else).
 * Desenvolvido por: Maria Heloisa
 */

// 1. Definindo as notas do aluno (você pode alterar esses valores para testar)
let nota1 = 7.5;
let nota2 = 8.0;
let nota3 = 6.0;

// 2. Calculando a média aritmética
let media = (nota1 + nota2 + nota3) / 3;

// Exibindo a média no console com duas casas decimais
console.log("Sua média final é: " + media.toFixed(2));

// 3. Estrutura condicional para verificar a situação do aluno
if (media >= 7.0) {
    console.log("Status: Aprovado(a)! Parabéns! 🎉");
} else if (media >= 5.0) {
    console.log("Status: Em recuperação. Precisa estudar mais um pouco! 📚");
} else {
    console.log("Status: Reprovado(a). Não desanime, tente novamente! 💪");
}
