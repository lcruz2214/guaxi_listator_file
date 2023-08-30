import os
import pandas as pd

def buscar_arquivos(caminho):
    file_list_dir = []
    file_list = []
    file_ext = []
    file_tamanho = []
    try:
        for subdir, dirs, files in os.walk(caminho):
            for file in files:
                arq, ext = os.path.splitext(file)
                file_path = os.path.join(subdir, file)
                file_list_dir.append(file_path)
                sz = round(os.path.getsize(file_path)/(1024^2),3)
                file_list.append(file)
                file_ext.append(ext)
                file_tamanho.append(sz)
        return [file_list, file_list_dir, file_ext, file_tamanho]
    except Exception as e:
        print(e)

texto = ['+------------------------------------------+',
         '|      Guaxi-Listator_File                 |',
         '+------------------------------------------+',
         '| Este é um gerador de lista de arquivos   |',
         '|                                          |',
         '| Ele vai criar uma lista de arquivos no   |',
         '| Excel - com nome do arquivo, caminho,    |',
         '| tamanho e extensão.                      |',
         '+------------------------------------------+',
         '| -A partir dessa lista é possível acessar |',
         '| os arquivo diretamente da planilha       |',
         '+------------------------------------------+']

for a in texto:
    print(a)

print('Diretório Atual >> ', os.getcwd())
diretorio = input('Informe o diretorio ou deixe em branco para buscar a partir do diretorio de execução atual: ')

if diretorio == '':
    diretorio = os.getcwd()

file_list = buscar_arquivos(diretorio)

df = pd.DataFrame(file_list[0], columns=['Arquivos'])
df['Caminho - click para abrir'] = file_list[1]
df['Extenção'] = file_list[2]
df['Tamanho MB'] = file_list[3]
df['Caminho - click para abrir'] = '=HYPERLINK("' + df['Caminho - click para abrir'] + '")'
df.to_excel('Lista_de_arquivos.xlsx', index=False)

print('Lista de arquivos gerada!')
