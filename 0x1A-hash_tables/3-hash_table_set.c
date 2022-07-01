#include "hash_tables.h"

/**
 * hash_table_set - Function that adds an element to the hash table
 * @ht: pointer to the hash table
 * @key: the key
 * @value: the value
 *
 * Return :1 if it succeeded, o otherwise
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	hash_node_t **array;
	int i;

	array = malloc(sizeof(hash_node_t));
	if (array == NULL)
		return (0);

	array = ht->array;

	if ((strlen(key) == 0) || (key == NULL)):
		return (0);

	for (i = 0; array != NULL; i++)
	{
		array = array[i];
	};

	array->key = key;
	array->value = value;

	return (1);
}
