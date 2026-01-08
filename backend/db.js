import mysql from "mysql2/promise";

export const db = await mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "oniq_store"
});

console.log("✅ Conectado a MySQL");

// Crear tabla de usuarios si no existe
const createTableQuery = `
  CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
`;

try {
  await db.execute(createTableQuery);
  console.log("✅ Tabla users lista");
} catch (err) {
  console.error("Error al crear tabla:", err);
}
