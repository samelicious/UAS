from email.policy import default
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def  __str__(self):
        return self.nama


class Barang(models.Model):
    Kodebrng = models.CharField(max_length=8, default='BRG')
    Nama = models.CharField(max_length=50)
    stock=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank = True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self) :
        return "{}.{}.{}".format(self.Kodebrng,self.Nama,self.harga)

class Karyawan(models.Model):
    NA = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    jobdesc = models.CharField(max_length=15)
    umur = models.IntegerField()
    jeniskelamin = models.CharField(max_length=10)
    alamat = models.CharField(max_length=50)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self) :
        return "{}.{}.{}".format(self.NA,self.nama,self.jobdesc)

class Order(models.Model):
    produk = models.CharField(max_length=10)
    satuan = models.IntegerField()
    jumlah = models.BigIntegerField()
    waktu_order=models.DateTimeField(auto_now_add=True)
    gbr_produk = models.CharField(max_length=150, blank = True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)
    

    def __str__(self) :
        return "{}.{}.{}".format(self.produk,self.jumlah,self.waktu_order)

class Transaksi(models.Model):
    kodetrans=models.CharField(max_length=10)
    tgltrans=models.DateTimeField(auto_now_add=True)
    total=models.BigIntegerField()

    def __str__(self):
        return self.kodetrans

class Detailtrans(models.Model):
    kodetrans=models.CharField(max_length=10)
    kodebrg=models.CharField(max_length=8)
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()

    def __str__(self):
        return "{}.{}".format(self.kodetrans,self.kodebrg)
    
