# Data Analysis of Brazilian Educational Entities

## Sumário

1. Introdução
2. Exploração dos Dados
3. 

## Introdução

### Objetivo

...Sobre as Pessoas Jurídicas que desempenham atividade econômica na área de Educação.

### Preparação da Base de Dados

1. Download dos arquivos no site da RFB
2. Reconstrução dos dados com auxílio do programa disponível em https://github.com/fabioserpa/CNPJ-full
3. 3 CSVs totalizando 17GB (Empresas, Sócios e CNAES Secundários)
4. Arquivos tem X, Y e Z Linhas

=> 1º Desafio superado

## Exploração dos Dados

1. Faz sentido trabalhar com um recorte dos dados: escolhi educação
2. Empresas são identificadas pelo CNAE (85)
3. Identificação do segmento de ensino que atua
4. Recorte dos Sócios
=> 2º Desafio - Separar os dados que serão necessários

### Complicações

1. É preciso lidar com 2 arquivos para identificar CNAE principal e secundários
2. Nem sempre os dados estão com os valores imaginados

### Descobertas

1. CNPJs por segmento de ensino
2. Utilização do MEI como recurso para iniciar um negócio "a todo custo"
3. Análises do setor público podem ser mais difíceis (CENSO da Educação)

## A Rede da Educação

1. Mídia tem anunciado expansões e aquisições em grandes grupos educacionais.
2. O que os dados dizem sobre isso?

### Construção da Rede

1. 1ª tentativa com a rede completa de educação gerou um grafo muito grande
2. Filtragem apenas sobre a "educação formal"
3. Construção do grafo direcionado "É sócio de"
4. Grafo de

=> 3ª Desafio: empresas podem ser sócias de empresas (mascarar?)

## Descobertas

## Conclusão
