/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sorted_list_insert.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 19:45:14 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/19 19:45:15 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

void	ft_sorted_list_insert(t_list **begin_list, void *data,
	int (*cmp)(void *, void *))
{
	t_list	*tmp;
	t_list	*new;

	if (!begin_list || !cmp)
		return ;
	new = ft_create_elem(data);
	if (!new)
		return ;
	if (!*begin_list)
	{
		*begin_list = new;
		return ;
	}
	if ((*cmp)((*begin_list)->data, data) >= 0)
	{
		new->next = *begin_list;
		*begin_list = new;
		return ;
	}
	tmp = *begin_list;
	while (tmp->next && (*cmp)(tmp->next->data, data) < 0)
		tmp = tmp->next;
	new->next = tmp->next;
	tmp->next = new;
}
