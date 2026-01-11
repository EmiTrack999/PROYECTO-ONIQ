# 🛍️ ONIQ STORE - Tienda Online Premium

## 📋 Descripción
Tienda online moderna y completa con funciones avanzadas desarrollada con **Python Flask** (backend) y **JavaScript vanilla** (frontend).

## ✨ Características Principales

### 🔐 Autenticación y Usuarios
- Registro e inicio de sesión con JWT
- Sistema de usuarios y administradores
- Gestión de perfiles

### 🛒 Gestión de Productos
- Catálogo completo de productos
- Búsqueda avanzada en tiempo real
- Filtros por categoría y precio
- Ordenamiento (precio, rating, popularidad)
- Vistas grid y lista
- Productos con imágenes, descripciones y stock

### 🛍️ Carrito de Compras
- Agregar/eliminar productos
- Actualizar cantidades
- Persistencia en localStorage
- Checkout y creación de órdenes
- Validación de stock

### ❤️ Wishlist
- Guardar productos favoritos
- Sincronización con el servidor
- Agregar al carrito desde wishlist

### ⭐ Sistema de Reseñas
- Calificaciones con estrellas (1-5)
- Comentarios de usuarios
- Rating promedio por producto
- Una reseña por usuario

### 📊 Panel de Análisis (Admin)
- Total de productos, órdenes y usuarios
- Ingresos totales
- Productos más vendidos
- Alertas de stock bajo
- Dashboard completo

### 🎯 Sistema de Recomendaciones
- Productos más populares
- Mejor valorados
- Basado en ventas

### 🎨 Interfaz de Usuario
- Diseño moderno y responsivo
- Animaciones suaves
- Notificaciones toast
- Modales interactivos
- Compatible con móviles

## 🛠️ Tecnologías Utilizadas

### Backend (Python)
- **Flask** - Framework web
- **SQLAlchemy** - ORM para base de datos
- **Flask-CORS** - Cross-Origin Resource Sharing
- **Flask-Bcrypt** - Encriptación de contraseñas
- **PyJWT** - JSON Web Tokens
- **SQLite** - Base de datos

### Frontend
- **HTML5** - Estructura
- **CSS3** - Estilos modernos con variables CSS
- **JavaScript (ES6+)** - Lógica del cliente
- **Fetch API** - Comunicación con el backend

## 📦 Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Instalar dependencias de Python

```bash
cd python_backend
pip install -r requirements.txt
```

### Paso 2: Iniciar el servidor Python

```bash
python app.py
```

El servidor se iniciará en: **http://localhost:5000**

### Paso 3: Abrir el frontend

Abre tu navegador y navega a:
- Registro: `http://localhost:5000/../public/register.html`
- Login: `http://localhost:5000/../public/login.html`
- Tienda: `http://localhost:5000/../public/store-enhanced.html`

O simplemente abre los archivos HTML directamente desde la carpeta `public/`.

## 📁 Estructura del Proyecto

```
oniq_store/
├── python_backend/
│   ├── app.py                  # Aplicación principal Flask
│   ├── requirements.txt        # Dependencias Python
│   └── oniq_store.db          # Base de datos SQLite (auto-generada)
│
├── backend/                    # Backend Node.js (alternativo)
│   ├── server.js
│   ├── db.js
│   └── ...
│
└── public/
    ├── index.html
    ├── login.html
    ├── register.html
    ├── store-enhanced.html     # Tienda mejorada (USAR ESTA)
    ├── css/
    │   ├── style.css
    │   └── store-enhanced.css  # Estilos de la tienda mejorada
    └── js/
        ├── auth.js
        └── store-enhanced.js   # JavaScript de la tienda mejorada
```

## 🔌 API Endpoints

### Autenticación
- `POST /api/auth/register` - Registrar usuario
- `POST /api/auth/login` - Iniciar sesión

### Productos
- `GET /api/products` - Listar productos (con filtros)
- `GET /api/products/:id` - Obtener producto por ID
- `POST /api/products` - Crear producto (Admin)
- `PUT /api/products/:id` - Actualizar producto (Admin)
- `DELETE /api/products/:id` - Eliminar producto (Admin)

### Órdenes
- `POST /api/orders` - Crear orden
- `GET /api/orders` - Obtener mis órdenes
- `GET /api/orders/:id` - Obtener orden específica

### Reseñas
- `POST /api/products/:id/reviews` - Agregar reseña

### Wishlist
- `GET /api/wishlist` - Obtener wishlist
- `POST /api/wishlist/:product_id` - Agregar a wishlist
- `DELETE /api/wishlist/:product_id` - Eliminar de wishlist

### Análisis
- `GET /api/analytics/dashboard` - Dashboard de análisis (Admin)
- `GET /api/recommendations` - Obtener recomendaciones
- `GET /api/categories` - Listar categorías

## 👤 Credenciales de Admin

Por defecto, se crea un usuario administrador:

- **Username:** `admin`
- **Password:** `admin123`
- **Email:** admin@oniq.com

## 🎨 Funciones Destacadas

### 1. **Búsqueda Inteligente**
Busca productos por nombre en tiempo real sin recargar la página.

### 2. **Filtros Avanzados**
- Por categoría (Electrónica, Audio, Wearables, etc.)
- Por rango de precio
- Ordenamiento múltiple

### 3. **Carrito Persistente**
El carrito se guarda en localStorage y persiste entre sesiones.

### 4. **Sistema de Stock**
Control automático de inventario al realizar compras.

### 5. **Notificaciones Toast**
Feedback visual inmediato para todas las acciones.

### 6. **Modales Interactivos**
- Detalles del producto
- Carrito de compras
- Wishlist

### 7. **Sistema de Rating**
Calificación visual con estrellas y promedio calculado.

## 🚀 Características Avanzadas del Backend Python

### Base de Datos Relacional
- Modelos con SQLAlchemy ORM
- Relaciones entre tablas
- Integridad referencial

### Seguridad
- Contraseñas hasheadas con Bcrypt
- Autenticación JWT con expiración
- Validación de datos
- Control de acceso (Admin/Usuario)

### Performance
- Consultas optimizadas
- Índices en base de datos
- Respuestas JSON eficientes

### Manejo de Errores
- Try-catch en todas las rutas
- Mensajes de error descriptivos
- Códigos HTTP apropiados

## 🔧 Configuración Avanzada

### Cambiar la Clave Secreta
En `app.py`, línea 16:
```python
app.config['SECRET_KEY'] = 'tu_clave_secreta_super_segura_aqui'
```

### Cambiar el Puerto
En `app.py`, última línea:
```python
app.run(debug=True, port=5000)  # Cambiar el puerto aquí
```

### Usar Base de Datos MySQL/PostgreSQL
Cambiar en `app.py`:
```python
# Para MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/oniq_store'

# Para PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/oniq_store'
```

## 📊 Datos de Ejemplo

El sistema incluye 10 productos de ejemplo:
- Laptop Gaming Pro
- Smartphone Ultra
- Auriculares Inalámbricos
- Smart Watch
- Teclado Mecánico RGB
- Mouse Gaming
- Monitor 4K
- Cámara Web HD
- Tablet Pro
- Disco SSD 1TB

## 🐛 Troubleshooting

### Error: Puerto ya en uso
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Error: Módulo no encontrado
```bash
pip install -r requirements.txt --upgrade
```

### Base de datos corrupta
Elimina el archivo `oniq_store.db` y reinicia el servidor. Se creará automáticamente.

## 📝 Próximas Características

- [ ] Pagos con Stripe/PayPal
- [ ] Sistema de cupones y descuentos
- [ ] Notificaciones por email
- [ ] Chat en vivo
- [ ] Sistema de envíos
- [ ] Múltiples imágenes por producto
- [ ] Comparación de productos
- [ ] Historial de compras
- [ ] Sistema de puntos/recompensas

## 👨‍💻 Desarrollo

Creado con ❤️ para demostrar una tienda online profesional y completa.

## 📄 Licencia

MIT License - Uso libre para proyectos personales y comerciales.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, crea un Pull Request.

---

**¡Disfruta de tu tienda ONIQ! 🚀**
