/* ------------------------------------------------------------------
   Maison Noirmont — Article : enveloppe des tableaux larges.

   Le CSS seul ne peut pas creer de conteneur de defilement autour d'un
   tableau : il faut un element. On le pose ici, et on ne declare le role
   et le libelle QUE si le tableau deborde reellement, afin de ne pas
   ajouter d'arret de tabulation inutile sur grand ecran.
   ------------------------------------------------------------------ */
(function () {
  var LIBELLE = 'Tableau, defilement horizontal';

  function envelopper() {
    var tableaux = document.querySelectorAll('.article-content table');
    for (var i = 0; i < tableaux.length; i++) {
      var t = tableaux[i];
      var p = t.parentNode;
      if (!p) continue;
      if (p.classList && p.classList.contains('nm-table-scroll')) continue;
      var boite = document.createElement('div');
      boite.className = 'nm-table-scroll';
      p.insertBefore(boite, t);
      boite.appendChild(t);
    }
  }

  function jauger() {
    var boites = document.querySelectorAll('.nm-table-scroll');
    for (var i = 0; i < boites.length; i++) {
      var b = boites[i];
      if (b.scrollWidth > b.clientWidth + 1) {
        b.setAttribute('tabindex', '0');
        b.setAttribute('role', 'region');
        b.setAttribute('aria-label', LIBELLE);
      } else {
        b.removeAttribute('tabindex');
        b.removeAttribute('role');
        b.removeAttribute('aria-label');
      }
    }
  }

  function demarrer() {
    envelopper();
    jauger();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', demarrer);
  } else {
    demarrer();
  }

  var minuteur = null;
  window.addEventListener('resize', function () {
    clearTimeout(minuteur);
    minuteur = setTimeout(jauger, 150);
  });
})();
