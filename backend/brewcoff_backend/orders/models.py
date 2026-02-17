from django.db import models
from menu.models import MenuItem

# Model untuk order/pesanan customer
class Order(models.Model):
    # Pilihan status order
    STATUS_CHOICES = [
        ('pending', 'Pending'),         # Baru masuk, belum diproses
        ('preparing', 'Preparing'),     # Sedang dibuat
        ('ready', 'Ready'),             # Siap diambil
        ('completed', 'Completed'),     # Sudah selesai/diambil
    ]
    
    customer_name = models.CharField(max_length=200, blank=True, default='Guest')  # Nama customer (default: Guest)
    table_number = models.CharField(max_length=10)  # Nomor meja
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Status order
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total harga keseluruhan
    created_at = models.DateTimeField(auto_now_add=True)  # Waktu order dibuat (otomatis)
    updated_at = models.DateTimeField(auto_now=True)  # Waktu terakhir diupdate (otomatis)
    
    def __str__(self):
        # Menampilkan info order di admin panel
        return f"Order #{self.id} - {self.customer_name} (Table {self.table_number})"
    
    class Meta:
        ordering = ['-created_at']  # Urutkan dari yang terbaru


# Model untuk item dalam order (detail pesanan)
class OrderItem(models.Model):
    # Relasi ke Order (1 order bisa punya banyak items)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    # Relasi ke MenuItem (menu apa yang dipesan)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)  # Jumlah item yang dipesan
    selected_modifiers = models.JSONField(default=dict)  # Simpan pilihan modifier (size, sugar, ice)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)  # Harga untuk item ini (base_price + modifiers) * quantity
    
    def __str__(self):
        # Menampilkan info order item di admin panel
        return f"{self.quantity}x {self.menu_item.name} (Order #{self.order.id})"
