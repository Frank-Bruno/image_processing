# Criando um nova imagem com tons de cinza

O novo nome da imgem segue o seguinte formato:

    "nome_da_image"_img_original.png

por exemplo, para uma imagem de nome moon.pgn o novo nome será:

    moon_img_original.png

# Criação das imagens com ruidos
Para cada imagem processada foi gerado uma nova para cada valor de ruído e densidade diferente.
* Ruído salt & pepper com densidade de 0.06 e 0.005
* Ruído Gaussiano com densidade de 0.001 e 0.03.

O padrão de nome das imagens criadas foi:

Tipo de ruído | valor da densidade | nome da imagem com ruído
------------- | ------------------ | ----------
salt & pepper | 0.06               | "nome_da_image"_01.png
salt & pepper | 0.005              | "nome_da_image"_02.png
Gaussiano     | 0.001              | "nome_da_image"_03.png
Gaussiano     | 0.03               | "nome_da_image"_04.png

# Criação das imagens filtradas
Para cada imagem com ruído foi gerado 3 novas imagens para cada um dos filtros, de média(averaging) e mediana(median), em que variam os valores do Kernel. (M=[3,5,7])


O padrão de nome das imagens criadas foi:

Tipo de filtro | valor de M | nome da imagem filtrada
-------------  | ---------- | ----------
averaging      | 3          | "nome_da_image_com_ruído"_03_avr.png
averaging      | 5          | "nome_da_image_com_ruído"_05_avr.png
averaging      | 7          | "nome_da_image_com_ruído"_07_avr.png
median         | 3          | "nome_da_image_com_ruído"_03_median.png
median         | 5          | "nome_da_image_com_ruído"_05_median.png
median         | 7          | "nome_da_image_com_ruído"_07_median.png
