#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para crear la base de datos completa de ONIQ Store desde cero
Similar al script de florería Josbet pero adaptado para tienda ONIQ
Base de datos: SQLite (para Replit)
"""

from app import app, db, User, Product, Order, OrderItem, Review, Wishlist, bcrypt
import os

def eliminar_db_anterior():
    """Elimina la base de datos anterior si existe"""
    db_path = 'oniq_store.db'
    if os.path.exists(db_path):
        os.remove(db_path)
        print("✓ Base de datos anterior eliminada")
    
    # También eliminar en instance/
    instance_path = 'instance/oniq_store.db'
    if os.path.exists(instance_path):
        os.remove(instance_path)
        print("✓ Base de datos en instance/ eliminada")

def crear_bd_completa():
    """Crea toda la estructura de la base de datos desde cero"""
    try:
        with app.app_context():
            print("="*60)
            print("🚀 CREANDO BASE DE DATOS ONIQ STORE")
            print("="*60)
            
            # Eliminar BD anterior
            print("\n📦 Paso 1: Limpiando base de datos anterior...")
            db.drop_all()
            eliminar_db_anterior()
            
            # Crear todas las tablas
            print("\n📦 Paso 2: Creando tablas...")
            db.create_all()
            print("✓ Tabla 'usuarios' creada")
            print("✓ Tabla 'productos' creada")
            print("✓ Tabla 'pedidos' creada")
            print("✓ Tabla 'items_pedido' creada")
            print("✓ Tabla 'reseñas' creada")
            print("✓ Tabla 'lista_deseos' creada")
            
            # Crear usuario admin
            print("\n📦 Paso 3: Creando usuario administrador...")
            hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin = User(
                username='admin',
                email='admin@oniq.com',
                password=hashed_password,
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print("✓ Usuario 'admin' creado")
            print("   👤 Username: admin")
            print("   🔑 Password: admin123")
            print("   📧 Email: admin@oniq.com")
            print("   👑 Es Admin: Sí")
            
            # Crear usuarios de ejemplo
            print("\n📦 Paso 4: Creando usuarios de prueba...")
            usuarios_ejemplo = [
                ('juan', 'juan@test.com', 'juan123'),
                ('maria', 'maria@test.com', 'maria123'),
                ('carlos', 'carlos@test.com', 'carlos123'),
            ]
            
            for username, email, password in usuarios_ejemplo:
                hashed = bcrypt.generate_password_hash(password).decode('utf-8')
                user = User(username=username, email=email, password=hashed, is_admin=False)
                db.session.add(user)
            
            db.session.commit()
            print(f"✓ {len(usuarios_ejemplo)} usuarios de prueba creados")
            
            # Insertar productos
            print("\n📦 Paso 5: Insertando productos...")
            productos = [
                # ELECTRÓNICA
                ('MacBook Pro M3', 'Laptop profesional con chip M3, 16GB RAM', 2499.99, 'Electrónica', 10, '💻', 4.9),
                ('iPad Air', 'Tablet versátil de 10.9 pulgadas', 699.99, 'Electrónica', 15, '📱', 4.7),
                ('iPhone 15 Pro Max', 'Smartphone premium con titanio', 1299.99, 'Electrónica', 20, '📱', 4.8),
                ('Samsung Galaxy S24 Ultra', 'Flagship con S Pen incluido', 1199.99, 'Electrónica', 18, '📱', 4.7),
                ('Nintendo Switch OLED', 'Consola portátil con pantalla OLED', 349.99, 'Electrónica', 25, '🎮', 4.6),
                ('PlayStation 5', 'Consola de nueva generación', 499.99, 'Electrónica', 12, '🎮', 4.8),
                ('Xbox Series X', 'Consola 4K HDR gaming', 499.99, 'Electrónica', 14, '🎮', 4.7),
                ('LG UltraGear 27" 4K', 'Monitor gaming 144Hz', 599.99, 'Electrónica', 12, '🖥️', 4.8),
                ('Dell UltraSharp 32"', 'Monitor profesional 4K', 749.99, 'Electrónica', 10, '🖥️', 4.7),
                
                # AUDIO
                ('AirPods Pro 2', 'Auriculares con cancelación activa de ruido', 249.99, 'Audio', 30, '🎧', 4.8),
                ('Sony WH-1000XM5', 'Auriculares premium con ANC', 399.99, 'Audio', 20, '🎧', 4.9),
                ('Bose QuietComfort 45', 'Auriculares inalámbricos cómodos', 329.99, 'Audio', 22, '🎧', 4.7),
                ('JBL Flip 6', 'Altavoz Bluetooth portátil resistente al agua', 129.99, 'Audio', 35, '🔊', 4.6),
                ('HomePod Mini', 'Altavoz inteligente compacto', 99.99, 'Audio', 28, '🔊', 4.5),
                
                # WEARABLES
                ('Apple Watch Series 9', 'Smartwatch con pantalla Always-On', 429.99, 'Wearables', 25, '⌚', 4.8),
                ('Samsung Galaxy Watch 6', 'Reloj inteligente con Wear OS', 329.99, 'Wearables', 20, '⌚', 4.6),
                ('Fitbit Charge 6', 'Pulsera fitness con GPS', 159.99, 'Wearables', 30, '⌚', 4.5),
                ('Xiaomi Smart Band 8', 'Pulsera inteligente económica', 49.99, 'Wearables', 50, '⌚', 4.4),
                
                # ACCESORIOS
                ('Magic Keyboard', 'Teclado inalámbrico premium', 149.99, 'Accesorios', 25, '⌨️', 4.7),
                ('Logitech MX Master 3S', 'Mouse ergonómico profesional', 99.99, 'Accesorios', 30, '🖱️', 4.8),
                ('Razer BlackWidow V4', 'Teclado mecánico gaming RGB', 179.99, 'Accesorios', 20, '⌨️', 4.7),
                ('Logitech G Pro Wireless', 'Mouse gaming inalámbrico', 129.99, 'Accesorios', 25, '🖱️', 4.6),
                ('Cable USB-C 2m', 'Cable de carga rápida', 19.99, 'Accesorios', 100, '🔌', 4.3),
                ('Hub USB-C 7 en 1', 'Adaptador multipuerto', 49.99, 'Accesorios', 40, '🔌', 4.5),
                ('Funda MacBook 13"', 'Funda protectora de neopreno', 29.99, 'Accesorios', 45, '💼', 4.4),
                ('Logitech StreamCam', 'Webcam 1080p para streaming', 169.99, 'Accesorios', 22, '📷', 4.6),
                
                # ALMACENAMIENTO
                ('Samsung SSD 990 Pro 2TB', 'SSD NVMe ultrarrápido', 199.99, 'Almacenamiento', 30, '💾', 4.8),
                ('WD My Passport 5TB', 'Disco duro externo portátil', 139.99, 'Almacenamiento', 35, '💾', 4.6),
                ('SanDisk Extreme 1TB', 'SSD portátil resistente', 159.99, 'Almacenamiento', 28, '💾', 4.7),
                ('Kingston 128GB USB', 'Memoria USB 3.2 rápida', 19.99, 'Almacenamiento', 60, '💾', 4.5),
                ('Seagate 8TB NAS', 'Disco duro para almacenamiento en red', 249.99, 'Almacenamiento', 15, '💾', 4.6),
            ]
            
            contador = 0
            for nombre, descripcion, precio, categoria, stock, imagen, rating in productos:
                producto = Product(
                    name=nombre,
                    description=descripcion,
                    price=precio,
                    category=categoria,
                    stock=stock,
                    image=imagen,
                    rating=rating
                )
                db.session.add(producto)
                contador += 1
            
            db.session.commit()
            print(f"✓ {contador} productos insertados")
            
            # Resumen final
            print("\n" + "="*60)
            print("✅ BASE DE DATOS CREADA EXITOSAMENTE")
            print("="*60)
            print(f"\n📊 ESTADÍSTICAS:")
            print(f"   👥 Usuarios: {User.query.count()}")
            print(f"   📦 Productos: {Product.query.count()}")
            print(f"   🛒 Pedidos: {Order.query.count()}")
            print(f"   ⭐ Reseñas: {Review.query.count()}")
            print(f"   ❤️  Lista de deseos: {Wishlist.query.count()}")
            
            print("\n🔐 CREDENCIALES DE ACCESO:")
            print("   👤 Usuario: admin")
            print("   🔑 Contraseña: admin123")
            print("   🌐 Rol: Administrador")
            
            print("\n👥 USUARIOS DE PRUEBA:")
            print("   • juan / juan123")
            print("   • maria / maria123")
            print("   • carlos / carlos123")
            
            print("\n🎯 PRÓXIMOS PASOS:")
            print("   1. Reinicia el servidor en Replit")
            print("   2. Ve a la página de login")
            print("   3. Usa: admin / admin123")
            print("   4. ¡Disfruta tu tienda!")
            print("\n" + "="*60)
            
            return True
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    crear_bd_completa()
