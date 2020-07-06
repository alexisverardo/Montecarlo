import numpy as np
import matplotlib.pyplot as pyplot
import math

def readAndTransformTxt():
    archivo = open("practica_datosPracticaMontecarlo.txt", 'r')
    datos = []
    for linea in archivo.readlines():
        divido = linea.split('	')
        datos.append(int(divido[1].rstrip("\n")))
    archivo.close()
    return datos
def datosEstadisticos(visitas):
    media = np.mean(visitas)
    varianza = np.var(visitas)
    desviacion = np.std(visitas)

    return {
        'media': media,
        'varianza': varianza,
        'desviacion': desviacion
    }
def distribucionNormal(desviacion, media):
    vis_min = min(visitas)
    vis_max = max(visitas)
    distr_norm = []
    for values in range(vis_min, vis_max):
        den = desviacion * math.sqrt(2 * 3.14159)
        miem = pow(2.71828, -0.5 * pow((values - media) / desviacion, 2))
        distr_norm.append(round((1 / den) * miem, 3))  # Calculo de Distr. Norm manualmente

    return distr_norm

def distribucionAcumulada(distr_norm):
    acum = 0
    distr_acum = []
    for ac in range(0, 40):
        acum = acum + distr_norm[ac]
        distr_acum.append(round(acum, 2))
    return distr_acum


def graficoNormal(distr_norm):
    pyplot.subplot(212)
    pyplot.plot(distr_norm, color='blue', linewidth=3)
    pyplot.grid(True)
    pyplot.title('Distribucion Normal')
    pyplot.savefig('normal.png')
    pyplot.close()
def graficoAcumulado(distr_acum):
    pyplot.subplot(211)
    pyplot.plot(distr_acum, color='red', linewidth=3)
    pyplot.grid(True)
    pyplot.title('Distribucion Acumulada')
    pyplot.savefig('acumulada.png')
    pyplot.close()

visitas = readAndTransformTxt()
estadisticas = datosEstadisticos(visitas)

print("Calculos Estadisticos")
print("Media: %.3f " % estadisticas['media'] + "Varianza: %.3f " % estadisticas['varianza'] + "Desviacion: %.3f " % estadisticas['desviacion'])
distr_norm = distribucionNormal(estadisticas['desviacion'], estadisticas['media'])
print("Distribucion Normal")
print(distr_norm)

distr_acum = distribucionAcumulada(distr_norm)
print("Distribucion Acumulada")
print(distr_acum)

# Graficos
graficoNormal(distr_norm)
graficoAcumulado(distr_acum)