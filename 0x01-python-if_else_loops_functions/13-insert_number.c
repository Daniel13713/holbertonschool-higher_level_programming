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
	listint_t *new = NULL, *current = NULL;

	if (head)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
		{
			free(new);
			return (NULL);
		}
		new->n = number;
		new->next = NULL;
		current = *head;

		while (current)
		{
			if (current->n >= number)
			{
				new->next = current;
				*head = new;
				return (new);
			}
			else if (current->n <= number && current->next->n >= number)
			{
				if (current->next != NULL)
				{
					new->next = current->next;
					current->next = new;
					return (new);
				}
			}
			current = current->next;
		}
	}
	return (NULL);
}
