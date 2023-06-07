#include "lists.h"
#include <stdbool.h>

/**
 * check_cycle - checks if singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: true or false
 */
bool check_cycle(listint_t *list)
{
	listint_t *previous, *current;

	if (list == NULL || list->next == NULL)
	{
		return (false);
	}
	previous = list;
	current = list;
	while (current != NULL && current->next != NULL)
	{
		previous = previous->next;
		current = current->next->next;
		if (previous == current)
			return (true);
	}
	return (false);
}
