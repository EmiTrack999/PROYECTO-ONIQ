"""
Script para añadir productos personalizados a la base de datos
Edita la lista de productos abajo y ejecuta este archivo
"""

from app import app, db, Product

# 📦 AÑADE TUS PRODUCTOS AQUÍ
# Formato: Product(name='Nombre', description='Descripción', price=99.99, category='Categoría', stock=10, image='emoji', rating=4.5)

productos_nuevos = [
    # ELECTRÓNICA
    Product(name='MacBook Pro M3', description='Laptop profesional con chip M3', price=2499.99, category='Electrónica', stock=10, image='💻', rating=4.9),
    Product(name='iPad Air', description='Tablet versátil de 10.9 pulgadas', price=699.99, category='Electrónica', stock=15, image='📱', rating=4.7),
    Product(name='iPhone 15 Pro Max', description='Smartphone premium con titanio', price=1299.99, category='Electrónica', stock=20, image='📱', rating=4.8),
    Product(name='Samsung Galaxy S24 Ultra', description='Flagship con S Pen incluido', price=1199.99, category='Electrónica', stock=18, image='📱', rating=4.7),
    Product(name='Nintendo Switch OLED', description='Consola portátil con pantalla OLED', price=349.99, category='Electrónica', stock=25, image='🎮', rating=4.6),
    Product(name='PlayStation 5', description='Consola de nueva generación', price=499.99, category='Electrónica', stock=12, image='🎮', rating=4.8),
    Product(name='Xbox Series X', description='Consola 4K HDR gaming', price=499.99, category='Electrónica', stock=14, image='🎮', rating=4.7),
    
    # AUDIO
    Product(name='AirPods Pro 2', description='Auriculares con cancelación activa de ruido', price=249.99, category='Audio', stock=30, image='🎧', rating=4.8),
    Product(name='Sony WH-1000XM5', description='Auriculares premium con ANC', price=399.99, category='Audio', stock=20, image='🎧', rating=4.9),
    Product(name='Bose QuietComfort 45', description='Auriculares inalámbricos cómodos', price=329.99, category='Audio', stock=22, image='🎧', rating=4.7),
    Product(name='JBL Flip 6', description='Altavoz Bluetooth portátil resistente al agua', price=129.99, category='Audio', stock=35, image='🔊', rating=4.6),
    Product(name='HomePod Mini', description='Altavoz inteligente compacto', price=99.99, category='Audio', stock=28, image='🔊', rating=4.5),
    
    # WEARABLES
    Product(name='Apple Watch Series 9', description='Smartwatch con pantalla Always-On', price=429.99, category='Wearables', stock=25, image='⌚', rating=4.8),
    Product(name='Samsung Galaxy Watch 6', description='Reloj inteligente con Wear OS', price=329.99, category='Wearables', stock=20, image='⌚', rating=4.6),
    Product(name='Fitbit Charge 6', description='Pulsera fitness con GPS', price=159.99, category='Wearables', stock=30, image='⌚', rating=4.5),
    Product(name='Xiaomi Smart Band 8', description='Pulsera inteligente económica', price=49.99, category='Wearables', stock=50, image='⌚', rating=4.4),
    
    # ACCESORIOS
    Product(name='Magic Keyboard', description='Teclado inalámbrico premium', price=149.99, category='Accesorios', stock=25, image='⌨️', rating=4.7),
    Product(name='Logitech MX Master 3S', description='Mouse ergonómico profesional', price=99.99, category='Accesorios', stock=30, image='🖱️', rating=4.8),
    Product(name='Razer BlackWidow V4', description='Teclado mecánico gaming RGB', price=179.99, category='Accesorios', stock=20, image='⌨️', rating=4.7),
    Product(name='Logitech G Pro Wireless', description='Mouse gaming inalámbrico', price=129.99, category='Accesorios', stock=25, image='🖱️', rating=4.6),
    Product(name='Cable USB-C 2m', description='Cable de carga rápida', price=19.99, category='Accesorios', stock=100, image='🔌', rating=4.3),
    Product(name='Hub USB-C 7 en 1', description='Adaptador multipuerto', price=49.99, category='Accesorios', stock=40, image='🔌', rating=4.5),
    Product(name='Funda MacBook 13"', description='Funda protectora de neopreno', price=29.99, category='Accesorios', stock=45, image='💼', rating=4.4),
    
    # ALMACENAMIENTO
    Product(name='Samsung SSD 990 Pro 2TB', description='SSD NVMe ultrarrápido', price=199.99, category='Almacenamiento', stock=30, image='💾', rating=4.8),
    Product(name='WD My Passport 5TB', description='Disco duro externo portátil', price=139.99, category='Almacenamiento', stock=35, image='💾', rating=4.6),
    Product(name='SanDisk Extreme 1TB', description='SSD portátil resistente', price=159.99, category='Almacenamiento', stock=28, image='💾', rating=4.7),
    Product(name='Kingston 128GB USB', description='Memoria USB 3.2 rápida', price=19.99, category='Almacenamiento', stock=60, image='💾', rating=4.5),
    Product(name='Seagate 8TB NAS', description='Disco duro para almacenamiento en red', price=249.99, category='Almacenamiento', stock=15, image='💾', rating=4.6),
    
    # MONITORES Y PANTALLAS
    Product(name='LG UltraGear 27" 4K', description='Monitor gaming 144Hz', price=599.99, category='Electrónica', stock=12, image='🖥️', rating=4.8),
    Product(name='Dell UltraSharp 32"', description='Monitor profesional 4K', price=749.99, category='Electrónica', stock=10, image='🖥️', rating=4.7),
    Product(name='Samsung Odyssey G7', description='Monitor curvo gaming', price=649.99, category='Electrónica', stock=14, image='🖥️', rating=4.6),
    
    # CÁMARAS Y FOTOGRAFÍA
    Product(name='GoPro Hero 12', description='Cámara de acción 5.3K', price=399.99, category='Electrónica', stock=18, image='📷', rating=4.7),
    Product(name='DJI Mini 4 Pro', description='Drone compacto con cámara 4K', price=759.99, category='Electrónica', stock=8, image='📷', rating=4.8),
    Product(name='Ring Video Doorbell', description='Timbre con cámara HD', price=99.99, category='Electrónica', stock=25, image='📷', rating=4.5),
    Product(name='Logitech StreamCam', description='Webcam 1080p para streaming', price=169.99, category='Accesorios', stock=22, image='📷', rating=4.6),
]

def añadir_productos():
    with app.app_context():
        print(f"📦 Añadiendo {len(productos_nuevos)} productos...")
        
        productos_añadidos = 0
        productos_existentes = 0
        
        for producto in productos_nuevos:
            # Verificar si el producto ya existe
            existe = Product.query.filter_by(name=producto.name).first()
            if existe:
                print(f"⚠️  '{producto.name}' ya existe, saltando...")
                productos_existentes += 1
            else:
                db.session.add(producto)
                productos_añadidos += 1
                print(f"✅ '{producto.name}' añadido")
        
        db.session.commit()
        
        print(f"\n🎉 ¡Completado!")
        print(f"   ✅ Productos nuevos: {productos_añadidos}")
        print(f"   ⚠️  Productos que ya existían: {productos_existentes}")
        print(f"   📊 Total en base de datos: {Product.query.count()}")

if __name__ == '__main__':
    añadir_productos()
