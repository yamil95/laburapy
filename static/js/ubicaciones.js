async function updateLocalidadOptions(provinciaSelect) {
    try {
      const provinciaId = provinciaSelect.value;
      const localidadSelect = document.getElementById('id_localidad');
  
      if (provinciaId) {
        const response = await fetch(`/get-localidades/${provinciaId}`);
        const data = await response.json(); 
  
        // Limpia las opciones actuales del campo localidad
        localidadSelect.options.length = 1;
  
        // Agrega las nuevas opciones de localidad
        data.forEach(localidad => {
          const option = document.createElement('option');
          option.value = localidad.id;
          option.text = localidad.nombre;
          localidadSelect.add(option);
        });
  
        // Habilita y marca como requerido el campo localidad
        localidadSelect.disabled = false;
        localidadSelect.required = true;
      } else {
        // Deshabilita y marca como no requerido el campo localidad
        localidadSelect.disabled = true;
        localidadSelect.required = false;
      }
    } catch (error) {
      console.error('Error al obtener las localidades:', error);
    }
  }
  
  // Agrega el event listener al campo provincia
  document.getElementById('id_provincia').addEventListener('change', function() {
    updateLocalidadOptions(this);
  });