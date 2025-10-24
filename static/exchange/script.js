
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

    // Logic for modal in divisa_list.html
    const modal = document.getElementById('divisa-modal');
    if (modal) {
        const openModalBtn = document.getElementById('open-modal-btn');
        const closeModalBtn = document.querySelector('.close-btn');
        const divisaForm = document.getElementById('divisa-form');
        const modalTitle = document.getElementById('modal-title');
        const editBtns = document.querySelectorAll('.edit-btn');

        const formActionCreate = divisaForm.action;

        // Open modal for creating
        openModalBtn.addEventListener('click', () => {
            modal.style.display = 'block';
            modalTitle.innerText = 'Crear Divisa';
            divisaForm.action = formActionCreate;
            divisaForm.reset();
            document.getElementById('id_nombre').value = '';
            document.getElementById('id_compra').value = '';
            document.getElementById('id_venta').value = '';
            document.getElementById('id_bandera').value = '';
        });

        // Open modal for editing
        editBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                modal.style.display = 'block';
                modalTitle.innerText = 'Editar Divisa';
                
                const pk = btn.dataset.pk;
                const formActionEdit = `/divisa/${pk}/edit/`;
                divisaForm.action = formActionEdit;

                document.getElementById('id_nombre').value = btn.dataset.nombre;
                document.getElementById('id_compra').value = btn.dataset.compra;
                document.getElementById('id_venta').value = btn.dataset.venta;
                document.getElementById('id_bandera').value = btn.dataset.bandera;
            });
        });

        // Close modal
        closeModalBtn.addEventListener('click', () => {
            modal.style.display = 'none';
        });

        window.addEventListener('click', (e) => {
            if (e.target == modal) {
                modal.style.display = 'none';
            }
        });
    }
});
