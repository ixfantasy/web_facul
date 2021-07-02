/* filter() - método que cria um novo metor com elementos do vetor que passam no teste */

var numero = [2, 45, 6, 23, 68, 72, 6, 7, 8];
var maior = numero.filter(maior);
	document.write("<br>Os números da matriz maiores que 18 são:" + maior);
	
	function maior(value){
		return value > 18;
	}
	
/* map - cria uma nova matriz executando uma função em cada elemento da matriz, sem alterar a matriz principal */

var numero1 = [2, 4, 6, 5, 7];
var numero2 = numero1.map(mult);

function mult(value){
	return value * 2;
}
	document.write("<br>A multiplicação de cada elemento é: " + numero2);
	
/* find() - retorna o primeiro valor da condição imposta */

var num = [4, 9, 16, 25, 29];
var primeiro = num.find(nova);

function nova(value){
	return value < 20;
}
	document.write("<br>O primeiro número é: " + primeiro);
	
/* reduce - executa uma função em cada elemento da matriz para produzir um único valor */

var num1 = [4, 9, 16, 25, 29];
var soma = num1.reduce(exemplo);

function exemplo(total, value){
	return total + value;
}
	document.write("<br>A soma dos valores é: " + soma);
	
/*Comandos Date - para criar a data e hora, usa-se new Date() */

var data = new Date();
	document.write("<br>A data e hora: " + data);
	document.write("<br>O dia de hoje é: " + data.getDay()); //vai trazer só o dia
	document.write("<br>O mês de hoje é: " + data.getMonth()); //traz o mês
	document.write("<br>O ano de hoje é: " + data.getFullYear()); //ano
	
/* Para mostrar o dia, mês de maneira escrita */

var data = new Date();
var dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"];
var meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

	document.write("<br>O dia de hoje é " + dias[data.getDay()]);
	document.write("<br>O mês atual é " + meses[data.getMonth()]);
	
/* Fuso internacional - toGMTString */

var data = new Date();
	document.write("<br>O fuso horário internacional é " + data.toGMTString());
	
/* fuso Local - toLocaleString() */

var data = new Date();
	document.write("<br>O horário local é " + data.toLocaleString());
	
/* Recuperar a hora */

var data = new Date();
	document.write("<br>A hora local é " + data.getHours());
	
/* Recuperar a hora intercional */

var data = new Date();
	document.write("<br>A hora intercional é " + data.getUTCHours());
	
/* Retornar os segundos */
var data = new Date();
	document.write("<br>Os segundos: " + data.getSeconds());
	
/* Retornar os minutos */
var data = new Date();
	document.write("<br>Os minutos: " + data.getMinutes());