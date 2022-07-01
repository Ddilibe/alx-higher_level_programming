#include "hash_tables.h"

/**
 * hash_table_print - function that prints a hash table
 * @ht: The hash table
 *
 * Return: nothing
 */
void hash_table_print(const hash_table_t *ht)
{
	hash_node_t **array;
	unsigned long int i, w = 0;

	array = malloc(sizeof(hash_node_t));
	if (array == NULL)
		i = 0;

	if (ht != NULL) 
	{
		printf("{");
		array = ht->array;
		for(i = 0; i < ht->size; i++)
		{
			if (array[i])
			{
				printf("'%s': '%s'", array[i]->key, array[i]->value);
				w++;
			}
			if (array[i+1] && w > 0 )
				printf(", ");
		}
		printf("}\n");
	}
}
