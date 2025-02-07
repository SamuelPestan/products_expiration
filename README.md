# ⏳ Control de Expiración de Productos

**Módulo para Odoo 18 que permite gestionar la expiración de productos y enviar alertas antes del vencimiento.**  
Ideal para empresas que manejan productos perecederos como alimentos, medicamentos o cosméticos.  

## 🚀 Características

- 📅 **Registro de fechas de caducidad** para productos.
- 🔔 **Notificaciones automáticas** antes del vencimiento.
- 📊 **Reportes de productos próximos a expirar**.
- 📉 **Gestión de desperdicio o promociones** antes del vencimiento.

---

## 📦 Instalación

### 1️⃣ **Copiar el módulo en Odoo**
Clona este repositorio dentro de la carpeta de módulos de Odoo:

```bash
cd /ruta/de/tu/odoo/addons/
git clone https://github.com/tuusuario/control_expiracion_productos.git
```

Reinicia el servidor de Odoo:

``` bash
sudo systemctl restart odoo
```

---

## 2️⃣ Instalar el módulo

- Activa el Modo Desarrollador en Odoo.
- Ve a **Apps** y haz clic en **Actualizar lista de aplicaciones**.
- Busca **Control de Expiración de Productos** y haz clic en **Instalar**.

## 🛠 Uso

### ➤ Acceder al módulo

Ve a **Inventario > Control de Expiración de Productos**.

### ➤ Añadir un producto con fecha de expiración

1. Crea un nuevo registro.
2. Selecciona el producto y establece la fecha de caducidad.
3. Guarda los cambios.

### ➤ Recibir alertas de expiración

Odoo enviará notificaciones automáticas cuando un producto esté próximo a vencer.

## 📂 Estructura del Proyecto

```bash
products_expiration/
│── models/
│   ├── product_expiration.py  # Modelo de expiración de productos
│── views/
│   ├── expiration_product_view.xml  # Definición de las vistas
│── data/
│   ├── expiration_cron.xml  # Tarea automática de verificación
│── __manifest__.py  # Configuración del módulo
│── __init__.py  # Inicialización del módulo
│── README.md  # Documentación

