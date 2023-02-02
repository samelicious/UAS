from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import produk, tambah_barang, Barang_View,Karyawan_View,Order_View,ubah_brg,hapus_brg,tambah_karyawan,tambah_order,ubah_karyawan,hapus_order,ubah_order,hapus_karyawan


def coba1(request):
    return HttpResponse('Hello Felas...')
def coba2(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render (request,'index.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',coba2),
    path('produk/',produk),
    path('addbrng/',tambah_barang),
    path('addbrng2/',tambah_karyawan),
    path('addbrng3/',tambah_order),
    path('Vbrg/',Barang_View,name='barang_view'),
    path('Vbrg2/',Karyawan_View,name='karyawan_view'),
    path('Vbrg3/',Order_View,name='order_view'),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('ubah2/<int:id_karyawan>',ubah_karyawan,name='ubah_karyawan'),
    path('ubah3/<int:id_order>',ubah_order,name='ubah_order'),
    path('hapus/<int:id_barang>',hapus_brg,name='hapus_brg'),
    path('hapus2/<int:id_karyawan>',hapus_karyawan,name='hapus_karyawan'),
    path('hapus3/<int:id_order>',hapus_order,name='hapus_order'),
]
