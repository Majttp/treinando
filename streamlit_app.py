import streamlit as st

st.title("Aprendendo")
st.write("Treinando")
st.header("Entendendo")
st.subheader("Passo a passo")

st.text("Permite escrever um texto")

#Apredendo Markdown
st.markdown("""---""")
st.markdown("Escrever texto")
st.markdown ("*Texto itálico*")
st.markdown("**Texto negrito**")
st.markdown("Esse é um tutorial, *é importante* **prestar atenção!** ")
st.markdown("# Texto maior")
st.markdown("## Texto menor")

st.markdown("""
            1. Criar listas 
            2. Criar Listas
            3. Criar listas
            """)
st.markdown("[Criar link](https://br.pinterest.com/)")
st.markdown(":rocket: :smile:")
st.markdown("### Html")
html_code="""
<h1 style='color:pink';>Esse é
um cabeçalho rosa</h1>
<p style = 'color:purple;'> Esse é
um parágrafo</p>
"""
st.markdown(html_code, unsafe_allow_html=True)

st.markdown("---")

st.markdown("Inserindo imagens")
st.image("image/Leao.jpeg")
st.markdown("*Leão de origami*")

colunas=st.columns(2)
colunas[0].image("Gifs/gotas.gif")
colunas[1].image("Gifs/jellyfish.gif")

st.video("Video/mov.mp4")

# Para criar um campo de upload
image=st.file_uploader("Escolha uma imagem", type=("jpg", "jpeg", "gif", "png"))
if image:
    st.image(image)




