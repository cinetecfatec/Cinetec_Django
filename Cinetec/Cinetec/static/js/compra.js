
$(document).ready(()=>{
       let livre = './icon_cadeiras/assento_disp.png';
       let selecionado = './icon_cadeiras/assento_livre.png';
       let ocupado = 'icon_cadeiras/assento_ocup.png';
    let preco = document.getElementById("preco").innerHTML;  
    let contador = 0;
   let cadera = document.getElementById("cadera");
   let todasCadera= [];
   let existe = localStorage.getItem("cadeiras")
   if (existe){
       todasCadera = JSON.parse(existe);
       todasCadera.forEach(element => {
       element.status == 'selecionado' ? contador++ : contador
       });
       calc()
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
       newElement.innerHTML = `<img id="${id}" src='${existeSalvo(existe, index)}' class='itemcadera'>`;
       cadera.appendChild(newElement);
        
       

       document.getElementById(id).addEventListener('click', function name(params) {
             let status = todasCadera.find(x => x.id === this.id).status;
            let img
            if (status == 'livre') {
                todasCadera.find(x => x.id === this.id).status = 'selecionado'
                img = selecionado;
                contador += 1
            } else if(status == 'selecionado') {
                todasCadera.find(x => x.id === this.id).status = 'livre'
                img = livre;
                contador -= 1
            };
            
           
           
           let id = "#" + this.id;
           let atual = $(this).attr('src');
           
           
           
           
           
           calc()
           console.log("aaaaaa")

           $(this).attr('src', img);
           localStorage.setItem("cadeiras", JSON.stringify(todasCadera));
       })
   }

   document.getElementById("compra").addEventListener('click', function(compra_){
    
       todasCadera.forEach(element => {
           if (element.status == 'selecionado') {
               element.status = 'ocupado'
               let id = "#" + element.id;
               $(id).attr('src', ocupado)
               contador--
           }
           
       });
       calc()
       localStorage.setItem("cadeiras", JSON.stringify(todasCadera));
   })
   
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
   
   function calc() {
       document.getElementById("preco").innerHTML = contador * 15
   }
   
   
});