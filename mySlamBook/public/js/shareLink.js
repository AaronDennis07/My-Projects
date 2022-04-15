const whatsAppIcon = document.getElementById('whatsAppIcon')
const copyLinkIcon = document.getElementById('copyLinkIcon')


function copyLink() {

   // navigator.clipboard.writeText(shareLink);
  
navigator.clipboard.writeText(shareLink).then(() => {
  alert("successfully copied");
})
.catch(() => {
  alert("something went wrong");
});
    //alert("Copied the text: " + shareLink);
  }
  
function whatsApp() {

        window.open( "whatsapp://send?text=" +shareLink);   
    }   
    whatsAppIcon.addEventListener('click',whatsApp)
    copyLinkIcon.addEventListener('click',copyLink)
