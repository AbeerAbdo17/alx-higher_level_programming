#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - Python float
 * @p:  oinput
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_bytes - Python bytes
 * @p: oinput
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t xsize = 0, xv = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	xsize = PyBytes_Size(p);
	printf("  size: %zd\n", xsize);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", xsize < 10 ? xsize + 1 : 10);
	while (xv < xsize + 1 && xv < 10)
	{
		printf(" %02hhx", str[xv]);
		xv++;
	}
	printf("\n");
}
/**
 * print_python_list - Python lists
 * @p: oinput
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t xsize = 0;
	PyObject *xitem;
	int xv = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		xsize = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", xsize);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (xv < xsize)
		{
			xitem = PyList_GET_ITEM(p, xv);
			printf("Element %d: %s\n", xv, xitem->ob_type->tp_name);
			if (PyBytes_Check(xitem))
				print_python_bytes(xitem);
			else if (PyFloat_Check(xitem))
				print_python_float(xitem);
			xv++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

