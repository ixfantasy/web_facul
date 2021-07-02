/* 1. Faça um Programa que peça um número e então mostre a mensagem: O número informado foi [número]. */

var x = prompt("Digite um número:");
	document.write("O número digitado é:\u00A0" + x);
	
/* 2. Faça um Programa que converta metros para centímetros. (Dica: 1 metro = 100 centímetros) */

var metro = prompt("Digite o valor em metros:");
	function centi(metro){
		return metro * 100
	}
		document.write("<br>O resultado em centímetros é:\u00A0" + centi(metro));
		
/* 3. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. Fórmula: Area = pi * raio² */

var raio = prompt("Digite o raio de um círculo:");
var are = 3.14 * (Math.pow(raio, 2));
	document.write("<br>A área do círculo é:\u00A0" + are);
	
/* 4. Faça um Programa que peça a temperatura em graus Farenheit, 
transforme e mostre a temperatura em graus Celsius. Fórmula: Celsius = (5 * (Farenheit -32) / 9). */

var faren = prompt("Digite a temperatura em Farenheit:");
	function cel(faren){
		return (5 * (faren - 32) / 9)
	}
var fix = cel(faren).toFixed(1);
		document.write("<br>A temperatura em Celsius é:\u00A0" + fix);
		
/* 5. Faça um Programa que peça o valor da gasolina e do álcool de um posto e diga qual é o combustível mais vantajoso abastecer, 
sabendo que somente é vantagem abastecer álcool se o preço do mesmo é menor ou igual a 70% do valor da gasolina. */

var gas = prompt("Digite o valor da gasolina:");
var alc = prompt("Digite o valor do álcool:");

	function porc(gas){
		return (gas * 70) / 100
	}
	if(porc(gas) >= alc){
		document.write("<br>O álcool é mais vantajoso!");
	} else {
		document.write("<br>A gasolina é mais vantajosa!");
	}
	
/* 6.Este é um exercício difícil! Você deve sortear 6 números de 1 a 60 e guardar numa array. 
Depois peça para o usuário dizer 6 números, um de cada vez (pode usar um prompt ou um input ) 
e guarde-os em uma outra array. Aí diga quantos números ele acertou. Sim, é a loteria certinha desta vez! Tente acertar os 6 números. 
Depois faça as contas de quantas chances você tem de acertar todos os 6. Você nunca mais vai jogar na loteria! */

var arr1 = new Array();
var arr2 = new Array();

for(var i = 0; i < 6; i++){
	var sorteio = Math.floor(Math.random() * 59) + 1;
	arr1[i] = sorteio;
}

for(var i = 0; i < 6; i++){
	var num = prompt("Digite um número:");
	arr2[i] = num;
}

var Cont = 0;

for(var i = 0; i < 6; i++){
	for(var j = 0; j < 6; j++){
		if(arr1[i] == arr2[j]){
			Cont++;
		}
	}
}

if(Cont == 6){
	document.write("<br>Você acertou todos os números!");
} else {
	document.write("<br>Você não acertou todos os números.");
}

	document.write("<br>Existem 50.063.860 combinações possíveis.");
	