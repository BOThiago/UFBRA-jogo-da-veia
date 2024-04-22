function setOnCeil(cell, pos) {
    const jogador1 = getCookie("jogador1");
    const jogador2 = getCookie("jogador2");
    const jogadorAtual = getCookie("jogadorAtual");

    fetch('/setOnCeil', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `pos=${pos}&jogador1=${jogador1}&jogador2=${jogador2}&jogadorAtual=${jogadorAtual}`
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao preencher a célula');
        }
        return response.text();
    })
    .then(result => {
        if (result === "Venceu!") document.getElementById(`cell${pos}`).innerText = result;
        document.getElementById(`cell${pos}`).innerText = result;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function reset() {
    fetch('/reset', {
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
            document.getElementById(`cell${i}`).innerText = " ";
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function restart() {
    fetch('/restart', {
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