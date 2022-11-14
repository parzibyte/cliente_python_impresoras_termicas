import requests

URL_PLUGIN_POR_DEFECTO = "http://localhost:8000"
TAMAÑO_IMAGEN_NORMAL = 0
TAMAÑO_IMAGEN_DOBLE_ANCHO = 1
TAMAÑO_IMAGEN_DOBLE_ALTO = 2
TAMAÑO_IMAGEN_DOBLE_ANCHO_Y_ALTO = 3
ALINEACION_IZQUIERDA = 0
ALINEACION_CENTRO = 1
ALINEACION_DERECHA = 2
RECUPERACION_QR_BAJA = 0
RECUPERACION_QR_MEDIA = 1
RECUPERACION_QR_ALTA = 2
RECUPERACION_QR_MEJOR = 3


class ConectorV3:

    def __init__(self, ruta=URL_PLUGIN_POR_DEFECTO, serial=""):
        self.operaciones = []
        self.ruta = ruta
        self.serial = serial

    def agregar_operacion(self, nombre, argumentos):
        self.operaciones.append({
            "nombre": nombre,
            "argumentos": argumentos,
        })

    def obtenerImpresoras(ruta=URL_PLUGIN_POR_DEFECTO):
        respuesta = requests.get(ruta+"/impresoras")
        return respuesta.json()

    def CargarImagenLocalEImprimir(self, ruta: str, tamaño: float, maximoAncho: float):
        return self.agregar_operacion("CargarImagenLocalEImprimir", [ruta, tamaño, maximoAncho])

    def Corte(self, lineas):
        return self.agregar_operacion("Corte", [lineas])

    def CorteParcial(self):
        return self.agregar_operacion("CorteParcial", [])

    def DefinirCaracterPersonalizado(self, caracterRemplazoComoCadena: str, matrizComoCadena: str):
        return self.agregar_operacion("DefinirCaracterPersonalizado", [caracterRemplazoComoCadena, matrizComoCadena])

    def DescargarImagenDeInternetEImprimir(self, urlImagen: str, tamaño: float, maximoAncho: float):
        return self.agregar_operacion("DescargarImagenDeInternetEImprimir", [urlImagen, tamaño, maximoAncho])

    def DeshabilitarCaracteresPersonalizados(self, ):
        return self.agregar_operacion("DeshabilitarCaracteresPersonalizados", [])

    def DeshabilitarElModoDeCaracteresChinos(self, ):
        return self.agregar_operacion("DeshabilitarElModoDeCaracteresChinos", [])

    def EscribirTexto(self, texto: str):
        return self.agregar_operacion("EscribirTexto", [texto])

    def EstablecerAlineacion(self, alineacion: float):
        return self.agregar_operacion("EstablecerAlineacion", [alineacion])

    def EstablecerEnfatizado(self, enfatizado: bool):
        return self.agregar_operacion("EstablecerEnfatizado", [enfatizado])

    def EstablecerFuente(self, fuente: float):
        return self.agregar_operacion("EstablecerFuente", [fuente])

    def EstablecerImpresionAlReves(self, alReves: bool):
        return self.agregar_operacion("EstablecerImpresionAlReves", [alReves])

    def EstablecerImpresionBlancoYNegroInversa(self, invertir: bool):
        return self.agregar_operacion("EstablecerImpresionBlancoYNegroInversa", [invertir])

    def EstablecerRotacionDe90Grados(self, rotar: bool):
        return self.agregar_operacion("EstablecerRotacionDe90Grados", [rotar])

    def EstablecerSubrayado(self, subrayado: bool):
        return self.agregar_operacion("EstablecerSubrayado", [subrayado])

    def EstablecerTamañoFuente(self, multiplicadorAncho: float, multiplicadorAlto: float):
        return self.agregar_operacion("EstablecerTamañoFuente", [multiplicadorAncho, multiplicadorAlto])

    def Feed(self, lineas):
        return self.agregar_operacion("Feed", [lineas])

    def HabilitarCaracteresPersonalizados(self):
        return self.agregar_operacion("HabilitarCaracteresPersonalizados", [])

    def HabilitarElModoDeCaracteresChinos(self):
        return self.agregar_operacion("HabilitarElModoDeCaracteresChinos", [])

    def ImprimirCodigoDeBarrasCodabar(self, contenido: str, alto: float, ancho: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoDeBarrasCodabar", [contenido, alto, ancho, tamañoImagen])

    def ImprimirCodigoDeBarrasCode128(self, contenido: str, alto: float, ancho: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoDeBarrasCode128", [contenido, alto, ancho, tamañoImagen])

    def ImprimirCodigoDeBarrasCode39(self, contenido: str, incluirSumaDeVerificacion: bool, modoAsciiCompleto: bool, alto: float, ancho: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoDeBarrasCode39", [contenido, incluirSumaDeVerificacion, modoAsciiCompleto, alto, ancho, tamañoImagen])

    def ImprimirCodigoDeBarrasCode93(self, contenido: str, alto: float, ancho: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoDeBarrasCode93", [contenido, alto, ancho, tamañoImagen])

    def ImprimirCodigoDeBarrasEan(self, contenido: str, alto: float, ancho: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoDeBarrasEan", [contenido, alto, ancho, tamañoImagen])

    def ImprimirCodigoDeBarrasEan8(self, contenido: str, alto: float, ancho: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoDeBarrasEan8", [contenido, alto, ancho, tamañoImagen])

    def ImprimirCodigoDeBarrasPdf417(self, contenido: str, nivelSeguridad: float, alto: float, ancho: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoDeBarrasPdf417", [contenido, nivelSeguridad, alto, ancho, tamañoImagen])

    def ImprimirCodigoDeBarrasTwoOfFiveITF(self, contenido: str, intercalado: bool, alto: float, ancho: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoDeBarrasTwoOfFiveITF", [contenido, intercalado, alto, ancho, tamañoImagen])

    def ImprimirCodigoDeBarrasUpcA(self, contenido: str, alto: float, ancho: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoDeBarrasUpcA", [contenido, alto, ancho, tamañoImagen])

    def ImprimirCodigoDeBarrasUpcE(self, contenido: str, alto: float, ancho: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoDeBarrasUpcE", [contenido, alto, ancho, tamañoImagen])

    def ImprimirCodigoQr(self, contenido: str, anchoMaximo: float, nivelRecuperacion: float, tamañoImagen: float):
        return self.agregar_operacion("ImprimirCodigoQr", [contenido, anchoMaximo, nivelRecuperacion, tamañoImagen])

    def ImprimirImagenEnBase64(self, imagenCodificadaEnBase64: str, tamaño: float, maximoAncho: float):
        return self.agregar_operacion("ImprimirImagenEnBase64", [imagenCodificadaEnBase64, tamaño, maximoAncho])

    def Iniciar(self, ):
        return self.agregar_operacion("Iniciar", [])

    def Pulso(self, pin: float, tiempoEncendido: float, tiempoApagado: float):
        return self.agregar_operacion("Pulso", [pin, tiempoEncendido, tiempoApagado])

    def TextoSegunPaginaDeCodigos(self, numeroPagina: float, pagina: str, texto: str):
        return self.agregar_operacion("TextoSegunPaginaDeCodigos", [numeroPagina, pagina, texto])

    def imprimirEn(self, nombreImpresora):
        payload = {
            "operaciones": self.operaciones,
            "nombreImpresora": nombreImpresora,
            "serial": self.serial,
        }
        respuesta = requests.post(self.ruta+"/imprimir", json=payload)
        return respuesta.json()
