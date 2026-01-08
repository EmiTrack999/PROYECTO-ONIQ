const API = "http://localhost:3000/api/auth";

const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");
const message = document.getElementById("message");

// LOGIN
if (loginForm) {
  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (res.ok) {
      localStorage.setItem("user", JSON.stringify(data.user));
      window.location.href = "store.html";
    } else {
      message.textContent = data.message;
    }
  });
}

// REGISTRO
if (registerForm) {
  registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, password })
    });

    const data = await res.json();

    if (res.ok) {
      alert("Registro exitoso ✅");
      window.location.href = "/";
    } else {
      message.textContent = data.message;
    }
  });
}
