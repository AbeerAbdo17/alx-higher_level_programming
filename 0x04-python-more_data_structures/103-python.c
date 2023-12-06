#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Python lists
 * @p: input
*/
void print_python_list(PyObject *p) {
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));


	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < PyList_Size(p); i++) {
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
/**
 * print_python_bytes - Python bytes
 * @p: input
*/
void print_python_bytes(PyObject *p) {
	printf("[.] Bytes object info\n");
	if (PyBytes_Check(p)) {
		printf("  size: %ld\n", PyBytes_GET_SIZE(p));
		printf("  trying string: %s\n", PyBytes_AS_STRING(p));
		printf("  first 10 bytes: ");
		for (Py_ssize_t i = 0; i < PyBytes_GET_SIZE(p) && i < 10; i++) {
			printf("%02hhx", ((char *)PyBytes_AS_STRING(p))[i]);
			if (i + 1 < PyBytes_GET_SIZE(p) && i + 1 < 10)
				printf(" ");
		}
		printf("\n");
	} else {
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
	}
}

