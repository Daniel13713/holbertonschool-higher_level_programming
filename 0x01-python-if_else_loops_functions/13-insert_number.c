#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * *insert_node - insert a new node and number
 *
 * @head: list
 * @number: new number
 * Return: New node or null if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current = NULL, *copy = *head;
	int i = 0, j = 0;

	if (head)
	{
		while (number > copy->n || head == NULL)
		{
			copy = copy->next;
			i++;
		}
		new = malloc(sizeof(listint_t));
		if (!new)
		{
			free(new);
			return (NULL);
		}
		new->n = number;
		new->next = NULL;
		if (i == 0)
		{
			new->next = *head;
			*head = new;
			return (new);
		}
		current = *head;
		for (j = 0; j < i - 1; j++)
		{
			current = current->next;
			if (!current)
			{
				free(new);
				return (NULL);
			}
		}
		new->next = current->next;
		current->next = new;
		new = new->next;
		return (new);
	}
	return (NULL);
}
