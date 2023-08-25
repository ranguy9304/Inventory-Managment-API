# from django.db import migrations


# class Migration(migrations.Migration):

#     dependencies = [
#         ('api', '0001_initial'),
#     ]

#     operations = [
#         migrations.RunSQL('''   
#             CREATE TRIGGER restock_trigger 
#             AFTER UPDATE ON api_product
#             FOR EACH ROW
#             BEGIN
#                 IF NEW.quantity < 10 THEN
#                     INSERT INTO api_restockrequest (product_id, created_at) 
#                     VALUES (NEW.id, NOW());
#                 END IF;
#             END;
#         '''),

#         migrations.RunSQL('''
#             CREATE TRIGGER order_trigger 
#             AFTER INSERT ON api_order
#             FOR EACH ROW
#             BEGIN
#                 UPDATE api_product 
#                 SET stock = stock - 1 
#                 WHERE id = NEW.product_id;
#             END;
#         ''')
#     ]


# #baibhav

# # fuck
# # tanish 
# #  subham
# # takayuki

# # kill
# # aditi   --> very competetive not team ... wants her thing to work only ( valid )
# # david jijo jiji --> not focused [ hidden chapri ] 23 mins to run yolo    bb are very good 
# # vaishnavai