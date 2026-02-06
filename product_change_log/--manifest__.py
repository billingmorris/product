{
    'name': 'Product Change Log',
    'version': '14.0.1.0.0',
    'summary': 'Registro de cambios en productos',
    'category': 'Inventory',
    'author': 'Tu Empresa',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_log_views.xml',
    ],
    'installable': True,
    'application': False,
}
