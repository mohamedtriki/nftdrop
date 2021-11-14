
document.getElementById('balance_add').addEventListener('click',function(){
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; 
  document.getElementById('add_balance').style.display="flex"
  document.documentElement.style.overflow="hidden"
},false)
document.getElementById('add_balance').addEventListener('click',function(){
    var isClickInsideElement = document.getElementById('balance_cont').contains(event.target);
    if (!isClickInsideElement) {
        document.getElementById('add_balance').style.display="none"
        document.documentElement.style.overflow="scroll"
    }    })

    // function balance() {
    //     document.getElementById('add_balance').style.display="flex";
    //     document.documentElement.style.overflow="hidden"

    // }

