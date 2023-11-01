#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	
	new->n = number;
	new->next = NULL;

	if (current == NULL || current->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
