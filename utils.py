import os
import requests
from bs4 import BeautifulSoup

RFB_URL = 'http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj'

DATASET_PART_PREFIX = 'Dados Abertos CNPJ'

DEBUG = True

def download_file(fileurl, path):
    response = requests.get(fileurl)
    with open(path, 'wb') as output:
        output.write(response.content)
    if DEBUG: 
        print('Downloaded file to {}'.format(path))


def download_dataset_parts(dirpath, start=1, end=None):
    rfb_page = requests.get(RFB_URL)
    soup = BeautifulSoup(rfb_page.content, 'html.parser')
    dataset_links = [l for l in soup.findAll('a') 
                        if DATASET_PART_PREFIX in l.text]
    if end is None:
        end = len(dataset_links)
    for link in dataset_links:
        part_number = int(link.text.split(DATASET_PART_PREFIX)[-1])
        if start <= part_number <= end:
            url = link.attrs['href']
            download_file(url, os.path.join(dirpath, url.split('/')[-1]))

if __name__ == "__main__":
    download_dataset_parts('data', start=9)