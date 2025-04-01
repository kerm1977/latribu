function timePicker(id){
   var input = document.getElementById(id);
   var timePicker = document.createElement('div');
   timePicker.classList.add('time-picker');
   input.value = '00:00';
  
   //open timepicker
   input.onclick= function(){
      timePicker.classList.toggle('open');
      
      this.setAttribute('disabled','disabled');
      timePicker.innerHTML +=`
      <div class="set-time mt-3">


         <label>Selecciona la Hora</label>       
         <div class="label mt-2">
      
            <a id="plusH" class="plusH button is-success"> + </a>

            <input class="input set" type="text" id="hour" value="00" style="width: 150px ">
            
            <a id="minusH" class="minusH button is-danger"> - </a>
         </div>

         <label>Seleccione los Minutos</label>           
         <div class="label">
            <a id="plusM" class="plusH button is-success"> + </a>

            <input class="input set" type="text" id="minute" value="00" style="width: 150px">
            
            <a id="minusM" class="minusM button is-danger"> - </a>
         </div>

      </div>
      <div id="submitTime" class="mt-4 plusH button is-info"> Seleccionar la Hora </div>`;
      this.after(timePicker);
      var plusH = document.getElementById('plusH');
      var minusH = document.getElementById('minusH');
      var plusM = document.getElementById('plusM');
      var minusM = document.getElementById('minusM');
      var h = parseInt(document.getElementById('hour').value);
      var m = parseInt(document.getElementById('minute').value);
     //increment hour
      plusH.onclick = function(){
         h = isNaN(h) ? 0 : h;
         if(h===23){
            h =-1;
         }
          h++; 
         document.getElementById('hour').value = (h<10?'0':0)+h;
      }
      //decrement hour
      minusH.onclick = function(){
         h = isNaN(h) ? 0 : h;
         if(h===0){
            h =24;
         }
         h--;
         document.getElementById('hour').value = (h<10?'0':0)+h;
      }
      //increment hour
      plusM.onclick = function(){
         m = isNaN(m) ? 0 : m;
         if(m===45){
            m =-15; 
         }
          m = m+15; 
         document.getElementById('minute').value = (m<10?'0':0)+m;
      }
      //decrement hour
      minusM.onclick = function(){
        m = isNaN(m) ? 0 : m;
         if(m===0){
            m =60;
         }
         m = m-15;
         document.getElementById('minute').value = (m<10?'0':0)+m;
      }
      
      //submit timepicker
      var submit = document.getElementById("submitTime");
      submit.onclick = function(){
        input.value = document.getElementById('hour').value+':'+document.getElementById('minute').value;
         input.removeAttribute('disabled');
         timePicker.classList.toggle('open');
         timePicker.innerHTML = '';
      }
   }
}

timePicker('timePicker');