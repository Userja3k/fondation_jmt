document.addEventListener('DOMContentLoaded', function() {
    // Theme toggle functionality
    const themeToggle = document.getElementById('theme-toggle');
    const moonIcon = document.getElementById('moon-icon');
    const sunIcon = document.getElementById('sun-icon');
    
    function setTheme(theme) {
        if (theme === 'dark') {
            document.body.classList.add('dark');
            moonIcon.classList.add('hidden');
            sunIcon.classList.remove('hidden');
            localStorage.setItem('jmt_theme', 'dark');
        } else {
            document.body.classList.remove('dark');
            moonIcon.classList.remove('hidden');
            sunIcon.classList.add('hidden');
            localStorage.setItem('jmt_theme', 'light');
        }
    }
    
    // Check user preference
    const storedTheme = localStorage.getItem('jmt_theme') || 'light';
    setTheme(storedTheme);
    
    // Toggle theme on click
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.body.classList.contains('dark') ? 'dark' : 'light';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            setTheme(newTheme);
        });
    }
    
    // Mobile menu toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
    
    // Expanding content
    const expandButtons = document.querySelectorAll('.expand-button');
    
    expandButtons.forEach(button => {
        button.addEventListener('click', function() {
            const target = document.getElementById(this.dataset.target);
            if (target) {
                target.classList.toggle('expanded');
                this.textContent = target.classList.contains('expanded') ? 'Voir moins' : 'Voir plus';
            }
        });
    });
    
    // Carousel functionality
    const carousels = document.querySelectorAll('.carousel');
    
    carousels.forEach(carousel => {
        const carouselItems = carousel.querySelectorAll('.carousel-item');
        const carouselInner = carousel.querySelector('.carousel-inner');
        let currentIndex = 0;
        
        function updateCarousel() {
            const itemWidth = carouselItems[0].offsetWidth;
            carouselInner.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
        }
        
        function nextSlide() {
            const maxIndex = carouselItems.length - getVisibleItems();
            currentIndex = currentIndex >= maxIndex ? 0 : currentIndex + 1;
            updateCarousel();
        }
        
        function prevSlide() {
            const maxIndex = carouselItems.length - getVisibleItems();
            currentIndex = currentIndex <= 0 ? maxIndex : currentIndex - 1;
            updateCarousel();
        }
        
        function getVisibleItems() {
            const width = window.innerWidth;
            if (width < 576) return 1;
            if (width < 992) return 2;
            return 3;
        }
        
        // Auto-slide every 5 seconds
        setInterval(nextSlide, 5000);
        
        // Handle window resize
        window.addEventListener('resize', updateCarousel);
        
        // Initialize
        updateCarousel();
    });
    
    // Video player
    const videoPlayers = document.querySelectorAll('.video-player video');
    
    videoPlayers.forEach(player => {
        player.controls = true;
    });
    
    // Search form
    const searchForm = document.getElementById('search-form');
    
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const searchInput = document.getElementById('search-input');
            if (searchInput.value.trim() === '') {
                e.preventDefault();
                alert('Veuillez entrer un terme de recherche');
            }
        });
    }
});