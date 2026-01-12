#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de diagnóstico completo para el problema de login
"""

from app import app, db, User, bcrypt

def diagnosticar_login():
    with app.app_context():
        print("="*60)
        print("🔍 DIAGNÓSTICO COMPLETO DEL LOGIN")
        print("="*60)
        
        # 1. Verificar si hay usuarios
        total_users = User.query.count()
        print(f"\n📊 Total de usuarios en la BD: {total_users}")
        
        if total_users == 0:
            print("❌ No hay usuarios en la base de datos!")
            print("🔧 Creando usuario admin ahora...")
            
            hashed = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin = User(
                username='admin',
                email='admin@oniq.com',
                password=hashed,
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ Usuario admin creado")
        
        # 2. Listar todos los usuarios
        print("\n👥 USUARIOS EN LA BASE DE DATOS:")
        for user in User.query.all():
            badge = " 👑 ADMIN" if user.is_admin else ""
            print(f"   ID: {user.id} | Username: '{user.username}' | Email: {user.email}{badge}")
        
        # 3. Buscar específicamente al admin
        print("\n🔍 BUSCANDO USUARIO 'admin'...")
        admin = User.query.filter_by(username='admin').first()
        
        if not admin:
            print("❌ ¡Usuario 'admin' NO EXISTE!")
            print("🔧 Esto explica el error. Creando admin ahora...")
            
            hashed = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin = User(
                username='admin',
                email='admin@oniq.com',
                password=hashed,
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ Usuario admin creado exitosamente")
            
            # Volver a buscar
            admin = User.query.filter_by(username='admin').first()
        
        # 4. Mostrar detalles del admin
        print("\n✅ USUARIO ADMIN ENCONTRADO:")
        print(f"   ID: {admin.id}")
        print(f"   Username: '{admin.username}'")
        print(f"   Email: {admin.email}")
        print(f"   Is Admin: {admin.is_admin}")
        print(f"   Password Hash: {admin.password[:50]}...")
        
        # 5. PRUEBA CRÍTICA: Verificar la contraseña
        print("\n🔐 PRUEBA DE CONTRASEÑA:")
        
        test_passwords = ['admin123', 'Admin123', 'ADMIN123', ' admin123', 'admin123 ']
        
        for pwd in test_passwords:
            result = bcrypt.check_password_hash(admin.password, pwd)
            status = "✅ CORRECTA" if result else "❌ INCORRECTA"
            print(f"   '{pwd}' → {status}")
        
        # 6. Crear nueva contraseña correcta si falla
        if not bcrypt.check_password_hash(admin.password, 'admin123'):
            print("\n⚠️  ¡LA CONTRASEÑA NO COINCIDE!")
            print("🔧 Regenerando contraseña correctamente...")
            
            # Generar nuevo hash
            new_hash = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin.password = new_hash
            db.session.commit()
            
            # Verificar de nuevo
            check = bcrypt.check_password_hash(admin.password, 'admin123')
            if check:
                print("✅ ¡Contraseña regenerada y FUNCIONA!")
            else:
                print("❌ Algo está muy mal con bcrypt")
        else:
            print("\n✅ La contraseña 'admin123' es CORRECTA")
        
        # 7. Resumen final
        print("\n" + "="*60)
        print("📋 RESUMEN:")
        print("="*60)
        admin = User.query.filter_by(username='admin').first()
        password_ok = bcrypt.check_password_hash(admin.password, 'admin123')
        
        if admin and password_ok:
            print("✅ Usuario admin existe")
            print("✅ Contraseña funciona")
            print("\n🎉 TODO DEBERÍA FUNCIONAR AHORA")
            print("\n🔐 Usa estas credenciales:")
            print("   👤 Usuario: admin")
            print("   🔑 Contraseña: admin123")
            print("\n⚠️  IMPORTANTE: Escribe 'admin123' exactamente así")
            print("   (sin espacios, todo minúsculas)")
        else:
            print("❌ Algo sigue mal")
            if not admin:
                print("   - Usuario admin no existe")
            if admin and not password_ok:
                print("   - Contraseña no funciona")
        
        print("="*60)

if __name__ == '__main__':
    diagnosticar_login()
