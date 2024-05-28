
$(document).ready(function() {
    let csrftoken = getCookie('csrftoken');
    let assentos_banco = Assentos(assentos);
    let sessao_id = Sessao(sessao);
    console.log("assentos_banco = ");
    console.log(assentos_banco);
    console.log("Sessão = ");
    console.log(sessao_id);
    let livre = "/static/img/assento_disp.png";
    let selecionado = "/static/img/assento_selecionado.png";
    let ocupado = "/static/img/assento_ocup.png";
    let contador = 0;
    let cadera = document.getElementById("cadera");
    let todasCadera= [];
    let existe = criarJsonAssentos(assentos_banco);
    
    if (existe){
        todasCadera = JSON.parse(existe);
    }

    for (let index = 0; index < 128; index++) {
        var newElement = document.createElement("div");
        let id = "cadera_"+index
        
        if(!existe){
            todasCadera.push({
                id: id,
                status:"livre",
            }) 
        }
        newElement.innerHTML = `<img id="${id}" src="${existeSalvo(existe, index)}" class='itemcadera'>`;
        cadera.appendChild(newElement);

        document.getElementById(id).addEventListener('click', function name(params) {
            let status = todasCadera.find(x => x.id === this.id).status;
            let img
            if (status == 'livre') {
                todasCadera.find(x => x.id === this.id).status = 'selecionado'
                img = selecionado;
            } else if(status == 'selecionado') {
                todasCadera.find(x => x.id === this.id).status = 'livre'
                img = livre;
            };
            
            let id = "#" + this.id;
            let atual = $(this).attr('src');


            $(this).attr('src', img);
            localStorage.setItem("cadeiras", JSON.stringify(todasCadera));
        });
    }

    document.getElementById("bt_compra").addEventListener('click', function(compra_) {
        let caminho = window.location.origin
        const endpoint = caminho +"/compras/ingresso_escolhido";


        let cadeirasSelecionadas = {
            id: 1,
            status:"livre"
        }
        
        if (!csrftoken) {
            console.error('CSRF token not found. Check if CSRF middleware is enabled or if the token is being set correctly.');
            return;
        }


        $.ajax({
            method: "POST",
            headers: {'X-CSRFToken': csrftoken}, // Inclui o token CSRF como cabeçalho
            url: endpoint,
            data: JSON.stringify(cadeirasSelecionadas),
            contentType: "application/json",
            success: function(resposta) {
                console.log(resposta);
                // Redirect to the next page after successful AJAX response
                window.location.href = `${caminho}/checkout/${sessao_id}`;
            },
            error: function(error) {
                console.error("Error during AJAX request:", error);
            }
        });
    });


    function existeSalvo(existe, index) {
        if(!existe) return livre;
        else {
            if(todasCadera[index].status == 'selecionado') {
                return selecionado;
            }
            else if(todasCadera[index].status == 'ocupado'){
                return ocupado;
            }
            else{
                return livre;
            }
        }
    }

    function criarJsonAssentos(assentos) {
        let jsonArray = [];
    
        for (let i = 0; i < assentos.length; i++) {
            let status = (assentos[i] === 'e') ? 'livre' : (assentos[i] === 'o') ? 'ocupado' : 'desconhecido';
            
            if (status === 'desconhecido') continue;
    
            let jsonEntry = {
                "id": "cadera_" + i,
                "status": status
            };
    
            jsonArray.push(jsonEntry);
        }
    
        return JSON.stringify(jsonArray, null, 2);
    }
    
});
function Assentos(assentos){
    return(assentos)
}

function Sessao (sessao){
    return sessao
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se o cookie possui o nome desejado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
