#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * plin - is_palindrome
 * @head: input
 * @las: end list
 * Return: 0 or 1
 */
int plin(listint_t **head, listint_t *las)
{
	if (!las)
		return (1);
	if (plin(head, las->next) && (*head)->n == las->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: input
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);
	return (plin(head, *head));
}
