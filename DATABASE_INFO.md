# ONIQ Store - Base de Datos

## ✅ Base de datos actual: SQLite con Python

Tu proyecto ya está usando **SQLite** con Python Flask y SQLAlchemy.

### Ubicación:
- **Archivo**: `python_backend/app.py`
- **Base de datos**: `python_backend/instance/oniq_store.db`
- **ORM**: SQLAlchemy

### Modelos incluidos:
- ✅ User (usuarios)
- ✅ Product (productos)
- ✅ Order (pedidos)
- ✅ OrderItem (items del pedido)
- ✅ Review (reseñas)
- ✅ Wishlist (lista de deseos)

### ⚠️ Problema con Vercel
SQLite no persiste en Vercel porque es serverless. Cada request reinicia el entorno.

## 🎯 Soluciones para producción:

### Opción 1: Usar base de datos en la nube (RECOMENDADO)

**Supabase (PostgreSQL gratis):**
1. Crear cuenta en supabase.com
2. Crear nuevo proyecto
3. Copiar la URL de conexión
4. Actualizar en app.py:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@host/db'
```

### Opción 2: Deploy completo en Render
- Render soporta SQLite persistente
- Gratis con algunas limitaciones
- Mejor para proyectos completos

### Opción 3: PythonAnywhere
- Hosting especializado en Python
- Soporta SQLite nativo
- Fácil de configurar

## 🗑️ Backend antiguo (Node.js)
La carpeta `backend/` con Node.js y MySQL **NO se está usando**.
Puedes eliminarla sin problemas.

¿Quieres que configure Supabase (PostgreSQL gratis) para que funcione en Vercel?
