#include <Python.h>
/**
 * print_python_list_info - fun prints some basic info about Python lists
 * @p: input
 */
void print_python_list_info(PyObject *p)
{
	int sz;
	int allc;
	int x;
	PyObject *bj;

	sz = Py_SIZE(p);
	allc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", allc);

	for (x = 0; x < sz; x++)
	{
		printf("Element %d: ", x);
		bj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(bj)->tp_name);
	}
}
