#include "lists.h"
#include <stdbool.h>

/**
 * check_cycle - checks if singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: true or false
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *previous;

	if (!list)
		return (0);

	current = list;
	previous = list;
	while (current && previous && previous->next)
	{
		current = current->next;
		previous = ->next->next;
		if (previous == current || previous == list)
			return (1);
	}
	return (0);
}
