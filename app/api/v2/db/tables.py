"""
Creating Data Tables
"""

dt1 = """ CREATE TABLE IF NOT EXISTS users(
 user_id SERIAL PRIMARY KEY NOT NULL,
 user_name VARCHAR(255) NOT NULL,
 email VARCHAR(255) NOT NULL,
 password VARCHAR(255) NOT NULL,
 role INTEGER NOT NULL,
 token VARCHAR(255) NOT NULL,
 created_at timestamp with time zone DEFAULT now()
);"""


dt2 =""" CREATE TABLE IF NOT EXISTS meals(
    meal_id SERIAL PRIMARY KEY NOT NULL,
    meal_name VARCHAR(255) NOT NULL,
    price REAL NOT NULL,
    created_at timestamp with time zone DEFAULT now()
);"""

dt3 = """ CREATE TABLE IF NOT EXISTS menus(
    menu_id SERIAL PRIMARY KEY NOT NULL,
    meal_name VARCHAR(255) NOT NULL,
    created_at timestamp with time zone DEFAULT now()
);""" 

dt4 = """ CREATE TABLE IF NOT EXISTS menuitems(
    menuitem_id SERIAL PRIMARY KEY NOT NULL,
    meal_id INTEGER NOT NULL,
    menu_id INTEGER NOT NULL,
    no_available INTEGER NOT NULL,
    created_at timestamp with time zone DEFAULT now(),
    FOREIGN KEY (meal_id) REFERENCES meals (meal_id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (menu_id) REFERENCES menus (menu_id)
    ON UPDATE CASCADE ON DELETE CASCADE
    
);
"""


dt5 = """ CREATE TABLE IF NOT EXISTS orders(
    order_id SERIAL PRIMARY KEY NOT NULL,
    menuitem_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    status INTEGER NOT NULL,
    total REAL NOT NUll,
    created_at timestamp with time zone DEFAULT now(),
    FOREIGN KEY (menuitem_id) REFERENCES menuitems (menuitem_id)
    ON UPDATE CASCADE ON DELETE CASCADE );
"""
queries = [dt1, dt2, dt3, dt4, dt5]