from django.db import models

# Model untuk kategori menu (Coffee, Non-Coffee, snack, dll)
class Category(models.Model):
    name = models.CharField(max_length=100) # nama kategori
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        # menampilkan nama kategori di admin panel
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories" #Plural name di admnin

# model untuk item menu(Americano, Latte, Croissant, dll)
class MenuItem(models.Model):
    # relasi ke category (1 category punya banya item)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=200) # Nama menu
    description = models.TextField() # deskripsi menu
    base_price = models.DecimalField(max_digits=10, decimal_places=2) # harga dasar 
    image = models.URLField(blank=True, null=True)# URL GAMBAR MENU(OPSIONAL)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # menampilkan nama menu di admil panel
        return self.name

# model untuk modifier/pilihan tambahan (Size, sugar level, ice level)
class Modifier(models.Model):
    MODIFIER_TYPES =[
        ('size', 'Size'), # ukuran (regular, large)
        ('sugar', 'Sugar Level'), # tingkat gula (Normal, less sugar, No sugar)
        ('ice', 'Ice Level'), # Tingakar es (Normal, less ice, No ice)
        ('temperature', "Temperature") # hot or ice
    ]

    # relasi ke menuItem (1 menu item bisa punya banya modifiers)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='modifiers')
    modifier_type = models.CharField(max_length=20, choices=MODIFIER_TYPES) # tipe modifier
    option_name = models.CharField(max_length=100) # nama pilihan
    price_adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        # menampilkan info lengkap modifier di admnin panel
        return f"{self.menu_item.name} - {self.modifier_type}: {self.option_name}"

