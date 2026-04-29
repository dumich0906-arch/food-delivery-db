
SELECT * FROM customers;

SELECT name, phone FROM restaurants WHERE cuisine = 'Итальянская';

SELECT * FROM orders WHERE status = 'Доставлен';

SELECT name, rating FROM restaurants ORDER BY rating DESC;

SELECT DISTINCT cuisine FROM restaurants;


SELECT c.name, o.items, o.total_amount 
FROM customers c 
JOIN orders o ON c.id = o.customer_id 
WHERE o.total_amount > 1000;

SELECT r.name, r.cuisine, COUNT(o.id) as order_count 
FROM restaurants r 
LEFT JOIN orders o ON r.id = o.restaurant_id 
GROUP BY r.id;

SELECT * FROM orders 
WHERE status = 'Доставлен' AND total_amount BETWEEN 500 AND 1500;

SELECT c.name, c.phone 
FROM customers c 
WHERE c.id IN (SELECT customer_id FROM orders WHERE status = 'Отменён');

SELECT r.name, r.rating 
FROM restaurants r 
WHERE r.rating >= 4.5 AND (r.cuisine = 'Японская' OR r.cuisine = 'Китайская');

SELECT * FROM orders 
WHERE order_date LIKE '2026-04%' AND status NOT IN ('Отменён', 'Ожидает');

SELECT c.name, SUM(o.total_amount) as total_spent 
FROM customers c 
JOIN orders o ON c.id = o.customer_id 
WHERE o.status != 'Отменён' 
GROUP BY c.id 
HAVING total_spent > 2000;

SELECT r.cuisine, AVG(r.rating) as avg_rating, COUNT(o.id) as total_orders
FROM restaurants r
LEFT JOIN orders o ON r.id = o.restaurant_id
GROUP BY r.cuisine
ORDER BY avg_rating DESC;

SELECT * FROM customers 
WHERE address LIKE '%Ленина%' OR address LIKE '%Пушкина%';

SELECT o.id, o.items, o.total_amount, c.name as customer, r.name as restaurant
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN restaurants r ON o.restaurant_id = r.id
WHERE o.status = 'В пути' AND o.total_amount > 800
ORDER BY o.order_date DESC;

SELECT status, COUNT(*) as count, AVG(total_amount) as avg_amount
FROM orders
GROUP BY status
HAVING count > 2;

SELECT * FROM restaurants 
WHERE rating BETWEEN 3.5 AND 4.2 AND cuisine NOT IN ('Русская', 'Американская');

SELECT c.name, COUNT(o.id) as order_count, MAX(o.total_amount) as max_order
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.id
HAVING order_count >= 2;

SELECT * FROM orders 
WHERE (status = 'Доставлен' OR status = 'В пути') 
AND total_amount > 500 
AND order_date > '2026-03-01';

SELECT r.name, r.phone, 
       (SELECT COUNT(*) FROM orders WHERE restaurant_id = r.id AND status = 'Доставлен') as delivered
FROM restaurants r
WHERE r.rating > 4.0;