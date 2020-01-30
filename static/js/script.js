var clients = {{ clients_as_json }}

window.addEventListener("DOMContentLoaded", (event) => {

    select_client = document.getElementById('sélection-client');
    adresse = document.getElementById('adresse');

    select_client.addEventListener('change', afficherAdresse);

});


function afficherAdresse() {
    console.log("changed");
    for(var i = 0; i < clients.length; i++) {
      if(clients[i].id == select_client.value) {
          adresse.innerHTML = "{{ clients[i].city }}"
      }
    }
}
