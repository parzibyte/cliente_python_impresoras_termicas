"""
    Script de demostración de uso. Recuerda que debes configurar la impresora y el conector.
    1. Descarga el conector:  https://github.com/parzibyte/plugin-impresora-termica-v3/releases/latest
    2. Configura tu impresora y compártela: https://parzibyte.me/blog/2017/12/11/instalar-impresora-termica-generica/
    3. Ejecuta el conector (no abre ventanas)
    4. Ejecuta este script.
    Ante cualquier duda: https://parzibyte.me/blog/2021/03/02/python-imprimir-impresora-termica/
"""
import ConectorPython

impresoras = ConectorPython.ConectorV3.obtenerImpresoras()
print("Las impresoras son:")
print(impresoras)

nombreImpresora = "PT210"  # Nota: esta impresora debe existir y estar compartida como se indica en https://parzibyte.me/blog/2017/12/11/instalar-impresora-termica-generica/
# Aquí va tu serial por si tienes uno:
serial = ""

amongUsComoCadena = """000001111000
000010000100
000100011110
000100100001
011100100001
010100100001
010100100001
010100011110
010100000010
011100000010
000100111010
000100101010
000111101110
000000000000
000000000000
000000000000
111010101110
100010101000
111010101110
001010100010
111011101110
000000000000
000000000000
000000000000"""
conector = ConectorPython.ConectorV3(serial=serial)
conector.Iniciar()
conector.DeshabilitarElModoDeCaracteresChinos()
conector.EstablecerAlineacion(ConectorPython.ALINEACION_CENTRO)
conector.DescargarImagenDeInternetEImprimir(
    "http://assets.stickpng.com/thumbs/587e32259686194a55adab73.png", 0, 216)
conector.Feed(1)
conector.EscribirTexto("Parzibyte's blog\n")
conector.EscribirTexto("Blog de un programador\n")
conector.TextoSegunPaginaDeCodigos(2, "cp850", "Teléfono: 123456798\n")
conector.EscribirTexto("Fecha y hora: 29/9/2022")
conector.Feed(1)
conector.EstablecerAlineacion(ConectorPython.ALINEACION_IZQUIERDA)
conector.EscribirTexto("____________________\n")
conector.TextoSegunPaginaDeCodigos(
    2, "cp850", "Venta de plugin para impresoras versión 3\n")
conector.EstablecerAlineacion(ConectorPython.ALINEACION_DERECHA)
conector.EscribirTexto("$25\n")
conector.EscribirTexto("____________________\n")
conector.EscribirTexto("TOTAL: $25\n")
conector.EscribirTexto("____________________\n")
conector.EstablecerAlineacion(ConectorPython.ALINEACION_CENTRO)
conector.HabilitarCaracteresPersonalizados()
conector.DefinirCaracterPersonalizado("$", amongUsComoCadena)
conector.EscribirTexto(
    "En lugar del simbolo de pesos debe aparecer un among us\n")
conector.EscribirTexto("TOTAL: $25\n")
conector.EstablecerEnfatizado(True)
conector.EstablecerTamañoFuente(1, 1)
conector.TextoSegunPaginaDeCodigos(2, "cp850", "¡Gracias por su compra!\n")
conector.Feed(1)
conector.ImprimirCodigoQr("https://parzibyte.me/blog", 160,
                          ConectorPython.RECUPERACION_QR_MEJOR, ConectorPython.TAMAÑO_IMAGEN_NORMAL)
conector.Feed(1)
conector.ImprimirCodigoDeBarrasCode128(
    "parzibyte.me", 80, 192, ConectorPython.TAMAÑO_IMAGEN_NORMAL)
conector.Feed(1)
conector.EstablecerTamañoFuente(1, 1)
conector.EscribirTexto("parzibyte.me\n")
conector.Feed(3)
conector.Corte(1)
conector.Pulso(48, 60, 120)
respuesta = conector.imprimirEn(nombreImpresora)
if respuesta == True:
    print("Impreso correctamente")
else:
    print("Error: " + respuesta)
