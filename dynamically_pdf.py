from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm, inch
from reportlab.lib.pagesizes import A4

ticket = (75*mm,297*mm)

c = canvas.Canvas('prueba.pdf', pagesize=ticket, bottomup=0)
textOb = c.beginText()
textOb.setTextOrigin(cm,cm)
textOb.setFont("Times-Roman", 9)

lines = [
    "PARROQUIA ECLESIÁSTICA",
    "NUESTRA SEÑORA DE LA ALBORADA",
    "AV. JOSE MARÍA EGAS Y AV. RODOLFO BAQUERIZO NAZUR",
    "RUC:0992206098001",
    "DETALLE DE COMPROBANTE NO TRIBUTARIO",
    "RESOLUCIÓN Nº NAC-DGERCGC12-00105",
    "CÓDIGO DESCRIPCIÓN CANT P.UNIT. VALOR",
    "-------------------------------------",
    "LÍNEA 8",
    "LÍNEA 9",
    "LÍNEA 10",
    "LÍNEA 11",
    "LÍNEA 12",
    "LÍNEA 13",
    "LÍNEA 14",
    "LÍNEA 15",
    "LÍNEA 16",
    "LÍNEA 17",
    "LÍNEA 18",
    "LÍNEA 19",
    "LÍNEA 20",
    "LÍNEA 21",
    "LÍNEA 22",
    "LÍNEA 23",
    "LÍNEA 24",
    "LÍNEA 25",
    "LÍNEA 26",
    "LÍNEA 27",
    "LÍNEA 28",
    "LÍNEA 29",
    "LÍNEA 30",
    "LÍNEA 31",
    "LÍNEA 32",
    "LÍNEA 33",
    "LÍNEA 34",
    "LÍNEA 35",
    "LÍNEA 36",
    "LÍNEA 37",
    "LÍNEA 38",
    "LÍNEA 39",
    "LÍNEA 40",
    "LÍNEA 41",
    "LÍNEA 42",
    "LÍNEA 43",
    "LÍNEA 44",
    "LÍNEA 45",
    "LÍNEA 46",
    "LÍNEA 47",
    "LÍNEA 48",
    "LÍNEA 49",
    "LÍNEA 50",
   
]

for count, line in enumerate(lines, start=1):
    textOb.textLine(line)
    if count %10 == 0:
        c.drawText(textOb)
        c.showPage()
c.save()