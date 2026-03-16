const menu = document.getElementById('menu-burger');
const navigation = document.getElementById('navigation');

// Toggle the burger menu
menu.addEventListener('click', () => {
    menu.classList.toggle('bx-x');
    navigation.classList.toggle('active');
});

// Close navbar when a link is clicked
const navLinks = document.querySelectorAll('#navigation a'); // Sélectionner tous les liens dans la navbar

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        menu.classList.remove('bx-x'); // Revenir à l'état initial du menu burger
        navigation.classList.remove('active'); // Fermer la navbar
    });
});

// script.js

// Exemple : alerte quand le site est chargé
window.addEventListener('DOMContentLoaded', (event) => {
    console.log('SUNU HABITAT prêt !');
});

// Exemple : scroll vers une section avec smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href'))
                .scrollIntoView({ behavior: 'smooth' });
    });
});

let menuDashboard = document.querySelector("#menu-dashboard")
let sidebar = document.querySelector(".sidebar")

menuDashboard.onclick = () => {
sidebar.classList.toggle("active")
}