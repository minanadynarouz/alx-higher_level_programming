#include "lists.h"

/**
 * is_palindrome - function checks if LL is palindrome
 * @head: LL
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int *ll_arr;
	size_t i = 0, start, end;
	listint_t *current = *head;

	ll_arr = malloc(sizeof(listint_t));
	if (ll_arr == NULL || *head == NULL)
		return (1);

	while (current != NULL)
	{
		ll_arr[i] = current->n;
		current = current->next;
		i++;
	}

	if (i % 2 == 0)
	{
		for (start = 0, end = i - 1; start < i / 2, end >= i / 2; start++, end--)
		{
			if (ll_arr[start] != ll_arr[end])
				return (0);
		}
	}
	else
	{
		for (start = 0, end = i - 1; start < i / 2, end > i / 2; start++, end--)
		{
			if (ll_arr[start] != ll_arr[end])
				return (0);
		}
	}
	free(ll_arr);
	return (1);
}
