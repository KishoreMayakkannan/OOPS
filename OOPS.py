class Product:
    #class attributes 
    def __init__(self,name,price,deal_price,rating):
        #istances Attributes
        self.name = name 
        self.price = price 
        self.deal_price = deal_price 
        self.rating = rating 
        self.you_save = price - deal_price 
    def display_product_details(self):
        print("Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("deal_price: {}".format(self.deal_price))
        print("You_save: {}".format(self.you_save))
        print("Rating: {}".format(self.rating))
    def get_deal_price(self):
        return self.deal_price
#Inheritance;subclass-->ElectronicItem ; superclass-->Product
class ElectronicItem(Product):
    #method Overriding
    def __init__(self,name,price,deal_price,rating,warranty_in_months):
        super().__init__(name,price,deal_price,rating)
        self.warranty_in_months = warranty_in_months
    #method Overriding
    def display_product_details(self):
        super().display_product_details()
        print("Warranty in months : {}".format(self.warranty_in_months))
# Multilevel Inheritance        
class Laptop(ElectronicItem):
    def __init__(self,name,price,deal_price,rating,warranty_in_months,ram,os,storage):
        super().__init__(name,price,deal_price,rating,warranty_in_months)
        self.ram = ram 
        self.os = os 
        self.storage = storage 
    def display_product_details(self):
        super().display_product_details()
        print("RAM : {}".format(self.ram))
        print("OS : {}".format(self.os))
        print("Storage : {}".format(self.storage))
        
    
#Inheritance;subclass-->GroceryItem ; superclass-->Product
class GroceryItem(Product):
    #method Overriding
    def __init__(self,name,price,deal_price,rating,expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.expiry_date = expiry_date
    #method Overriding
    def display_product_details(self):
        super().display_product_details()
        print("Expiry date : {}".format(self.expiry_date))        

class Order:
    #class attribute
    delivery_charge = {"prime_delivery" : 0 , "normal_delivery": 50}
    
    def __init__ (self,delivery_speed,delivery_address):
        self.items_in_cart = [] # list contains (product,quantity) -->composition = one class instance used attribute
        self.delivery_speed = delivery_speed 
        self.delivery_address = delivery_address 
        
    def add_item(self,product,quantity):
         item = (product,quantity)
         self.items_in_cart.append(item)
        
    def display_order_details(self):
        print("Order type : {}".format(self.delivery_speed))
        print("Delivery address : {}".format(self.delivery_address))
        for product,quantity in self.items_in_cart:
            print("--------------")
            product.display_product_details()
            print("Quantity : {}\n".format(quantity))
        print("--------------")
        order_delivery_charges = Order.get_delivery_charges(self.delivery_speed) 
        print("Delivery charges:{}".format(order_delivery_charges))
        print("Total Bill : {}".format(self.get_total_bill()))
    
    def get_total_bill(self):
        total_bill = 0 
        for product,quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity 
            total_bill += price 
        order_delivery_charges = Order.get_delivery_charges(self.delivery_speed)
        total_bill += order_delivery_charges
        return total_bill    
        
    @classmethod
    def get_delivery_charges(cls,order_type):
        return cls.delivery_charge[order_type]
    
#instantiation : (creating an instance of class = object)  
tv = ElectronicItem("TV",40000,35000,4.5,24)
flour = GroceryItem("wheatFlour",100,90,4,"Jan-2021")
laptop = Laptop("lenovo",40000,35000,4.5,24,"8 GB","Linux","1 TB SSD")
# tv.display_product_details()
# flour.display_product_details()
my_order = Order("normal_delivery","chennai")
my_order.add_item(tv,1)
my_order.add_item(laptop,2)

my_order.display_order_details()