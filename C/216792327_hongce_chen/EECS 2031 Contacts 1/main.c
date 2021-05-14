#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include "ContactNode.h"

int main(int argc, char* argv[])
{

ContactNode* person[3] = {NULL, NULL, NULL};
for(int i=0; i < 3; i++)
{
ContactNode temp;
printf("Person %d\n", i+1);
printf("Enter name:\n");
fgets(temp.contactName, 50, stdin);
temp.contactName[strlen(temp.contactName)-1]='\0';
printf("Enter phone number:\n");
fgets(temp.contactPhoneNum, 50, stdin);
temp.contactPhoneNum[strlen(temp.contactPhoneNum)]='\0';
printf("You entered: %s, %s\n", temp.contactName, temp.contactPhoneNum);
person[i]=(ContactNode*)malloc(sizeof(ContactNode));
*person[i]=CreateContactNode(person[i], temp.contactName, temp.contactPhoneNum, NULL);
}
InsertContactAfter(person[0], person[1]);
InsertContactAfter(person[1], person[2]);
printf("\n");
printf("CONTACT LIST\n");
PrintContactNode(person[0]);
PrintContactNode(person[1]);
PrintContactNode(person[2]);
printf("\n");
return 0;
}