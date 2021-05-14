// #ifndef SHOPPING_CART_H
// #define SHOPPING_CART_H

#include <stdio.h>
#include <stdlib.h>
#include "ItemToPurchase.h"

typedef struct ShoppingCart{
   char customerName[50];
   char currentDate[50];
   ItemToPurchase cartItems[10];
   int cartSize;
   char itemDescription[50];
   }ShoppingCart;
   
ShoppingCart AddItem(ItemToPurchase thisItem, ShoppingCart cart);
ShoppingCart RemoveItem(char name[], ShoppingCart cart);
ShoppingCart ModifyItem(char name[50], ShoppingCart cart);
int GetNumItemsInCart(ShoppingCart cart);
int GetCostOfCart(ShoppingCart cart);
void PrintTotal(ShoppingCart cart);
void PrintDescriptions(ShoppingCart cart);