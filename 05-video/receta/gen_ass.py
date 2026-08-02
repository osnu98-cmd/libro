import unicodedata
from PIL import ImageFont
FUENTE="fuentes/Outfit-Bold.ttf"
BASE=142; TOPE=240; MARGEN=16; ADELANTO=0.20; ANCHO=720-2*MARGEN-6
AC=r"\c&H00C8FF&"; BL=r"\c&HFFFFFF&"
_c={}
def _f(s):
    if s not in _c: _c[s]=ImageFont.truetype(FUENTE,s)
    return _c[s]
def ancho(t,s): return _f(s).getlength(t)
def caber(t, tope, ancho_max, piso_sx):
    s=tope
    while s>110:
        r=ancho_max/ancho(t,s)
        if r>=piso_sx: return s, int(min(100,r*100))
        s-=4
    return 110, int(min(100, ancho_max/ancho(t,110)*100))
def norm(w):
    w="".join(c for c in unicodedata.normalize("NFD",w.lower()) if unicodedata.category(c)!="Mn")
    return "".join(c for c in w if c.isalnum())
LIMPIA=".,;:¿¡—–-«»\"'"   # el ? y el ! se conservan: son parte del sentido

CAB=f"""[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Sub,Outfit,{BASE},&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,9,5,2,{MARGEN},{MARGEN},132,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""

def construir(bloques, salida, claves=(), nombres=(), max_pal=3):
    claves={norm(k) for k in claves}; nombres={norm(k) for k in nombres}
    palabras=[]; lim=[]; n=0; usados=set()
    for spans, txt in bloques:
        ws=txt.split(); total=sum(b-a for a,b in spans)
        peso=[len(w)+1.6 for w in ws]; tp=sum(peso)
        t=0.0; marcas=[]
        for p in peso:
            marcas.append((t,t+total*p/tp)); t+=total*p/tp
        def real(x, spans=spans):
            acc=0.0
            for a,b in spans:
                d=b-a
                if x<=acc+d+1e-9: return a+(x-acc)
                acc+=d
            return spans[-1][1]
        for w,(a,b) in zip(ws,marcas):
            k=norm(w)
            t=""
            if k in nombres and k not in usados: t="nombre"; usados.add(k)
            elif k in claves and k not in usados: t="clave"; usados.add(k)
            palabras.append({"w":w,"a":real(a),"b":real(b),"t":t})
        n+=len(ws); lim.append(n)
    # trozos por ANCHO MEDIDO, no por número de letras: así ningún trozo se achica
    CH=[]; buf=[]
    def cabe(b, extra):
        return ancho(" ".join(x["w"] for x in b+[extra]), BASE) <= ANCHO
    for i,p in enumerate(palabras):
        if p["t"]:
            if buf: CH.append(buf); buf=[]
            CH.append([p]); continue
        if buf and (len(buf)>=max_pal or not cabe(buf,p)):
            CH.append(buf); buf=[]
        buf.append(p)
        if (i+1) in lim: CH.append(buf); buf=[]
    if buf: CH.append(buf)
    for i,ch in enumerate(CH):
        if len(ch)==1 and ch[0]["t"]:
            fin = CH[i+1][0]["a"] if i+1<len(CH) else ch[0]["b"]+0.5
            ch[0]["b"]=min(max(ch[0]["b"], ch[0]["a"]+0.55), fin)
    def ts(t):
        t=max(0.0,t-ADELANTO)
        return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
    ev=[]; info=[]; placas=[]; condensados=0
    for ch in CH:
        if len(ch)==1 and ch[0]["t"]:
            p=ch[0]; txt=p["w"].upper().strip(LIMPIA)
            if p["t"]=="nombre":
                placas.append([norm(txt), round(p["a"],2), round(p["b"],2)])
                continue          # las placas se dibujan aparte
            s,sx=caber(txt, TOPE, ANCHO, 0.62)
            info.append((txt,s,sx))
            ev.append(f"Dialogue: 0,{ts(p['a'])},{ts(p['b'])},Sub,,0,0,0,,"
                      f"{{\\fs{s}\\fscx{int(sx*0.93)}\\fscy93\\t(0,80,\\fscx{sx}\\fscy100)\\c&H00C8FF&\\fad(45,80)}}{txt}")
            continue
        plano=" ".join(x["w"] for x in ch)
        # altura SIEMPRE 142; si no cabe a lo ancho, se condensa
        w=ancho(plano,BASE); sx=100
        if w>ANCHO:
            sx=int(ANCHO/w*100); condensados+=1
        for i,wd in enumerate(ch):
            a,b=wd["a"],wd["b"]
            if b-a<0.06: b=a+0.06
            if i==0:
                ini=int(sx*0.96)
                pre=(f"{{\\fscx{ini}\\fscy96\\t(0,70,\\fscx{sx}\\fscy100)}}")
            else:
                pre=f"{{\\fscx{sx}\\fscy100}}"
            linea=pre+"".join("{"+(AC if j==i else BL)+"}"+x["w"]+" " for j,x in enumerate(ch)).strip()
            ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},Sub,,0,0,0,,{linea}")
    open(salida,"w").write(CAB+"\n".join(ev)+"\n")
    return len(CH), info, condensados, placas
