from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buying_cost, selling_cost, manufactuer) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_cost, product.manufacturer_id]
    results = run_sql(sql, values)
    # id = results[0]['id']
    product.id = id
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)