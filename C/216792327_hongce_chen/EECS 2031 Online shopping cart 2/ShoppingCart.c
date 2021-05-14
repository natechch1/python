#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ShoppingCart.h"

ShoppingCart AddItem(ItemToPurchase thisItem, ShoppingCart cart){
   cart.cartItems[cart.cartSize] = thisItem;
   cart.cartSize++;
   return cart;
   }
   
ShoppingCart RemoveItem(char name[], ShoppingCart cart){
   char itemFound = 'n';
   for (int i = 0; i < cart.cartSize; i++) {
      if (strcmp(name, cart.cartItems[i].itemName) == 0) {
         itemFound = 'y';
       // cart.cartItems[i] = cart.cartItems[i + 1];
         for (int j = i; j < cart.cartSize; j++) {
            cart.cartItems[j] = cart.cartItems[j + 1];
            
         }
      }
   }
   if (itemFound == 'y') {
      cart.cartSize = cart.cartSize - 1;
      printf("REMOVE ITEM FROM CART\n");
      printf("Enter name of item to remove:\n\n");
   }
   if (itemFound == 'n') {
       printf("REMOVE ITEM FROM CART\n");
   printf("Enter name of item to remove:\n");
      printf("Item not found in cart. Nothing removed.\n\n");
   }
   
   // for (int i = 0; i < cart.cartSize; i++) {
   //    if (strcmp(name, cart.cartItems[i].itemName) == 0) {
   //       cart.cartItems[i].itemQuantity = 0;
   //       cart.cartItems[i].itemPrice = 0;
   //    }
   // }
   
  
return cart;
}
   
   

ShoppingCart ModifyItem(char name[50], ShoppingCart cart){
   int num;
   char itemFound = 'n';
   scanf("%d",&num);
   
    for (int i = 0; i < cart.cartSize; i++) {
      if (strcmp(name, cart.cartItems[i].itemName) == 0) {
         cart.cartItems[i].itemQuantity = num;
         itemFound = 'y';
      }  
   }
   if(itemFound == 'n'){
      printf("Item not found in cart. Nothing modified.\n\n");
      }
   return cart;
   
   }
   
int GetNumItemsInCart(ShoppingCart cart){
   int count = 0;
   for (int i = 0; i < cart.cartSize; i++) {
      count += cart.cartItems[i].itemQuantity;
   }
   return count;
}
   
int GetCostOfCart(ShoppingCart cart){
   int total = 0;
   for (int i = 0; i < cart.cartSize; i++) {
      total += cart.cartItems[i].itemPrice * cart.cartItems[i].itemQuantity;
   }
   return total;
   }
   
void PrintTotal(ShoppingCart cart){
    printf("%s's Shopping Cart - %s\n", cart.customerName, cart.currentDate);
    printf("Number of Items: %d\n\n", GetNumItemsInCart(cart));
   if (GetNumItemsInCart(cart) == 0) {
     printf("SHOPPING CART IS EMPTY\n");
   } 
   else {
      for (int i = 0; i < cart.cartSize; i++) {
         PrintItemCost(cart.cartItems[i]);
      }
   }
   printf("\nTotal: $%d\n\n", GetCostOfCart(cart));
}
   
void PrintDescriptions(ShoppingCart cart){
   printf("%s\'s Shopping Cart - %s\n\n",cart.customerName,cart.currentDate);
   printf("Item Descriptions\n");
   for (int i = 0; i < cart.cartSize; i++) {
      PrintItemDescription(cart.cartItems[i]);
   }
   printf("\n");
   }
    