#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ShoppingCart.h"



void PrintMenu(ShoppingCart cart);
ShoppingCart MenuAddItem(ShoppingCart cart);
ShoppingCart MenuRemoveItem(ShoppingCart cart);
ShoppingCart MenuChangeItemQty(ShoppingCart cart);
void MenuPrintDescriptions(ShoppingCart cart);
void MenuOutputCart(ShoppingCart cart);

int main(int argc, char const *argv[]) {
char name[50];
char date[20];
char choice = ' ';
char tmp;
ShoppingCart cart;
printf("Enter Customer's Name:\n");
fgets(name, 50, stdin);
name[strlen(name) - 1] = '\0';
printf("Enter Today's Date:\n");
fgets(date, 50, stdin);
date[strlen(date) - 1] = '\0';

strcpy(cart.customerName, name);
strcpy(cart.currentDate, date);
cart.cartSize = 0;
printf("\n");
printf("Customer Name: %s\n", cart.customerName);
printf("Today's Date: %s\n\n", cart.currentDate);

PrintMenu(cart);
// printf("Choose an option:\n");
while (choice != 'q'){
   

scanf(" %c%c", &choice, &tmp);
switch (choice) {
   case 'a':
      cart = MenuAddItem(cart);
      PrintMenu(cart);
      printf("Choose an option:\n");
   break;
  
   case 'r':
      cart = MenuRemoveItem(cart);
      PrintMenu(cart);
      printf("Choose an option:\n");
   break;
   
   case 'f':
   printf("Choose an option:\n");
   break;
   case 's':
   printf("Choose an option:\n");
   printf("Choose an option:\n");
   break;
  
   

   case 'i':
      MenuPrintDescriptions(cart);
      PrintMenu(cart);
      printf("Choose an option:\n");
   break;

   case 'o':
      MenuOutputCart(cart);
      PrintMenu(cart);
      printf("Choose an option:\n");
   break;
   
   case 'c':
      cart = MenuChangeItemQty(cart);
      PrintMenu(cart);
      printf("Choose an option:\n");
   break;
      
   case 'q':
   break;
   
   default:
   break;
}
} 
return 0;
}

void PrintMenu(ShoppingCart cart) {
printf("MENU\n");
printf("a - Add item to cart\n");
printf("r - Remove item from cart\n");
printf("c - Change item quantity\n");
printf("i - Output items' descriptions\n");
printf("o - Output shopping cart\n");
printf("q - Quit\n\n");
}

ShoppingCart MenuAddItem(ShoppingCart cart) {
char item_name[50];
char item_desc[100];
int item_price = 0;
int item_qty = 0;
ItemToPurchase item;

printf("ADD ITEM TO CART\n");
printf("Enter the item name:\n");
fgets(item_name, 50, stdin);
item_name[strlen(item_name) - 1] = '\0';
strcpy(item.itemName, item_name);

printf("Enter the item description:\n");
fgets(item_desc, 100, stdin);
item_desc[strlen(item_desc) - 1] = '\0';
strcpy(item.itemDescription, item_desc);

printf("Enter the item price:\n");
scanf("%d", &item_price);
item.itemPrice = item_price;

printf("Enter the item quantity:\n\n");
scanf("%d", &item_qty);
item.itemQuantity = item_qty;

cart = AddItem(item, cart);
return cart;
}

ShoppingCart MenuRemoveItem(ShoppingCart cart) {
   char name[50];
   fgets(name,50,stdin);
   name[strlen(name) - 1] = '\0';
   cart = RemoveItem(name,cart);
   // for (int i = 0; i < cart.cartSize; i++) {
   //    if (strcmp(item_name, cart.cartItems[i].itemName) == 1) {
   //     cart = RemoveItem(item_name, cart);
   //    } 
   //    else {
   //     printf("Item not found in cart. Nothing removed.\n\n");
   //    }
   // }
      return cart;
}

ShoppingCart MenuChangeItemQty(ShoppingCart cart) {
   char name[50];

   printf("CHANGE ITEM QUANTITY\n");
   printf("Enter the item name:\n");
   printf("Enter the new quantity:\n");
   fgets(name, 50, stdin);
   name[strlen(name) - 1] = '\0';
   cart = ModifyItem(name,cart);
   return cart;
}

void MenuPrintDescriptions(ShoppingCart cart) {
   printf("OUTPUT ITEMS' DESCRIPTIONS\n");
   PrintDescriptions(cart);
}

void MenuOutputCart(ShoppingCart cart) {
   printf("OUTPUT SHOPPING CART\n");
   PrintTotal(cart);
}