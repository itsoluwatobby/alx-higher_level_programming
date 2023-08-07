#include "lists.h"

/**
 * check_cycle - function that finds the loop in a linked list.
 * @list: list of listint_t
 * Return: no cycle - 0,cycle - 1
*/

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
