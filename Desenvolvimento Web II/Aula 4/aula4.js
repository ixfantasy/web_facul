/* CONDIÇÃO WHILE: só executa enquanto for verdadeiro (V). */

var i = 0;

while(i < 3){
	alert(i);
	i++;
}

var i = prompt("Entre com um número:");

while(i < 3){
	alert(i);
	i++;
}

/* SWITCH: para condições múltiplas */

var sexo = prompt("Entre com F para feminino ou M para masculino:");

switch(sexo){
	case "M":
	case "m":
		alert("Masculino");
		break;
	case "F":
	case "f":
		alert("Feminino");
		break;
	default:
		alert("Opção inválida");
}

/* FOR: estrutura de repetição */

for(var i = 0; i < 5; i++){
	alert(i);
}

for(var i = 5; i > 0; i--){
	alert(i);
}

/* VETOR: pode ser declarado de 3 maneiras diferentes:
	• método construtor;
	• método literal;
	• criação de índices. */
	
	/* MÉTODO CONSTRUTOR new Array */
var disciplina = new Array("Desenvolvimento Web 2", "Programação", "BD", "Atividade Integradora");
	document.write(disciplina);
	
	// mostrar a posição dos elementos no array
var disciplina = new Array("Web", "Prog", "BD", "Ativ.");
	document.write("<br>" + disciplina[1]);
	
	// mostrar a quantidade de elementos dentro do vetor: length
var frutas = new Array("Maçã", "Banana", "Laranja", "Manga");
	document.write("<br>A quantidade de elementos é:\u00A0" + frutas.length);
	
	// mostrar a posição do elemento: indexOf
var frutas = new Array("Maçã", "Banana", "Laranja", "Manga");
	document.write("<br>A posição do elemento é:\u00A0" + frutas.indexOf("Manga"));

	// mostrar qual é a última ocorrência de um elemento repetido: lastIndexOf
var frutas = new Array("Maçã", "Banana", "Laranja", "Banana", "Manga");
	document.write("<br>A última ocorrência do elemento é:\u00A0" + frutas.lastIndexOf("Banana"));
	
/* MÉTODO LITERAL [] */
	
var prova = ["AV1", "AV2", "AV3", "Reprovado"];
	document.write("<br>" + prova);
	
	// uma string também é um vetor
var x = "laranja";
	document.write("<br>" + x);
	
	// mostrar a quantidade de letras/elementos na string
var x = "laranja";
	document.write("<br>O vetor tem:\u00A0" + x.length+ "\u00A0 letras");
	
/* CRIAÇÃO DE ÍNDICES */
	
var frutas = new Array ();
	frutas[0] = "Maçã";
	frutas[1] = "Morango";
	frutas[2] = "Pera";
	frutas[3] = "Uva";
		document.write("<br>" + frutas);
		
var cidade = ["pelotas", "são lourenço", "porto alegre"];
	for(var i = 0; i < cidade.length; i++){
		alert(cidade[i]);
	}
	
	// Função de ordenação
/* REVERSE: inverte a ordem dos elementos */
	
var cidade = ["Pelotas", "São Lourenço", "Porto Alegre"];
	document.write("<br>A ordem contrária dos elementos é:\u00A0" + cidade.reverse());
	
/* SORT: para colocar em ordem alfabética */

var cidade=["Pelotas", "São Lourenço", "Porto Alegre"];
	document.write("<br>A ordem alfabética dos elementos é:\u00A0" + cidade.sort());
	
	// Cortes e emendas
/* Método Join: para alterar o separador padrão, que é a vírgula */

var cidade = ["Pelotas", "São Lourenço", "Porto Alegre"];
	document.write("<br>" + cidade.join("-"));
	document.write("<br>" + cidade.join(" "));
	document.write("<br>" + cidade.join(""));
	
/* Método Concat: para inserir novos elementos no vetor */

var cidade = ["Pelotas", "São Lourenço", "Porto Alegre"];
	document.write("<br>" + cidade); // o original
	document.write("<br>" + cidade.concat("Pernambuco", "Aracaju")); // novos elementos adicionados
	
var nomes = ["Pedro", "Ana", "Maria"];
nomes.sort();
	document.write("<br>" + nomes.join(" "));
nomes.reverse();
	document.write("<br>" + nomes.join("♥"));