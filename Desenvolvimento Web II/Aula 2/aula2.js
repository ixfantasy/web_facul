/* Método Math: para utilizar junto com os operadores
	• abs: transforma um número negativo em positivo.
	• max: retorna; mostra o maior valor.
	• min: retorna; mostra o menor valor.
	• pow: para elevar um número à uma potência. O primeiro número é o valor de base, e o segundo é a potência.
	• round: arredonda um valor. Exemplo: 9.2 arredonda para 9, enquanto 9.5 arredonda para 10.
	• ceil: arredonda um valor, obrigatoriamente, para cima. Exemplo: tanto 9.2 como 9.5 arredondam para 10.
	• floor: arredonda um valor, obrigatoriamente, para baixo. Exemplo: tanto 9.2 como 9.5 arredondam para 9.
	• random: trabalha com valores aleatórios entre 0 e 1. Para sortear entre valores específicos, utiliza-se ()*valor.
	• sqrt: raiz quadrada.
	• cbrt: raiz cúbica. */
	
	document.write("<font face=Verdana size=4 color=pink>Método Math</font>");
	
var a = Math.abs(-50);
	document.write("<font face=Verdana size=1><br>O resultado é:\u00A0" + a);
	
var b = Math.max(30, 62, 25, 80, 75);
	document.write("<br>O maior valor é:\u00A0" + b);
	
var c = Math.min(30, 62, 25, 80, 75);
	document.write("<br>O menor valor é:\u00A0" + c);
	
var d = Math.pow(2, 10);
	document.write("<br>2<sup>10</sup>:\u00A0" + d);
	
var e = Math.round(9.2);
	document.write("<br>O valor 9.2 arredondado normalmente é:\u00A0" + e);
	
var f = Math.ceil(9.2);
	document.write("<br>O valor 9.2 arredondado para cima é:\u00A0" + f);
	
var g = Math.floor(9.2);
	document.write("<br>O valor 9.2 arredondado para baixo é:\u00A0" + g);
	
var h = Math.random();
var l = h.toFixed(2); //para definir o número de casas decimais. Cria uma nova variável e utiliza o toFixed(valor);
	document.write("<br>O valor aleatório é:\u00A0" + l); //ao definir o número de casas decimais, imprime a nova variável
	
var i = Math.random()*50;
var m = i.toFixed(0);
	document.write("<br>O valor aleatório entre 0 e 50:\u00A0" + m);
	
var j = Math.sqrt(49);
	document.write("<br>A raiz quadrada de 49 é:\u00A0" + j);
	
var k = Math.cbrt(8);
	document.write("<br>A raiz cúbica de 8 é:\u00A0" + k);
	
/* Operadores de comparação
	• == (igual): verifica se os dados são iguais.
	• === (igual idêntico): verifica se os dados são iguais e de mesmo tipo.
	• != (diferente): verifica se os dados são diferentes.
	• !== (identidade diferente): verifica se os dados possuem identidades; tipos diferentes.
	• > (operador maior): verifica se um valor é maior que o outro.
	• < (operador menor): verifica se um valor é menor que o outro.
	• >= (maior ou igual): verifica se um valor é maior ou igual ao outro.
	• <= (menor ou igual): verifica se um valor é menor ou igual ao outro.
	*/
	
	document.write("<br><hr /><font face=Verdana size=4 color=pink>Operadores de Comparação</font>");

var x = 6;
var y = "6";
	document.write("<br>Os valores são iguais?\u00A0" + (x == y));
	document.write("<br>Os valores são iguais idênticos?\u00A0" + (x === y));
	document.write("<br>Os valores são diferentes?\u00A0" + (x != 6));
	document.write("<br>Os valores possuem identidades diferentes?\u00A0" + (x !== "6"));
	
var maior = prompt("Entre com um valor:");
	document.write("<br>O valor digitado é maior que 10?\u00A0" + (maior > 10));
	document.write("<br>O valor digitado é maior ou igual a 15?\u00A0" + (maior >= 15));
	
var menor = prompt("Entre com um outro valor:");
	document.write("<br>O valor digitado é menor que 10?\u00A0" + (menor < 10));
	document.write("<br>O valor digitado é menor ou igual a 5?\u00A0" + (menor <= 5));
	
/* Operadores Lógicos
	• && (AND): as duas premissas precisam ser verdadeiras.
	• || (OR): uma das premissas precisa ser verdadeira.
	• ! (NOT): inverte o valor lógico.
	*/
	
	document.write("<br><hr /><font face=Verdana size=4 color=pink>Operadores Lógicos</font>");
	
var w = prompt("Entre com um valor:");
	document.write("<br>O valor digitado é maior ou igual a 1, e menor ou igual a 10?\u00A0" + ((w >= 1) && (w <= 10)));
	document.write("<br>O valor digitado é menor que 5 ou maior que 10?\u00A0" + ((w < 5) || (w > 10)));
	document.write("<br>O valor digitado é menor que 5?\u00A0" + (!(w < 5)));

	
