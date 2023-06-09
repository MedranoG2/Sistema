input -with-image {
    position: relative;
}

input -with-image input {
    padding - left: 30px; /* Espacio para la imagen */
}

input -with-image:before {
    content: "";
    background - image: url("{% static 'path/to/image.png' %}");
    background - repeat: no - repeat;
    background - position: left center;
    position: absolute;
    left: 5px; /* Posición izquierda de la imagen */
    top: 50 %; /* Centrar verticalmente */
    transform: translateY(-50 %);
    width: 20px; /* Ancho de la imagen */
    height: 20px; /* Altura de la imagen */
}