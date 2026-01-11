// Configuración de API
const API_URL = 'http://localhost:5000/api';
let token = localStorage.getItem('token');
let currentUser = JSON.parse(localStorage.getItem('user') || '{}');
let cart = JSON.parse(localStorage.getItem('cart') || '[]');
let wishlist = [];
let allProducts = [];
let currentFilters = {
    search: '',
    category: 'all',
    minPrice: null,
    maxPrice: null,
    sortBy: 'created_at'
};

// ========== INICIALIZACIÓN ==========

document.addEventListener('DOMContentLoaded', () => {
    if (!token) {
        window.location.href = 'login.html';
        return;
    }
    
    initializeApp();
});

async function initializeApp() {
    document.getElementById('username').textContent = currentUser.username || 'Usuario';
    
    await loadProducts();
    await loadWishlist();
    updateCartDisplay();
    setupEventListeners();
}

// ========== EVENT LISTENERS ==========

function setupEventListeners() {
    // Búsqueda
    document.getElementById('searchBtn').addEventListener('click', handleSearch);
    document.getElementById('searchInput').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSearch();
    });
    
    // Categorías
    document.querySelectorAll('.category-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            currentFilters.category = e.target.dataset.category;
            filterAndDisplayProducts();
        });
    });
    
    // Ordenamiento
    document.getElementById('sortSelect').addEventListener('change', (e) => {
        currentFilters.sortBy = e.target.value;
        filterAndDisplayProducts();
    });
    
    // Filtro de precio
    document.getElementById('applyPriceFilter').addEventListener('click', () => {
        currentFilters.minPrice = parseFloat(document.getElementById('minPrice').value) || null;
        currentFilters.maxPrice = parseFloat(document.getElementById('maxPrice').value) || null;
        filterAndDisplayProducts();
    });
    
    // Carrito y Wishlist
    document.getElementById('cartBtn').addEventListener('click', openCartModal);
    document.getElementById('wishlistBtn').addEventListener('click', openWishlistModal);
    
    // Logout
    document.getElementById('logoutBtn').addEventListener('click', logout);
    
    // Modales
    document.querySelectorAll('.modal-close').forEach(closeBtn => {
        closeBtn.addEventListener('click', (e) => {
            e.target.closest('.modal').style.display = 'none';
        });
    });
    
    // Vista Grid/List
    document.querySelectorAll('.view-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            const view = e.target.dataset.view;
            const grid = document.getElementById('productsGrid');
            grid.className = view === 'list' ? 'products-list' : 'products-grid';
        });
    });
}

// ========== CARGAR PRODUCTOS ==========

async function loadProducts() {
    showLoading(true);
    
    try {
        const response = await fetch(`${API_URL}/products`);
        
        if (response.ok) {
            allProducts = await response.json();
            filterAndDisplayProducts();
        } else {
            showToast('Error al cargar productos', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showToast('Error de conexión', 'error');
    } finally {
        showLoading(false);
    }
}

function filterAndDisplayProducts() {
    let filtered = [...allProducts];
    
    // Filtro de búsqueda
    if (currentFilters.search) {
        filtered = filtered.filter(p => 
            p.name.toLowerCase().includes(currentFilters.search.toLowerCase())
        );
    }
    
    // Filtro de categoría
    if (currentFilters.category !== 'all') {
        filtered = filtered.filter(p => p.category === currentFilters.category);
    }
    
    // Filtro de precio
    if (currentFilters.minPrice !== null) {
        filtered = filtered.filter(p => p.price >= currentFilters.minPrice);
    }
    if (currentFilters.maxPrice !== null) {
        filtered = filtered.filter(p => p.price <= currentFilters.maxPrice);
    }
    
    // Ordenamiento
    switch (currentFilters.sortBy) {
        case 'price_asc':
            filtered.sort((a, b) => a.price - b.price);
            break;
        case 'price_desc':
            filtered.sort((a, b) => b.price - a.price);
            break;
        case 'rating':
            filtered.sort((a, b) => b.rating - a.rating);
            break;
        case 'popular':
            filtered.sort((a, b) => b.sales_count - a.sales_count);
            break;
        default:
            break;
    }
    
    displayProducts(filtered);
}

function displayProducts(products) {
    const grid = document.getElementById('productsGrid');
    
    if (products.length === 0) {
        grid.innerHTML = '<div class="no-products">No se encontraron productos 😢</div>';
        return;
    }
    
    grid.innerHTML = products.map(product => `
        <div class="product-card" data-id="${product.id}">
            <div class="product-image">${product.image || '📦'}</div>
            <div class="product-badge">${product.category}</div>
            <div class="product-wishlist-btn" onclick="toggleWishlist(${product.id}, event)">
                ${wishlist.some(w => w.product_id === product.id) ? '❤️' : '🤍'}
            </div>
            
            <div class="product-info">
                <h3 class="product-name">${product.name}</h3>
                <div class="product-rating">
                    ${'⭐'.repeat(Math.round(product.rating))}${'☆'.repeat(5 - Math.round(product.rating))}
                    <span class="rating-number">${product.rating}</span>
                </div>
                <div class="product-price-row">
                    <span class="product-price">$${product.price.toFixed(2)}</span>
                    <span class="product-stock">${product.stock > 0 ? `${product.stock} disponibles` : 'Agotado'}</span>
                </div>
                <div class="product-sales">🔥 ${product.sales_count} vendidos</div>
                
                <div class="product-actions">
                    <button class="btn-quick-add" onclick="quickAddToCart(${product.id})" ${product.stock === 0 ? 'disabled' : ''}>
                        🛒 Agregar
                    </button>
                    <button class="btn-view-details" onclick="openProductModal(${product.id})">
                        Ver Detalles
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

// ========== BÚSQUEDA ==========

function handleSearch() {
    currentFilters.search = document.getElementById('searchInput').value;
    filterAndDisplayProducts();
}

// ========== CARRITO ==========

function quickAddToCart(productId) {
    const product = allProducts.find(p => p.id === productId);
    
    if (!product || product.stock === 0) {
        showToast('Producto no disponible', 'error');
        return;
    }
    
    const existingItem = cart.find(item => item.product_id === productId);
    
    if (existingItem) {
        if (existingItem.quantity < product.stock) {
            existingItem.quantity++;
        } else {
            showToast('Stock máximo alcanzado', 'warning');
            return;
        }
    } else {
        cart.push({
            product_id: productId,
            name: product.name,
            price: product.price,
            image: product.image,
            quantity: 1,
            stock: product.stock
        });
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartDisplay();
    showToast(`${product.name} agregado al carrito`, 'success');
}

function updateCartDisplay() {
    const count = cart.reduce((total, item) => total + item.quantity, 0);
    document.getElementById('cartCount').textContent = count;
}

function openCartModal() {
    const modal = document.getElementById('cartModal');
    const cartItemsDiv = document.getElementById('cartItems');
    
    if (cart.length === 0) {
        cartItemsDiv.innerHTML = '<div class="empty-cart">Tu carrito está vacío 🛒</div>';
        document.getElementById('cartTotal').textContent = '$0.00';
    } else {
        cartItemsDiv.innerHTML = cart.map((item, index) => `
            <div class="cart-item">
                <div class="cart-item-image">${item.image}</div>
                <div class="cart-item-info">
                    <h4>${item.name}</h4>
                    <p class="cart-item-price">$${item.price.toFixed(2)}</p>
                </div>
                <div class="cart-item-quantity">
                    <button onclick="updateCartQuantity(${index}, -1)">-</button>
                    <span>${item.quantity}</span>
                    <button onclick="updateCartQuantity(${index}, 1)">+</button>
                </div>
                <div class="cart-item-total">$${(item.price * item.quantity).toFixed(2)}</div>
                <button class="cart-item-remove" onclick="removeFromCart(${index})">🗑️</button>
            </div>
        `).join('');
        
        const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        document.getElementById('cartTotal').textContent = `$${total.toFixed(2)}`;
    }
    
    modal.style.display = 'flex';
}

function updateCartQuantity(index, change) {
    const item = cart[index];
    const newQuantity = item.quantity + change;
    
    if (newQuantity <= 0) {
        removeFromCart(index);
        return;
    }
    
    if (newQuantity > item.stock) {
        showToast('Stock máximo alcanzado', 'warning');
        return;
    }
    
    item.quantity = newQuantity;
    localStorage.setItem('cart', JSON.stringify(cart));
    openCartModal();
    updateCartDisplay();
}

function removeFromCart(index) {
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    openCartModal();
    updateCartDisplay();
}

// ========== CHECKOUT ==========

document.addEventListener('DOMContentLoaded', () => {
    const checkoutBtn = document.getElementById('checkoutBtn');
    if (checkoutBtn) {
        checkoutBtn.addEventListener('click', async () => {
            if (cart.length === 0) {
                showToast('El carrito está vacío', 'warning');
                return;
            }
            
            try {
                const response = await fetch(`${API_URL}/orders`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify({
                        items: cart.map(item => ({
                            product_id: item.product_id,
                            quantity: item.quantity
                        }))
                    })
                });
                
                if (response.ok) {
                    const data = await response.json();
                    showToast(`¡Orden creada exitosamente! ID: ${data.order_id}`, 'success');
                    cart = [];
                    localStorage.setItem('cart', JSON.stringify(cart));
                    updateCartDisplay();
                    document.getElementById('cartModal').style.display = 'none';
                    loadProducts(); // Recargar para actualizar stock
                } else {
                    const error = await response.json();
                    showToast(error.message || 'Error al crear la orden', 'error');
                }
            } catch (error) {
                console.error('Error:', error);
                showToast('Error de conexión', 'error');
            }
        });
    }
});

// ========== WISHLIST ==========

async function loadWishlist() {
    try {
        const response = await fetch(`${API_URL}/wishlist`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        
        if (response.ok) {
            wishlist = await response.json();
            document.getElementById('wishlistCount').textContent = wishlist.length;
        }
    } catch (error) {
        console.error('Error al cargar wishlist:', error);
    }
}

async function toggleWishlist(productId, event) {
    event.stopPropagation();
    
    const isInWishlist = wishlist.some(w => w.product.id === productId);
    
    try {
        const url = `${API_URL}/wishlist/${productId}`;
        const method = isInWishlist ? 'DELETE' : 'POST';
        
        const response = await fetch(url, {
            method,
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        
        if (response.ok) {
            await loadWishlist();
            filterAndDisplayProducts(); // Actualizar iconos
            showToast(isInWishlist ? 'Eliminado de wishlist' : 'Agregado a wishlist', 'success');
        }
    } catch (error) {
        console.error('Error:', error);
        showToast('Error al actualizar wishlist', 'error');
    }
}

function openWishlistModal() {
    const modal = document.getElementById('wishlistModal');
    const wishlistItemsDiv = document.getElementById('wishlistItems');
    
    if (wishlist.length === 0) {
        wishlistItemsDiv.innerHTML = '<div class="empty-wishlist">Tu wishlist está vacía ❤️</div>';
    } else {
        wishlistItemsDiv.innerHTML = wishlist.map(item => `
            <div class="wishlist-item">
                <div class="wishlist-item-image">${item.product.image}</div>
                <div class="wishlist-item-info">
                    <h4>${item.product.name}</h4>
                    <p class="wishlist-item-price">$${item.product.price.toFixed(2)}</p>
                </div>
                <div class="wishlist-item-actions">
                    <button class="btn-primary" onclick="quickAddToCart(${item.product.id})">🛒 Agregar</button>
                    <button class="btn-secondary" onclick="toggleWishlist(${item.product.id}, event)">🗑️</button>
                </div>
            </div>
        `).join('');
    }
    
    modal.style.display = 'flex';
}

// ========== MODAL DE PRODUCTO ==========

let currentProductId = null;
let selectedRating = 0;

async function openProductModal(productId) {
    currentProductId = productId;
    
    try {
        const response = await fetch(`${API_URL}/products/${productId}`);
        
        if (response.ok) {
            const product = await response.json();
            
            document.getElementById('modalImage').textContent = product.image || '📦';
            document.getElementById('modalName').textContent = product.name;
            document.getElementById('modalDescription').textContent = product.description || 'Sin descripción';
            document.getElementById('modalPrice').textContent = `$${product.price.toFixed(2)}`;
            document.getElementById('modalStock').textContent = product.stock > 0 ? `${product.stock} disponibles` : 'Agotado';
            document.getElementById('modalRating').innerHTML = `
                ${'⭐'.repeat(Math.round(product.rating))}${'☆'.repeat(5 - Math.round(product.rating))}
                <span>${product.rating} (${product.reviews.length} reseñas)</span>
            `;
            
            // Mostrar reseñas
            const reviewsList = document.getElementById('reviewsList');
            if (product.reviews.length > 0) {
                reviewsList.innerHTML = product.reviews.map(review => `
                    <div class="review">
                        <div class="review-header">
                            <strong>${review.user}</strong>
                            <span class="review-rating">${'⭐'.repeat(review.rating)}</span>
                        </div>
                        <p class="review-comment">${review.comment}</p>
                        <span class="review-date">${new Date(review.created_at).toLocaleDateString()}</span>
                    </div>
                `).join('');
            } else {
                reviewsList.innerHTML = '<p>No hay reseñas aún. ¡Sé el primero en dejar una!</p>';
            }
            
            document.getElementById('productModal').style.display = 'flex';
        }
    } catch (error) {
        console.error('Error:', error);
        showToast('Error al cargar producto', 'error');
    }
}

// Controles de cantidad en modal
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('decreaseQty')?.addEventListener('click', () => {
        const input = document.getElementById('quantityInput');
        if (input.value > 1) input.value = parseInt(input.value) - 1;
    });
    
    document.getElementById('increaseQty')?.addEventListener('click', () => {
        const input = document.getElementById('quantityInput');
        input.value = parseInt(input.value) + 1;
    });
    
    document.getElementById('addToCartModal')?.addEventListener('click', () => {
        const quantity = parseInt(document.getElementById('quantityInput').value);
        const product = allProducts.find(p => p.id === currentProductId);
        
        if (product) {
            for (let i = 0; i < quantity; i++) {
                quickAddToCart(currentProductId);
            }
            document.getElementById('productModal').style.display = 'none';
        }
    });
    
    // Sistema de rating
    document.querySelectorAll('#starRating .star').forEach(star => {
        star.addEventListener('click', () => {
            selectedRating = parseInt(star.dataset.rating);
            updateStarDisplay();
        });
    });
    
    // Enviar reseña
    document.getElementById('submitReview')?.addEventListener('click', async () => {
        if (selectedRating === 0) {
            showToast('Por favor selecciona una calificación', 'warning');
            return;
        }
        
        const comment = document.getElementById('reviewComment').value;
        
        try {
            const response = await fetch(`${API_URL}/products/${currentProductId}/reviews`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    rating: selectedRating,
                    comment
                })
            });
            
            if (response.ok) {
                showToast('Reseña enviada exitosamente', 'success');
                selectedRating = 0;
                document.getElementById('reviewComment').value = '';
                updateStarDisplay();
                openProductModal(currentProductId); // Recargar
            } else {
                const error = await response.json();
                showToast(error.message || 'Error al enviar reseña', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showToast('Error de conexión', 'error');
        }
    });
});

function updateStarDisplay() {
    document.querySelectorAll('#starRating .star').forEach((star, index) => {
        star.textContent = index < selectedRating ? '★' : '☆';
    });
}

// ========== UTILIDADES ==========

function showLoading(show) {
    document.getElementById('loadingSpinner').style.display = show ? 'flex' : 'none';
}

function showToast(message, type = 'info') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast toast-${type} show`;
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    localStorage.removeItem('cart');
    window.location.href = 'login.html';
}

// Cerrar modales al hacer clic fuera
window.onclick = (event) => {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
};
