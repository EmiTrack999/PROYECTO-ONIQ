// ONIQ Store - Versión Simple sin Backend (Para Vercel)
// Todos los datos en localStorage

const productos = [
    { id: 1, name: 'MacBook Pro M3', description: 'Laptop profesional con chip M3, 16GB RAM', price: 2499.99, category: 'Electrónica', stock: 10, image: '💻', rating: 4.9 },
    { id: 2, name: 'iPad Air', description: 'Tablet versátil de 10.9 pulgadas', price: 699.99, category: 'Electrónica', stock: 15, image: '📱', rating: 4.7 },
    { id: 3, name: 'iPhone 15 Pro Max', description: 'Smartphone premium con titanio', price: 1299.99, category: 'Electrónica', stock: 20, image: '📱', rating: 4.8 },
    { id: 4, name: 'Samsung Galaxy S24 Ultra', description: 'Flagship con S Pen incluido', price: 1199.99, category: 'Electrónica', stock: 18, image: '📱', rating: 4.7 },
    { id: 5, name: 'Nintendo Switch OLED', description: 'Consola portátil con pantalla OLED', price: 349.99, category: 'Electrónica', stock: 25, image: '🎮', rating: 4.6 },
    { id: 6, name: 'PlayStation 5', description: 'Consola de nueva generación', price: 499.99, category: 'Electrónica', stock: 12, image: '🎮', rating: 4.8 },
    { id: 7, name: 'Xbox Series X', description: 'Consola 4K HDR gaming', price: 499.99, category: 'Electrónica', stock: 14, image: '🎮', rating: 4.7 },
    { id: 8, name: 'AirPods Pro 2', description: 'Auriculares con cancelación activa de ruido', price: 249.99, category: 'Audio', stock: 30, image: '🎧', rating: 4.8 },
    { id: 9, name: 'Sony WH-1000XM5', description: 'Auriculares premium con ANC', price: 399.99, category: 'Audio', stock: 20, image: '🎧', rating: 4.9 },
    { id: 10, name: 'Bose QuietComfort 45', description: 'Auriculares inalámbricos cómodos', price: 329.99, category: 'Audio', stock: 22, image: '🎧', rating: 4.7 },
    { id: 11, name: 'JBL Flip 6', description: 'Altavoz Bluetooth portátil resistente al agua', price: 129.99, category: 'Audio', stock: 35, image: '🔊', rating: 4.6 },
    { id: 12, name: 'Apple Watch Series 9', description: 'Smartwatch con pantalla Always-On', price: 429.99, category: 'Wearables', stock: 25, image: '⌚', rating: 4.8 },
    { id: 13, name: 'Samsung Galaxy Watch 6', description: 'Reloj inteligente con Wear OS', price: 329.99, category: 'Wearables', stock: 20, image: '⌚', rating: 4.6 },
    { id: 14, name: 'Fitbit Charge 6', description: 'Pulsera fitness con GPS', price: 159.99, category: 'Wearables', stock: 30, image: '⌚', rating: 4.5 },
    { id: 15, name: 'Magic Keyboard', description: 'Teclado inalámbrico premium', price: 149.99, category: 'Accesorios', stock: 25, image: '⌨️', rating: 4.7 },
    { id: 16, name: 'Logitech MX Master 3S', description: 'Mouse ergonómico profesional', price: 99.99, category: 'Accesorios', stock: 30, image: '🖱️', rating: 4.8 },
    { id: 17, name: 'Razer BlackWidow V4', description: 'Teclado mecánico gaming RGB', price: 179.99, category: 'Accesorios', stock: 20, image: '⌨️', rating: 4.7 },
    { id: 18, name: 'Samsung SSD 990 Pro 2TB', description: 'SSD NVMe ultrarrápido', price: 199.99, category: 'Almacenamiento', stock: 30, image: '💾', rating: 4.8 },
    { id: 19, name: 'WD My Passport 5TB', description: 'Disco duro externo portátil', price: 139.99, category: 'Almacenamiento', stock: 35, image: '💾', rating: 4.6 },
    { id: 20, name: 'Monitor 4K 27"', description: 'Monitor gaming 144Hz', price: 599.99, category: 'Electrónica', stock: 12, image: '🖥️', rating: 4.8 },
];

let cart = JSON.parse(localStorage.getItem('oniq_cart')) || [];
let wishlist = JSON.parse(localStorage.getItem('oniq_wishlist')) || [];
let currentCategory = 'all';
let currentSort = 'name';
let searchQuery = '';

// Inicializar
document.addEventListener('DOMContentLoaded', () => {
    loadProducts();
    updateCartCount();
    updateWishlistCount();
    setupEventListeners();
});

// Event Listeners
function setupEventListeners() {
    document.getElementById('searchBtn').addEventListener('click', () => {
        searchQuery = document.getElementById('searchInput').value;
        loadProducts();
    });

    document.getElementById('searchInput').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            searchQuery = e.target.value;
            loadProducts();
        }
    });

    document.querySelectorAll('.category-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            currentCategory = e.target.dataset.category;
            loadProducts();
        });
    });

    document.getElementById('sortBy').addEventListener('change', (e) => {
        currentSort = e.target.value;
        loadProducts();
    });

    document.getElementById('cartBtn').addEventListener('click', showCart);
    document.getElementById('wishlistBtn').addEventListener('click', showWishlist);
    
    document.querySelectorAll('.close-modal').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.target.closest('.modal').style.display = 'none';
        });
    });
    
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal')) {
            e.target.style.display = 'none';
        }
    });
}

// Cargar productos
function loadProducts() {
    let filteredProducts = productos;
    
    if (currentCategory !== 'all') {
        filteredProducts = filteredProducts.filter(p => p.category === currentCategory);
    }
    
    if (searchQuery) {
        filteredProducts = filteredProducts.filter(p => 
            p.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
            p.description.toLowerCase().includes(searchQuery.toLowerCase())
        );
    }
    
    filteredProducts.sort((a, b) => {
        switch(currentSort) {
            case 'price-asc': return a.price - b.price;
            case 'price-desc': return b.price - a.price;
            case 'rating': return b.rating - a.rating;
            default: return a.name.localeCompare(b.name);
        }
    });
    
    displayProducts(filteredProducts);
}

// Mostrar productos
function displayProducts(products) {
    const grid = document.getElementById('productsGrid');
    grid.innerHTML = products.map(product => `
        <div class="product-card">
            <div class="product-image">${product.image}</div>
            <button class="wishlist-btn ${isInWishlist(product.id) ? 'active' : ''}" 
                    onclick="toggleWishlist(${product.id})">
                ${isInWishlist(product.id) ? '❤️' : '🤍'}
            </button>
            <div class="product-info">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <div class="product-rating">${'⭐'.repeat(Math.floor(product.rating))} ${product.rating}</div>
                <div class="product-price">$${product.price.toFixed(2)}</div>
                <div class="product-actions">
                    <button class="btn-add-cart" onclick="addToCart(${product.id})">
                        🛒 Agregar
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

// Carrito
function addToCart(productId) {
    const product = productos.find(p => p.id === productId);
    const existing = cart.find(item => item.id === productId);
    
    if (existing) {
        existing.quantity++;
    } else {
        cart.push({ ...product, quantity: 1 });
    }
    
    localStorage.setItem('oniq_cart', JSON.stringify(cart));
    updateCartCount();
    showToast('Producto agregado al carrito', 'success');
}

function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    localStorage.setItem('oniq_cart', JSON.stringify(cart));
    updateCartCount();
    showCart();
}

function updateQuantity(productId, change) {
    const item = cart.find(i => i.id === productId);
    if (item) {
        item.quantity += change;
        if (item.quantity <= 0) {
            removeFromCart(productId);
        } else {
            localStorage.setItem('oniq_cart', JSON.stringify(cart));
            showCart();
        }
    }
}

function showCart() {
    const modal = document.getElementById('cartModal');
    const cartItems = document.getElementById('cartItems');
    
    if (cart.length === 0) {
        cartItems.innerHTML = '<p class="empty-cart">Tu carrito está vacío</p>';
        document.getElementById('cartTotal').textContent = '0.00';
    } else {
        cartItems.innerHTML = cart.map(item => `
            <div class="cart-item">
                <div class="cart-item-image">${item.image}</div>
                <div class="cart-item-info">
                    <h4>${item.name}</h4>
                    <p>$${item.price.toFixed(2)}</p>
                </div>
                <div class="cart-item-quantity">
                    <button onclick="updateQuantity(${item.id}, -1)">-</button>
                    <span>${item.quantity}</span>
                    <button onclick="updateQuantity(${item.id}, 1)">+</button>
                </div>
                <button class="btn-remove" onclick="removeFromCart(${item.id})">🗑️</button>
            </div>
        `).join('');
        
        const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        document.getElementById('cartTotal').textContent = total.toFixed(2);
    }
    
    modal.style.display = 'flex';
}

function updateCartCount() {
    const count = cart.reduce((sum, item) => sum + item.quantity, 0);
    document.getElementById('cartCount').textContent = count;
}

// Wishlist
function isInWishlist(productId) {
    return wishlist.includes(productId);
}

function toggleWishlist(productId) {
    if (isInWishlist(productId)) {
        wishlist = wishlist.filter(id => id !== productId);
        showToast('Eliminado de favoritos', 'info');
    } else {
        wishlist.push(productId);
        showToast('Agregado a favoritos', 'success');
    }
    
    localStorage.setItem('oniq_wishlist', JSON.stringify(wishlist));
    updateWishlistCount();
    loadProducts();
}

function showWishlist() {
    const modal = document.getElementById('wishlistModal');
    const wishlistItems = document.getElementById('wishlistItems');
    
    const wishlistProducts = productos.filter(p => wishlist.includes(p.id));
    
    if (wishlistProducts.length === 0) {
        wishlistItems.innerHTML = '<p class="empty-cart">No tienes favoritos</p>';
    } else {
        wishlistItems.innerHTML = wishlistProducts.map(product => `
            <div class="cart-item">
                <div class="cart-item-image">${product.image}</div>
                <div class="cart-item-info">
                    <h4>${product.name}</h4>
                    <p>$${product.price.toFixed(2)}</p>
                </div>
                <button class="btn-add-cart" onclick="addToCart(${product.id})">🛒 Agregar</button>
                <button class="btn-remove" onclick="toggleWishlist(${product.id})">❌</button>
            </div>
        `).join('');
    }
    
    modal.style.display = 'flex';
}

function updateWishlistCount() {
    document.getElementById('wishlistCount').textContent = wishlist.length;
}

// Checkout
function checkout() {
    if (cart.length === 0) {
        showToast('El carrito está vacío', 'error');
        return;
    }
    
    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    showToast(`¡Compra realizada! Total: $${total.toFixed(2)}`, 'success');
    
    cart = [];
    localStorage.setItem('oniq_cart', JSON.stringify(cart));
    updateCartCount();
    document.getElementById('cartModal').style.display = 'none';
}

// Toast
function showToast(message, type = 'info') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast show ${type}`;
    setTimeout(() => toast.classList.remove('show'), 3000);
}
