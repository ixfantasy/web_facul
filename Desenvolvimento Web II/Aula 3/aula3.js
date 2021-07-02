/* FUNCTION: function nome_função(variável1, variável2) */

function somar(x, y){ /* Parâmetro; a variável é criada através da função */
	document.write("<font face='Verdana' size=1>A soma de x e y é:\u00A0" + (x + y)); /* Dentro das chaves fica a execução do programa. Fora, os valores */
}

	/* Valores podem ser pré-definidos, ou pode pedir para o usuário digitar através do prompt */
somar(8, 10);

	/* Passando os valores pelo prompt */
function somar1(x, y){ /* Utilizar nomes diferentes para evitar conflito */
	document.write("<br>A soma de x e y é:\u00A0" + (x + y));
}

var x = parseInt(prompt("Valor 1:"));
var y = parseInt(prompt("Valor 2:"));

somar1(x, y);

	/* Criando outra função para subtração */
function sub(x, y){
	document.write("<br>A subtração de x e y é:\u00A0" + (x - y));
}

sub(100, 60);

function sub1(x, y){
	document.write("<br>A subtração de x e y é:\u00A0" + (x - y));
}

var x = parseInt(prompt("Valor 3:"));
var y = parseInt(prompt("Valor 4:"));

sub1(x, y);

	/* Criando função para multiplicação */
function mult(x, y){
	document.write("<br>A multiplicação de x e y é:\u00A0" + (x * y));
}

mult(10, 10);

function mult1(x, y){
	document.write("<br>A multiplicação de x e y é:\u00A0" + (x * y));
}

var x = parseInt(prompt("Valor 5:"));
var y = parseInt(prompt("Valor 6:"));

mult1(x, y);

	/* Criando função para divisão */
function div(x, y){
	document.write("<br>A divisão de x e y é:\u00A0" + (x / y));
}

div(10, 5);

function div1(x, y){
	document.write("<br>A divisão de x e y é:\u00A0" + (x / y));
}

var x = parseInt(prompt("Valor 7:"));
var y = parseInt(prompt("Valor 8:"));

div1(x, y);

	document.write("<hr size=5 color='pink' />");

/* FUNÇÃO RETURN */

function teste(x, y){
	return x + y
}

var x = +(prompt("Valor 9:"));
var y = +(prompt("Valor 10:")); /* No lugar de escrever parseInt, é possível colocar somente um + na frente para identificar que é um número */
	document.write("O resultado da soma é:\u00A0" + teste(x, y)); /* pede o retorno da função, que seria a soma */
	
function teste1(x, y){
	return x * y
}

var x = +(prompt("Valor 11:"));
var y = +(prompt("Valor 12:"));
	document.write("<br>O resultado da multiplicação é:\u00A0" + teste1(x, y));
	
	document.write("<hr size=5 color='pink' />");
	
/* CONDIÇÃO IF, ELSE */

	/* if */
var idade = 8;

if(idade <= 10){
	document.write("Criança!");
}

	document.write("<hr size=2 color='pink' />");


	/* if else */
var idade = prompt("Digite a sua idade:");

if(idade <= 10){
	document.write("Criança!");
} else {
	document.write("Adolescente!");
}

	document.write("<hr size=2 color='pink' />");

	/* if else if */
var idade = prompt("Digite a sua idade novamente:");

if(idade <= 10){
	document.write("Criança!");
} else if(idade > 12 && idade <= 16){
	document.write("Pré-adolescente!");
} else if(idade > 16 && idade <= 21){
	document.write("Adolescente!");
} else {
	document.write("Melhor idade!");
}

	document.write("<hr size=2 color='pink' />");

	/* if dentro de if */
var nota = prompt("Sua nota:");

if(nota >= 6){
	document.write("Aprovado!");
} else {
	document.write("Reprovado!");
	if(nota == 5){
		document.write("<br>Em recuperação!");
	}
}

	document.write("<hr size=5 color='pink' />");
	
	/* OPERADOR THIS */
	
alert(this.document.title); /* para chamar; trazer o título */
document.write(this.document.title);

	/* OPERADOR IN: indica se existe a propriedade especificada */
	
Aluno={ /* criou uma classe */
	nome:"Thereza", /* que recebe atributos */
	email:"prof.thereza.gondim@soulasalle.com.br",
	endereco:"rua A"
}

alert("nome" in Aluno); /* para identificar se existe o atributo "nome" na classe "Aluno" */
alert("telefone" in Aluno);

	/* OPERADOR DELETE: para remover uma propriedade */
delete Aluno.endereco;
document.write("<br>");
document.write("endereco" in Aluno);