/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_sort.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 19:45:05 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/19 19:45:06 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

int	ft_list_size(t_list *begin_list)
{
	t_list	*tmp;
	int		size;

	if (!begin_list)
		return (0);
	size = 1;
	tmp = begin_list;
	while (tmp && tmp->next)
	{
		tmp = tmp->next;
		size++;
	}
	return (size);
}

void	ft_list_sort(t_list **begin_list, int (*cmp)(void *, void *))
{
	t_list	*tmp;
	void	*swap;
	int		size;
	int		i;

	if (!begin_list || !*begin_list || !cmp)
		return ;
	size = ft_list_size(*begin_list);
	i = -1;
	while (++i < size)
	{
		tmp = *begin_list;
		while (tmp && tmp->next)
		{
			if ((*cmp)(tmp->data, tmp->next->data) > 0)
			{
				swap = tmp->data;
				tmp->data = tmp->next->data;
				tmp->next->data = swap;
			}
			tmp = tmp->next;
		}
	}
}
