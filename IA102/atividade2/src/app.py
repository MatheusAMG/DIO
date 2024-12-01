import streamlit as st
from services.blob_service import upload_blob
from services.document_inteligence import analize_credit_card

def configure_interface():
   st.title("Upload de arquivos para Azure")
   uploaded_file = st.file_uploader("Escolha um arquivo")

   if uploaded_file is not None:
      filename = uploaded_file.name
      blob_url = upload_blob(uploaded_file,filename)
      if blob_url:
         st.write(f"Arquivo {filename} enviado com sucesso para Azure")
         credit_card_info = analize_credit_card(blob_url)
         show_image_and_validation(blob_url,credit_card_info)
      else:
         st.write(f"Erro ao enviar o arquivo{filename} para o Azure Blob Storage")

def show_image_and_validation(blob_url, credit_card_info):
   st.image(blob_url, caption="Imagem enviada", use_column_width=True)
   st.write("resultado da validacao:")
   if credit_card_info and credit_card_info["card_name"]:
      st.markdown(f"<h1 style='color: green;'> Cartao Valido</h1>",unsafe_allow_html=True)
      st.write(f"Nome do titular: {credit_card_info['card_name']}")
      st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
      st.write(f"Data de validade: {credit_card_info['expirity_date']}")
   else:
      st.markdown(f"<h1 style='color: red;'> Cartao Inalido</h1>",unsafe_allow_html=True)
      st.write("Esse não é um cartao valido")

if __name__ == "__main__":
   configure_interface()