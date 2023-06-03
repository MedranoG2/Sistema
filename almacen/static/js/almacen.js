$(document).ready(function () {
    $('#id_Fksku').change(function () {
        var valorSeleccionado = $(this).val();
        $('#id_nombreFksu').val(valorSeleccionado);
    });
});
