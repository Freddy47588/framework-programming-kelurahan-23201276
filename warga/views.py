from django.views.generic import ListView, DetailView
from .models import Warga, Pengaduan

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'

class WargaListView(ListView):
    model = Warga  # template default: warga/warga_list.html
    
class WargaDetailView(DetailView):
    model = Warga  # template default: warga/warga_detail.html

