// Función para mostrar una alerta SweetAlert2
function showAlert(message, type) {
    Swal.fire({
        icon: type,
        text: message,
        showConfirmButton: false,
        timer: 3000
    });
}

// Función para enviar el formulario mediante Ajax
function submitForm() {
    const form = document.getElementById('myForm');
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showAlert(data.message, 'success');
                form.reset();
            } else {
                for (const error of data.errors) {
                    showAlert(error, 'error');
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showAlert('Se produjo un error al enviar el formulario, No hay suficiente cantidad del producto', 'error');
        });
}

// Event listener para enviar el formulario al hacer clic en el botón "Guardar"
document.getElementById('saveButton').addEventListener('click', function (e) {
    e.preventDefault();
    submitForm();
});

///
function submitBarcodeForm() {
    const barcodeForm = document.getElementById('barcodeForm');
    const barcodeInput = document.getElementById('buscar').value;

    if (barcodeInput.trim() !== '') {
        fetch(barcodeForm.action + `?codigoBarras=${barcodeInput}`)
            .then(response => response.json())
            .then(data => {
                if (data.success === false) {
                    showAlert(data.message, 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showAlert('Se produjo un error al procesar el código de barras.', 'error');
            });
    }
}

// Event listener para enviar el formulario de código de barras al hacer clic en el botón
document.getElementById('barcodeButton').addEventListener('click', function (e) {
    e.preventDefault();
    submitBarcodeForm();
});