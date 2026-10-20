/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sorted_list_merge.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 19:45:17 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/20 23:08:55 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

t_list	*merge(t_list *begin_list1, t_list *begin_list2,
	int (*cmp)(void *, void *))
{
	t_list	tmp;
	t_list	*tail;

	tmp.next = NULL;
	tail = &tmp;
	while (begin_list1 && begin_list2)
	{
		if ((*cmp)((begin_list1)->data, begin_list2->data) <= 0)
		{
			tail->next = begin_list1;
			begin_list1 = begin_list1->next;
		}
		else
		{
			tail->next = begin_list2;
			begin_list2 = begin_list2->next;
		}
		tail = tail->next;
	}
	if (begin_list1)
		tail->next = begin_list1;
	else
		tail->next = begin_list2;
	return (tmp.next);
}

void	ft_sorted_list_merge(t_list **begin_list1, t_list *begin_list2,
	int (*cmp)(void *, void *))
{
	if (!begin_list1 || !cmp)
		return ;
	*begin_list1 = merge(*begin_list1, begin_list2, cmp);
}
