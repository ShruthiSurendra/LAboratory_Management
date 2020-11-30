from django.contrib import admin
from .models import DoctorRegister
from .models import BloodRegister
from .models import VitaminRegister
from .models import HormoneRegister
from .models import SerologyRegister
from .models import CopdRegister

admin.site.register(HormoneRegister)
admin.site.register(VitaminRegister)
admin.site.register(DoctorRegister)
admin.site.register(BloodRegister)
admin.site.register(SerologyRegister)
admin.site.register(CopdRegister)

