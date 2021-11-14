gsap.to("#header", {
  scrollTrigger: {
  trigger: "#big_cont",
  start: "90% 100%", 
  end: "+=500",
scrub:true} ,background:'white'

});
document.getElementById('signup').addEventListener('click',function(){
  document.getElementById('login_page').style.display="none"
  document.getElementById('signup_page').style.display="flex"
  document.documentElement.style.overflow="hidden"
})

document.getElementById('signin').addEventListener('click',function(){
  document.getElementById('signup_page').style.display="none"
  document.getElementById('login_page').style.display="flex"
  document.documentElement.style.overflow="hidden"
})
document.getElementById('signup_page').addEventListener('click',function(){
  var isClickInsideElement = document.getElementById('signup_cont').contains(event.target);
  if (!isClickInsideElement) {
      document.getElementById('signup_page').style.display="none"
      document.documentElement.style.overflow="scroll"
  }
})
document.getElementById('login_page').addEventListener('click',function(){
  var isClickInsideElement = document.getElementById('login_cont').contains(event.target);
  if (!isClickInsideElement) {
      document.getElementById('login_page').style.display="none"
      document.documentElement.style.overflow="scroll"
  }    })

