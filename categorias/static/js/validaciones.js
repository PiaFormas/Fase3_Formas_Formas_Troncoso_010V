<script>
		
	function validarFormulario(){

		var txtNombre = document.getElementById('nombre').value;
		var txtApellido = document.getElementById('apellido').value;
		var txtDireccion = document.getElementById('direccion').value;
		var txtComuna = document.getElementById('comuna').value;
		var txtCorreo = document.getElementById('correo').value;
		var txtUsuario = document.getElementById('usuario').value;
		
	

		//Test campo obligatorio
		if(txtNombre == null || txtNombre.length == 0 || /^\s+$/.test(txtNombre)){
			alert('ERROR: El campo nombre no debe ir vacío o lleno de solamente espacios en blanco');
			document.datos.nombre.focus();
			return false;
		}

		
		if(txtApellido == null || txtApellido.length == 0){
			alert('ERROR: Debe ingresar un apellido');
			document.datos.apellido.focus();
			return false;
		}

		//Test correo
		if(!(/\S+@\S+\.\S+/.test(txtCorreo))){
			alert('ERROR: Debe escribir un correo válido');
			document.datos.correo.value="";
			document.datos.correo.focus();
			return false;
		}

		
	
	
		return true;
	}

	</script>