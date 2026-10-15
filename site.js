(function(){
  var bar=document.getElementById("progress");
  if(bar && document.querySelector(".post")){
    var tick=function(){var h=document.documentElement;var m=h.scrollHeight-h.clientHeight;bar.style.width=(m>0?(h.scrollTop/m)*100:0)+"%";};
    window.addEventListener("scroll",tick,{passive:true});tick();
  }
  var pills=document.querySelectorAll(".pill");
  pills.forEach(function(b){b.addEventListener("click",function(){
    pills.forEach(function(x){x.classList.remove("on")});b.classList.add("on");
    var f=b.getAttribute("data-f");
    document.querySelectorAll("#grid .card").forEach(function(c){c.hidden=(f!=="all"&&c.getAttribute("data-cat")!==f);});
  });});
  var links=document.querySelectorAll(".toc a");
  if(links.length && "IntersectionObserver" in window){
    var map={};links.forEach(function(a){map[a.getAttribute("href").slice(1)]=a;});
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(e.isIntersecting){links.forEach(function(a){a.classList.remove("on")});var a=map[e.target.id];if(a)a.classList.add("on");}
    });},{rootMargin:"-20% 0px -70% 0px"});
    document.querySelectorAll(".prose h2").forEach(function(h){io.observe(h)});
  }
})();
