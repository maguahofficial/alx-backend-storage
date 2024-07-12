-- ThisScript creates a trigger to decrease the
-- quantity of an item after adding a new order.
CREATE TRIGGER decrease_i AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
