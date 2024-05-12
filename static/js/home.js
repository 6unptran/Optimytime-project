msg_from_bot = "Hello, I am Optimytime. How can I help you today?";
$(function() {
  $("li#f1").click(function() {
    window.location = "http://127.0.0.1:5500/templates/note.html"
  });
  $("li#f2").click(function() {
    window.location = "http://127.0.0.1:5500/templates/login.html"
  });
});
async function fetchapi(userMessage) {
    try {
      const response = await fetch(`/requests_msg?hehe=${userMessage}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });
        const data = await response.json();
        return data.message;
    } catch (error) {
        console.error("Error:", error);
        // Bạn có thể trả về một giá trị mặc định hoặc báo lỗi tại đây
    }
}

async function onsend() {
    const boxChat = document.getElementById("boxchat");
    const message = document.getElementById("message");
    const userMessage = message.value; // Get user's message 
    
    // Only proceed if there's a message
    if (userMessage.trim() !== "") {
      // User HTML (modified for dynamic message)
      const userHTML = `
        <div class="d-flex justify-content-start mb-4">
          <div class="img_cont_msg">
            <img src="../static/image/avt.jpeg" 
            class="rounded-circle user_img_msg">
          </div>
          <div class="msg_cotainer">
            ${await fetchapi(userMessage)} 
            <span class="msg_time"> ${getCurrentTime()} </span> 
          </div>
        </div>
      `;
      // Bot HTML (you'll need logic to generate the bot's response)
      const botHTML = `
        <div class="d-flex justify-content-end mb-4">
          <div class="msg_cotainer_send">
            ${userMessage}
            <span class="msg_time_send"> ${getCurrentTime()} </span>
          </div>
          <div class="img_cont_msg">
            <img src="../static/image/avtuser.png" class="rounded-circle user_img_msg"> 
          </div>
        </div>
      `;
  
      // Create elements & append

  
      const newBotChat = document.createElement("div");
      newBotChat.innerHTML = botHTML;
      boxChat.appendChild(newBotChat);

      const newUserChat = document.createElement("div");
      newUserChat.innerHTML = userHTML;
      boxChat.appendChild(newUserChat);
  
      message.value = ""; // Clear input field
      boxChat.scrollTop = boxChat.scrollHeight; // Scroll to the bottom of the chat
    } 
  }
  
  // Helper for getting the current time
  function getCurrentTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes} AM, Today`; 
  } 
  