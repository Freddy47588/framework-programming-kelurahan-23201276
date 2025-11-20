from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
# from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets # Impor viewsets
from .serializers import WargaSerializer
from .models import Warga



# --- API VIEWS ---
# class WargaListAPIView(ListAPIView):
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer

# class WargaDetailAPIView(RetrieveAPIView):
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer

# class PengaduanListAPIView(ListAPIView):
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer

# class PengaduanDetailAPIView(RetrieveAPIView):
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer


class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer


class WargaPengaduanSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer


class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')
    
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'
    ordering = ['nama_lengkap']

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'warga'

    def get_queryset(self):
        return Warga.objects.prefetch_related('pengaduan')

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'
    ordering = ['-tanggal_lapor']

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')
