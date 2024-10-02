import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
file_path = 'data/Internet_limpio.xlsx'
data_tecnologia = pd.read_excel(file_path, sheet_name='Totales Accesos Por Tecnología')
data_penetracion_poblacion = pd.read_excel(file_path, sheet_name='Penetración-poblacion')
data_penetracion_hogares = pd.read_excel(file_path, sheet_name='Penetracion-hogares')
data_velocidad = pd.read_excel(file_path, sheet_name='Accesos por velocidad')

# Limpiar nombres de columnas eliminando espacios en blanco al principio o final
data_tecnologia.columns = data_tecnologia.columns.str.strip()
data_penetracion_poblacion.columns = data_penetracion_poblacion.columns.str.strip()
data_penetracion_hogares.columns = data_penetracion_hogares.columns.str.strip()
data_velocidad.columns = data_velocidad.columns.str.strip()

# Añadimos una columna ficticia 'Tipo de Provincia' en el dataset para clasificar entre rural y urbanizada
data_penetracion_poblacion['Tipo de Provincia'] = data_penetracion_poblacion['Provincia'].apply(lambda x: 'Rural' if x in ['Formosa', 'La Rioja', 'Catamarca'] else 'Urbanizada')
data_penetracion_hogares['Tipo de Provincia'] = data_penetracion_hogares['Provincia'].apply(lambda x: 'Rural' if x in ['Formosa', 'La Rioja', 'Catamarca'] else 'Urbanizada')
data_velocidad['Tipo de Provincia'] = data_velocidad['Provincia'].apply(lambda x: 'Rural' if x in ['Formosa', 'La Rioja', 'Catamarca'] else 'Urbanizada')

# Crear menú de navegación
st.sidebar.title("Menú de navegación")
page = st.sidebar.selectbox("Selecciona una página", ["Introducción", "Accesos a Internet por Tecnología", "Penetración del Servicio de Internet", "Calidad del Servicio", "Conclusiones"])

# Página de introducción
if page == "Introducción":
    st.title("Telecomunicaciones en Argentina")
    st.header("Introducción")
    st.write("""
    Este análisis explora el estado actual de las telecomunicaciones en Argentina, enfocándose en la penetración de internet y la calidad del servicio en provincias rurales y urbanizadas.
    """)

    # Filtro por tipo de provincia en la introducción
    tipo_provincia = st.sidebar.selectbox("Selecciona el tipo de provincia", ['Todas', 'Rural', 'Urbanizada'])

    # Mostrar información sobre cómo se clasifican las provincias
    st.info("Las provincias han sido clasificadas como 'Rural' o 'Urbanizada' según criterios de densidad de población y desarrollo tecnológico. Formosa, La Rioja y Catamarca han sido clasificadas como rurales para este análisis.")

    if tipo_provincia != 'Todas':
        data_intro = data_penetracion_poblacion[data_penetracion_poblacion['Tipo de Provincia'] == tipo_provincia]
    else:
        data_intro = data_penetracion_poblacion

    # Gráfico comparativo de penetración por provincias
    fig_intro = px.bar(data_intro, x='Provincia', y='Accesos por cada 100 hab', color='Tipo de Provincia',
                       title='Penetración de Internet por Provincia',
                       labels={'Accesos por cada 100 hab': 'Accesos por cada 100 Habitantes'})
    st.plotly_chart(fig_intro)

# Página de Accesos a Internet por Tecnología
elif page == "Accesos a Internet por Tecnología":
    st.title("Accesos a Internet por Tecnología")

    # Gráfico de evolución de accesos por tecnología
    fig_tecnologia = px.line(data_tecnologia, x='Periodo', y=['Fibra óptica', 'Cablemodem', 'ADSL', 'Wireless'],
                             title='Evolución de Accesos por Tecnología',
                             labels={'value': 'Número de Accesos', 'Periodo': 'Trimestre'})
    st.plotly_chart(fig_tecnologia)

    # Explicación de los KPIs con tooltip
    st.info("Este gráfico muestra la evolución de las principales tecnologías de acceso a internet. A pesar del crecimiento de la fibra óptica, el ADSL sigue teniendo una fuerte presencia, especialmente en áreas rurales. Este dato es clave para comprender la persistencia del ADSL frente a tecnologías más avanzadas.")

# Página de Penetración del Servicio de Internet con comparaciones
elif page == "Penetración del Servicio de Internet":
    st.title("Penetración del Servicio de Internet")

    provincias = ['Todas'] + list(data_penetracion_poblacion['Provincia'].unique())
    selected_provinces = st.sidebar.multiselect("Selecciona provincias para comparar", provincias, default='Todas')
    tipo_provincia = st.sidebar.selectbox("Selecciona el tipo de provincia", ['Todas', 'Rural', 'Urbanizada'])

    # Filtrar los datos según el tipo de provincia y la selección de provincias
    if tipo_provincia != 'Todas':
        data_poblacion_filtered = data_penetracion_poblacion[data_penetracion_poblacion['Tipo de Provincia'] == tipo_provincia]
        data_hogares_filtered = data_penetracion_hogares[data_penetracion_hogares['Tipo de Provincia'] == tipo_provincia]
    else:
        data_poblacion_filtered = data_penetracion_poblacion
        data_hogares_filtered = data_penetracion_hogares

    if 'Todas' not in selected_provinces:
        data_poblacion_filtered = data_poblacion_filtered[data_poblacion_filtered['Provincia'].isin(selected_provinces)]
        data_hogares_filtered = data_hogares_filtered[data_hogares_filtered['Provincia'].isin(selected_provinces)]

    # Gráfico comparativo de penetración en población y hogares
    fig_poblacion = px.bar(data_poblacion_filtered, 
                           x='Provincia', y='Accesos por cada 100 hab', color='Tipo de Provincia',
                           title=f'Comparativa de Penetración en la Población',
                           labels={'Accesos por cada 100 hab': 'Accesos por cada 100 Habitantes'})
    st.plotly_chart(fig_poblacion)

    fig_hogares = px.bar(data_hogares_filtered, 
                         x='Provincia', y='Accesos por cada 100 hogares', color='Tipo de Provincia',
                         title=f'Comparativa de Penetración en los Hogares',
                         labels={'Accesos por cada 100 hogares': 'Accesos por cada 100 Hogares'})
    st.plotly_chart(fig_hogares)

# Página de Calidad del Servicio (Velocidades de Conexión)
elif page == "Calidad del Servicio":
    st.title("Calidad del Servicio - Velocidades de Conexión")

    provincias = ['Todas'] + list(data_velocidad['Provincia'].unique())
    selected_provinces = st.sidebar.multiselect("Selecciona provincias para comparar", provincias, default=['Todas'])
    tipo_provincia = st.sidebar.selectbox("Selecciona el tipo de provincia", ['Todas', 'Rural', 'Urbanizada'])

    # Filtrar los datos según el tipo de provincia y la selección de provincias
    if tipo_provincia != 'Todas':
        data_velocidad_filtered = data_velocidad[data_velocidad['Tipo de Provincia'] == tipo_provincia]
    else:
        data_velocidad_filtered = data_velocidad

    if 'Todas' not in selected_provinces:
        data_velocidad_filtered = data_velocidad_filtered[data_velocidad_filtered['Provincia'].isin(selected_provinces)]

    # Gráfico de distribución de velocidades comparando provincias
    fig_velocidad = px.bar(data_velocidad_filtered, x='Provincia', 
                           y=['HASTA 512 kbps', '+ 512 Kbps - 1 Mbps', '+ 1 Mbps - 6 Mbps',
                              '+ 6 Mbps - 10 Mbps', '+ 10 Mbps - 20 Mbps', '+ 20 Mbps - 30 Mbps'],
                           color='Tipo de Provincia',
                           title=f'Comparativa de Velocidades de Conexión entre Provincias',
                           labels={'value': 'Número de Accesos', 'Provincia': 'Provincias'})
    st.plotly_chart(fig_velocidad)

# Página de Conclusiones
elif page == "Conclusiones":
    st.title("Conclusiones y Recomendaciones")

    st.write("**Conclusiones Clave:**")
    st.write("1. **Alta penetración en provincias urbanizadas**: Las provincias urbanizadas como Buenos Aires muestran una mayor penetración en la población y los hogares.")
    st.write("2. **Desafíos en zonas rurales**: Provincias rurales como Formosa y La Rioja enfrentan dificultades para mejorar la infraestructura y la penetración del servicio de internet.")
    st.write("3. **Calidad del servicio**: Las velocidades de conexión son mayores en zonas urbanizadas, mientras que las zonas rurales suelen presentar mayores dependencias de tecnologías más lentas como el ADSL.")

    st.write("4. **Inversión en tecnología wireless** en áreas rurales podría ser más rentable y rápida de implementar que la expansión de la fibra óptica, debido a la baja densidad de población en estas áreas.")
    st.write("5. **Expansión de la infraestructura de fibra óptica** en áreas urbanizadas y suburbanas es crucial para seguir satisfaciendo la demanda de mayores velocidades de conexión.")

    # Gráfico de apoyo en las recomendaciones
    fig_conclusiones = px.bar(data_penetracion_hogares, x='Provincia', y='Accesos por cada 100 hogares',
                              color='Tipo de Provincia',
                              title='Comparativa de Penetración del Internet en los Hogares',
                              labels={'Accesos por cada 100 hogares': 'Accesos por cada 100 Hogares'})
    st.plotly_chart(fig_conclusiones)
