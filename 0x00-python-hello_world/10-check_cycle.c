#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - Linked list cycle
 * @list: input
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *sl = list, *fa = list;

	while ((fa && fa->next) != NULL)
	{
		sl = sl->next;
		fa = fa->next->next;
		if (sl == fa)
			return (1);
	}
	return (0);
}
