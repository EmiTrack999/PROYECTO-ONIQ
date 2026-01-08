import { db } from "../db.js";
import bcrypt from "bcrypt";

// REGISTRO
export const register = async (req, res) => {
  try {
    const { name, email, password } = req.body;

    if (!name || !email || !password) {
      return res.status(400).json({ message: "Todos los campos son obligatorios" });
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    const query = `
      INSERT INTO users (name, email, password)
      VALUES (?, ?, ?)
    `;

    await db.execute(query, [name, email, hashedPassword]);
    res.json({ message: "Usuario registrado correctamente ✅" });
  } catch (err) {
    if (err.code === "ER_DUP_ENTRY") {
      return res.status(400).json({ message: "El correo ya existe" });
    }
    console.error("Error en registro:", err);
    res.status(500).json({ message: "Error al registrar usuario" });
  }
};

// LOGIN
export const login = async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ message: "Email y contraseña son obligatorios" });
    }

    const query = "SELECT * FROM users WHERE email = ?";
    const [results] = await db.execute(query, [email]);

    if (results.length === 0) {
      return res.status(400).json({ message: "Usuario no encontrado" });
    }

    const user = results[0];
    const match = await bcrypt.compare(password, user.password);

    if (!match) {
      return res.status(401).json({ message: "Contraseña incorrecta" });
    }

    res.json({
      message: "Login exitoso",
      user: {
        id: user.id,
        name: user.name,
        email: user.email
      }
    });
  } catch (err) {
    console.error("Error en login:", err);
    res.status(500).json({ message: "Error en el servidor" });
  }
};
