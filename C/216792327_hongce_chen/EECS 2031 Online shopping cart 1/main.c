#include<stdio.h>
#include <stdlib.h>
#include<string.h>
#include "ItemToPurchase.h"

int main(void) {
   ItemToPurchase* item[2] = {NULL,NULL};
   int cost = 0;
    char c;
   for(int i = 0; i < 2; i++){
      ItemToPurchase temp;
      printf("Item %d\n", i+1);
      printf("Enter the item name:\n");
      fgets(temp.itemName, 50, stdin);
      temp.itemName[strlen(temp.itemName)-1]='\0';
      scanf("%d", &temp.itemPrice);
      printf("Enter the item price:\n");
      scanf("%d", &temp.itemQuantity);
      printf("Enter the item quantity:\n\n");
     

      temp.itemCost = temp.itemPrice * temp.itemQuantity;
      cost += temp.itemCost;
      item[i] = (ItemToPurchase*)malloc(sizeof(ItemToPurchase));
      *item[i] = CreatItemNode(item[i], temp.itemName, temp.itemPrice, temp.itemQuantity,temp.itemCost);
      // *item[i] = nextNode(item[i]);
      c = getchar();
      while(c != '\n' && c != EOF) {
          c = getchar();
         }
      }
  // InsertItemAfter(item[0],item[1]);
   printf("TOTAL COST\n");
   PrintItemCost(item[0]);
   PrintItemCost(item[1]);
   printf("\n");
   printf("Total: $%d\n",cost);
   return 0;
}