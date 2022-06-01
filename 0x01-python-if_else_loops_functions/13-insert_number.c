#include "lists.h"
/**
 * insert_node - Inserts a new node in sorted order
 * @head: Pointer to pointer of the first node of listint_t list
 * @number: Integer to be included in the new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert;
	listint_t *current, *original;

	current = *head;
	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return NULL;
	insert->n = number;
	original = current;
	while (original->next->n < number || current->next != NULL)
	{
		original = current;
		current = current->next;
	}
	original->next = insert;
	insert->next = current;
	return *head;
}
