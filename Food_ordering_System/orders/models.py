from django.db import models
from datetime import datetime



class Category(models.Model):
    category_title = models.CharField(max_length=200)
    category_gif = models.ImageField(upload_to="media")
    category_description = models.TextField()
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
    
        return f"{self.category_title}"

    def has_add_permission(self):
        return False

class RegularPizza(models.Model):

    pizza_choice = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)
    category_description = models.TextField() 

    class Meta:
        verbose_name = "List of Regular Pizza"
        verbose_name_plural = "List of Regular Pizza"

    def __str__(self):
      
        return f"Regular Pizza : {self.pizza_choice}"

class Pizza(models.Model):

    pizza_choice = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)
    category_description = models.TextField() 

    class Meta:
        verbose_name = "List of Sicilian Pizza"
        verbose_name_plural = "List of Sicilian Pizza"
    
    def __str__(self):
      
        return f"Sicilian Pizza : {self.pizza_choice}"

class Toppings(models.Model):
  
    topping_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "List of Pizza Toppings"
        verbose_name_plural = "List of Pizza Toppings"
    

    def __str__(self):
       
        return f"{self.topping_name}"


class Sub(models.Model):
  
    sub_filling = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "List of Subway Food"
        verbose_name_plural = "List of Subway Food"
    

    def __str__(self):
      
        return f"Sub : {self.sub_filling}"

class Pasta(models.Model):
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "List of Pasta"
        verbose_name_plural = "List of Pasta"


    def __str__(self):
       
        return f"{self.dish_name}"


class Salad(models.Model):
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "List of Salad"
        verbose_name_plural = "List of Salad"


    def __str__(self):
       
        return f"Salad : {self.dish_name}"



class DinnerPlatters(models.Model):
    dish_name = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "List of Diner Platters"
        verbose_name_plural = "List of Diner Platters"


    def __str__(self):
       
        return f"Platter : {self.dish_name}"

class UserOrder(models.Model):
    username = models.CharField(max_length=200) 
    order = models.TextField() 
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    time_of_order  = models.DateTimeField(default=datetime.now, blank=True)
    delivered = models.BooleanField()

    class Meta:
        verbose_name = "User Order List"
        verbose_name_plural = "User Order List"

    def __str__(self):
       
        return f"Order placed by  : {self.username} on {self.time_of_order.date()} at {self.time_of_order.time().strftime('%H:%M:%S')}"

class SavedCarts(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    cart = models.TextField() 
    
    class Meta:
        verbose_name = "Saved Users Cart"
        verbose_name_plural = "Saved Users Cart"


    def __str__(self):
      
        return f"Saved cart for {self.username}"
