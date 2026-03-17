const menu = document.getElementById('menu-burger');
const navigation = document.getElementById('navigation');

// Toggle the burger menu
if(menu){
    menu.addEventListener('click', () => {
        menu.classList.toggle('bx-x');
        navigation.classList.toggle('active');
    });
}

// Close navbar when a link is clicked
const navLinks = document.querySelectorAll('#navigation a');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        menu.classList.remove('bx-x');
        navigation.classList.remove('active');
    });
});

// Exemple : alerte quand le site est chargé
window.addEventListener('DOMContentLoaded', (event) => {
    console.log('SUNU HABITAT prêt !');
});

const userToggle = document.getElementById("user-toggle");
const dropdown = document.getElementById("dropdown");

if(userToggle){
    userToggle.onclick = () => {
        dropdown.classList.toggle("active");
    };
}

// fermer si on clique ailleurs
window.addEventListener("click", function(e){
    if(!userToggle.contains(e.target)){
        dropdown.classList.remove("active");
    }
});

const menuDashboard = document.getElementById('menu-dashboard');
const sidebar = document.getElementById('sidebar');

if(menuDashboard && sidebar){
    menuDashboard.addEventListener('click', () => {
        menuDashboard.classList.toggle('bx-x');
        sidebar.classList.toggle('active');
    });
}

// fermer sidebar après clic lien
const navLink = document.querySelectorAll('#sidebar a');

navLink.forEach(link => {
    link.addEventListener('click', () => {
        sidebar.classList.remove('active');
        menuDashboard.classList.remove('bx-x');
    });
});