// Agregar SweetAlert2 para el botón de eliminación
const btnEliminacion = document.querySelectorAll('.btnEliminacion');
btnEliminacion.forEach((btn) => {
    btn.addEventListener('click', (event) => {
        event.preventDefault();
        Swal.fire({
            title: '¿Estás seguro?',
            text: 'Esta acción no se puede deshacer',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = btn.getAttribute('href');
            }
        });
    });
});