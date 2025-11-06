(function () {
  if (window.__siteNavInitialized) {
    return;
  }
  window.__siteNavInitialized = true;

  function getAppStoreLink() {
    const userAgent = navigator.userAgent || navigator.vendor || window.opera;

    if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
      return 'https://apps.apple.com/app/id6751612917';
    }

    if (/android/i.test(userAgent)) {
      return 'https://play.google.com/store/apps/details?id=com.pottypalai.app';
    }

    if (/windows phone/i.test(userAgent)) {
      return 'https://play.google.com/store/apps/details?id=com.pottypalai.app';
    }

    return 'both';
  }

  function handleDownloadClick(event) {
    event.preventDefault();
    const storeLink = getAppStoreLink();

    if (storeLink === 'both') {
      window.open('https://play.google.com/store/apps/details?id=com.pottypalai.app', '_blank', 'noopener');
    } else {
      window.open(storeLink, '_blank', 'noopener');
    }
  }

  function closeMobileMenu(menu, trigger) {
    if (!menu) return;
    menu.classList.remove('active');
    if (trigger) {
      trigger.classList.remove('active');
    }
    document.body.style.overflow = '';
  }

  document.addEventListener('DOMContentLoaded', function () {
    const downloadLinks = document.querySelectorAll('.download-link');
    downloadLinks.forEach(link => {
      link.addEventListener('click', handleDownloadClick);
    });

    const hamburgerMenu = document.getElementById('hamburgerMenu');
    const mobileMenu = document.getElementById('mobileMenu');

    if (hamburgerMenu && mobileMenu) {
      hamburgerMenu.addEventListener('click', () => {
        const isActive = hamburgerMenu.classList.toggle('active');
        mobileMenu.classList.toggle('active', isActive);
        document.body.style.overflow = isActive ? 'hidden' : '';
      });

      const menuLinks = mobileMenu.querySelectorAll('a');
      menuLinks.forEach(link => {
        link.addEventListener('click', () => closeMobileMenu(mobileMenu, hamburgerMenu));
      });

      mobileMenu.addEventListener('click', (event) => {
        if (event.target === mobileMenu) {
          closeMobileMenu(mobileMenu, hamburgerMenu);
        }
      });

      document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && mobileMenu.classList.contains('active')) {
          closeMobileMenu(mobileMenu, hamburgerMenu);
        }
      });
    }
  });
})();
