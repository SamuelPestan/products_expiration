{
    'name': 'Control de Expiración de Productos',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Gestiona la expiración de productos perecederos',
    'author': 'Samuel Pestana',
    'depends': ['base', 'stock', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/expiracion_productos_view.xml',
        'data/expiracion_cron.xml',
    ],
    'installable': True,
    'application': True,
}
