$(document).ready(()=>{
    $(".burguer-container").click(function(){
        $(this).toggleClass("active");
        $(".sidebar").toggleClass("show");
        
       });
       $('main').click(function(){
           $('.sidebar').removeClass('show');
           $('.burguer-container').removeClass('active');
           
       }); 
});