function setOnCeil(cell, pos) {
    const jogadorAtual = getCookie("jogadorAtual");
    if (!cell.classList.contains('enabled')) {
        return;
    }
    fetch('/game/setOnCeil', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `pos=${pos}&jogadorAtual=${jogadorAtual}`
    })
    .then(response => {
        if (!response.ok) {
            alert('Erro ao preencher a célula');
            throw new Error('Erro ao preencher a célula');
        }
        return response.json();
    })
    .then(result => {
        const novoJogadorAtual = getCookie("jogadorAtual");
        document.querySelector(".jogador").innerText = `Jogador atual: ${novoJogadorAtual}`;
        document.getElementById(`cell${pos}`).innerText = result.forma;
        if(result.message){
            document.querySelector(".jogador").innerText = result.message;
            toggleGame();
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function reset() {
    fetch('/game/reset', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => {
        if (!response.ok) throw new Error('Erro ao preencher a célula');
        return response.text();
    })
    .then(result => {
        for (let i = 0; i < 9; i++) {
            document.getElementById(`cell${i}`).innerText = "";
        }
        toggleGame();
        const jogadorAtual = getCookie("jogadorAtual");
        document.querySelector(".jogador").innerText = `Jogador atual: ${jogadorAtual}`;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function restart() {
    fetch('/game/restart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => {
        if (!response.ok) throw new Error('Erro ao resetar !');
        window.location.href = '/';
        return response.text();
    })
    .then(result => {
        for (let i = 0; i < 9; i++) {
            document.getElementById(`cell${i}`).innerText = " ";
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function getCookie(name) {
    var cookieArr = document.cookie.split(';');
    for (var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split('=');
        if (name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null;
}

function toggleGame(){
    let cells = document.getElementsByName("cell");
    cells.forEach(cell => {
        cell.classList.toggle("enabled");
    });
}

document.addEventListener("DOMContentLoaded", function() {
    const jogadorAtual = getCookie("jogadorAtual");
    document.querySelector(".jogador").innerText = `Jogador atual: ${jogadorAtual}`;
});