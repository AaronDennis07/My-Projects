
const navigationButtons = document.querySelectorAll('.navigator')


navigationButtons.forEach((btn,i)=>{
    btn.addEventListener('click',()=>{
        if(i===0){
            div2.hidden = true;
            div1.hidden = false;
            div3.hidden = true;
            console.log(1)
        }
        else if(i===1){
            div2.hidden = false;
            div1.hidden = true;
            div3.hidden = true;
            console.log(2)
        }
        else if(i===2){
            div2.hidden = true;
            div1.hidden = true;
            div3.hidden = false;
            console.log(3)
        }
    })
})