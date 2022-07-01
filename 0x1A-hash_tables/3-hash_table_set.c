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
	hash_node_t *array;
	unsigned long int i = 0;
	unsigned long int h;
	unsigned long int index;
	const unsigned char *str;

	array = malloc(sizeof(hash_node_t));
	if (array == NULL)
		return (0);

	str = (const unsigned char*)key;

	if ((strlen(key) == 0) || (key == NULL))
		return (0);

	h = ht->size;
	index = key_index(str, h);
	array->key = strdup(key);
	array->value = strdup(value);

	if (ht->array[index])
	{
		while ((ht->array[i]) && (i < h))
			i++;
		index = i;
	}
	ht->array[index] = array;
	
	return (1);
}
