#include "hash_tables.h"

/**
 * key_index - Function that gives you the index of a key.
 * @key: the key
 * @size: The size of the array
 *
 * Return: the index at which the data should be saved
 */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int index;
	unsigned long int develop;

	index = hash_djb2(key);

	develop = index % size;

	return (develop);
}	
