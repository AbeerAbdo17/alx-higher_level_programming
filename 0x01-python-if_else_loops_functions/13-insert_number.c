#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - that inserts a number into a sorted singly linked list
 * @head: input
 * @number: input
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *nw = NULL;
	listint_t *tp = NULL;

	if (!head)
		return (NULL);
	nw = malloc(sizeof(listint_t));
	if (!nw)
		return (NULL);
	nw->n = number;
	nw->next = NULL;
	if (!*head || (*head)->n > number)
	{
		nw->next = *head;
		return (*head = nw);
	}
	else
	{
		while (curr && curr->n < number)
		{
			tp = curr;
			curr = curr->next;
		}
		tp->next = nw;
		nw->next = curr;
	}
	return (nw);
}
