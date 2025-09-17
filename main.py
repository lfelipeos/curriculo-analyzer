import pdfplumber
import pandas as pd
import os

def extrair_texto_pdf(caminho):
    with pdfplumber.open(caminho) as pdf:
        texto = ''
        for paginas in pdf.pages:
            texto += paginas.extract_text() + '\n'
    return texto

def analisar_curricculo(texto):
    palavras_chave = ['Python', 'Excel', 'Power BI', 'Machine Learning', 'Java']
    resultado = {palavra: palavra in texto for palavra in palavras_chave}
    return resultado

def processar_pasta(pasta):
    dados = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.pdf'):
            texto = extrair_texto_pdf(os.path.join(pasta, arquivo))
            analise = analisar_curricculo(texto)
            analise['arquivo'] = arquivo
            dados.append(analise)
    return pd.DataFrame(dados)

if __name__ == '__main__':
    df = processar_pasta('curriculos')
    df.to_csv('resultado.csv', index=False)
    print(df)