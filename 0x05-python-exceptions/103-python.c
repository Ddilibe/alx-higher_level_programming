#include <stdio.h>
#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_bytes - prints bytes information
 *
 * @p: python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return ;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);


	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		if (string[i] >= 0)
			printf("  %02x", string[i]);
		else
			printf("  %02x", 256 + string[i]);
	}
	printf("\n");
}
/**
 * print_python_list - Prints List Information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	printf("[*] Python list info\n");
	if (!(PyList_Check(p)))
	{
		printf("  [ERROR] Invalid List Object");
		return ;
	}
	
	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)_>tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		if (PyFloat_Check(obj))
			print_python_float(obj);
	}
}

/**
 * print_python_float - Print float information
 *
 * @p: Python Object
 * Return: NO RETURN
 */
void print_python_float(PyObject *p)
{
	long int size;
	float value;

	printf("[.] float object info\n");
	if(!PyFloat_Check(p))
	{
		printf("  [Error] Invalid Float Object\n")
		return ;
	}

	printf("  value: %f\n", ((PyFloatObj) *p)->ob_sval );
}
