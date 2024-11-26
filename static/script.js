document.getElementById("add-form").addEventListener("submit", function(event) {
    event.preventDefault();
  
    let name = document.getElementById("name").value;
    let age = document.getElementById("age").value;
  
    if (name && age) {
      let dataList = document.getElementById("data-list");
      let itemDiv = document.createElement("div");
  
      itemDiv.innerHTML = `
        <span>${name} - ${age} anos</span>
        <button class="delete-btn">Excluir</button>
      `;
  
      dataList.appendChild(itemDiv);
  
      // Limpar o formulário após adicionar
      document.getElementById("add-form").reset();
    }
  });
  
  document.getElementById("data-list").addEventListener("click", function(event) {
    if (event.target.classList.contains("delete-btn")) {
      event.target.parentElement.remove();
    }
  });
  