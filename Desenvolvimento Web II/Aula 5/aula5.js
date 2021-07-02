/* Método CONCAT: método para criar um novo vetor, mesclando (concatenando) vetores existentes */

var meninas = ["Maria", "Joana", "Paula"];
var meninos = ["Mario", "Joao", "Paulo"];

var pessoas = meninas.concat(meninos);
	document.write("<br>" + pessoas.join(", "));

var arr1 = ["Maria", "Joana", "Paula"];
var arr2 = ["Mario", "Joao", "Paulo"];
var arr3 = ["Roberto", "Juliana"];

var pessoas1 = arr1.concat(arr2, arr3);
	document.write("<br>" + pessoas1.join(", "));
	
/* Método SLICE: divide um pedaço de um vetor em um novo vetor. Isso não modifica o vetor original */

var frutas = ["Maça", "Banana", "Manga", "Abacaxi"];
	document.write("<br>" + frutas.join(", "));
	document.write("<br>" + frutas.slice(2).join(", ")); // define o índice que será cortado
	
/* Método SPLICE: adiciona novos elementos no array */

var frutas1 = ["Maça", "Banana", "Manga", "Abacaxi", "Morango"]; /* o primeiro é o índice, o segundo é o número de elemetos deletados */
	document.write("<br>" + frutas1.splice(1, 3, "Uva", "Laranja", "Melancia"));
	document.write("<br>" + frutas1);
	
/* Fila Fifo (First In First Out):
	Método PUSH: adiciona um novo elemento no final do array */
	
var aluno = ["Renato", "Guilherme", "Jorbe", "Camila"];
aluno.push("Walace", "Joaquina"); // o elemento adicionado
	document.write("<br>" + aluno.join(", "));
	
/* Método SHIFT: remove o primeiro elemento do vetor */

var aluno1 = ["Renato", "Guilherme", "Jorbe", "Camila"];
aluno1.shift();
	document.write("<br>" + aluno1);
	
/* Método POP: remove o último elemento do vetor */

var aluno2 = ["Renato", "Guilherme", "Jorbe", "Camila"];
aluno2.pop();
	document.write("<br>" + aluno2);
	
/* Método UNSHIFT: adiciona elementos no início do vetor */

var aluno3 = ["Renato", "Guilherme", "Jorbe"];
aluno3.unshift("Maria", "Fulana");
	document.write("<br>" + aluno3);
	
/* Função EVERY: checa se todos os elementos de um vetor passam num "teste". Se um for F, tudo é F */

var aluno4 = ["Renato", "Guilherme", "Jorbe", "Camila", 15465165];

function todos(elem){ // elem verifica se todos os elementos são uma string
	return(typeof elem == "string");
}
	document.write("<br>" + aluno4.every(todos));
	
/* Função SOME: checa se qualquer um dos elementos de um vetor passa no teste */

var x = ["Renato", "Guilherme", 12];
function diferente(elem){
	return(typeof elem == "number");
}
	document.write("<br>" + x.some(diferente));
	
/* Função FILTER: filtra o array com base na busca que foi submetida */

var frutas10 = ["Maça", "Banana", "Manga", "Abacaxi", "Morango"]; // procura uma vez dentro do elemento
function lista(elem){
	return(elem.indexOf("an") > 0); // faz uma busca dos elementos que possuem "an" na posição maior que 0
}
	document.write("<br>" + frutas10.filter(lista));


