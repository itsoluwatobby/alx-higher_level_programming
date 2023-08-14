#include <Python.h>

/**
 * print_python_list_info - function that prints the basic info
 *			about python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, copy, index;
	PyObject *object;

	size = Py_SIZE(p);
	copy = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", copy);

	for (index = 0; index < size; index++)
	{
		printf("Element %d: ", index);

		object = PyList_GetItem(p, index);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
