import base64
import matplotlib.pyplot as plt
from io import BytesIO
from django.views import generic
from .models import Votacion

class IndexView(generic.TemplateView):
    template_name = "graphic.html"
    context_data = ""

    def generate_pie_chart(self, votaciones):
        anios = [votacion.anio for votacion in votaciones]
        partidos = [votacion.partido for votacion in votaciones]
        votos = [votacion.voto for votacion in votaciones]

        colors = ['red', 'blue', 'green','orange', 'pink']
        explode = (0.1, 0.1, 0.1, 0.2,0.1)

        # plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), dpi=100)

        # Gráfico de pastel
        patches, texts, autotexts = ax1.pie(votos, labels=partidos, colors=colors, autopct='%1.1f%%', explode=explode,
                                             shadow=True, startangle=360, wedgeprops={"linewidth": 2, "edgecolor": "white"})
        ax1.add_artist(plt.Circle((0, 0), 0))

        # Añadir la leyenda con el número de votos en el gráfico de pastel
        for autotext, voto in zip(autotexts, votos):
            autotext.set_color('white')  # Establecer el color del texto a blanco
            autotext.set_fontsize(10)     # Establecer el tamaño de la fuente del texto
            

        # Gráfico de barras
        ax2.bar(partidos, votos, color=colors)
        ax2.set_xlabel('Partido')
        ax2.set_ylabel('Cantidad de votos')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')

        return graphic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        votaciones = Votacion.objects.all()
        context['graphic'] = self.generate_pie_chart(votaciones)
        return context