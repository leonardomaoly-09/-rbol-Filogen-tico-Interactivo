import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
st.set_page_config(
    page_title="Explorador Filogenético Interactivo",
    page_icon="🌳",
    layout="wide"
)

# -----------------------------
# TÍTULO
# -----------------------------
st.markdown(
    """
    <h1 style='text-align:center;'>🌳 Explorador Filogenético Interactivo</h1>
    <h3 style='text-align:center;'>Descubre las relaciones evolutivas entre especies</h3>
    """,
    unsafe_allow_html=True
)

st.write("---")

# -----------------------------
# OBJETIVO
# -----------------------------
st.info(
    "🎯 Objetivo: Explorar las relaciones evolutivas entre especies mediante "
    "la comparación de características biológicas y la representación de un árbol filogenético."
)

# -----------------------------
# BASE DE DATOS EDUCATIVA
# -----------------------------

especies = {
    "Humano": {
        "grupo": "Mamífero",
        "similitud": {
            "Chimpancé": 98.8,
            "Gorila": 98.3,
            "Perro": 94
        },
        "dato": "Los humanos y chimpancés comparten gran parte de su información genética."
    },

    "Chimpancé": {
        "grupo": "Mamífero",
        "similitud": {
            "Humano": 98.8,
            "Gorila": 98,
            "Perro": 93
        },
        "dato": "Los chimpancés son uno de los parientes vivos más cercanos del ser humano."
    },

    "Gorila": {
        "grupo": "Mamífero",
        "similitud": {
            "Humano": 98.3,
            "Chimpancé": 98
        },
        "dato": "Los gorilas pertenecen al grupo de los grandes simios."
    },

    "Perro": {
        "grupo": "Mamífero",
        "similitud": {
            "Lobo": 99
        },
        "dato": "Los perros domésticos están estrechamente relacionados con los lobos."
    },

    "Lobo": {
        "grupo": "Mamífero",
        "similitud": {
            "Perro": 99
        },
        "dato": "Los lobos y perros tienen un parentesco evolutivo cercano."
    },

    "Águila": {
        "grupo": "Ave",
        "similitud": {},
        "dato": "Las aves evolucionaron a partir de dinosaurios terópodos."
    },

    "Cocodrilo": {
        "grupo": "Reptil",
        "similitud": {},
        "dato": "Los cocodrilos son reptiles con una historia evolutiva antigua."
    }
}


lista_especies = list(especies.keys())


# -----------------------------
# SELECCIÓN DE ESPECIES
# -----------------------------

st.subheader("🧬 Selecciona cuatro especies")

col1, col2 = st.columns(2)

with col1:
    especie1 = st.selectbox("Especie 1", lista_especies)

    especie2 = st.selectbox(
        "Especie 2",
        [e for e in lista_especies if e != especie1]
    )

with col2:
    especie3 = st.selectbox(
        "Especie 3",
        [e for e in lista_especies if e not in [especie1, especie2]]
    )

    especie4 = st.selectbox(
        "Especie 4",
        [e for e in lista_especies if e not in [especie1, especie2, especie3]]
    )


seleccionadas = [
    especie1,
    especie2,
    especie3,
    especie4
]


# -----------------------------
# GENERAR ÁRBOL
# -----------------------------

if st.button("🌳 Generar árbol filogenético"):

    st.success("Árbol generado correctamente")

    G = nx.Graph()

    for especie in seleccionadas:
        G.add_node(especie)

    for i in range(len(seleccionadas)):
        for j in range(i+1, len(seleccionadas)):

            e1 = seleccionadas[i]
            e2 = seleccionadas[j]

            if e2 in especies[e1]["similitud"]:
                G.add_edge(e1, e2)


    st.subheader("🌿 Representación evolutiva")

    fig, ax = plt.subplots(figsize=(8,5))

    pos = nx.spring_layout(G, seed=20)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3000,
        node_color="#7DCEA0",
        font_size=10,
        ax=ax
    )

    st.pyplot(fig)


    # -----------------------------
    # INFORMACIÓN
    # -----------------------------

    st.subheader("📊 Análisis de especies")

    for especie in seleccionadas:

        st.write(
            f"""
            🧬 **{especie}**

            - Grupo biológico: {especies[especie]['grupo']}
            - Curiosidad: {especies[especie]['dato']}
            """
        )


    st.subheader("📈 Comparaciones genéticas")

    for i in range(len(seleccionadas)):

        for j in range(i+1, len(seleccionadas)):

            a = seleccionadas[i]
            b = seleccionadas[j]

            if b in especies[a]["similitud"]:

                st.write(
                    f"🔹 {a} - {b}: {especies[a]['similitud'][b]} % de similitud"
                )


# -----------------------------
# CRÉDITOS
# -----------------------------

st.write("---")

st.markdown(
    """
    <h3 style='text-align:center;'>👩‍💻 Creadores</h3>

    <p style='text-align:center;'>
    Maolis Leonardo<br>
    Gabriela Brito
    </p>
    """,
    unsafe_allow_html=True
)
