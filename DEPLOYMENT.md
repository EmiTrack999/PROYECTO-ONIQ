# ONIQ Store - Deployment

## ✅ Archivos subidos correctamente

Tu proyecto ya está en GitHub y configurado para Vercel.

## 📝 Configuración en Vercel Dashboard

1. **Ir a tu proyecto en Vercel**
2. **Settings → General → Build & Development Settings:**
   - Framework Preset: `Other`
   - Build Command: (vacío)
   - Output Directory: `public`
   - Install Command: `pip install -r requirements.txt`

3. **Root Directory:**
   - Dejar como `.` (punto - raíz del proyecto)

4. **Settings → Environment Variables:**
   - Añadir: `FLASK_ENV = production`

5. **Redeploy:**
   - Ve a "Deployments" → Click en los 3 puntos → "Redeploy"

## 🎯 URLs actualizadas

El código ahora detecta automáticamente:
- **Local**: `http://localhost:5000/api`
- **Producción**: `/api` (tu dominio Vercel)

## ⚠️ Nota importante

Vercel + Python tiene limitaciones:
- Base de datos SQLite no persiste (se reinicia cada deploy)
- Para producción real considera: **Render**, **Railway** o **PythonAnywhere**

## 🚀 Alternativa recomendada

**Opción 1: Todo en Vercel** (limitado)
- Frontend: ✅ Funciona bien
- Backend: ⚠️ SQLite no persiste

**Opción 2: Separar (RECOMENDADO)**
- Frontend en Vercel
- Backend en Render.com (gratis) con PostgreSQL

¿Necesitas ayuda configurando Render para el backend?
