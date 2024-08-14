// alert("Hello! I am an alert box!!");

document.addEventListener("keyup", e=>{
  if (e.target.matches("#buscador")){
      if (e.key ==="Escape")e.target.value = ""
      document.querySelectorAll(".search_article").forEach(fruta =>{
          fruta.textContent.toLowerCase().includes(e.target.value.toLowerCase())
            ?fruta.classList.remove("filtro")
            :fruta.classList.add("filtro")
      })
  }
})


  // e.target.matches("#buscador")
  // console.log(e.target.value)
