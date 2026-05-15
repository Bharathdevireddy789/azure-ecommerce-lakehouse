CREATE TABLE IF NOT EXISTS category_sales (
    category VARCHAR(255),
    total_sales FLOAT,
    product_count INT
);

CREATE TABLE IF NOT EXISTS top_products (
    id INT,
    title TEXT,
    category VARCHAR(255),
    price FLOAT,
    rating FLOAT
);