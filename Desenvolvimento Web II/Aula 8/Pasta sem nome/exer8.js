// 1.Calcule a media de diversas notas digitadas pelo usuário.

var nota, nota1, media;

function calcular(quadro){
	media = (nota + nota1) / 2;
	
	quadro.value = media;	
}

// 2. Faça um programa que entre com cinco números e imprima o quadrado de cada número.

var num1, num2, num3, num4, num5;

function quadrado(quadr){
	num1 = num1 * num1;
	num2 = num2 * num2;
	num3 = num3 * num3;
	num4 = num4 * num4;
	num5 = num5 * num5;
	
	quadr.value = num1 + "\n" + num2 + "\n" + num3 + "\n" + num4 + "\n" + num5;
}
	