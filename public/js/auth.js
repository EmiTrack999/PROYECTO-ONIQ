// 🎭 LOGIN FANTASMA - Sin base de datos, todo en localStorage
// Perfecto para Vercel y despliegues sin backend

const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");
const message = document.getElementById("message");

// LOGIN FANTASMA
if (loginForm) {
  loginForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Validación simple
    if (!username || !password) {
      message.textContent = "❌ Por favor completa todos los campos";
      message.style.color = "crimson";
      return;
    }

    // Guardar sesión fantasma
    const fakeToken = btoa(`${username}:${Date.now()}`);
    const fakeUser = {
      id: Math.random().toString(36).substr(2, 9),
      username: username,
      email: `${username}@oniq.com`,
      isAdmin: username.toLowerCase() === 'admin'
    };

    localStorage.setItem("token", fakeToken);
    localStorage.setItem("user", JSON.stringify(fakeUser));

    // Mensaje de éxito
    message.textContent = "✅ ¡Bienvenido! Accediendo a la tienda...";
    message.style.color = "#28a745";

    // Redirigir a la tienda
    setTimeout(() => {
      window.location.href = "store-enhanced.html";
    }, 800);
  });
}

// REGISTRO FANTASMA
if (registerForm) {
  registerForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const username = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Validación simple
    if (!username || !email || !password) {
      message.textContent = "❌ Por favor completa todos los campos";
      message.style.color = "crimson";
      return;
    }

    if (password.length < 4) {
      message.textContent = "❌ La contraseña debe tener al menos 4 caracteres";
      message.style.color = "crimson";
      return;
    }

    // Simular registro exitoso
    message.textContent = "✅ ¡Registro exitoso! Redirigiendo al login...";
    message.style.color = "#28a745";

    setTimeout(() => {
      window.location.href = "login.html";
    }, 1200);
  });
}
