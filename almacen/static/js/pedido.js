$(document).ready(function () {
    $('#id_nombreProductoB').change(function () {
        var valorSeleccionado = $(this).val();
        $('#id_Fksku').val(valorSeleccionado);
    });
});
