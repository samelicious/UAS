from django.shortcuts import render,redirect
from dashboard.form import FormBarang,FormKaryawan,FormOrder
from dashboard.models import Barang,Karyawan,Order
from django.contrib import messages
# Create your views here.
def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs
    }
    return render(request,'tampil_brg.html',konteks)

def Karyawan_View(request):
    karyawans=Karyawan.objects.all()

    konteks={
        'karyawans':karyawans
        }
    return render(request,'tampil_brg2.html',konteks)

def Order_View(request):
    orders=Order.objects.all()

    konteks={
        'orders':orders
    }
    return render(request,'tampil_brg3.html',konteks)

def tambah_barang(request):
    if request.POST:
        form= FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil!")
            form = FormBarang()
            konteks = {
                'form': form,
            }
            return render(request, 'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks={
            'form':form,
        }
    return render(request,'tambah_barang.html',konteks)

def tambah_karyawan(request):
    if request.POST:
        form= FormKaryawan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil!")
            form = FormKaryawan()
            konteks = {
                'form': form,
            }
            return render(request, 'tambah_karyawan.html',konteks)
    else:
        form=FormKaryawan()
        konteks={
            'form':form,
        }
    return render(request,'tambah_karyawan.html',konteks)

def tambah_order(request):
    if request.POST:
        form= FormOrder(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil!")
            form = FormOrder()
            konteks = {
                'form': form,
            }
            return render(request, 'tambah_order.html',konteks)
    else:
        form=FormOrder()
        konteks={
            'form':form,
        }
    return render(request,'tambah_order.html',konteks)


def produk (request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html',konteks)

def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs':barangs
        }
    return render(request,'ubah_brg.html',konteks)

def ubah_karyawan(request,id_karyawan):
    karyawans=Karyawan.objects.get(id=id_karyawan)
    if request.POST:
        form=FormKaryawan(request.POST,instance=karyawans)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil diubah")
            return redirect('ubah_karyawan',id_karyawan=id_karyawan)
    else:
        form=FormKaryawan(instance=karyawans)
        konteks = {
            'form':form,
            'karyawans':karyawans
        }
    return render(request,'ubah_karyawan.html',konteks)

def ubah_order(request,id_order):
    orders=Order.objects.get(id=id_order)
    if request.POST:
        form=FormOrder(request.POST,instance=orders)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil diubah")
            return redirect('ubah_order',id_order=id_order)
    else:
        form=FormOrder(instance=orders)
        konteks = {
            'form':form,
            'orders':orders
        }
    return render(request,'ubah_order.html',konteks)

def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data Terhapus")
    return redirect('barang_view')

def hapus_karyawan(request,id_karyawan):
    karyawans=Karyawan.objects.filter(id=id_karyawan)
    karyawans.delete()
    messages.success(request,"Data Terhapus")
    return redirect('karyawan_view')

def hapus_order(request,id_order):
    orders=Order.objects.filter(id=id_order)
    orders.delete()
    messages.success(request,"Data Terhapus")
    return redirect('order_view')