#include "hash_tables.h"

/**
 * hash_table_create - a function that creates a hash table
 * @size: the size of the array
 *
 * Return: a pointer if success and Null if fail
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_node_t **array;
	hash_table_t *table;
	unsigned long int i;

	table = malloc(sizeof(hash_table_t));
	if (table == NULL)
		return NULL;

	array = malloc(sizeof(hash_node_t) * size);
	if (array == NULL)
		return NULL;

	for (i = 0; i < size; i++)
		*(array+i) = NULL;

	table->array = array;
	table->size = size;
	
	return (table);
}
