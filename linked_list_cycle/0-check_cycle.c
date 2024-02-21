#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - Check if the linked list has a cycle
 * @list: Type listint_s pointer of node
 * Return: 1 if has a cycle 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *fiesta, *ferrari;

;	if (list == NULL)
		return (0);

	fiesta = list;
	ferrari = list;

	while (ferrari != NULL && ferrari->next != NULL)
	{
		fiesta = fiesta->next;
		ferrari = ferrari->next->next;

		if (fiesta == ferrari)
			return (1);
	}
	return (0);

}
