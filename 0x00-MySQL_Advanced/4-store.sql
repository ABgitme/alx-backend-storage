-- Create a trigger that decreases the quantity of an item after a new order is added
-- Update the quantity of the ordered item in the items table
-- Decrease the quantity by the amount ordered
-- Match the item by item_id in the order
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
