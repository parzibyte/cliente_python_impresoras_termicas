"""
    Una clase para interactuar con el plugin
    @author parzibyte
    @date 2021-02-11
"""
import json
import requests
"""
    Constantes
"""
AccionTextoConAcentos = "textoacentos"
AccionQrComoImagen = "qrimagen"
AccionImagen = "imagen"
AccionText = "text"
AccionCut = "cut"
AccionPulse = "pulse"
AccionCutPartial = "cutpartial"
AccionJustification = "setJustification"
AccionTextSize = "setTextSize"
AccionFont = "setFont"
AccionEmphasize = "setEmphasis"
AccionFeed = "feed"
AccionQr = "qrCode"
AlineacionCentro = "center"
AlineacionDerecha = "right"
AlineacionIzquierda = "left"
FuenteA = "A"
FuenteB = "B"
FuenteC = "C"
AccionBarcode128 = "barcode128"
AccionBarcode39 = "barcode39"
AccionBarcode93 = "barcode93"
AccionBarcodeItf = "barcodeitf"
AccionBarcodeJan13 = "barcodejan13"
AccionBarcodeJan8 = "barcodejan8"
AccionBarcodeTextAbove = "barcodetextabove"
AccionBarcodeTextBelow = "barcodetextbelow"
AccionBarcodeTextNone = "barcodetextnone"
AccionBarcodeUPCA = "barcodeUPCA"
AccionBarcodeUPCE = "barcodeUPCE"
AccionImagenLocal = "imagenlocal"

URL_PLUGIN_POR_DEFECTO = "http://localhost:8000"


class Operacion:
    def __init__(self, operacion, datos):
        self.operacion = operacion
        self.datos = datos


class Conector:

    def __init__(self, ruta=URL_PLUGIN_POR_DEFECTO):
        self.operaciones = []
        self.ruta = ruta

    def obtenerImpresoras(ruta=URL_PLUGIN_POR_DEFECTO):
        respuesta = requests.get(ruta+"/impresoras")
        return respuesta.json()

    # Función ayudante
    def agregar_operacion(self, accion, datos):
        self.operaciones.append({
            "accion": accion,
            "datos": str(datos),
        })

    def texto(self, texto):
        self.agregar_operacion(AccionText, texto)
        return self

    def textoConAcentos(self, texto):
        self.agregar_operacion(AccionTextoConAcentos, texto)
        return self

    def feed(self, cantidad):
        self.agregar_operacion(AccionFeed, cantidad)
        return self

    def establecerTamanioFuente(self, multiplicadorAncho, multiplicadorAlto):
        self.agregar_operacion(
            AccionTextSize, f"{multiplicadorAncho},{multiplicadorAlto}")
        return self

    def establecerFuente(self, fuente):
        if fuente not in [FuenteA, FuenteB, FuenteC]:
            raise Exception("La fuente no es válida")
        self.agregar_operacion(AccionFont, fuente)
        return self

    def establecerEnfatizado(self, valor):
        if valor not in [0, 1]:
            raise Exception("Valor debe ser 1 o 0")
        self.agregar_operacion(AccionEmphasize, valor)
        return self

    def establecerJustificacion(self, justificacion):
        if justificacion not in [AlineacionCentro, AlineacionDerecha, AlineacionIzquierda]:
            raise Exception("Justificación inválida")
        self.agregar_operacion(AccionJustification, justificacion)
        return self

    def cortar(self):
        self.agregar_operacion(AccionCut, "")
        return self

    def abrirCajon(self):
        self.agregar_operacion(AccionPulse, "")
        return self

    def cortarParcialmente(self):
        self.agregar_operacion(AccionCutPartial, "")
        return self

    def imagenDesdeUrl(self, url):
        self.agregar_operacion(AccionImagen, url)
        return self

    def imagenLocal(self, ubicacion):
        self.agregar_operacion(AccionImagenLocal, ubicacion)
        return self

    def qr(self, contenido):
        self.agregar_operacion(AccionQr, contenido)
        return self

    def qrComoImagen(self, contenido):
        self.agregar_operacion(AccionQrComoImagen, contenido)
        return self

    def validarTipoDeCodigoDeBarras(self, tipo):
        validos = [
            AccionBarcode128,
            AccionBarcode39,
            AccionBarcode93,
            AccionBarcodeItf,
            AccionBarcodeJan13,
            AccionBarcodeJan8,
            AccionBarcodeTextAbove,
            AccionBarcodeTextBelow,
            AccionBarcodeTextNone,
            AccionBarcodeUPCA,
            AccionBarcodeUPCE,
        ]
        if tipo not in validos:
            raise Exception("Código de barras inválido")

    def codigoDeBarras(self, contenido, tipo):
        self.validarTipoDeCodigoDeBarras(tipo)
        self.agregar_operacion(tipo, contenido)

    def imprimirEn(self, nombreImpresora):
        payload = {
            "operaciones": self.operaciones,
            "impresora": nombreImpresora,
        }
        respuesta = requests.post(self.ruta+"/imprimir", json=payload)
        return respuesta.json()
