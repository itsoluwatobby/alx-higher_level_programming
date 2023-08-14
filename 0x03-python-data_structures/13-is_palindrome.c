#include "lists.h"

listint_t *listint_rev(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * listint_rev - function that reverses a singly-linked listint_t list.
 * @head: pointer to the firt node of the list.
 *
 * Return: pointer to the head of the reversed list.
 */
listint_t *listint_rev(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - function that checks if a singly linked list
 *		is a palindrome.
 * @head: pointer to the head of the list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy, *reversed, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	copy = *head;
	while (copy)
	{
		size++;
		copy = copy->next;
	}

	copy = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		copy = copy->next;

	if ((size % 2) == 0 && copy->n != copy->next->n)
		return (0);

	copy = copy->next->next;
	reversed = listint_rev(&copy);
	mid = reversed;

	copy = *head;
	while (reversed)
	{
		if (copy->n != reversed->n)
			return (0);
		copy = copy->next;
		reversed = reversed->next;
	}
	listint_rev(&mid);

	return (1);
}
