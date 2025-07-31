import streamlit as st
import fitz  # PyMuPDF
import re

st.set_page_config(page_title="Ficha Técnica Consumo Humano", layout="wide")
st.title("Generador de Fichas Técnicas (Consumo Humano)")

# 1. Subida de PDF
pdf_file = st.file_uploader("Sube la ficha técnica del proveedor (PDF)", type="pdf")

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def regex_search(pattern, text, default=""):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return default

auto_fields = {}
if pdf_file:
    texto = extract_text_from_pdf(pdf_file)
    st.subheader("Texto extraído del PDF")
    st.text_area("Texto extraído", value=texto, height=200)
    
    # Ejemplo de autocompletado de campos con regex
    auto_fields["producto"] = regex_search(r"PRODUCTO\s*:\s*([^\n]+)", texto)
    auto_fields["ref"] = regex_search(r"Ref\s*:\s*([^\n]+)", texto)
    auto_fields["empresa"] = regex_search(r"DIRECCION COMERCIAL\s*([^\n]+)", texto)
    auto_fields["peso"] = regex_search(r"CONGELADO\s*([^\n]+)", texto)
    auto_fields["zona_fao"] = regex_search(r"zona FAO n\.? (\d+)", texto)
    auto_fields["ingredientes"] = regex_search(r"INGREDIENTES\s*([^\n]+)", texto)
    auto_fields["nombre_cientifico"] = regex_search(r"Nombre Cientifico\s*:\s*([^\n]+)", texto)
    auto_fields["metodo_pesca"] = regex_search(r"Metodo Pesca\s*:\s*([^\n]+)", texto)
    auto_fields["color"] = regex_search(r"Color\s*([^\n]+)", texto)
    auto_fields["textura"] = regex_search(r"Textura\s*([^\n]+)", texto)
    auto_fields["aspecto"] = regex_search(r"Aspecto\s*([^\n]+)", texto)
    auto_fields["humedad"] = regex_search(r"Humedad\s*:\s*([^\n]+)", texto)
    auto_fields["plomo"] = regex_search(r"Plomo\s*([^\n]+)", texto)
    auto_fields["mercurio"] = regex_search(r"Mercurio\s*([^\n]+)", texto)
    auto_fields["listeria"] = regex_search(r"Listeria monocytogenes\s*([^\n]+)", texto)
    auto_fields["conservacion"] = regex_search(r"Conservacion\s*:\s*([^\n]+)", texto)
    auto_fields["caducidad"] = regex_search(r"Caducidad\s*:\s*([^\n]+)", texto)
    auto_fields["irradiacion"] = regex_search(r"IRRADIACION\s*([^\n]+)", texto)
    auto_fields["ogm"] = regex_search(r"Producto Libre de OGM", texto, "Libre de OGM")

else:
    texto = ""
    auto_fields = {}

# 2. Formulario editable
st.header("Datos principales")
col1, col2 = st.columns(2)
with col1:
    producto = st.text_input("Producto", auto_fields.get("producto", "Recorte de salmón ahumado congelado"))
    referencia = st.text_input("Referencia", auto_fields.get("ref", "1328-N v4"))
    empresa = st.text_input("Empresa", auto_fields.get("empresa", "MACFONT, S.A."))
    peso = st.text_input("Peso", auto_fields.get("peso", "1 kg"))
    zona_fao = st.text_input("Zona FAO", auto_fields.get("zona_fao", "27"))
    metodo_pesca = st.text_input("Método de pesca", auto_fields.get("metodo_pesca", "De granja en Noruega"))
with col2:
    ingredientes = st.text_area("Ingredientes", auto_fields.get("ingredientes", "Salmón, sal y regulador de la acidez: lactato de sodio"))
    nombre_cientifico = st.text_input("Nombre científico", auto_fields.get("nombre_cientifico", "Salmo salar"))
    color = st.text_input("Color", auto_fields.get("color", "Naranja-rojo-marrón"))
    textura = st.text_input("Textura", auto_fields.get("textura", "Típica"))
    aspecto = st.text_input("Aspecto", auto_fields.get("aspecto", "Recortes irregulares"))

st.header("Aspectos físico-químicos")
col3, col4 = st.columns(2)
with col3:
    humedad = st.text_input("Humedad (%)", auto_fields.get("humedad", "2.3-3.5"))
    plomo = st.text_input("Plomo (mg/kg)", auto_fields.get("plomo", "0.30"))
    mercurio = st.text_input("Mercurio (mg/kg)", auto_fields.get("mercurio", "0.30"))
with col4:
    listeria = st.text_input("Listeria monocytogenes (ufc/g)", auto_fields.get("listeria", "100"))
    conservacion = st.text_input("Conservación", auto_fields.get("conservacion", "<-18ºC"))
    caducidad = st.text_input("Caducidad (meses)", auto_fields.get("caducidad", "18"))
    irradiacion = st.text_input("Irradiación", auto_fields.get("irradiacion", "Producto libre de irradiación"))
    ogm = st.text_input("OGM", auto_fields.get("ogm", "Libre de OGM"))

if st.button("Generar ficha técnica final"):
    st.success("⚙️ Generar PDF corporativo (próxima fase)")
    st.info("Todos los datos pueden editarse y se guardarán para la generación final.")

st.caption("Prototipo de extracción y autocompletado. Mejora los patrones regex según tus PDFs.")