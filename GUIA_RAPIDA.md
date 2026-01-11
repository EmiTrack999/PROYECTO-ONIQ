# 🚀 GUÍA RÁPIDA - ONIQ Store

## ✅ El servidor Python está corriendo en http://localhost:5000

## 📋 CÓMO USAR LA TIENDA

### 1️⃣ ACCEDER A LA APLICACIÓN

Abre tu navegador y navega a:

```
d:\TIENDA_ONIQ\oniq_store\public\welcome.html
```

O directamente:
- **Login:** `d:\TIENDA_ONIQ\oniq_store\public\login.html`
- **Registro:** `d:\TIENDA_ONIQ\oniq_store\public\register.html`
- **Tienda Mejorada:** `d:\TIENDA_ONIQ\oniq_store\public\store-enhanced.html`

### 2️⃣ CREDENCIALES DE PRUEBA

**Usuario Admin (ya creado):**
- Username: `admin`
- Password: `admin123`

**O crea tu propio usuario:**
1. Ve a register.html
2. Completa el formulario
3. Inicia sesión

### 3️⃣ FUNCIONES PRINCIPALES

#### 🛍️ Explorar Productos
- **10 productos de ejemplo** ya cargados
- Categorías: Electrónica, Audio, Wearables, Accesorios, Almacenamiento

#### 🔍 Buscar y Filtrar
- Barra de búsqueda en el header
- Filtros por categoría
- Filtros por precio (Min/Max)
- Ordenar por: Precio, Rating, Popularidad, Más recientes

#### 🛒 Carrito de Compras
1. Clic en botón "🛒 Agregar" en cualquier producto
2. Clic en el icono del carrito (esquina superior derecha)
3. Modificar cantidades con +/-
4. Clic en "Proceder al Pago" para crear la orden

#### ❤️ Wishlist
1. Clic en el corazón (🤍) de cualquier producto
2. Se guarda en el servidor
3. Ver tu wishlist en el icono ❤️ del header
4. Agregar al carrito desde wishlist

#### ⭐ Dejar Reseñas
1. Clic en "Ver Detalles" de un producto
2. Scroll hacia abajo
3. Selecciona estrellas (1-5)
4. Escribe un comentario
5. Clic en "Enviar Reseña"

#### 📊 Panel Admin (solo para admin)
- Endpoint: `http://localhost:5000/api/analytics/dashboard`
- Ver estadísticas completas
- Productos más vendidos
- Alertas de stock bajo

### 4️⃣ CARACTERÍSTICAS AVANZADAS

✨ **Persistencia del Carrito**: El carrito se guarda en localStorage
✨ **Stock Automático**: Se actualiza automáticamente al comprar
✨ **Rating Dinámico**: El rating promedio se recalcula con cada reseña
✨ **Búsqueda en Tiempo Real**: Sin necesidad de recargar la página
✨ **Notificaciones Toast**: Feedback visual para todas las acciones
✨ **Vista Grid/List**: Cambia entre vista de cuadrícula y lista
✨ **Responsive Design**: Funciona perfectamente en móviles

### 5️⃣ ENDPOINTS DE API DISPONIBLES

```
GET    /api/products              - Listar productos (con filtros)
GET    /api/products/:id          - Ver producto específico
POST   /api/products              - Crear producto (Admin)
PUT    /api/products/:id          - Actualizar producto (Admin)
DELETE /api/products/:id          - Eliminar producto (Admin)

POST   /api/orders                - Crear orden
GET    /api/orders                - Mis órdenes
GET    /api/orders/:id            - Ver orden específica

GET    /api/wishlist              - Mi wishlist
POST   /api/wishlist/:product_id  - Agregar a wishlist
DELETE /api/wishlist/:product_id  - Eliminar de wishlist

POST   /api/products/:id/reviews  - Dejar reseña

GET    /api/analytics/dashboard   - Dashboard (Admin)
GET    /api/recommendations       - Productos recomendados
GET    /api/categories            - Listar categorías
```

### 6️⃣ EJEMPLOS DE USO CON FILTROS

**Buscar productos:**
```
http://localhost:5000/api/products?search=laptop
```

**Filtrar por categoría:**
```
http://localhost:5000/api/products?category=Electrónica
```

**Filtrar por precio:**
```
http://localhost:5000/api/products?min_price=100&max_price=500
```

**Ordenar por precio (menor a mayor):**
```
http://localhost:5000/api/products?sort_by=price_asc
```

**Combinar filtros:**
```
http://localhost:5000/api/products?category=Electrónica&min_price=200&sort_by=rating
```

### 7️⃣ PROBAR LA APLICACIÓN

1. **Registra un usuario nuevo**
2. **Explora los productos**
3. **Agrega productos al carrito**
4. **Crea una orden** (verifica que el stock se actualice)
5. **Agrega productos a wishlist**
6. **Deja una reseña** en un producto
7. **Prueba los filtros y búsqueda**

### 8️⃣ DATOS DE EJEMPLO INCLUIDOS

- ✅ 10 productos en diferentes categorías
- ✅ Usuario admin creado
- ✅ Base de datos SQLite (oniq_store.db)
- ✅ Stocks iniciales configurados

### 9️⃣ ESTRUCTURA DE LA BASE DE DATOS

```
users          → Usuarios registrados
products       → Catálogo de productos
orders         → Órdenes de compra
order_items    → Items de cada orden
reviews        → Reseñas de productos
wishlist       → Lista de deseos de usuarios
```

### 🔟 TROUBLESHOOTING

**❌ Error: Cannot connect to server**
- Verifica que el servidor Python esté corriendo
- Revisa la consola del terminal

**❌ Error: Token inválido**
- Cierra sesión y vuelve a iniciar
- Borra localStorage: `localStorage.clear()`

**❌ Base de datos corrupta**
- Detén el servidor
- Elimina `oniq_store.db`
- Reinicia el servidor (se recreará automáticamente)

**❌ Puerto ocupado**
```bash
# Cambiar puerto en app.py (última línea):
app.run(debug=True, port=5001)  # Cambiar a otro puerto
```

---

## 🎯 PRÓXIMOS PASOS RECOMENDADOS

1. ✨ Agregar más productos
2. 🎨 Personalizar colores y estilos
3. 💳 Integrar pasarela de pago (Stripe/PayPal)
4. 📧 Sistema de notificaciones por email
5. 📦 Gestión de envíos y tracking
6. 🖼️ Múltiples imágenes por producto
7. 💬 Chat en vivo con soporte
8. 🏆 Sistema de puntos y recompensas

---

## 📞 SOPORTE

Si tienes problemas o preguntas:
1. Revisa la consola del navegador (F12)
2. Revisa la consola del servidor Python
3. Consulta el README.md completo

---

**¡Disfruta tu tienda ONIQ! 🚀🛍️**
