#include "hash_tables.h"

/**
 * hash_table_delete - Function that deletes a hash table
 * @ht: the hash table
 *
 * Return: Nothing
 */

void hash_table_delete(hash_table_t *ht)
{
	hash_node_t **array;
	unsigned long int i;

	array = malloc(sizeof(hash_node_t));
	if (array == NULL)
		i = 0;

	array = ht->array;

	for(i = 0; i < ht->size; i++)
	{
		if (array[i])
			free(array[i]);
	}
	free(array);
	free(ht);
}
