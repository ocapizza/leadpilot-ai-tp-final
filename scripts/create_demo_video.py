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
            "Demo de entrega",
            [
                "Automatizacion de gestion de leads B2B con Gmail, Airtable, OpenAI y n8n.",
                "El flujo registra, clasifica, solicita aprobacion humana y deja trazabilidad.",
                "OpenAI queda listo para que el profesor conecte su propia API key.",
            ],
            (36, 110, 185),
        ),
        20,
    ),
    (
        image_slide(
            "Arquitectura",
            "01_diagrama_arquitectura.png",
            "Gmail dispara el flujo. n8n orquesta. Airtable funciona como memoria operativa. OpenAI clasifica y redacta. Gmail resuelve la aprobacion humana y la respuesta final.",
        ),
        25,
    ),
    (
        image_slide(
            "Workflow n8n",
            "02_flujo_n8n_evidencia.png",
            "El workflow incluye trigger, normalizacion, registro en Airtable, clasificacion IA, control de datos faltantes, aprobacion HITL y rutas de cierre.",
        ),
        30,
    ),
    (
        image_slide(
            "Base Airtable",
            "03_airtable_schema_evidencia.png",
            "La base tiene tablas Leads, Clientes y Errores. Permite seguir estados, decision humana, score de IA, hilo de Gmail y errores.",
        ),
        25,
    ),
    (
        image_slide(
            "Pruebas",
            "04_test_estres_evidencia.png",
            "Se documentaron casos de prueba para lead completo, datos faltantes, rechazo humano, error de API y control anti bucle.",
        ),
        25,
    ),
    (
        text_slide(
            "Estado final",
            [
                "GitHub esta actualizado con README, workflow n8n, esquema Airtable, prompt y evidencias.",
                "Airtable ya esta creado y conectado con credencial PAT.",
                "Gmail ya esta conectado en n8n.",
                "Solo falta que el profesor agregue su credencial OpenAI para ejecutar end-to-end.",
            ],
            (35, 139, 91),
        ),
        25,
    ),
    (
        text_slide(
            "Links para correccion",
            [
                "Repositorio: https://github.com/ocapizza/leadpilot-ai-tp-final",
                "Airtable Leads: https://airtable.com/appRAWorY6yPb4QJn/tblEx4UKF4j0bkVvr/viwd1TlkGIsdGkjva",
                "n8n Cloud: https://delroy2026.app.n8n.cloud/workflow/qSfCEYFOYzLFvlGc?projectId=KJrQfW9cIoac0mkH",
            ],
            (86, 99, 190),
        ),
        30,
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
