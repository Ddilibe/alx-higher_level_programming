#include "lists.h"

int is_palindrome(listint_t **head)
{ 
	int *ptr;
	int p = 0, y = 1, r, e, u;
	listint_t *current, *new_head;

	current = new_head = *head;
	ptr = malloc(sizeof(int));

	while (current != NULL)
	{
		*(ptr + p) = current->n;
		current = current->next;
		p++;
	}

	e = p-1, r = 0, u = 0;

	while (u < p)
	{
	        if (*(ptr + e) != *(ptr + r))
		{
			y = 0;
			break;
		}
		e--, r++, u++;
	}		
	return (y);
}
