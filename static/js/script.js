console.log("ejpaezi")

window.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM entièrement chargé et analysé");


    select_client = document.getElementById('sélection-client')
    adresse = document.getElementById('adresse')

    select_client.addEventListener('onchange',afficherAdresse(select_client, adresse ));

  });


function afficherAdresse(select_client, adresse ) {
  adresse.innerHTML = select_client.value
}
