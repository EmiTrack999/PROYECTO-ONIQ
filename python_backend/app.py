from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import jwt
from functools import wraps
import os

app = Flask(__name__, static_folder='../public', static_url_path='')
CORS(app)

# Configuración
app.config['SECRET_KEY'] = 'tu_clave_secreta_super_segura_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oniq_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# ========== MODELOS DE BASE DE DATOS ==========

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)
    
    # Relaciones
    orders = db.relationship('Order', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)
    wishlist = db.relationship('Wishlist', backref='user', lazy=True)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100))
    stock = db.Column(db.Integer, default=0)
    image = db.Column(db.String(500))
    rating = db.Column(db.Float, default=0.0)
    sales_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    reviews = db.relationship('Review', backref='product', lazy=True)
    order_items = db.relationship('OrderItem', backref='product', lazy=True)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, processing, shipped, delivered
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

# ========== MIDDLEWARE DE AUTENTICACIÓN ==========

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'message': 'Token no proporcionado'}), 401
        
        try:
            if token.startswith('Bearer '):
                token = token.split(' ')[1]
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
            if not current_user:
                return jsonify({'message': 'Usuario no encontrado'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 401
        except:
            return jsonify({'message': 'Token inválido'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# ========== RUTAS DE AUTENTICACIÓN ==========

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username or not email or not password:
        return jsonify({'message': 'Faltan datos'}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'El usuario ya existe'}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'El email ya está registrado'}), 400
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'Usuario registrado exitosamente'}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Credenciales inválidas'}), 401
    
    token = jwt.encode({
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(days=7)
    }, app.config['SECRET_KEY'], algorithm='HS256')
    
    return jsonify({
        'token': token,
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_admin': user.is_admin
        }
    }), 200

# ========== RUTAS DE PRODUCTOS ==========

@app.route('/api/products', methods=['GET'])
def get_products():
    # Filtros y búsqueda
    search = request.args.get('search', '')
    category = request.args.get('category', '')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    sort_by = request.args.get('sort_by', 'created_at')
    
    query = Product.query
    
    if search:
        query = query.filter(Product.name.ilike(f'%{search}%'))
    
    if category:
        query = query.filter_by(category=category)
    
    if min_price:
        query = query.filter(Product.price >= min_price)
    
    if max_price:
        query = query.filter(Product.price <= max_price)
    
    # Ordenamiento
    if sort_by == 'price_asc':
        query = query.order_by(Product.price.asc())
    elif sort_by == 'price_desc':
        query = query.order_by(Product.price.desc())
    elif sort_by == 'rating':
        query = query.order_by(Product.rating.desc())
    elif sort_by == 'popular':
        query = query.order_by(Product.sales_count.desc())
    else:
        query = query.order_by(Product.created_at.desc())
    
    products = query.all()
    
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': p.price,
        'category': p.category,
        'stock': p.stock,
        'image': p.image,
        'rating': p.rating,
        'sales_count': p.sales_count
    } for p in products]), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    
    reviews = [{
        'id': r.id,
        'user': r.user.username,
        'rating': r.rating,
        'comment': r.comment,
        'created_at': r.created_at.isoformat()
    } for r in product.reviews]
    
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category': product.category,
        'stock': product.stock,
        'image': product.image,
        'rating': product.rating,
        'sales_count': product.sales_count,
        'reviews': reviews
    }), 200

@app.route('/api/products', methods=['POST'])
@token_required
def add_product(current_user):
    if not current_user.is_admin:
        return jsonify({'message': 'No autorizado'}), 403
    
    data = request.get_json()
    
    product = Product(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price'),
        category=data.get('category'),
        stock=data.get('stock', 0),
        image=data.get('image', '')
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify({'message': 'Producto agregado', 'id': product.id}), 201

@app.route('/api/products/<int:product_id>', methods=['PUT'])
@token_required
def update_product(current_user, product_id):
    if not current_user.is_admin:
        return jsonify({'message': 'No autorizado'}), 403
    
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.category = data.get('category', product.category)
    product.stock = data.get('stock', product.stock)
    product.image = data.get('image', product.image)
    
    db.session.commit()
    
    return jsonify({'message': 'Producto actualizado'}), 200

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
@token_required
def delete_product(current_user, product_id):
    if not current_user.is_admin:
        return jsonify({'message': 'No autorizado'}), 403
    
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({'message': 'Producto eliminado'}), 200

# ========== RUTAS DE REVIEWS ==========

@app.route('/api/products/<int:product_id>/reviews', methods=['POST'])
@token_required
def add_review(current_user, product_id):
    data = request.get_json()
    
    product = Product.query.get_or_404(product_id)
    
    # Verificar si ya existe una review
    existing_review = Review.query.filter_by(
        user_id=current_user.id,
        product_id=product_id
    ).first()
    
    if existing_review:
        return jsonify({'message': 'Ya has dejado una reseña para este producto'}), 400
    
    review = Review(
        user_id=current_user.id,
        product_id=product_id,
        rating=data.get('rating'),
        comment=data.get('comment', '')
    )
    
    db.session.add(review)
    
    # Actualizar rating del producto
    reviews = Review.query.filter_by(product_id=product_id).all()
    avg_rating = sum(r.rating for r in reviews + [review]) / len(reviews + [review])
    product.rating = round(avg_rating, 1)
    
    db.session.commit()
    
    return jsonify({'message': 'Reseña agregada', 'rating': product.rating}), 201

# ========== RUTAS DE ÓRDENES ==========

@app.route('/api/orders', methods=['POST'])
@token_required
def create_order(current_user):
    data = request.get_json()
    items = data.get('items', [])
    
    if not items:
        return jsonify({'message': 'El carrito está vacío'}), 400
    
    total = 0
    order_items = []
    
    for item in items:
        product = Product.query.get(item['product_id'])
        if not product:
            return jsonify({'message': f'Producto {item["product_id"]} no encontrado'}), 404
        
        if product.stock < item['quantity']:
            return jsonify({'message': f'Stock insuficiente para {product.name}'}), 400
        
        total += product.price * item['quantity']
        order_items.append({
            'product': product,
            'quantity': item['quantity']
        })
    
    # Crear orden
    order = Order(user_id=current_user.id, total=total)
    db.session.add(order)
    db.session.flush()
    
    # Agregar items y actualizar stock
    for item in order_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product'].id,
            quantity=item['quantity'],
            price=item['product'].price
        )
        db.session.add(order_item)
        
        # Actualizar stock y ventas
        item['product'].stock -= item['quantity']
        item['product'].sales_count += item['quantity']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Orden creada exitosamente',
        'order_id': order.id,
        'total': total
    }), 201

@app.route('/api/orders', methods=['GET'])
@token_required
def get_orders(current_user):
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    
    return jsonify([{
        'id': o.id,
        'total': o.total,
        'status': o.status,
        'created_at': o.created_at.isoformat(),
        'items': [{
            'product_name': item.product.name,
            'quantity': item.quantity,
            'price': item.price
        } for item in o.items]
    } for o in orders]), 200

@app.route('/api/orders/<int:order_id>', methods=['GET'])
@token_required
def get_order(current_user, order_id):
    order = Order.query.get_or_404(order_id)
    
    if order.user_id != current_user.id and not current_user.is_admin:
        return jsonify({'message': 'No autorizado'}), 403
    
    return jsonify({
        'id': order.id,
        'total': order.total,
        'status': order.status,
        'created_at': order.created_at.isoformat(),
        'items': [{
            'product_id': item.product.id,
            'product_name': item.product.name,
            'quantity': item.quantity,
            'price': item.price
        } for item in order.items]
    }), 200

# ========== RUTAS DE WISHLIST ==========

@app.route('/api/wishlist', methods=['GET'])
@token_required
def get_wishlist(current_user):
    wishlist_items = Wishlist.query.filter_by(user_id=current_user.id).all()
    
    return jsonify([{
        'id': item.id,
        'product': {
            'id': item.product_id,
            'name': Product.query.get(item.product_id).name,
            'price': Product.query.get(item.product_id).price,
            'image': Product.query.get(item.product_id).image
        }
    } for item in wishlist_items]), 200

@app.route('/api/wishlist/<int:product_id>', methods=['POST'])
@token_required
def add_to_wishlist(current_user, product_id):
    product = Product.query.get_or_404(product_id)
    
    existing = Wishlist.query.filter_by(
        user_id=current_user.id,
        product_id=product_id
    ).first()
    
    if existing:
        return jsonify({'message': 'Producto ya está en la wishlist'}), 400
    
    wishlist_item = Wishlist(user_id=current_user.id, product_id=product_id)
    db.session.add(wishlist_item)
    db.session.commit()
    
    return jsonify({'message': 'Producto agregado a wishlist'}), 201

@app.route('/api/wishlist/<int:product_id>', methods=['DELETE'])
@token_required
def remove_from_wishlist(current_user, product_id):
    wishlist_item = Wishlist.query.filter_by(
        user_id=current_user.id,
        product_id=product_id
    ).first_or_404()
    
    db.session.delete(wishlist_item)
    db.session.commit()
    
    return jsonify({'message': 'Producto eliminado de wishlist'}), 200

# ========== RUTAS DE ANÁLISIS Y ESTADÍSTICAS ==========

@app.route('/api/analytics/dashboard', methods=['GET'])
@token_required
def analytics_dashboard(current_user):
    if not current_user.is_admin:
        return jsonify({'message': 'No autorizado'}), 403
    
    total_products = Product.query.count()
    total_orders = Order.query.count()
    total_users = User.query.count()
    total_revenue = db.session.query(db.func.sum(Order.total)).scalar() or 0
    
    # Productos más vendidos
    top_products = db.session.query(Product).order_by(Product.sales_count.desc()).limit(5).all()
    
    # Productos con bajo stock
    low_stock = Product.query.filter(Product.stock < 10).all()
    
    return jsonify({
        'summary': {
            'total_products': total_products,
            'total_orders': total_orders,
            'total_users': total_users,
            'total_revenue': round(total_revenue, 2)
        },
        'top_products': [{
            'name': p.name,
            'sales': p.sales_count,
            'revenue': p.price * p.sales_count
        } for p in top_products],
        'low_stock_alerts': [{
            'id': p.id,
            'name': p.name,
            'stock': p.stock
        } for p in low_stock]
    }), 200

# ========== RECOMENDACIONES ==========

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    # Productos más populares
    popular = Product.query.order_by(Product.sales_count.desc()).limit(6).all()
    
    # Productos mejor valorados
    top_rated = Product.query.filter(Product.rating >= 4.0).order_by(Product.rating.desc()).limit(6).all()
    
    return jsonify({
        'popular': [{
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'image': p.image,
            'rating': p.rating
        } for p in popular],
        'top_rated': [{
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'image': p.image,
            'rating': p.rating
        } for p in top_rated]
    }), 200

# ========== CATEGORÍAS ==========

@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = db.session.query(Product.category, db.func.count(Product.id)).group_by(Product.category).all()
    
    return jsonify([{
        'name': cat[0],
        'count': cat[1]
    } for cat in categories if cat[0]]), 200

# ========== RUTAS PARA SERVIR ARCHIVOS HTML ==========

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'welcome.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# ========== RUTA DE PRUEBA ==========

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'Backend Python ONIQ funcionando correctamente! 🐍🚀'}), 200

# ========== INICIALIZACIÓN ==========

def init_db():
    with app.app_context():
        db.create_all()
        
        # Crear usuario admin si no existe
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin = User(
                username='admin',
                email='admin@oniq.com',
                password=hashed_password,
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print('✅ Usuario admin creado (username: admin, password: admin123)')
        
        # Agregar productos de ejemplo si no hay productos
        if Product.query.count() == 0:
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
            print('✅ Productos de ejemplo agregados')

if __name__ == '__main__':
    with app.app_context():
        init_db()
    print('🚀 Servidor Python iniciando en http://localhost:5000')
    app.run(debug=True, port=5000)
