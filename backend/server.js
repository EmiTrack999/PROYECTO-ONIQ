import express from "express";
import cors from "cors";
import { fileURLToPath } from "url";
import { dirname, join } from "path";

import authRoutes from "./routes/auth.routes.js";
import productRoutes from "./routes/product.routes.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const publicPath = join(__dirname, "../public");

const app = express();

// Middlewares
app.use(cors());
app.use(express.json());
app.use(express.static(publicPath));

// Rutas
app.use("/api/auth", authRoutes);
app.use("/api/products", productRoutes);

// Test
app.get("/api/test", (req, res) => {
  res.json({ message: "Servidor ONIQ funcionando correctamente 🚀" });
});

// Servidor
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`✅ Servidor corriendo en http://localhost:${PORT}`);
});
