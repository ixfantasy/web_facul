function acendelamp(){
	document.getElementById("luz").src="lamp on.png";
}

function apagalamp(){
	document.getElementById("luz").src="lamp off.png";
}

function quebralamp(){
	document.getElementById("luz").src="broken lamp.png";
}

var nome, email, num=0;

function cadastro(quadro){
	info="Usuário número:" + (++num) + "\n";
	info+="Nome:" + nome + "\n"; // += concatena strings
	info+="E-mail:" + email + "\n";
	quadro.value += info; // o += adiciona os novos elementos, enquanto somente = substitui pelo novo elemento
}

function mudacor(cor){
	document.bgColor=cor;
}