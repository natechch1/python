#include<stdio.h>
#include<string.h>

#include "ItemToPurchase.h"

ItemToPurchase CreatItemNode(struct ItemToPurchase* thisItem, char name[], int price, int quantity,int cost){
   strcpy(thisItem->itemName, name);
   thisItem->itemPrice = price;
   thisItem->itemQuantity = quantity;
   // thisItem->nextNode = address;
   thisItem->itemCost = cost;
   return *thisItem;
   }
   
// ItemToPurchase nextNode(ItemToPurchase* thisItem){
//    return thisItem->nextNode ;
//    }

// ItemToPurchase calCost(ItemToPurchase* thisItem){
//    thisItem->itemCost = thisItem->itemQuantity * thisItem->itemPrice;
//    return;
//    }

// void InsertItemAfter(ItemToPurchase* thisItem, ItemToPurchase* nextItem){
//    ItemToPurchase* tmpNext = NULL;
//    tmpNext = thisItem->nextNode;
//    thisItem->nextNode = nextItem;
//    nextItem->nextNode = tmpNext;
// return;
//    }

void MakeItemBlank(ItemToPurchase* thisItem){
   strcpy(thisItem->itemName ,"none");
   thisItem->itemPrice = 0;
   thisItem->itemQuantity = 0;
   return;
   }

void PrintItemCost(ItemToPurchase* thisItem){
   printf("%s %d @ $%d = $%d\n",thisItem->itemName,thisItem->itemQuantity,thisItem->itemPrice,thisItem->itemCost);
   return;
   }