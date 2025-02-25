document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById("grafica").getContext("2d");

    // Datos de prueba (puedes cargarlos desde un archivo JSON)
    const datos = {
        labels: ["Camarón", "Tilapia", "Atún", "Mojarra", "Trucha"],
        datasets: [{
            label: "Producción (toneladas)",
            data: [500, 300, 800, 450, 250], // Datos ficticios
            backgroundColor: ["#ff6384", "#36a2eb", "#ffce56", "#4bc0c0", "#9966ff"],
            borderColor: "#000",
            borderWidth: 1
        }]
    };

    new Chart(ctx, {
        type: "bar",  // Tipo de gráfico
        data: datos,
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
});
