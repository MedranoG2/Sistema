<script>
    document.addEventListener("DOMContentLoaded", function () {
        var input = document.getElementById("buscar");
    input.addEventListener("input", function () {
            var filter = input.value.toLowerCase();
    var rows = document.querySelectorAll("tbody tr");
    rows.forEach(function (row) {
                var nombre = row.querySelector("td:nth-child(3)").textContent.toLowerCase();
    if (nombre.includes(filter)) {
        row.style.display = "";
                } else {
        row.style.display = "none";
                }
            });
        });
    });
</script>