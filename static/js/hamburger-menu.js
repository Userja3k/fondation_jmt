document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('nav-menu');

  // Test rapide pour vérifier l'affichage du menu hamburger
  console.log('Script chargé : hamburger-menu.js');

  // Vérification des éléments
  if (!hamburger || !navMenu) {
    console.error('Les éléments hamburger ou nav-menu sont introuvables.');
  } else {
    console.log('Les éléments hamburger et nav-menu sont présents.');
  }

  if (hamburger && navMenu) {
    // Initially hide nav menu on small screens
    if (window.innerWidth <= 768) {
      navMenu.classList.remove('active');
    }

    // Simplification de la gestion des événements pour le menu hamburger
    hamburger.addEventListener('click', function () {
      const expanded = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', !expanded);
      navMenu.classList.toggle('active');
      hamburger.classList.toggle('active');
    });

    // Test pour vérifier si la classe 'active' est appliquée correctement
    hamburger.addEventListener('click', function () {
      console.log('Classe active sur navMenu:', navMenu.classList.contains('active'));
      console.log('Classe active sur hamburger:', hamburger.classList.contains('active'));
    });

    // Fermer le menu lorsque l'utilisateur clique en dehors
    document.addEventListener('click', function (event) {
      if (!navMenu.contains(event.target) && !hamburger.contains(event.target)) {
        navMenu.classList.remove('active');
        hamburger.setAttribute('aria-expanded', false);
        hamburger.classList.remove('active');
      }
    });
  }

  // Suppression du test temporaire pour forcer l'affichage du menu
  // navMenu.classList.add('active');
  // console.log('Classe active forcée sur navMenu.');
});
