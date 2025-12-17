function verificar_senha(){
    let senha = document.getElementById('senha');
    let confirmacao = document.getElementById('confirmacao');
    let botao = document.getElementById('idbotao');

    if(senha.value === confirmacao.value){
        botao.type = 'submit';
    }else{
        let msgerro = document.getElementById('errosenha');
        msgerro.textContent = 'senha e confirmação devem ser iguais';
    }
}