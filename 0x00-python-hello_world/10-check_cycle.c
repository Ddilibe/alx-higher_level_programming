#include "lists.h"

/**
 * check_cycle - Function to  check whether a singly
 * linked list has a cycle within
 * list - Pointer to a part pf the list
 * Return: 1 if there is a cycle else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *ahead, *behind;
	ahead = behind = list;

	while (ahead && behind && ahead->next)
	{
		behind = behind->next;
		ahead = ahead->next->next;
		if (behind == ahead)
			return (1);
	}
	return (0);
}
