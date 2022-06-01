#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert;
	listint_t *current;

	current = *head;
	insert = malloc(sizeof(listint_t
