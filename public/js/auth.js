// Configuración de API - Compatible con Node.js y Python Flask
const API_NODE = "http://localhost:3000/api/auth";
const API_PYTHON = window.location.hostname === 'localhost'
    ? 'http://localhost:5000/api/auth'
    : '/api/auth';

// Detectar qué backend está disponible
let API = API_PYTHON; // Por defecto usar Python

const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");
const message = document.getElementById("message");

// LOGIN
if (loginForm) {
  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (res.ok) {
      localStorage.setItem("token", data.token);
      localStorage.setItem("user", JSON.stringify(data.user));
      window.location.href = "store-enhanced.html";
    } else {
      message.textContent = data.message;
      message.style.color = "crimson";
    }
  });
}

// REGISTRO
if (registerForm) {
  registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, password })
    });

    const data = await res.json();

    if (res.ok) {
      message.textContent = "✅ Registro exitoso. Redirigiendo al login...";
      message.style.color = "#28a745";
      setTimeout(() => {
        window.location.href = "login.html";
      }, 1500);
    } else {
      message.textContent = data.message;
      message.style.color = "crimson";
    }
  });
}
