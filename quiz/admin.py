from django.contrib import admin
from .models import Cpu, Disk, Gpu, Ram, Cooler, Case, PSU, MB
# Register your models here.
admin.site.register(Cpu)
admin.site.register(Disk)
admin.site.register(Gpu)
admin.site.register(Ram)
admin.site.register(Cooler)
admin.site.register(Case)
admin.site.register(PSU)
admin.site.register(MB)
