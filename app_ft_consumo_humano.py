import streamlit as st

st.set_page_config(page_title="Generador Ficha Técnica - Consumo Humano", layout="wide")

st.title("Generador de Fichas Técnicas - Consumo Humano")

# 1. Subida de PDF (todavía sin procesado automático)
pdf_file = st.file_uploader("Sube la ficha técnica del proveedor (PDF)", type="pdf")

# 2. Formulario editable con los campos principales
st.header("Datos principales")
col1, col2 = st.columns(2)
with col1:
    producto = st.text_input("Producto", "Recorte de salmón ahumado congelado")
    referencia = st.text_input("Referencia", "1328-N v4")
    empresa = st.text_input("Empresa", "MACFONT, S.A.")
    peso = st.text_input("Peso del envase", "1 kg")
    zona_fao = st.text_input("Zona FAO", "27")
    metodo_pesca = st.text_input("Método de pesca", "De granja en Noruega")
with col2:
    ingredientes = st.text_area("Ingredientes", "Salmón, sal y regulador de la acidez: lactato de sodio")
    nombre_cientifico = st.text_input("Nombre científico", "Salmo salar")
    contacto = st.text_area("Contacto", "C/Manel Quer, 5-7, Entlo. 2B, 17002 GIRONA (Spain)")

st.header("Descripción y Normativa")
descripcion = st.text_area("Descripción del producto", "Producto elaborado con pescado congelado y una vez descongelado. Uso previsto: como ingrediente para producto industria-alimentario.")
normativa = st.text_area("Normativa general aplicable", """Reglamento (CE) 852/2004 – Higiene
Reglamento (UE) 1169/2011 – Información alimentaria
Reglamento (CE) 178/2002 – APPCC
Reglamento (CE) 2073/2005 – Criterios microbiológicos
Reglamento (CE) 1881/2006 – Contaminantes
Reglamento (CE) 1829/2003 y 1830/2003 – OGM""")

st.header("Características y Aspectos")
col3, col4 = st.columns(2)
with col3:
    color = st.text_input("Color", "Naranja-rojo-marrón")
    textura = st.text_input("Textura", "Típica")
    aspecto = st.text_input("Aspecto", "Recortes irregulares")
    humedad = st.text_input("Humedad (%)", "2.3-3.5")
    cuerpos_extranos = st.text_input("Cuerpos extraños", "No inherentes - ausencia")
with col4:
    plomo = st.text_input("Plomo (mg/kg)", "0.30")
    mercurio = st.text_input("Mercurio (mg/kg)", "0.30")
    PCB = st.text_input("PCB (ng/g)", "75")
    dioxinas = st.text_input("Dioxinas (pg/g)", "3.5")
    dioxinas_similares = st.text_input("Dioxinas similares (pg/g)", "8.5")
    listeria = st.text_input("Listeria monocytogenes (ufc/g)", "100")

st.header("Conservación y Presentación")
conservacion = st.text_input("Conservación", "<-18ºC")
caducidad = st.text_input("Caducidad (meses)", "18")
formato = st.text_area("Formato de presentación", "Caja de 10 kg (10x1kg), palet de 50 cajas = 500 kg. Producto envasado al vacío.")

st.header("Otros")
irradiacion = st.text_input("Irradiación", "Producto libre de irradiación")
ogm = st.text_input("OGM", "Libre de OGM")

st.header("Alergenos principales")
pescado = st.checkbox("Pescado y derivados", value=True)
lactato = st.checkbox("Lactato de sodio", value=True)

# Puedes añadir más alérgenos aquí

if st.button("Generar ficha técnica final"):
    st.success("⚙️ Generar PDF corporativo (funcionalidad futura)")
    st.info("Todos los datos pueden editarse y se guardarán para la generación final.")

st.caption("Prototipo inicial. Personaliza los campos según tu producto.")