# ☕ BrewCoff - Coffee Shop Website

Proyek website coffee shop yang dibuat secara kolaboratif.

## 👥 Tim

| Nama | Role | Folder Kerja | Branch |
|------|------|-------------|--------|
| **m1neeS** | Backend Developer | `Backend/` | `backend` |
| **piddd** | Frontend Developer | `Frontend/` | `frontend` |

---

## 📁 Struktur Project
```
BrewCoff/
├── Frontend/              ← Folder kerja Frontend Developer
│   ├── css/
│   ├── js/
│   ├── menu.html
│   ├── splashscreen.html
│   └── ...
│
├── Backend/               ← Folder kerja Backend Developer
│   ├── brewcoff_backend/
│   ├── menu/
│   ├── orders/
│   ├── manage.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

## 🔀 Alur Kerja Git (PENTING! BACA SEBELUM MULAI)

### ⚠️ Aturan Utama
1. **JANGAN** kerja langsung di branch `main`
2. **JANGAN** edit file di folder orang lain
3. **SELALU** pull dulu sebelum mulai kerja
4. **SELALU** kerja di branch masing-masing

### 🟢 Setup Awal (1x saja)

**Clone repo:**
```bash
git clone https://github.com/m1neeS/BrewCoff.git
cd BrewCoff
```

**Buat branch sesuai role:**
```bash
# Backend:
git checkout -b backend

# Frontend:
git checkout -b frontend
```

### 🔄 Alur Kerja Sehari-hari

**Sebelum mulai kerja:**
```bash
git checkout main
git pull origin main
git checkout <branch-kamu>
git merge main
```

**Selesai koding? Push!**
```bash
git add .
git commit -m "feat: deskripsi singkat"
git push origin <branch-kamu>
```

**Merge ke main:**
1. Buka GitHub → Pull Requests
2. New Pull Request → pilih branch kamu → main
3. Create Pull Request → minta teman review → Merge

### 📝 Format Commit Message
- `feat: fitur baru`
- `fix: perbaiki bug`
- `style: perubahan tampilan`
- `docs: update dokumentasi`

---

## 🛠️ Setup Development

### Backend (Django)
```bash
cd Backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Server: http://127.0.0.1:8000/

### Frontend
Buka file HTML di browser atau gunakan Live Server di VS Code.

---

## 🔗 API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | /api/menu/categories/ | List semua kategori |
| GET | /api/menu/items/ | List semua menu |
| GET | /api/menu/items/{id}/ | Detail 1 menu + modifier |
| GET | /api/menu/search/?q=latte | Search menu |
| POST | /api/orders/ | Buat order baru |
| GET | /api/orders/{id}/ | Cek status order |

---

## ⚠️ Catatan
- `venv/` dan `__pycache__/` jangan di-push (sudah di .gitignore)
- Kalau ada conflict, hubungi teman dulu sebelum resolve
- Selalu komunikasi sebelum merge ke main