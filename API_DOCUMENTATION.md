# 📚 BrewCoff Backend API Documentation

Dokumentasi lengkap untuk integrasi Frontend dengan Backend API.

---

## 🚀 Getting Started

### Base URL
```
http://127.0.0.1:8000
```

### Menjalankan Backend Server
```bash
cd backend/brewcoff_backend
python manage.py runserver
```

Server akan jalan di `http://127.0.0.1:8000/`

---

## 📋 Menu API

### 1. Get All Categories (dengan items)
**Endpoint:** `GET /api/menu/categories/`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Coffee",
    "description": "Kopi pilihan terbaik",
    "items": [
      {
        "id": 1,
        "name": "Americano",
        "description": "Espresso dengan air panas",
        "base_price": "25000.00",
        "image": null,
        "is_available": true,
        "category": 1,
        "category_name": "Coffee",
        "modifiers": [
          {
            "id": 1,
            "modifier_type": "size",
            "option_name": "Regular",
            "price_adjustment": "0.00"
          },
          {
            "id": 2,
            "modifier_type": "size",
            "option_name": "Large",
            "price_adjustment": "5000.00"
          }
        ],
        "created_at": "2026-02-17T10:30:00Z"
      }
    ]
  }
]
```

**Contoh JavaScript:**
```javascript
fetch('http://127.0.0.1:8000/api/menu/categories/')
  .then(response => response.json())
  .then(data => {
    console.log('Categories:', data);
    // Loop categories dan tampilkan di UI
  })
  .catch(error => console.error('Error:', error));
```

---

### 2. Get All Menu Items
**Endpoint:** `GET /api/menu/items/`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Americano",
    "description": "Espresso dengan air panas",
    "base_price": "25000.00",
    "image": null,
    "is_available": true,
    "category": 1,
    "category_name": "Coffee",
    "modifiers": [...],
    "created_at": "2026-02-17T10:30:00Z"
  }
]
```

---

### 3. Get Menu Item Detail
**Endpoint:** `GET /api/menu/items/{id}/`

**Example:** `GET /api/menu/items/1/`

**Response:** (sama seperti single item di atas)

---

### 4. Search Menu
**Endpoint:** `GET /api/menu/items/?search={keyword}`

**Example:** `GET /api/menu/items/?search=latte`

**Contoh JavaScript:**
```javascript
const searchMenu = (keyword) => {
  fetch(`http://127.0.0.1:8000/api/menu/items/?search=${keyword}`)
    .then(response => response.json())
    .then(data => {
      console.log('Search results:', data);
    });
};

searchMenu('latte');
```

---

## 🛒 Orders API

### 1. Create Order
**Endpoint:** `POST /api/orders/`

**Request Body:**
```json
{
  "customer_name": "Guest",
  "table_number": "1",
  "total_price": "50000.00",
  "items": [
    {
      "menu_item": 1,
      "quantity": 2,
      "selected_modifiers": {
        "size": "Large",
        "sugar": "Normal",
        "ice": "Less Ice",
        "temperature": "Ice"
      },
      "subtotal": "50000.00"
    }
  ]
}
```

**Response:**
```json
{
  "id": 1,
  "customer_name": "Guest",
  "table_number": "1",
  "status": "pending",
  "total_price": "50000.00",
  "created_at": "2026-02-17T12:00:00Z",
  "updated_at": "2026-02-17T12:00:00Z",
  "items": [
    {
      "id": 1,
      "menu_item": 1,
      "menu_item_detail": {
        "id": 1,
        "name": "Americano",
        "base_price": "25000.00"
      },
      "quantity": 2,
      "selected_modifiers": {
        "size": "Large",
        "sugar": "Normal",
        "ice": "Less Ice",
        "temperature": "Ice"
      },
      "subtotal": "50000.00"
    }
  ]
}
```

**Contoh JavaScript:**
```javascript
const createOrder = async (orderData) => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/orders/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(orderData)
    });
    
    const data = await response.json();
    console.log('Order created:', data);
    return data;
  } catch (error) {
    console.error('Error creating order:', error);
  }
};

// Contoh penggunaan
const orderData = {
  customer_name: 'Guest',
  table_number: '5',
  total_price: 75000,
  items: [
    {
      menu_item: 1,
      quantity: 2,
      selected_modifiers: {
        size: 'Large',
        sugar: 'Less Sugar',
        ice: 'Normal',
        temperature: 'Ice'
      },
      subtotal: 50000
    },
    {
      menu_item: 2,
      quantity: 1,
      selected_modifiers: {
        size: 'Regular',
        temperature: 'Hot'
      },
      subtotal: 25000
    }
  ]
};

createOrder(orderData);
```

---

### 2. Get All Orders
**Endpoint:** `GET /api/orders/`

**Response:**
```json
[
  {
    "id": 1,
    "customer_name": "Guest",
    "table_number": "1",
    "status": "pending",
    "total_price": "50000.00",
    "created_at": "2026-02-17T12:00:00Z",
    "updated_at": "2026-02-17T12:00:00Z",
    "items": [...]
  }
]
```

---

### 3. Get Order Detail
**Endpoint:** `GET /api/orders/{id}/`

**Example:** `GET /api/orders/1/`

---

### 4. Update Order Status
**Endpoint:** `PATCH /api/orders/{id}/update_status/`

**Request Body:**
```json
{
  "status": "preparing"
}
```

**Valid Status:**
- `pending` - Baru masuk
- `preparing` - Sedang dibuat
- `ready` - Siap diambil
- `completed` - Selesai

**Contoh JavaScript:**
```javascript
const updateOrderStatus = async (orderId, newStatus) => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/orders/${orderId}/update_status/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ status: newStatus })
    });
    
    const data = await response.json();
    console.log('Order updated:', data);
    return data;
  } catch (error) {
    console.error('Error updating order:', error);
  }
};

// Contoh: Update order 1 jadi "preparing"
updateOrderStatus(1, 'preparing');
```

---

### 5. Get Orders by Table Number
**Endpoint:** `GET /api/orders/by_table/?table_number={number}`

**Example:** `GET /api/orders/by_table/?table_number=1`

**Contoh JavaScript:**
```javascript
const getOrdersByTable = (tableNumber) => {
  fetch(`http://127.0.0.1:8000/api/orders/by_table/?table_number=${tableNumber}`)
    .then(response => response.json())
    .then(data => {
      console.log(`Orders for table ${tableNumber}:`, data);
    });
};

getOrdersByTable('5');
```

---

## 📊 Analytics API (untuk Dashboard)

### 1. Dashboard Summary
**Endpoint:** `GET /api/analytics/summary/`

**Response:**
```json
{
  "sales": {
    "today": 150000.0,
    "week": 1250000.0,
    "month": 5000000.0
  },
  "orders": {
    "today": 15,
    "by_status": [
      {
        "status": "pending",
        "count": 3
      },
      {
        "status": "preparing",
        "count": 5
      },
      {
        "status": "ready",
        "count": 2
      },
      {
        "status": "completed",
        "count": 5
      }
    ]
  }
}
```

**Contoh JavaScript:**
```javascript
fetch('http://127.0.0.1:8000/api/analytics/summary/')
  .then(response => response.json())
  .then(data => {
    console.log('Sales today:', data.sales.today);
    console.log('Orders today:', data.orders.today);
    console.log('Orders by status:', data.orders.by_status);
  });
```

---

### 2. Popular Items
**Endpoint:** `GET /api/analytics/popular-items/`

**Query Parameters:**
- `limit` (optional) - Jumlah items yang ditampilkan (default: 10)

**Example:** `GET /api/analytics/popular-items/?limit=5`

**Response:**
```json
[
  {
    "menu_item__id": 1,
    "menu_item__name": "Americano",
    "menu_item__base_price": "25000.00",
    "total_ordered": 50,
    "total_revenue": "1250000.00"
  },
  {
    "menu_item__id": 2,
    "menu_item__name": "Latte",
    "menu_item__base_price": "30000.00",
    "total_ordered": 45,
    "total_revenue": "1350000.00"
  }
]
```

---

### 3. Revenue by Category
**Endpoint:** `GET /api/analytics/revenue-by-category/`

**Response:**
```json
[
  {
    "category_id": 1,
    "category_name": "Coffee",
    "revenue": 3500000.0
  },
  {
    "category_id": 2,
    "category_name": "Non-Coffee",
    "revenue": 1200000.0
  },
  {
    "category_id": 3,
    "category_name": "Snack",
    "revenue": 800000.0
  }
]
```

---

### 4. Order Trends (7 hari terakhir)
**Endpoint:** `GET /api/analytics/order-trends/`

**Response:**
```json
[
  {
    "date": "2026-02-17",
    "orders": 25,
    "revenue": 750000.0
  },
  {
    "date": "2026-02-16",
    "orders": 30,
    "revenue": 900000.0
  },
  {
    "date": "2026-02-15",
    "orders": 28,
    "revenue": 840000.0
  }
]
```

**Contoh JavaScript (untuk Chart):**
```javascript
fetch('http://127.0.0.1:8000/api/analytics/order-trends/')
  .then(response => response.json())
  .then(data => {
    const dates = data.map(item => item.date);
    const revenues = data.map(item => item.revenue);
    
    // Gunakan data ini untuk Chart.js atau library chart lainnya
    console.log('Dates:', dates);
    console.log('Revenues:', revenues);
  });
```

---

## 🔄 Alur Lengkap Customer Order

### 1. Customer Scan QR Code
```javascript
// QR Code berisi URL: https://brewcoff.com/?table=5
// Frontend ambil table number dari URL
const urlParams = new URLSearchParams(window.location.search);
const tableNumber = urlParams.get('table');
console.log('Table Number:', tableNumber);

// Simpan di localStorage
localStorage.setItem('tableNumber', tableNumber);
```

### 2. Tampilkan Menu
```javascript
// Fetch categories dengan items
fetch('http://127.0.0.1:8000/api/menu/categories/')
  .then(response => response.json())
  .then(categories => {
    // Loop dan tampilkan di UI
    categories.forEach(category => {
      console.log(`Category: ${category.name}`);
      category.items.forEach(item => {
        console.log(`  - ${item.name}: Rp ${item.base_price}`);
      });
    });
  });
```

### 3. Customer Pilih Menu & Modifiers
```javascript
// Simpan cart di localStorage atau state management
let cart = [];

const addToCart = (menuItem, quantity, modifiers) => {
  // Hitung subtotal
  let subtotal = parseFloat(menuItem.base_price) * quantity;
  
  // Tambah harga modifiers
  modifiers.forEach(mod => {
    subtotal += parseFloat(mod.price_adjustment) * quantity;
  });
  
  cart.push({
    menu_item: menuItem.id,
    quantity: quantity,
    selected_modifiers: modifiers,
    subtotal: subtotal
  });
  
  console.log('Cart:', cart);
};
```

### 4. Checkout & Create Order
```javascript
const checkout = async () => {
  const tableNumber = localStorage.getItem('tableNumber');
  
  // Hitung total price
  const totalPrice = cart.reduce((sum, item) => sum + item.subtotal, 0);
  
  const orderData = {
    customer_name: 'Guest',
    table_number: tableNumber,
    total_price: totalPrice,
    items: cart
  };
  
  try {
    const response = await fetch('http://127.0.0.1:8000/api/orders/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(orderData)
    });
    
    const order = await response.json();
    console.log('Order created:', order);
    
    // Simpan order ID untuk tracking
    localStorage.setItem('orderId', order.id);
    
    // Redirect ke halaman tracking
    window.location.href = `/tracking?order=${order.id}`;
  } catch (error) {
    console.error('Error:', error);
  }
};
```

### 5. Order Tracking
```javascript
const trackOrder = (orderId) => {
  // Polling setiap 5 detik untuk update status
  setInterval(() => {
    fetch(`http://127.0.0.1:8000/api/orders/${orderId}/`)
      .then(response => response.json())
      .then(order => {
        console.log('Order status:', order.status);
        
        // Update UI berdasarkan status
        if (order.status === 'ready') {
          alert('Pesanan kamu sudah siap!');
        }
      });
  }, 5000);
};

// Ambil order ID dari URL
const urlParams = new URLSearchParams(window.location.search);
const orderId = urlParams.get('order');
trackOrder(orderId);
```

---

## 🎨 Contoh Lengkap: Menu Page

```html
<!DOCTYPE html>
<html>
<head>
  <title>BrewCoff Menu</title>
</head>
<body>
  <h1>Menu</h1>
  <div id="menu-container"></div>
  
  <script>
    // Fetch dan tampilkan menu
    fetch('http://127.0.0.1:8000/api/menu/categories/')
      .then(response => response.json())
      .then(categories => {
        const container = document.getElementById('menu-container');
        
        categories.forEach(category => {
          // Buat section untuk setiap kategori
          const categoryDiv = document.createElement('div');
          categoryDiv.innerHTML = `<h2>${category.name}</h2>`;
          
          category.items.forEach(item => {
            const itemDiv = document.createElement('div');
            itemDiv.innerHTML = `
              <h3>${item.name}</h3>
              <p>${item.description}</p>
              <p>Rp ${item.base_price}</p>
              <button onclick="addToCart(${item.id})">Add to Cart</button>
            `;
            categoryDiv.appendChild(itemDiv);
          });
          
          container.appendChild(categoryDiv);
        });
      });
  </script>
</body>
</html>
```

---

## ⚠️ Error Handling

```javascript
const fetchWithErrorHandling = async (url, options = {}) => {
  try {
    const response = await fetch(url, options);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Fetch error:', error);
    alert('Terjadi kesalahan. Silakan coba lagi.');
    return null;
  }
};

// Contoh penggunaan
const data = await fetchWithErrorHandling('http://127.0.0.1:8000/api/menu/items/');
if (data) {
  console.log('Data:', data);
}
```

---

## 📝 Notes untuk Frontend Developer

1. **CORS sudah disetup** - Frontend bisa akses API dari localhost:5500
2. **Customer name default "Guest"** - Bisa dikosongkan atau diisi
3. **Table number wajib** - Dari QR code scan
4. **Selected modifiers format bebas** - Bisa object/array, yang penting konsisten
5. **Total price & subtotal** - Hitung di frontend sebelum kirim ke backend
6. **Status order** - Hanya 4 status: pending, preparing, ready, completed
7. **Polling untuk tracking** - Gunakan setInterval untuk cek status order
8. **Image URL** - Bisa null, handle di frontend dengan placeholder

---

## 🚀 Tips Integrasi

1. **Gunakan async/await** untuk code yang lebih clean
2. **Buat helper functions** untuk fetch API
3. **Handle loading state** saat fetch data
4. **Handle error** dengan baik (network error, 404, 500, dll)
5. **Gunakan localStorage** untuk simpan cart & table number
6. **Test dengan Postman** dulu sebelum integrasi ke frontend

---

## 📞 Contact

Kalau ada pertanyaan atau butuh bantuan integrasi, hubungi:
- Backend Developer: **m1neeS**
- Frontend Developer: **piddd**

Happy coding! ☕
