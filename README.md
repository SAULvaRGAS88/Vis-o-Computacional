
# Detecção de Faces e Boca com Feedback Visual

---

## 📄 Descrição do Projeto

Este projeto implementa uma aplicação em tempo real para **detecção de rostos e identificação da região da boca com análise de cor RGB média**, utilizando a biblioteca **OpenCV**. A aplicação exibe um vídeo com feedback visual, destacando a boca detectada com um retângulo verde e exibindo a média das cores da região da boca.

---

## ⚙️ Funcionalidades

1. **Detecção em tempo real de rostos e regiões da boca**:
   - O sistema identifica rostos no vídeo capturado pela webcam.
   - Identifica a localização da região da boca dentro do rosto detectado.

2. **Análise da cor média da região da boca detectada**:
   - A cor da região da boca é calculada em termos da média RGB (vermelho, verde e azul).
   - O feedback da cor é exibido na tela e no console.

3. **Interface com o usuário através de comandos simples**:
   - Pressionando a tecla `b`, é possível visualizar no console a cor RGB da última boca detectada.
   - Pressionando a tecla `q`, o programa finaliza a execução.

4. **Feedback visual direto na tela**:
   - A boca detectada é destacada com um retângulo verde.
   - A mensagem com a média das cores da boca é exibida no canto superior esquerdo da janela.

---

## 🛠️ Bibliotecas Necessárias

Este projeto utiliza a biblioteca **OpenCV** para processamento de imagem e detecção de rostos e bocas.

### 🔧 Instalação da Biblioteca
Certifique-se de ter o OpenCV instalado. Para instalar:

```bash
pip install opencv-python
pip install opencv-python-headless
```

---

## 🏁 Modo de Uso

### 1. **Instalação das Dependências**
Após garantir que o Python está instalado em sua máquina, instale as bibliotecas necessárias:

```bash
pip install opencv-python opencv-python-headless
```

---

### 2. **Execução**
Execute o código:

```bash
python main.py
```

Certifique-se de que sua webcam está conectada ao sistema.

---

### 3. **Interatividade**
- **`b`**: Exibe a cor média da boca no console.
- **`q`**: Encerra a aplicação.

---

## 🛠️ Estrutura do Código

### **Função Principal**
A função `main()` é a responsável pela execução do loop principal da aplicação, captura o vídeo da webcam e realiza as detecções.

```python
def main():
    classificador_de_faces, classificador_da_boca = inicializar_detector_de_faces_e_boca()
    captura_de_video = cv2.VideoCapture(0)  # Captura da webcam
```

---

### **Detecção de Rostos e Boca**
O método `detectar_faces_e_boca` processa os quadros da webcam, detecta rostos e identifica a região da boca.

```python
faces = classificador_de_faces.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
bocas = classificador_da_boca.detectMultiScale(regiao_rosto, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))
```

As bocas detectadas são destacadas e a cor média da região da boca é calculada.

```python
cv2.putText(quadro, feedback_texto, 
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
```

---

## 💡 Recursos e Pré-requisitos
- **OpenCV** para detecção de rosto e boca.
- Webcam conectada ao computador.
- Sistema com Python instalado.

---

## 🚀 Como Contribuir

Caso encontre algum erro ou deseje implementar novas funcionalidades, sinta-se livre para abrir um **Pull Request** com a sua contribuição.

---

## 📄 Licença
Este projeto é de código aberto. Sinta-se livre para usar e modificar conforme necessário.

---

## 📧 Contato

Caso precise entrar em contato para dúvidas ou sugestões, você pode enviar um e-mail para **[seuemail@dominio.com](mailto:seuemail@dominio.com)**.

---

## 🏆 Agradecimentos

Obrigado à comunidade **OpenCV** pela ferramenta incrível que tornou este projeto possível. A tecnologia de visão computacional é uma área incrível e cheia de potencial! 

---
