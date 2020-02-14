from django.db import models

TAG_CHOICES = (
    ('Core', 'C'),
    ('Speed', 'S'),
    ('Both', 'B')
)

SOCKET_CHOICES = (
    ('AM4', 'AM4'),
    ('1151', '1151'),
    ('2066', '2066'),
    ('TR4', 'TR4'), 
)

TYPE_CHOICES = (
    ('SSD', 'SSD'),
    ('HDD', 'HDD'),
)

SIZE_CHOICES = (
    ('M.2', 'M.2'),
    ('2.5', '2.5'),
    ('PCIe Card', 'PCIe'),
    ('3.5', '3.5'),
)

CHIPSET_CHOICES = (
    ('AMD', 'AMD'),
    ('Nvidia', 'Nvidia')
)

MEMORY_CHOICES = (
    ('GDDR5', 'GDDR5'),
    ('GDDR5X', 'GDDR5X'),
    ('GDDR6', 'GDDR6'),
    ('HBM2', 'HBM2'),
)

GPU_CHOICES = (
    ('Thermals', 'Thermals'),
    ('Performance', 'Perf'),
    ('Price', 'Price')
)

COOLER_SIZE_CHOICES = (
    ('120mm', '120mm'),
    ('140mm', '140mm'),
    ('240mm', '240mm'),
    ('280mm', '280mm'),
    ('Μικρή', 'Μικρή'),
    ('Μεσαία', 'Μεσαία'),
    ('Μεγάλη', 'Μεγάλη'),
)

COOLER_TYPE_CHOICES = (
    ('Απλή χρήση', 'Απλή χρήση'),
    ('Ελαφρύ OC', 'Ελαφρύ OC'),
    ('OC', 'OC')
)

MB_SIZE_CHOICES = (
    ('ATX', 'ATX'),
    ('m-ATX', 'm-ATX'),
    ('mini-ITX', 'mini-ITX')
)

CASE_TYPE_CHOICES = (
    ('Airflow', 'A'),
    ('Silence', 'S'),
    ('Normal', 'N')
)

CERTIFICATE_CHOICES = (
    ('None', 'N'),
    ('80+', '80+'),
    ('Bronze', 'B'),
    ('Silver', 'S'),
    ('Gold', 'G'),
    ('Platinum', 'P'),
    ('Titanium', 'T')
)

MODULAR_CHOICES = (
    ('Full Modular', 'FM'),
    ('Semi Modular', 'SM'),
    ('Full Wired', 'FW')
)

MB_OC_CHOICES = (
    ('None', 'N'),
    ('Normal-OC', 'N-OC'),
    ('OC', 'OC')
)

QUESTION_CHOICES = (
    ('Γενικές', 'Γενικές'),
    ('Ερωτήσεις επεξεργαστή', 'Ερωτήσεις επεξεργαστή'),
    ('Ερωτήσεις μητρικής', 'Ερωτήσεις μητρικής'),
    ('Ερωτήσεις ψύξης', 'Ερωτήσεις ψύξης'),
    ('Ερωτήσεις μνήμης', 'Ερωτήσεις μνήμης'),
    ('Ερωτήσεις κάρτας γραφικών', 'Ερωτήσεις κάρτας γραφικών'),
    ('Ερωτήσεις δίσκου', 'Ερωτήσεις δίσκου'),
    ('Ερωτήσεις τροφοδοτικού', 'Ερωτήσεις τροφοδοτικού'),
    ('Ερωτήσεις κουτιού', 'Ερωτήσεις κουτιού')
)

class Cpu(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=5)
    oc = models.BooleanField()
    igpu = models.BooleanField()
    price = models.FloatField()
    speed = models.FloatField()
    tag = models.CharField(max_length=5, choices=TAG_CHOICES)
    socket = models.CharField(max_length=4, choices=SOCKET_CHOICES)
    cores = models.IntegerField()
    threads = models.IntegerField()
    tdp = models.IntegerField()
    def __str__(self):
        return self.name

class Disk(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    size = models.CharField(max_length=9, choices=SIZE_CHOICES)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    capacity = models.IntegerField()
    rpm = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    def __str__(self):
        return self.name
    
class Gpu(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    memory = models.IntegerField()
    chipset = models.CharField(max_length=6, choices=CHIPSET_CHOICES)
    memoryType = models.CharField(max_length=6, choices=MEMORY_CHOICES)
    tag = models.CharField(max_length=11, choices=GPU_CHOICES)
    tdp = models.IntegerField()
    def __str__(self):
        return self.name

class Ram(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()
    type = models.CharField(max_length=4, default='DDR4')
    modules = models.IntegerField()
    price = models.FloatField()
    frequency = models.IntegerField()
    CAS = models.IntegerField()
    def __str__(self):
        return self.name

class Cooler(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=COOLER_TYPE_CHOICES)
    price = models.FloatField()
    size = models.CharField(max_length=6, choices=COOLER_SIZE_CHOICES)
    noise = models.FloatField(blank=True, null=True)
    def __str__(self):
        return self.name

class Case(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    mbSize = models.CharField(max_length=8, choices=MB_SIZE_CHOICES)
    RGB = models.BooleanField()
    window = models.BooleanField()
    type = models.CharField(max_length=7, choices=CASE_TYPE_CHOICES)
    def __str__(self):
        return self.name

class PSU(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    watt = models.IntegerField()
    certificate = models.CharField(max_length=8, choices=CERTIFICATE_CHOICES)
    modular = models.CharField(max_length=12, choices=MODULAR_CHOICES)
    def __str__(self):
        return self.name

class MB(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    size = models.CharField(max_length=8, choices=MB_SIZE_CHOICES)
    socket = models.CharField(max_length=4, choices=SOCKET_CHOICES)
    chipset = models.CharField(max_length=9)
    oc = models.CharField(max_length=10, choices=MB_OC_CHOICES)
    memory_slots = models.IntegerField()
    wifi = models.BooleanField()
    m_2slots = models.IntegerField()
    sata = models.IntegerField()
    usb = models.IntegerField()
    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    tag = models.CharField(max_length=25, choices=QUESTION_CHOICES)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
