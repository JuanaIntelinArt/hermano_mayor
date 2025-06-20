🧒 Big Brother System
Big Brother System es una aplicación en Python que simula el registro y la gestión de un programa de acompañamiento para niños por parte de "hermanos mayores". Permite registrar participantes, crear grupos, tomar asistencia y generar reportes.

📁 Estructura del Proyecto
graphql
Copy
Edit
big_brother_system/
│
├── big_brother.py          # Lógica principal del sistema (clase BigBrotherSystem)
├── interface.py            # Interfaz de texto (menú interactivo)
├── main.py                 # Punto de entrada del programa
├── report_generator.py     # Generador de reportes en texto
└── sample_data.py          # Datos de ejemplo para pruebas
🚀 Cómo usar
css
python main.py
Sigue el menú para ver hermanos, niños, grupos y generar reportes.

🧠 Funcionalidades principales
Registrar hermanos mayores y niños.

Crear grupos con un hermano mayor y varios niños.

Registrar asistencia diaria y incidentes.

Generar reportes de grupo en base a un rango de fechas.

📌 Ejemplo de Menú
pgsql
Big Brother System
1. View big brothers
2. View registered children
3. View groups
4. Generate group report
5. Exit
📄 Ejemplo de Reporte
yaml

GROUP 1 REPORT
Period: 2025-06-01 to 2025-06-20
----------------------------------
Total days: 20
Days with records: 5

ATTENDANCE:
- Luis Rodriguez: 5 of 5 days
- Ana Martinez: 4 of 5 days

INCIDENTS:
- Carlos was absent due to illness (2025-06-19)
📚 Requisitos
Python 3.7 o superior

No requiere librerías externas

🔧 Mejoras futuras (opcional)
Interfaz gráfica

Persistencia en base de datos o archivos

Exportación de reportes a PDF o CSV

