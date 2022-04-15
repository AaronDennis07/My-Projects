const btns = document.querySelectorAll('.btn')
const divs = document.querySelectorAll('.divs')
const form = document.querySelector('form')
const div2 = document.getElementById('div2')
const div1 = document.getElementById('div1')
const div3 = document.getElementById('div3')
const backBtns = document.querySelectorAll('.backBtns')



btns.forEach((btn,i)=>{
   
    btn.addEventListener("click",(e)=>{
        if(i===9){
            btns[10].disabled = false
        }
        
        
        divs[i].classList.add('hide')
        if(i<btns.length-1){
        divs[i+1].classList.remove('hide')
    }
    })
})


backBtns.forEach((btn,i)=>{
   
    btn.addEventListener("click",(e)=>{
        divs[i].classList.remove('hide')
        if(i<btns.length-1){
        divs[i+1].classList.add('hide')
    }
    })
})




// navigationButtons.forEach((btn,i)=>{
//     btn.addEventListener('click',()=>{
//         if(i===0){
//             div2.hidden = true;
//             div1.hidden = false;
//             div3.hidden = true;
//             console.log(1)
//         }
//         else if(i===1){
//             div2.hidden = false;
//             div1.hidden = true;
//             div3.hidden = true;
//             console.log(2)
//         }
//         else if(i===2){
//             div2.hidden = true;
//             div1.hidden = true;
//             div3.hidden = false;
//             console.log(3)
//         }
//     })
// })

// second.addEventListener('click',(evt)=>{
//     div2.hidden = false;
//     div1.hidden = true;
//     div3.hidden = true;
// })
// first.addEventListener('click',(evt)=>{
//     div2.hidden = true;
//     div1.hidden = false;
//     div3.hidden = true;
// })
// third.addEventListener('click',(evt)=>{
//     div2.hidden = true;
//     div1.hidden = true;
//     div3.hidden = false;
// })
