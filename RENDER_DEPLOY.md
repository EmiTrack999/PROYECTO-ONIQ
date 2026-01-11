# 🚀 Guía completa para subir ONIQ Store a Render.com

## ✅ Paso 1: Preparar el proyecto (YA ESTÁ LISTO)

Ya he configurado todo lo necesario:
- ✅ `render.yaml` - Configuración de servicios
- ✅ `requirements.txt` - Dependencias con PostgreSQL
- ✅ `app.py` - Base de datos automática (PostgreSQL en producción, SQLite local)

## 📝 Paso 2: Crear cuenta en Render

1. Ve a **https://render.com**
2. Click en **"Get Started"** o **"Sign Up"**
3. Regístrate con GitHub (RECOMENDADO) o email

## 🔗 Paso 3: Conectar tu repositorio GitHub

1. En el dashboard de Render, click en **"New +"**
2. Selecciona **"Blueprint"** (para usar render.yaml)
3. Click en **"Connect a repository"**
4. Autoriza a Render para acceder a tu GitHub
5. Busca y selecciona **"PROYECTO-ONIQ"**
6. Click en **"Connect"**

## ⚙️ Paso 4: Configurar el deployment

Render leerá automáticamente el archivo `render.yaml` que creé.

### Configuración automática:
- 🌐 **Web Service**: `oniq-store` (tu aplicación Flask)
- 🗄️ **Database**: `oniq-db` (PostgreSQL gratis)
- 🐍 **Runtime**: Python 3
- 💰 **Plan**: Free

### Variables de entorno (opcionales):
Si quieres añadir más seguridad:
1. En el dashboard → tu servicio → **"Environment"**
2. Añadir:
   - `SECRET_KEY` = (genera una clave aleatoria)
   - `FLASK_ENV` = `production`

## 🎯 Paso 5: Deploy

1. Click en **"Apply"** para crear los servicios
2. Render automáticamente:
   - ✅ Crea la base de datos PostgreSQL
   - ✅ Instala dependencias (`pip install -r requirements.txt`)
   - ✅ Inicia tu aplicación
   - ✅ Te da una URL pública (ej: `https://oniq-store.onrender.com`)

⏱️ El primer deploy tarda **5-10 minutos**

## 🔍 Paso 6: Verificar el deployment

1. Ve a **"Logs"** para ver el progreso
2. Busca el mensaje: `🚀 Servidor Python iniciando...`
3. Cuando veas **"Application startup complete"**, ya está listo
4. Click en la URL para abrir tu tienda

## 🌐 Paso 7: Actualizar URLs en el código (OPCIONAL)

Si quieres que funcione con tu dominio de Render:

1. Copia tu URL de Render (ej: `https://oniq-store.onrender.com`)
2. Los archivos JS ya detectan automáticamente la URL correcta

## 🔄 Paso 8: Deployments automáticos

Cada vez que hagas `git push` a tu repositorio, Render automáticamente:
1. Detecta los cambios
2. Rebuild automático
3. Deploy de la nueva versión

## ⚡ Ventajas de Render vs Vercel

✅ Base de datos PostgreSQL persistente (gratis)
✅ Aplicación Flask completa (no serverless)
✅ Los datos NO se pierden entre requests
✅ Mejor para aplicaciones Python
✅ Logs completos y debugging
✅ SSL/HTTPS automático
✅ 750 horas gratis al mes

## 🚨 IMPORTANTE: Plan Free de Render

- ⏸️ Se duerme después de 15 minutos sin uso
- ⏱️ El primer request después de dormir tarda ~30 segundos
- 💡 Solución: Usar un servicio de "ping" gratuito para mantenerlo activo

## 🎉 ¡Listo!

Tu tienda estará disponible en:
- 🌐 `https://oniq-store.onrender.com` (o el nombre que elijas)
- 📱 Funciona en móviles
- 🔒 HTTPS automático
- 🗄️ Base de datos persistente

## 📞 Soporte

Si tienes errores:
1. Revisa los **Logs** en el dashboard de Render
2. Busca líneas rojas (errores)
3. Los errores comunes ya están solucionados en el código

¿Necesitas ayuda? Avísame qué error ves en los logs.
