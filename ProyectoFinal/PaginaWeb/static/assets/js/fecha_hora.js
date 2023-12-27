document.addEventListener('DOMContentLoaded', function() {
    // Función para obtener la fecha y hora actual y actualizar el contenido en el footer
    function mostrarFechaHora() {
      var fechaHora = new Date();
      var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: false };
  
      // Formatea la fecha y hora
      var fechaHoraFormateada = fechaHora.toLocaleDateString('es-ES', options);
  
      // Muestra la fecha y hora en el elemento con el id "fecha-hora"
      document.getElementById("fecha-hora").innerHTML =fechaHoraFormateada;
    }
  
    // Llama a la función cuando la página se carga y cada 1 minuto (60,000 milisegundos)
    mostrarFechaHora();
    setInterval(mostrarFechaHora, 60000);
  });
  