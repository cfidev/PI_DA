
# Proyecto: Análisis de Telecomunicaciones en Argentina

## Descripción del Proyecto

Este proyecto se enfoca en el análisis del sector de las telecomunicaciones en Argentina, con un énfasis especial en la penetración de internet en las diferentes provincias del país y la calidad del servicio. La principal actividad analizada es el acceso a internet, comparando la adopción de diferentes tecnologías de conexión y las diferencias entre zonas rurales y urbanizadas. Se busca identificar patrones, correlaciones y oportunidades de mejora para cerrar la brecha digital entre las diferentes regiones del país.

## Objetivos

- **Analizar la penetración de internet** en la población y los hogares por provincia.
- **Comparar la calidad del servicio** de internet, evaluando las velocidades de conexión disponibles en distintas regiones.
- **Identificar tendencias tecnológicas** en el acceso a internet (Fibra Óptica, ADSL, Wireless, etc.) y su evolución a lo largo del tiempo.
- **Proponer recomendaciones** para mejorar la infraestructura en las zonas rurales y cerrar la brecha digital.

## Estructura del Proyecto

El proyecto está dividido en varias secciones interactivas desarrolladas con **Streamlit**. Estas secciones permiten a los usuarios explorar los datos, realizar comparaciones y obtener conclusiones basadas en los gráficos presentados.

### Secciones

1. **Introducción**:
   - Presenta el contexto del análisis, resaltando la importancia de las telecomunicaciones en Argentina. 
   - Incluye un gráfico interactivo que muestra la penetración de internet en las provincias, diferenciando entre zonas rurales y urbanizadas.

2. **Accesos a Internet por Tecnología**:
   - Muestra la evolución de las principales tecnologías de acceso a internet en Argentina a lo largo del tiempo.
   - Las tecnologías analizadas incluyen Fibra Óptica, Cablemodem, ADSL y Wireless.
   - Se hace especial énfasis en la persistencia del ADSL en áreas rurales y el crecimiento de la Fibra Óptica en áreas urbanizadas.

3. **Penetración del Servicio de Internet**:
   - Compara la penetración de internet en la población y en los hogares por provincia.
   - Los usuarios pueden seleccionar provincias específicas o ver un análisis general de todas las provincias.
   - Se puede filtrar por tipo de provincia (rural o urbanizada), permitiendo identificar diferencias significativas en la penetración de internet.

4. **Calidad del Servicio**:
   - Analiza las velocidades de conexión en cada provincia, permitiendo comparar la calidad del servicio entre zonas rurales y urbanizadas.
   - Los gráficos muestran la distribución de accesos a diferentes velocidades, desde conexiones lentas (hasta 512 kbps) hasta conexiones rápidas (más de 30 Mbps).

5. **Conclusiones y Recomendaciones**:
   - Resume los hallazgos clave del análisis, destacando las provincias con mayor y menor penetración de internet, así como las diferencias en la calidad del servicio entre zonas rurales y urbanizadas.
   - Proporciona recomendaciones específicas para mejorar la infraestructura, incluyendo la expansión de la fibra óptica en zonas urbanizadas y el uso de tecnologías wireless en zonas rurales.

## Uso del Proyecto

### Requisitos

- **Python 3.8+**
- **Streamlit**
- **Pandas**
- **Plotly**

Instala las dependencias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Ejecutar la aplicación

Una vez instaladas las dependencias, puedes ejecutar la aplicación Streamlit con el siguiente comando:

```bash
streamlit run app.py
```

Esto abrirá una ventana del navegador donde podrás interactuar con las diferentes secciones del análisis.

### Estructura de Archivos

```bash
PI_DA/
│
├── data/
│   └── Internet_limpio.xlsx  # Base de datos limpia utilizada para el análisis
│
├── notebooks/
│   └── eda.ipynb             # Análisis Exploratorio de Datos (EDA) realizado
│
├── app.py                    # Aplicación principal desarrollada con Streamlit
│
├── requirements.txt          # Lista de dependencias del proyecto
│
└── README.md                 # Este archivo README
```

## Recomendaciones Futuros Análisis

- **Inversión en infraestructura rural**: Las zonas rurales pueden beneficiarse de tecnologías wireless (como LTE avanzado o 5G) debido a los costos más bajos y la facilidad de despliegue. La fibra óptica sigue siendo la mejor opción para áreas urbanizadas con alta densidad de población.
- **Mejora de la velocidad de conexión**: Las provincias que aún dependen de ADSL deberían planear un cambio progresivo hacia tecnologías más modernas, como la fibra óptica y el cablemodem.
- **Cerrar la brecha digital**: Se recomienda priorizar las áreas rurales con baja penetración y bajas velocidades de conexión para asegurar que más personas tengan acceso a internet de alta calidad.

## Licencia

Este proyecto se encuentra bajo la Licencia MIT.
