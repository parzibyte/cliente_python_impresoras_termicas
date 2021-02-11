"""
    Script de demostración de uso. Recuerda que debes configurar la impresora y el conector.
    Todo lo encuentras en: https://parzibyte.me/blog/2021/02/09/presentando-plugin-impresoras-termicas-version-2/
"""
from ConectorPlugin import Conector, AccionBarcodeJan13, AlineacionCentro

# Esto es para obtener las impresoras. No es obligatorio hacerlo siempre que se quiera imprimir
impresoras = Conector.obtenerImpresoras()
print(f"Las impresoras son: {impresoras}")

c = Conector()
c.textoConAcentos("¡Me llamo María José!\n")
c.establecerEnfatizado(1)
c.texto("Año 2021\n")
c.establecerEnfatizado(0)
c.texto("Sin enfatizado\n")
c.establecerTamanioFuente(2, 2)
c.texto("Texto de 2, 2\n")
c.establecerTamanioFuente(1, 1)
c.establecerJustificacion(AlineacionCentro)
c.texto("Texto centrado\n")
c.texto("Código de barras:\n")
c.codigoDeBarras("7506129445966", AccionBarcodeJan13)
c.qrComoImagen("Parzibyte")
c.texto("Imagen de URL:\n")
c.imagenDesdeUrl("https://github.com/parzibyte.png")
c.feed(5)
c.cortar()
c.abrirCajon()
# Recuerda cambiar por el nombre de tu impresora
respuesta = c.imprimirEn("POS58")
if respuesta == True:
    print("Impresión correcta")
else:
    print(f"Error. El mensaje es: {respuesta}")
