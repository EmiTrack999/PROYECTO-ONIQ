"""
Script para resetear la base de datos y crear el usuario admin
Ejecutar en Replit si el admin no funciona
"""

from app import app, db, User, Product, bcrypt
import os

def reset_database():
    with app.app_context():
        print("🗑️  Eliminando base de datos antigua...")
        
        # Eliminar todas las tablas
        db.drop_all()
        print("✅ Tablas eliminadas")
        
        # Crear todas las tablas de nuevo
        db.create_all()
        print("✅ Tablas creadas")
        
        # Crear usuario admin
        hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
        admin = User(
            username='admin',
            email='admin@oniq.com',
            password=hashed_password,
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print('✅ Usuario admin creado')
        print('   Username: admin')
        print('   Password: admin123')
        
        # Agregar productos de ejemplo
        sample_products = [
            Product(name='Laptop Gaming Pro', description='Laptop de alta gama para gaming', price=1299.99, category='Electrónica', stock=15, image='💻', rating=4.5),
            Product(name='Smartphone Ultra', description='Teléfono inteligente de última generación', price=899.99, category='Electrónica', stock=25, image='📱', rating=4.7),
            Product(name='Auriculares Inalámbricos', description='Auriculares con cancelación de ruido', price=199.99, category='Audio', stock=50, image='🎧', rating=4.3),
            Product(name='Smart Watch', description='Reloj inteligente con GPS', price=299.99, category='Wearables', stock=30, image='⌚', rating=4.4),
            Product(name='Teclado Mecánico RGB', description='Teclado para gaming con iluminación', price=129.99, category='Accesorios', stock=40, image='⌨️', rating=4.6),
            Product(name='Mouse Gaming', description='Mouse ergonómico con sensor óptico', price=59.99, category='Accesorios', stock=60, image='🖱️', rating=4.5),
            Product(name='Monitor 4K', description='Monitor ultra HD de 27 pulgadas', price=449.99, category='Electrónica', stock=20, image='🖥️', rating=4.8),
            Product(name='Cámara Web HD', description='Cámara web para streaming', price=89.99, category='Accesorios', stock=35, image='📷', rating=4.2),
            Product(name='Tablet Pro', description='Tablet con stylus incluido', price=599.99, category='Electrónica', stock=18, image='📲', rating=4.6),
            Product(name='Disco SSD 1TB', description='Unidad de estado sólido rápida', price=119.99, category='Almacenamiento', stock=45, image='💾', rating=4.7)
        ]
        
        for product in sample_products:
            db.session.add(product)
        
        db.session.commit()
        print('✅ 10 productos de ejemplo agregados')
        print('\n🎉 ¡Base de datos reseteada exitosamente!')
        print('\n📋 Ahora puedes hacer login con:')
        print('   Usuario: admin')
        print('   Contraseña: admin123')

if __name__ == '__main__':
    reset_database()
