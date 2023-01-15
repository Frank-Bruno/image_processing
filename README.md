# Projeto de Processamento de imagem
Este projeto tem com objetivo o estudo de processamento de imagem usando a biblioteca do opencv, além da  resolução de dois problemas propóstos sobre filtragem de imagem.
* 1) Realçar o constraste de uma imagem.
* 2) Remover o ruído do tipo "salt & pepper" e "gaussian" de uma imagem. 

## 1) Realçar o constraste de uma imagem
### a) Estude o código abaixo.

~~~Matlab
I = imread('moon.tif');
h = fspecial('unsharp')
I2 = imfilter(I,h);
imshow(I), title('Original Image')
figure, imshow(I2), title('Filtered Image')
~~~

### b) Ao invés do filtro h acima (obtido com fspecial), construa você mesmo um filtro que produza resultado semelhante, de realce de contraste, e informe a matriz que denota este filtro.

~~~Python
import numpy as np
import cv2

img = cv2.imread('/home/frank/Imagens/moon.png')

alfa=0
kernel = np.array([[-alfa,alfa-1,-alfa],[alfa-1, alfa+5, alfa-1],[-alfa, alfa-1, -alfa]]) * (1/(alfa+1))

img_unsharp = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image", img_unsharp)
cv2.imwrite("/home/frank/Imagens/moon_unsharp.png", img_unsharp)
cv2.waitKey()
~~~

~~~Python
Matriz = [[ 0. -1.  0.] 
          [-1.  5. -1.] 
          [ 0. -1.  0.]]
~~~

### c) Explique o motivo do seu filtro realçar o contraste e coloque uma imagem filtrada por ele no seu relatório, junto com a original. Pode ser a própria “moon.tif” ou outra.

O filtro de nitidez é um operador de nitidez simples cujo nome deriva do fato de que ele aprimora as bordas (e outros componentes de alta frequência em uma imagem) por meio de um procedimento que subtrai uma versão de nitidez ou suavizada de uma imagem da imagem original.

![imagem original](https://github.com/Frank-Bruno/image_processing/blob/main/enhance_contrast/moon.png)
![imagem filtrada](https://github.com/Frank-Bruno/image_processing/blob/main/enhance_contrast/moon_unsharp.png)

### d) O seu filtro pode ser entendido como “passa-baixa” ou “passa-alta”?

É um filtro passa-alta, pois subtrai as frequências mais baixas da imagem.

## 2) Remover o ruído do tipo “salt & pepper” e “gaussian” de imagens
**siga os passo:** 

1. Obtenha uma foto que tenha um fundo relativamente homogêneo (“quase” uma
única cor) e um ou mais objetos em 1º plano. A resolução mínima é de 200 x 200
pixels (pode ser maior). Pode ser uma foto sua ou de um rosto obtido na Internet.
Não repita a foto usada por um colega nem deixe repetirem a sua.
2. Se a imagem for colorida, a converta para tons de cinza, usando 8 bits por pixel,
com valores de 0 a 255. A função rgb2gray.m faz isso. A imagem em tons de cinza
será chamada de “im_original”.
3. Usando a função imnoise, crie uma versão ruidosa da imagem original com ruído do
tipo “salt & pepper” e densidade (“density”, parâmetro da imnoise) de 0.06. Repita
o passo mas com density de apenas 0.005. Além destas duas imagens com ruído salt
& pepper, gere imagens com ruído Gaussiano de média 0 e variâncias 0.001 e 0.03,
por exemplo, com o comando:
~~~Matlab
imnoise(im_original,'gaussian',0,0.001)
~~~
No final, você deve ter 4 versões ruidosas da imagem original.\
Sua tarefa é usar filtros para reduzir o ruído das versões ruidosas e comparar com a imagem
original. A figura de mérito da filtragem será a PSNR, ou “razão sinal de pico / ruido”, que
usa como “pico” o valor máximo de um pixel que é igual a 255 neste caso. A PSNR pode
ser calculada em dB como segue:

~~~Matlab
error=im_original-im_pouco_ruido; %imagem de erro
MSE=mean(error(:).^2) %error(:) eh um vetor
PSNR = 10*log10(255^2/MSE) %valor em dB
~~~

Os dois filtros a serem usados são o de média e mediana. O de média pode ser obtido com
_fspecial('average',M)_, onde M indica que o kernel do filtro é de dimensão
M x M. Depois de se obter o kernel do filtro, pode-se usar a função filter2 para executar a
filtragem. O filtro de mediana pode usar diretamente a função medfilt2 com algo como
_medfilt2(noisyImage,[M M])_
onde o [M M] indica uma região de M x M pixels da qual se extrai a mediana. Para ambos
os filtros, variem os valores de M no conjunto {3, 5, 7}.

4. Para cada uma das 4 versões ruidosas, para cada um dos dois tipos de filtro (média e
mediana) e para cada um dos 3 valores de M, calcule a PSNR entre a imagem
original e a imagem ruidosa após passar pelo filtro. Para ter uma ideia dos valores
envolvidos, calcule também a PSNR entre a imagem original e a versão ruidosa,
sem passar por filtro.

**Responda no relatório o seguinte:**
### a) Por que para o ruído salt & pepper o filtro de mediana é tão melhor que o de média? 

A imagem consiste em milhares de pixels e os pixels poluídos pelo ruído geralmente são isolados uns dos outros. Para remover esses pixels isolados, uma ideia simples é substituir o valor do pixel pelo valor do pixel circundante. O filtro da mediana é baseado nessa ideia, que estabelece uma janela de tamanho n*n.\
Ele verifica cada pixel da esquerda para a direita e de cima para baixo, classifica os n2 pixels contidos no valor do pixel e seleciona o valor intermediário para substituir o valor do pixel do pixel de processamento, removendo assim o ruído de impulso. Este processamento simples funciona bem para imagens com baixa densidade de contaminação de ruído, mas à medida que a densidade de ruído aumenta, os ruídos não são mais isolados. Para garantir o efeito de remoção, o tamanho da janela precisa ser ampliado, o que também leva a bordas e detalhes borrados.

### b) A PSNR é uma figura de mérito objetiva, mas analisando as imagens de forma subjetiva, qual o filtro que conserva melhor as bordas dos objetos na imagem?

O filto de média apresenta imagens com bordas mais detalhadas, entretando quando o ruído apresenta alta densidade tende a ter dificuldades para tratar a imagem. Por outro lado, o filtro de mediana consegue eliminar uma maior quantidade de ruído mas apresenta bordas dos objetos da imagem com menos detalhes.

### c) Quando o ruído é Gaussiano e a PSNR é relativamente alta, os filtros não parecem ajudar muito (melhorar a PSNR). Mas quando a PSNR é baixa, eles parecem melhorar. Você concorda? Se sim, qual o motivo deste comportamento? Se não, em qual aspecto o raciocínio está incompleto? 

PSNR é a relação sinal-ruído de pico (em dB) entre duas imagens, então quanto maior o PSNR, melhor é a qualidade da imagem. Então para valores altos de PSNR os filtros tendem a fazer menos efeitos nas imagens.


### d) Pensando no custo computacional dos processos de filtragem, qual o filtro que demanda mais poder de processamento, o de média ou mediana? 

O filtro de mediana, pois considera cada pixel na imagem por vez e olha para seus vizinhos próximos para decidir se é ou não representativo de seus arredores. Em vez de simplesmente substituir o valor do pixel pela média dos valores dos pixels vizinhos, ele o substitui pela mediana desses valores.
