# 🚀 Guía completa para subir ONIQ Store a Replit

## ✅ Paso 1: Preparar el proyecto (YA ESTÁ LISTO)

Ya he configurado todo lo necesario:
- ✅ `.replit` - Configuración de Replit
- ✅ `requirements.txt` - Dependencias Python
- ✅ `app.py` - Backend Flask configurado
- ✅ Base de datos SQLite (automática)

## 📝 Paso 2: Crear cuenta en Replit

1. Ve a **https://replit.com**
2. Click en **"Sign Up"**
3. Regístrate con:
   - 📧 Email
   - 🐙 GitHub (RECOMENDADO - más rápido)
   - 🔑 Google

## 🔗 Paso 3: Importar desde GitHub

### Opción A: Importar directamente (RECOMENDADO)

1. En Replit, click en **"Create Repl"**
2. Selecciona **"Import from GitHub"**
3. Pega la URL de tu repositorio:
   ```
   https://github.com/EmiTrack999/PROYECTO-ONIQ
   ```
4. Replit detectará automáticamente que es un proyecto Python
5. Click en **"Import from GitHub"**

### Opción B: Conectar repositorio existente

1. Crea un nuevo Repl → **"Python"**
2. En el Shell, ejecuta:
   ```bash
   git clone https://github.com/EmiTrack999/PROYECTO-ONIQ.git .
   ```

## ⚙️ Paso 4: Configuración automática

Replit leerá el archivo `.replit` y configurará:
- 🐍 Python 3.11
- 📦 Instalación automática de dependencias
- 🚀 Comando de inicio: `python python_backend/app.py`
- 🌐 Puerto 5000 → 80 (público)

## 🎯 Paso 5: Instalar dependencias

En la pestaña **"Shell"** de Replit, ejecuta:

```bash
pip install -r requirements.txt
```

Esto instalará:
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- Flask-Bcrypt
- PyJWT

## ▶️ Paso 6: Iniciar el proyecto

1. Click en el botón **"Run"** (▶️) en la parte superior
2. Replit ejecutará automáticamente: `python python_backend/app.py`
3. Verás en la consola:
   ```
   🗄️  Base de datos: SQLite (desarrollo)
   🚀 Servidor Python iniciando en puerto 5000...
   * Running on http://0.0.0.0:5000
   ```
4. Replit te mostrará una vista previa en el navegador integrado

## 🌐 Paso 7: Obtener tu URL pública

1. Una vez iniciado, Replit genera una URL automática:
   ```
   https://<tu-repl-name>.<tu-usuario>.repl.co
   ```
2. Esta URL es pública y puedes compartirla
3. Ejemplo: `https://oniq-store.emicoding.repl.co`

## 🔧 Paso 8: Configurar variables de entorno (OPCIONAL)

Si quieres añadir seguridad adicional:

1. Ve a **"Tools"** → **"Secrets"** (🔒)
2. Añade las variables:
   - `SECRET_KEY` = `tu-clave-secreta-aqui`
   - `FLASK_ENV` = `production`

## 📱 Paso 9: Probar la aplicación

1. Abre la URL de tu Repl
2. Deberías ver la página de bienvenida con el tema negro y dorado
3. Prueba el login con:
   - 👤 Usuario: `admin`
   - 🔑 Contraseña: `admin123`

## 🔄 Paso 10: Deployments automáticos

### Mantener el Repl activo (24/7)

Por defecto, Replit apaga tu app después de 1 hora sin uso.

**Opciones:**

### 🆓 Opción Gratuita: Always On (con límites)
1. En tu Repl, ve a la pestaña lateral
2. Click en el icono de configuración (⚙️)
3. Habilita **"Always On"**
4. ⚠️ Límite: Solo unos pocos Repls siempre activos en plan gratuito

### 💰 Opción Premium: Replit Hacker Plan ($7/mes)
- ✅ Always On ilimitado
- ✅ Más CPU y RAM
- ✅ Sin límites de Repls privados
- ✅ Mejor rendimiento

### 🔄 Opción DIY: UptimeRobot (Gratis)
1. Ve a **https://uptimerobot.com**
2. Crea una cuenta gratis
3. Añade tu URL de Replit
4. Configurar ping cada 5 minutos
5. Esto mantiene tu Repl "despierto"

## 🔗 Paso 11: Conectar con tu dominio GitHub (Opcional)

Cada vez que actualices tu GitHub:

1. En el Shell de Replit:
   ```bash
   git pull origin main
   ```
2. O usa el botón de Git integrado en Replit
3. Click en **"Run"** de nuevo

## ⚡ Ventajas de Replit

✅ Configuración super rápida (5 minutos)
✅ Editor de código en el navegador
✅ No necesitas instalar nada en tu PC
✅ Base de datos SQLite persistente
✅ Colaboración en tiempo real
✅ Console y Shell integrados
✅ Git integrado
✅ SSL/HTTPS automático
✅ Debugging fácil
✅ Ideal para desarrollo y demos

## ⚠️ Limitaciones del plan gratuito

- 💤 Se duerme después de 1 hora sin uso (excepto Always On)
- 🐌 CPU y RAM limitadas
- 💾 500 MB de almacenamiento
- 🔄 1 Always On Repl gratuito

## 🎨 Personalizar tu Repl

### Cambiar nombre del Repl:
1. Click en el nombre del Repl (arriba a la izquierda)
2. Escribe: `ONIQ-Store`

### Cambiar descripción:
1. Settings → **"Description"**
2. Añade: `Tienda online ONIQ con tema negro y dorado`

## 📊 Monitorear tu aplicación

En Replit puedes ver:
- 📈 **Console**: Logs en tiempo real
- 🐛 **Debugger**: Debugging paso a paso
- 📁 **Files**: Explorador de archivos
- 🗄️ **Database**: Ver base de datos SQLite

## 🚨 Solución de problemas comunes

### Error: "No module named 'flask'"
**Solución:**
```bash
pip install -r requirements.txt
```

### Error: "Address already in use"
**Solución:**
1. Stop el Repl actual
2. Click en Run de nuevo

### La base de datos se borra
**Solución:**
- Asegúrate de que `instance/` esté en tu repositorio (pero no el archivo .db)
- Replit persiste archivos en la carpeta del proyecto

### El Repl se detiene solo
**Solución:**
- Habilita Always On (plan gratuito tiene 1 gratis)
- O usa UptimeRobot para hacer ping

## 🎉 ¡Listo!

Tu tienda estará disponible en:
- 🌐 `https://<tu-repl>.repl.co`
- 📱 Funciona en móviles
- 🔒 HTTPS automático
- 💾 Base de datos persistente
- ⚡ Actualización instantánea (solo presiona Run)

## 🔧 Comandos útiles en Shell

```bash
# Ver logs en tiempo real
python python_backend/app.py

# Instalar una dependencia nueva
pip install nombre-paquete

# Actualizar desde GitHub
git pull origin main

# Ver archivos de base de datos
ls python_backend/instance/

# Limpiar cache de Python
find . -type d -name __pycache__ -exec rm -r {} +
```

## 📞 Próximos pasos

1. ✅ Importa el proyecto desde GitHub
2. ✅ Click en Run
3. ✅ Copia tu URL y compártela
4. 📧 (Opcional) Habilita Always On
5. 🎨 (Opcional) Personaliza más el diseño

¿Necesitas ayuda? Avísame qué error ves en la consola de Replit.
