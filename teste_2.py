import tabula
import pandas as pd
import zipfile
import os

def extract_tables():
    try:
        # Extrai todas as tabelas do PDF
        tables = tabula.read_pdf(
            "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
            pages="all",
            multiple_tables=True,
            lattice=True
        )
        
        # Concatena as tabelas
        df_final = pd.concat(tables, ignore_index=True)


        # Substitui o OD e AMB do cabeçalho nos nomes da legenda
        df_final = df_final.rename(columns ={
            "OD": "Seg. Odontológica",
            "AMB": "Seg. Ambulatorial"
        })
        
        
        # Substitui abreviações OD e AMB das células no nome da legenda (Fiquei em dúvida em qual era pra subsituir)
        # df_final["OD"] = df_final["OD"].replace(mapping)
        # df_final["AMB"] = df_final["AMB"].replace(mapping)
        
        return df_final
    
    except Exception as e:
        print(f"Erro ao extrair tabelas: {e}")
        return None

# Funcão para salvar o dataframe em CSV
def save_as_csv(df):
    try:
        csv_path = "rol_procedimentos_anexo_i.csv"
        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        return csv_path
    
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")
        return None

# Função para colocar o arquivo CSV dentro de um arquivo zip
def csv_to_zip(csv_path):
    try:
        if csv_path and os.path.exists(csv_path):
            with zipfile.ZipFile("Teste_gabriel_andre.zip", "w") as zipf:
                zipf.write(csv_path)
            print("Arquivo ZIP criado!")
        else:
            print("Erro: CSV não encontrado para zip.")
    except Exception as e:
        print(f"Erro ao criar arquivo zip: {e}")


def main():
    df_final = extract_tables()
    
    if df_final is not None:
        csv_path = save_as_csv(df_final)
    csv_to_zip(csv_path)

if __name__ == "__main__":
    main()