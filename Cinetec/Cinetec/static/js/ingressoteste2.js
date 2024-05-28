$(document).ready(function() {
    let caminho = window.location.origin
    const endpoint = caminho +"/compras/ingresso_escolhido";
    const id_json = document.getElementById("json_id")
    const status_json = document.getElementById("json_status")
    // let  cabecalho = {
    //     method: "POST",
    //     body: JSON.stringify(cadeirasSelecionadas)
    // }
    res = fetch(endpoint)
    .then(res=>res.text())
    .then(dados=>{
        console.log(dados)
    })

});