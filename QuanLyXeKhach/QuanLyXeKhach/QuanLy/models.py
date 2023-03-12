from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_nhaxe = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=150, blank=True)

class NhaXe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nhaxe')
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d')
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

class TuyenXe(models.Model):
    nhaxe = models.ForeignKey(NhaXe, on_delete=models.CASCADE, related_name='tuyenxe')
    diem_di = models.CharField(max_length=255)
    diem_den = models.CharField(max_length=255)

class ChuyenXe(models.Model):
    tuyenxe = models.ForeignKey(TuyenXe, on_delete=models.CASCADE, related_name='chuyenxe')
    nhaxe = models.ForeignKey(NhaXe, on_delete=models.CASCADE, related_name='chuyenxe')
    gio_di = models.DateTimeField()
    gio_den = models.DateTimeField()
    gia_ve = models.FloatField(default=0)
    so_luong_ve = models.IntegerField(default=0)

class VeXe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vexe')
    chuyenxe = models.ForeignKey(ChuyenXe, on_delete=models.CASCADE, related_name='vexe')
    ngay_dat_ve = models.DateTimeField(auto_now_add=True)
    thanhtoan_online = models.BooleanField(default=False)
    da_nhan_ve = models.BooleanField(default=False)

class GiaoHang(models.Model):
    ten_nguoi_gui = models.CharField(max_length=255)
    sdt_nguoi_gui = models.CharField(max_length=15)
    email_nguoi_gui = models.EmailField()
    ten_nguoi_nhan = models.CharField(max_length=255)
    sdt_nguoi_nhan = models.CharField(max_length=15)
    email_nguoi_nhan = models.EmailField()
    # nhaxe = models.ForeignKey(NhaXe, on_delete=models.CASCADE, related_name='nhaxe')
    # chuyenxe = models.ForeignKey(ChuyenXe, on_delete=models.CASCADE, related_name='chuyenxe')
    thoigian_vanchuyen = models.DateTimeField(auto_now_add=True)
    is_received = models.BooleanField(default=False)


class DoanhThu(models.Model):
    # nhaxe = models.ForeignKey(NhaXe, on_delete=models.CASCADE, related_name='nhaxe')
    # chuyenxe = models.ForeignKey(ChuyenXe, on_delete=models.CASCADE, related_name='chuyenxe')
    doanh_thu_ngay = models.DateField()
    doanh_thu_thang = models.DecimalField(max_digits=7, decimal_places=2)




