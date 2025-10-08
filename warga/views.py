from django.views.generic import ListView, DetailView
from .models import Warga

class WargaListView(ListView):
    model = Warga  # template default: warga/warga_list.html
    
class WargaDetailView(DetailView):
    model = Warga  # template default: warga/warga_detail.html

