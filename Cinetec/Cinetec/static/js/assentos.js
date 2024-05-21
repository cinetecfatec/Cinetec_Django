
$(document).ready(function() {
    console.log("documento", document.getElementById("bt_compra"))
    let assentos_banco = Assentos(assentos);
    console.log("assentos_banco = ");
    console.log(assentos_banco);
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

    fetch(caminho +"/compras/ingresso_escolhido",
{
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify(todasCadera)
})
.then(window.location.href = caminho +"/compras/ingresso_escolhido")


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


