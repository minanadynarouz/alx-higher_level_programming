#include "lists.h"

/**
 * is_palindrome - function checks if LL is palindrome
 * @head: LL
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int *ll_arr, count = 0;
	size_t i = 0, start, end;
	listint_t *current = *head;

	while (current != NULL)
	{
		count++;
		current = current->next;
	}

	ll_arr = malloc(sizeof(int) * count);
	if (ll_arr == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		ll_arr[i] = current->n;
		current = current->next;
		i++;
	}

	for (start = 0, end = i - 1; start < end; start++, end--)
	{
		if (ll_arr[start] != ll_arr[end])
		{
			free(ll_arr);
			return (0);
		}
	}
	free(ll_arr);
	return (1);
}
