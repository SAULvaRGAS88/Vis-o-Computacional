import cv2

# Variável global para armazenar os valores da última cor média detectada
feedback_atual = None


def inicializar_detector_de_faces_e_boca():
    """
    Carrega os classificadores necessários para detectar rosto e boca no vídeo.

    Retorna:
        classificador_de_faces: Classificador para detectar rostos.
        classificador_da_boca: Classificador para detectar a boca.
    """
    # Carrega os classificadores de detecção pré-treinados da OpenCV
    classificador_de_faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    classificador_da_boca = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    # Verifica se os classificadores foram carregados corretamente
    if classificador_de_faces.empty() or classificador_da_boca.empty():
        raise IOError("Não foi possível carregar os modelos de detecção.")

    # Retorna os classificadores de rosto e boca
    return classificador_de_faces, classificador_da_boca


def detectar_faces_e_boca(quadro, classificador_de_faces, classificador_da_boca):
    """
    Detecta faces e a região da boca no vídeo e gera feedback visual.

    Parâmetros:
        quadro (ndarray): O quadro do vídeo capturado.
        classificador_de_faces (CascadeClassifier): Classificador para detectar rostos.
        classificador_da_boca (CascadeClassifier): Classificador para detectar a boca.

    Retorna:
        quadro (ndarray): O quadro atualizado com as detecções e feedback visual.
    """
    global feedback_atual  # Usando variável global para armazenar dados de feedback

    # Converte o quadro para escala de cinza, facilitando a detecção
    cinza = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)

    # Detectando faces no vídeo
    faces = classificador_de_faces.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Para cada face detectada, tenta identificar a região da boca
    for (x, y, largura, altura) in faces:
        # Define a região do rosto onde a boca provavelmente está localizada
        regiao_rosto = cinza[y + int(altura / 2):y + altura, x:x + largura]

        # Detecta a boca nessa região
        bocas = classificador_da_boca.detectMultiScale(regiao_rosto, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

        for (bx, by, bw, bh) in bocas:
            # Desenha um retângulo verde ao redor da boca detectada
            cv2.rectangle(quadro, 
                          (x + bx, y + int(altura / 2) + by), 
                          (x + bx + bw, y + int(altura / 2) + by + bh), 
                          (0, 255, 0), 2)

            # Calcula a região da boca para análise de cores
            regiao_boca = quadro[y + int(altura / 2) + by:y + int(altura / 2) + by + bh, x + bx:x + bx + bw]

            # Calcula a cor média da região da boca no espaço RGB
            media_rgb = regiao_boca.mean(axis=(0, 1))  # Média dos valores R, G e B

            # Salva os dados da cor como feedback atual
            feedback_atual = media_rgb

            # Cria uma mensagem de feedback com a cor média calculada
            feedback_texto = f"R: {int(media_rgb[2])} G: {int(media_rgb[1])} B: {int(media_rgb[0])}"

            # Desenha o feedback na tela no canto superior esquerdo
            cv2.putText(quadro, feedback_texto, 
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    return quadro


def main():
    """
    Função principal para executar a lógica de captura de vídeo,
    detecção de faces e boca e exibição de feedback visual.
    """
    # Inicializa os detectores de faces e boca
    classificador_de_faces, classificador_da_boca = inicializar_detector_de_faces_e_boca()

    # Captura vídeo da webcam padrão
    captura_de_video = cv2.VideoCapture(0)  # 0 indica a webcam padrão

    # Verifica se a webcam foi inicializada corretamente
    if not captura_de_video.isOpened():
        raise Exception("Não foi possível abrir a webcam.")

    try:
        # Loop principal para processar o vídeo em tempo real
        while True:
            # Captura um quadro do vídeo da webcam
            ret, quadro = captura_de_video.read()
            if not ret:
                break  # Encerra se a leitura falhar

            # Detecta as faces e a região da boca no quadro e gera feedback visual
            quadro = detectar_faces_e_boca(quadro, classificador_de_faces, classificador_da_boca)

            # Exibe o vídeo com as detecções e feedback visual na tela
            cv2.imshow('Detecção de Faces e Boca com Feedback', quadro)

            # Verifica se a tecla 'b' foi pressionada para exibir no console
            if cv2.waitKey(1) & 0xFF == ord('b'):
                if feedback_atual is not None:
                    # Exibe no console os valores RGB da última detecção da boca
                    print(f"Cor média da boca detectada - R: {int(feedback_atual[2])}, G: {int(feedback_atual[1])}, B: {int(feedback_atual[0])}")
                else:
                    print("Nenhuma detecção realizada para exibir.")

            # Permite sair do loop pressionando a tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Libera a webcam e fecha todas as janelas abertas ao final da execução
        captura_de_video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Executa a função principal
    main()
