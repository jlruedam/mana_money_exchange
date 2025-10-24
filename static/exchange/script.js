
const observerOptions = {
    threshold: 0.1, 
    rootMargin: '0px 0px -50px 0px' //
};


const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            
        }
    });
}, observerOptions);


function initScrollAnimations() {
    const animatedElements = document.querySelectorAll(
        '.second-section, .calculator, .we-info, .third-section, .benefit-info, .fourth-section, .office-container, .semi-footer'
    );
    
    animatedElements.forEach(element => {
        observer.observe(element);
    });
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollAnimations);
} else {
    initScrollAnimations();
}

// Cerrar el menú móvil cuando se hace clic en un enlace
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle');
    const navLinks = document.querySelectorAll('.nav-menu a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (menuToggle && menuToggle.checked) {
                menuToggle.checked = false;
            }
        });
    });
});
