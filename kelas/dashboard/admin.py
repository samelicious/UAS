from atexit import register
from django.contrib import admin

# Register your models here.
from .models import Barang,Karyawan,Order,Detailtrans,Transaksi,Jenis

class kolomBarang(admin.ModelAdmin):
    list_display=['Kodebrng','Nama','stock','harga','link_gbr','jenis_id']
    search_fields=['Kodebrng','Nama']
    list_filter=['jenis_id']
    list_per_page=5

class kolomKaryawan(admin.ModelAdmin):
    list_display=['NA','nama','jobdesc','umur','jeniskelamin','alamat','jenis_id']
    search_fields=['NA','nama']
    list_filter=['jobdesc','jenis_id']
    list_per_page=5

admin.site.register(Barang)
admin.site.register(Karyawan)
admin.site.register(Order)
admin.site.register(Detailtrans)
admin.site.register(Transaksi)
admin.site.register(Jenis)