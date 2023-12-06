#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Python lists
 * @p: input
*/
void print_python_list(PyObject *p)
{
	long int xsiz, xv;
	pyListObject *xlis;
	PyObject *xob;

	xsiz = ((pyVarObject *)(p))->ob_size;
	xlis = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", xsiz);
	printf("[*] Allocated = %ld\n", xlis->allocated);

	for (xv = 0; xv < xsiz; xv++)
	{
		xob = ((PyListObject *)p)->ob_item[xv];
		printf("Element %ld: %s\n", xv, ((xob)->ob_type)->tp_name);
		if (pyBytes_check(xob))
			print_python_bytes(xob);
	}
}
/**
 * print_python_bytes - Python bytes
 * @p: input
*/
void print_python_bytes(PyObject *p)
{
	char xstr;
	llong int xsiz, xv, xlim;

	printf("[.] Bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf( "  [ERROR] Invalid Bytes Object\n");
		return;
	}

}
