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
git clone https://github.com/SamuelPestan/products_expiration.git
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

## 📂 Estructura del proyecto

``` bash
products_expiration/                 # Carpeta principal del módulo
│── __init__.py                       # Archivo para definir los módulos a cargar
│── __manifest__.py                    # Archivo de descripción del módulo
│
├── models/                           # Modelos de datos
│   │── __init__.py                    # Importación de modelos
│   │── product_expiration.py           # Modelo principal de expiración de productos
│
├── views/                            # Vistas del módulo
│   │── expiracion_productos_view.xml  # Definición de las vistas del módulo
│
├── data/                             # Datos iniciales y cron jobs
│   │── expiracion_cron.xml            # Configuración del cron job
│
├── security/                         # Reglas de acceso
│   │── ir.model.access.csv            # Permisos de seguridad
```
