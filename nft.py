from PIL import Image, ImageDraw, ImageChops
import random

def mudar_cor():
    return(random.randint(0,255),random.randint(0,255),random.randint(0,255))

def entre_cor(inicio_cor, final_cor, factor:float ):
    result = 1 - factor
    return(
        int(inicio_cor[0]* result + final_cor[0]*factor),
        int(inicio_cor[1]* result + final_cor[1]*factor),
        int(inicio_cor[2]* result + final_cor[2]*factor),
    )

def gerar(path:str):
    print("passo em python 2022")
    
    img_size_px = 128
    padding_px = 16
    img_bg_color = (0,0,0)

    inicio_cor = mudar_cor()
    final_cor = mudar_cor()

    image = Image.new("RGB",size = (img_size_px, img_size_px),color = (img_bg_color))

    draw = ImageDraw.Draw(image)

    pontos = []

   
    for _ in range(10):
        random_ponto = (
            random.randint(padding_px , img_size_px - padding_px ),
            random.randint(padding_px , img_size_px - padding_px ),

        )
        pontos.append(random_ponto)

    min_x = min([p[0] for p in pontos])
    max_x = max([p[0] for p in pontos])
    min_y = min([p[1] for p in pontos])
    max_y = max([p[1] for p in pontos])
    
    delta_x = min_x -(img_size_px - min_x)
    delta_y = min_y -(img_size_px - max_y)

    for i , ponto in enumerate(pontos):
        pontos[i] = (ponto[0] - delta_x // 2, ponto[1]- delta_y // 2)
    #draw.rectangle((min_x,min_y,max_x,max_y), outline =(0,0,255))


    thickness = 0
    n_pontos = len(pontos)- 1

    for i, ponto in enumerate(pontos):

        coberta_image = Image.new("RGB",size = (img_size_px, img_size_px),color = (img_bg_color))
        coberta_draw = ImageDraw.Draw(coberta_image)

        ponto1 = ponto
        if i == n_pontos:
            ponto2 = pontos[0]
        else:
            ponto2 = pontos[i+1]

        line_xy = ((ponto1, ponto2))
        color_factor = i / n_pontos
        line_color = entre_cor(inicio_cor, final_cor, color_factor )
        thickness += 1
        coberta_draw.line(line_xy, fill = line_color , width = thickness)
        image = ImageChops.add(image, coberta_image)
   
    image.save(path)

if __name__ == "__main__":
    for i in range(10):#Gerando 10 imagens
        gerar(f"teste_image_{i}.png")  

