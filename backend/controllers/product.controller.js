import { db } from "../db.js";

export const getProducts = async (req, res) => {
  try {
    const [results] = await db.query("SELECT * FROM products");
    res.json(results);
  } catch (err) {
    console.error("Error al obtener productos:", err);
    res.status(500).json({ message: "Error al obtener productos" });
  }
};

export const addProduct = async (req, res) => {
  try {
    const { name, price, image } = req.body;

    if (!name || !price) {
      return res.status(400).json({ message: "Faltan datos" });
    }

    const sql = "INSERT INTO products (name, price, image) VALUES (?, ?, ?)";
    await db.execute(sql, [name, price, image]);

    res.json({ message: "Producto agregado correctamente" });
  } catch (err) {
    console.error("Error al agregar producto:", err);
    res.status(500).json({ message: "Error al agregar producto" });
  }
};
