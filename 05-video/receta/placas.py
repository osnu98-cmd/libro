from PIL import Image, ImageDraw, ImageFont
F="fuentes/Outfit-Bold.ttf"
W,H=720,1280; BASE_Y=1152; ANCHO_MAX=704
def placa(txt, archivo, tam=196, pad_x=20, pad_y=14):
    txt=txt.upper()
    f=ImageFont.truetype(F,tam)
    ref=f.getbbox("ÁÑQM")                 # altura fija para todas las placas
    top,bot=ref[1],ref[3]; alto=bot-top
    bb=f.getbbox(txt); tw=bb[2]-bb[0]
    cap=Image.new("RGBA",(tw+8,alto+8),(0,0,0,0))
    ImageDraw.Draw(cap).text((-bb[0]+4,-top+4),txt,font=f,fill=(16,16,16,255))
    disp=ANCHO_MAX-2*pad_x
    if cap.width>disp: cap=cap.resize((disp,cap.height),Image.LANCZOS)
    pw,ph=cap.width+2*pad_x, cap.height+2*pad_y
    card=Image.new("RGBA",(pw,ph),(0,0,0,0))
    ImageDraw.Draw(card).rounded_rectangle([0,0,pw-1,ph-1],radius=14,fill=(255,255,255,248))
    card.alpha_composite(cap,(pad_x,pad_y))
    l=Image.new("RGBA",(W,H),(0,0,0,0))
    l.alpha_composite(card,((W-pw)//2, BASE_Y-ph))
    l.save(archivo); return pw,ph
