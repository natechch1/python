#include <stdio.h>
#include <stdlib.h>
#include "ContactNode.h"


ContactNode CreateContactNode(struct ContactNode* contact, char name[50], char number[50], ContactNode* address)
{

strcpy(contact->contactName, name);
strcpy(contact->contactPhoneNum, number);
contact->nextNodePtr=address;

return *contact;
}
void InsertContactAfter(ContactNode* contact, ContactNode* nextcontact)
{
ContactNode* tmpNext = NULL;
tmpNext = contact->nextNodePtr;
contact->nextNodePtr = nextcontact;
nextcontact->nextNodePtr = tmpNext;
return;
}
ContactNode* GetNextContact(ContactNode* contact)
{
return contact->nextNodePtr;
}
void PrintContactNode(const ContactNode* contact)
{
printf("Name: %s\n", contact->contactName);
printf("Phone number: %s\n", contact->contactPhoneNum);//same as above
return;
}