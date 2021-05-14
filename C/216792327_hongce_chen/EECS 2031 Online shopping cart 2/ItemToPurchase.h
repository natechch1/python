#ifndef ITEM_TO_PURCHASE_H
#define ITEM_TO_PURCHASE_H
#include <stdio.h>
#include <stdlib.h>
#define ITEM_DESC_LEN 100

typedef struct ItemToPurchase{
   char itemName[50];
   int itemPrice;
   int itemQuantity;
   int itemCost;
   char itemDescription[ITEM_DESC_LEN];
   //struct ItemToPurchase* nextNode;
}ItemToPurchase;

ItemToPurchase CreatItemNode(struct ItemToPurchase* thisItem, char name[], int price, int quantity, int cost);
void MakeItemBlank(ItemToPurchase* thisItem); 
void PrintItemCost(ItemToPurchase thisItem);
// ItemToPurchase calCost(ItemToPurchase* thisItem);
void InsertItemAfter(ItemToPurchase* thisItem, ItemToPurchase* nextItem);
ItemToPurchase nextNode(ItemToPurchase* thisItem);
void PrintItemDescription(ItemToPurchase thisItem);

#endif