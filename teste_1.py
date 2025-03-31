# Teste 1: Web Scrapping
import requests, zipfile, os
from bs4 import BeautifulSoup

# Função para filtrar os links dos PDFs por meio da biblioteca BeautifulSoup
def get_html_text(url):

        response = requests.get(url)
        html_text = BeautifulSoup(response.text, 'html.parser')

        # Lista para os links dos PDFs
        pdf_links = []

        # Iterando pela página HTML e selecionando apenas os links contidos
        for a in html_text.find_all('a', href=True):
            href = a['href'].lower()
            
            # Checando se os links possuem o nome "Anexo I" ou "Anexo II" e se terminam com ".pdf"
            if ('anexo i' in href or 'anexo_i' in href or 'anexo1' in href) and href.endswith(".pdf"):
                pdf_links.append(a['href'])
            elif ('anexo ii' in href or 'anexo_ii' in href or 'anexo2' in href) and href.endswith(".pdf"):
                pdf_links.append(a['href'])
        print("Links filtrados: ", pdf_links)

        return pdf_links

# Função para baixar os PDFs e criar um arquivo zip
def convert_to_zip(links):

    # Criando um diretório temporário para os PDFs
    os.makedirs("pdf_temp", exist_ok=True)

    # Lista para os PDFs baixados
    pdf_downloaded = []

    # Baixando os PDFs e adicionando em pdf_downloaded
    for link in links:
         
        try:
            response = requests.get(link, stream=True)
            response.raise_for_status()

            pdf_name = os.path.basename(link)
            pdf_path = os.path.join('pdf_temp', pdf_name)

            with open(pdf_path, 'wb') as pdf_file:
                for c in response.iter_content(1024):
                    pdf_file.write(c)
                pdf_downloaded.append(pdf_path)    
            print("PDF baixado: ", pdf_name)

        except Exception as e:
            print(f"Erro ao baixar {link}: {e}")

    # Colocando os dois arquivos PDF em um arquivo zip
    with zipfile.ZipFile("anexos.zip", 'w') as zipf:
        for pdf in pdf_downloaded:
            zipf.write(pdf, os.path.basename(pdf))
            print("PDFs adicionados ao zip:", pdf)

    print("Arquivo anexos.zip criado.")
              

def main():
    pdf_links = get_html_text("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
    convert_to_zip(pdf_links)



if __name__ == "__main__":
    main()