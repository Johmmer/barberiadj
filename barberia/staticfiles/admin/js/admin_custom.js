document.addEventListener('DOMContentLoaded', function() {
    // Encuentra todos los campos de filtro
    const filterInputs = document.querySelectorAll('input[name="cliente"]');
    
    // Aplica el placeholder a cada campo encontrado
    filterInputs.forEach(input => {
        input.placeholder = 'Buscar por nombre o apellido...';
        input.style.minWidth = '200px';
    });
    
    // Opcional: Añade estilos CSS para mejorar la apariencia
    const style = document.createElement('style');
    style.textContent = `
        input[name="cliente"] {
            padding: 6px 10px;
            border-radius: 4px;
            border: 1px solid #ddd;
            margin-left: 10px;
        }
        input[name="cliente"]:focus {
            outline: none;
            border-color: #447e9b;
            box-shadow: 0 0 0 2px rgba(70, 130, 180, 0.2);
        }
    `;
    document.head.appendChild(style);
});
