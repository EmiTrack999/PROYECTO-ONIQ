"""
Script para verificar el estado del usuario admin
y recrearlo si es necesario
"""

from app import app, db, User, bcrypt

def verificar_admin():
    with app.app_context():
        print("🔍 Verificando usuario admin...\n")
        
        # Buscar usuario admin
        admin = User.query.filter_by(username='admin').first()
        
        if not admin:
            print("❌ Usuario admin NO existe")
            print("🔧 Creando usuario admin...\n")
            
            # Crear admin
            hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin = User(
                username='admin',
                email='admin@oniq.com',
                password=hashed_password,
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            
            print("✅ Usuario admin creado exitosamente!")
            print("   Username: admin")
            print("   Password: admin123")
            print("   Email: admin@oniq.com")
            print("   Is Admin: True")
            
        else:
            print("✅ Usuario admin existe")
            print(f"   ID: {admin.id}")
            print(f"   Username: {admin.username}")
            print(f"   Email: {admin.email}")
            print(f"   Is Admin: {admin.is_admin}")
            print(f"   Password Hash: {admin.password[:30]}...")
            
            # Verificar que la contraseña funcione
            test_password = 'admin123'
            password_ok = bcrypt.check_password_hash(admin.password, test_password)
            
            print(f"\n🔐 Prueba de contraseña 'admin123': {'✅ CORRECTA' if password_ok else '❌ INCORRECTA'}")
            
            if not password_ok:
                print("\n⚠️  La contraseña NO coincide. Actualizando...")
                admin.password = bcrypt.generate_password_hash('admin123').decode('utf-8')
                db.session.commit()
                print("✅ Contraseña actualizada correctamente")
        
        # Mostrar todos los usuarios
        print(f"\n📊 Total de usuarios en la base de datos: {User.query.count()}")
        print("\n👥 Lista de usuarios:")
        for user in User.query.all():
            admin_badge = " 👑" if user.is_admin else ""
            print(f"   - {user.username} ({user.email}){admin_badge}")
        
        print("\n" + "="*50)
        print("🎉 Verificación completada")
        print("="*50)
        print("\n📝 Ahora intenta hacer login con:")
        print("   Usuario: admin")
        print("   Contraseña: admin123")

if __name__ == '__main__':
    verificar_admin()
