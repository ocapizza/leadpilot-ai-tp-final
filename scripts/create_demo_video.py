from pathlib import Path
import textwrap

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
EVIDENCIAS = ROOT / "evidencias"
OUT = EVIDENCIAS / "demo_leadpilot_ai.mp4"
W, H = 1280, 720
FPS = 24


def font(size, bold=False):
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for p in candidates:
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


FONT_TITLE = font(52, True)
FONT_SUBTITLE = font(30)
FONT_BODY = font(28)
FONT_SMALL = font(22)


def draw_wrapped(draw, text, xy, width, font_obj, fill, line_gap=10):
    x, y = xy
    avg = max(font_obj.getlength("abcdefghijklmnopqrstuvwxyz") / 26, 1)
    chars = max(int(width / avg), 10)
    lines = []
    for paragraph in text.split("\n"):
        lines.extend(textwrap.wrap(paragraph, width=chars) or [""])
    for line in lines:
        draw.text((x, y), line, font=font_obj, fill=fill)
        y += font_obj.size + line_gap
    return y


def base(bg=(246, 248, 251)):
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 92), fill=(20, 36, 50))
    d.text((56, 26), "LeadPilot AI - TP Final AI Automation", font=FONT_SUBTITLE, fill=(255, 255, 255))
    d.rectangle((56, 640, W - 56, 644), fill=(36, 110, 185))
    d.text((56, 660), "GitHub: github.com/ocapizza/leadpilot-ai-tp-final", font=FONT_SMALL, fill=(62, 73, 88))
    return img


def text_slide(title, bullets, accent=(36, 110, 185)):
    img = base()
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((56, 130, 1224, 600), radius=18, fill=(255, 255, 255), outline=(221, 228, 236), width=2)
    d.rectangle((56, 130, 72, 600), fill=accent)
    d.text((104, 170), title, font=FONT_TITLE, fill=(20, 36, 50))
    y = 260
    for b in bullets:
        d.ellipse((108, y + 10, 122, y + 24), fill=accent)
        y = draw_wrapped(d, b, (140, y), 960, FONT_BODY, (38, 49, 64), 8) + 16
    return img


def image_slide(title, image_name, caption):
    img = base()
    d = ImageDraw.Draw(img)
    d.text((56, 116), title, font=FONT_TITLE, fill=(20, 36, 50))
    src = Image.open(EVIDENCIAS / image_name).convert("RGB")
    max_w, max_h = 720, 420
    src.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    x = 56
    y = 215
    d.rounded_rectangle((x - 12, y - 12, x + src.width + 12, y + src.height + 12), radius=12, fill=(255, 255, 255), outline=(221, 228, 236), width=2)
    img.paste(src, (x, y))
    draw_wrapped(d, caption, (840, 230), 360, FONT_BODY, (38, 49, 64), 8)
    return img


slides = [
    (
        text_slide(
            "Video demo - LeadPilot AI",
            [
                "Objetivo: demostrar el flujo completo sin exponer API keys ni credenciales.",
                "Recorrido del demo: Trigger en Gmail, procesamiento en n8n y resultado final registrado.",
                "Duracion preparada para la consigna: 3 minutos.",
            ],
            (36, 110, 185),
        ),
        16,
    ),
    (
        image_slide(
            "1. Trigger",
            "02_flujo_n8n_evidencia.png",
            "El flujo comienza con el nodo Gmail Trigger. Escucha correos recientes con asuntos relacionados a Lead, Consulta o Presupuesto. El filtro temporal newer_than:1d ayuda a evitar reprocesos y bucles.",
        ),
        25,
    ),
    (
        text_slide(
            "Entrada esperada",
            [
                "Un potencial cliente envia un email con nombre, email, asunto y mensaje comercial.",
                "El trigger toma el correo y entrega esas variables al orquestador.",
                "No se muestran credenciales ni configuraciones sensibles durante el demo.",
            ],
            (36, 110, 185),
        ),
        18,
    ),
    (
        image_slide(
            "2. Procesamiento en n8n",
            "02_flujo_n8n_evidencia.png",
            "n8n normaliza variables, registra el lead en Airtable, llama a OpenAI para clasificar y redactar, evalua datos faltantes con IF y deriva a la ruta correcta.",
        ),
        30,
    ),
    (
        image_slide(
            "Human-in-the-loop",
            "01_diagrama_arquitectura.png",
            "Antes de contactar al cliente, el flujo solicita aprobacion humana por Gmail. Si se aprueba, envia la respuesta final; si se rechaza, registra la decision y no contacta al lead.",
        ),
        24,
    ),
    (
        image_slide(
            "3. Resultado final",
            "03_airtable_schema_evidencia.png",
            "El resultado queda trazado en Airtable: estado del lead, score de IA, prioridad, thread de Gmail, decision humana, respuesta sugerida y errores cuando corresponde.",
        ),
        26,
    ),
    (
        image_slide(
            "Camino infeliz",
            "04_test_estres_evidencia.png",
            "El test de estres incluye datos incompletos, rechazo humano y fallas controladas. Esos casos verifican filtros, rutas de error y trazabilidad.",
        ),
        21,
    ),
    (
        text_slide(
            "Cierre de demo",
            [
                "Entregables: PDF de arquitectura, JSON de n8n, link de Airtable en README, capturas y video.",
                "Seguridad: no hay API keys en GitHub ni en el video.",
                "OpenAI queda listo para que el profesor conecte su propia API key durante la correccion.",
            ],
            (35, 139, 91),
        ),
        20,
    ),
]


def main():
    EVIDENCIAS.mkdir(exist_ok=True)
    with imageio.get_writer(str(OUT), fps=FPS, codec="libx264", quality=8, macro_block_size=16) as writer:
        for slide, seconds in slides:
            frame = slide.convert("RGB")
            for _ in range(seconds * FPS):
                writer.append_data(np.asarray(frame))
    print(OUT)


if __name__ == "__main__":
    main()
