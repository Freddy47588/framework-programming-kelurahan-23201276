from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView  # pastikan diimport
from .models import Warga, Pengaduan
from .forms import WargaForm

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'  # pakai form yang sama dari modul 3
    success_url = reverse_lazy('warga-list')


class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'


class WargaListView(ListView):
    model = Warga  # template default: warga/warga_list.html


class WargaDetailView(DetailView):
    model = Warga  # template default: warga/warga_detail.html



class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')


class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')
