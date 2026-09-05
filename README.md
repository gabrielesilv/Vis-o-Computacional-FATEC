# Processamento de Imagens Digitais com OpenCV

Este projeto foi desenvolvido com o objetivo de estudar e praticar conceitos básicos de **Processamento Digital de Imagens utilizando Python e OpenCV**.

Os exemplos de imagem abordam leitura de imagens, manipulação de pixels, separação e junção de canais, inversão de cores, alteração de brilho e cálculo de histogramas.

---

## Sobre o OpenCV

O **OpenCV (Open Source Computer Vision Library)** é uma biblioteca utilizada para processamento de imagens, visão computacional e aplicações relacionadas à inteligência artificial.

Com o OpenCV é possível:

- Ler e exibir imagens;
- Salvar imagens;
- Separar e unir canais de cores;
- Converter espaços de cores;
- Alterar brilho e contraste;
- Aplicar filtros e transformações;
- Trabalhar com vídeos e câmeras;
- Desenvolver aplicações de visão computacional.

---

## Tecnologias utilizadas

- Python 3
- OpenCV
- Visual Studio Code

---

## Instalação

Verifique se o Python está instalado:

```bash
py --version
```

Instale o OpenCV:

```bash
py -m pip install opencv-python
```

Para verificar a instalação:

```bash
py -c "import cv2; print(cv2.__version__)"
```

---

## Como executar

No terminal, acesse a pasta do projeto e execute o arquivo desejado:

```bash
py abrir_imagem.py
```

Também é possível executar os arquivos diretamente pelo botão **Executar** do Visual Studio Code.

---

# Funcionalidades

## 1. Leitura e exibição de imagens

Uma imagem pode ser carregada utilizando:

```python
imagem = cv2.imread("baboon.jpg")
```

E exibida com:

```python
cv2.imshow("Imagem", imagem)
```

O programa aguarda uma tecla antes de fechar a janela:

```python
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Também é possível carregar uma imagem diretamente em tons de cinza:

```python
img = cv2.imread("baboon.jpg", 0)
```

A leitura e exibição da imagem são demonstradas no arquivo `abrir_imagem.py`.

---

## 2. Manipulação de pixels

Uma imagem pode ser entendida como uma matriz de pixels.

Para acessar um pixel:

```python
img[x][y]
```

Nesse contexto:

- `x` representa a linha;
- `y` representa a coluna.

Em uma imagem em tons de cinza, os valores dos pixels normalmente ficam entre `0` e `255`:

```text
0 ------------------------ 255
Preto                     Branco
```

É possível percorrer todos os pixels utilizando dois `for`:

```python
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        # operação sobre o pixel
```

---

## 3. Alteração de brilho

O brilho pode ser alterado modificando os valores dos pixels.

### Usando `for`

No arquivo `acessando_pixel.py`, a imagem é clareada adicionando `50` ao valor de cada pixel:

```python
imgB = img.copy()

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        imgB[x][y] = min(img[x][y] + 50, 255)
```

O `min(..., 255)` impede que o valor ultrapasse o limite máximo de `255`.

Por exemplo:

```text
100 + 50 = 150
200 + 50 = 250
230 + 50 = 280 → 255
```

Essa abordagem é útil para entender como a alteração de brilho acontece diretamente sobre os pixels.

### Usando `cv2.convertScaleAbs()`

Também é possível utilizar uma função do próprio OpenCV:

```python
img_brilho = cv2.convertScaleAbs(
    img,
    alpha=1.0,
    beta=70
)
```

Nesse exemplo, `beta=70` aumenta o brilho da imagem. Para escurecer, pode ser utilizado um valor negativo.

O arquivo `ajuste_brilho.py` demonstra essa abordagem.

---

## 4. Histograma

O histograma representa a distribuição dos valores dos pixels de uma imagem.

Em uma imagem em tons de cinza:

- **Eixo X** → intensidade do pixel, de `0` a `255`;
- **Eixo Y** → quantidade de pixels.

O histograma pode ser calculado com:

```python
hist_original = cv2.calcHist(
    [img],
    [0],
    None,
    [256],
    [0, 256]
)
```

Também é possível calcular o histograma da imagem após o aumento de brilho:

```python
hist_clareada = cv2.calcHist(
    [imgB],
    [0],
    None,
    [256],
    [0, 256]
)
```

Ao aumentar o brilho, os valores dos pixels tendem a aumentar. Por isso, a distribuição de intensidades tende a se deslocar para valores maiores.

O cálculo dos histogramas está presente no arquivo `acessando_pixel.py`.

---

## 5. Inversão de cores

A inversão das cores pode ser feita com:

```python
imgI = cv2.bitwise_not(imagem)
```

Essa operação produz um efeito semelhante ao negativo de uma fotografia.

O resultado pode ser exibido com:

```python
cv2.imshow("imagem invertida", imgI)
```

Essa funcionalidade está demonstrada no arquivo `imagem_invertida.py`.

---

## 6. Separação e junção dos canais BGR

O OpenCV trabalha, por padrão, com a ordem **BGR**:

- **B** — Blue (Azul)
- **G** — Green (Verde)
- **R** — Red (Vermelho)

Os canais podem ser separados utilizando:

```python
blue, green, red = cv2.split(imagem)
```

Depois, podem ser unidos novamente:

```python
imagemRGB = cv2.merge((blue, green, red))
```

Cada canal também pode ser exibido individualmente:

```python
cv2.imshow("Canal Blue", blue)
cv2.imshow("Canal Green", green)
cv2.imshow("Canal Red", red)
```

Essa funcionalidade está demonstrada no arquivo `merge_imagem.py`.

> **Observação:** apesar do nome da variável `imagemRGB`, a junção acima continua utilizando a ordem BGR do OpenCV.

---

# Espaços de cores

O OpenCV permite converter uma imagem entre diferentes espaços de cores utilizando:

```python
cv2.cvtColor()
```

### BGR

É o formato padrão utilizado pelo OpenCV:

```text
Blue → Green → Red
```

É diferente do RGB, que utiliza:

```text
Red → Green → Blue
```

### HSV

O espaço HSV é composto por:

- **H (Hue)** — Matiz/cor;
- **S (Saturation)** — Saturação;
- **V (Value)** — Valor/brilho.

Exemplo:

```python
imagem_hsv = cv2.cvtColor(
    imagem,
    cv2.COLOR_BGR2HSV
)
```

### YCrCb

Separa principalmente luminosidade e informações de cor:

- **Y** — Luminosidade;
- **Cr** — Componente relacionada ao vermelho;
- **Cb** — Componente relacionada ao azul.

```python
imagem_ycrcb = cv2.cvtColor(
    imagem,
    cv2.COLOR_BGR2YCrCb
)
```

### LAB

Possui três componentes:

- **L** — Luminosidade;
- **A** — Variação entre verde e vermelho;
- **B** — Variação entre azul e amarelo.

```python
imagem_lab = cv2.cvtColor(
    imagem,
    cv2.COLOR_BGR2LAB
)
```

---

# Salvando imagens

Para salvar uma imagem como arquivo:

```python
cv2.imwrite("resultado.jpg", imagem)
```

O `copy()` e o `imwrite()` possuem funções diferentes:

```python
imagem_copia = imagem.copy()
```

cria uma cópia da imagem na memória, enquanto:

```python
cv2.imwrite("resultado.jpg", imagem_copia)
```

salva a imagem como arquivo no computador.

---

# Principais funções

| Função | Descrição |
|---|---|
| `cv2.imread()` | Lê uma imagem |
| `cv2.imshow()` | Exibe uma imagem |
| `cv2.imwrite()` | Salva uma imagem |
| `cv2.cvtColor()` | Converte espaços de cores |
| `cv2.split()` | Separa os canais |
| `cv2.merge()` | Junta os canais |
| `cv2.bitwise_not()` | Inverte as cores |
| `cv2.convertScaleAbs()` | Ajusta brilho e contraste |
| `cv2.calcHist()` | Calcula o histograma |
| `cv2.waitKey()` | Aguarda uma tecla |
| `cv2.destroyAllWindows()` | Fecha as janelas |
| `image.copy()` | Cria uma cópia da imagem |


---

# Possíveis melhorias

O projeto pode ser expandido futuramente com:

- Conversão para escala de cinza;
- Equalização de histograma;
- Ajuste de contraste;
- Aplicação de filtros;
- Detecção de bordas;
- Redimensionamento;
- Rotação e recorte;
- Captura pela webcam;
- Processamento de vídeos;
- Menu interativo para escolher as operações.

---

# Conclusão

Este projeto apresenta conceitos fundamentais de Processamento Digital de Imagens com Python e OpenCV.

Durante o desenvolvimento são praticados conceitos como pixels, canais BGR, manipulação de imagens, estruturas de repetição, alteração de brilho, inversão de cores e histogramas**, além de uma introdução aos principais espaços de cores utilizados no OpenCV.

Os arquivos `baboon.jpg` e `FluorescentCells.jpg` são utilizados como imagens de estudo nos exemplos.
