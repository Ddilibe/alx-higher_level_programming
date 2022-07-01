#include "hash_tables.h"

/**
 * hash_table_get - function that retrives a value associated with a key
 * @ht: the hash table we want to look into
 * @key: the key we are looking for
 *
 * Return: The value associated if success or NULL if fail
 */

char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned long int index;
	const unsigned char *str;
	unsigned long int h;
	const hash_table_t *new;
	hash_node_t **array;

	array = malloc(sizeof(hash_node_t));
	if (array == NULL)
		return (NULL);

	new = malloc(sizeof(hash_table_t) * ht->size);
	if (new == NULL)
		return (NULL);

	str = (const unsigned char *)key;
	h = ht->size;
	new = ht;
	array = new->array;
	index = key_index(str, h);


	if (array[index])
	{
		return (array[index]->value);	
	}
	return (NULL);
}
