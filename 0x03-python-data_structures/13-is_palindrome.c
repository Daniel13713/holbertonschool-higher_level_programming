#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - funtions that determinate palindrome linked list
 *
 * @head: linked list
 * Return: 0 if no is palindrome, 1 if yes
 */
int is_palindrome(listint_t **head)
{
listint_t *temp = NULL;
int array[1024];
int i = 0, j = 0;

temp = *head;

while (temp != NULL)
{
array[i] = temp->n;
temp = temp->next;
i++;
}

while (j < i / 2)
{
if (array[j] != array[(i - 1) - j])
{
return (0);
}
j++;
}
return (1);
}
