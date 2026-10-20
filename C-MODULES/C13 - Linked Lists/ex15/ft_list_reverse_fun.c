/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_reverse_fun.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 19:45:09 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/19 19:45:10 by yassabda         ###   ########.fr       */
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

void	ft_list_reverse_fun(t_list *begin_list)
{
	t_list	*tmp;
	t_list	*right;
	void	*swap;
	int		i;
	int		j;

	int (size) = ft_list_size(begin_list);
	tmp = begin_list;
	i = -1;
	while (++i < size / 2)
	{
		right = begin_list;
		j = -1;
		while (++j < size - i - 1)
			right = right->next;
		swap = tmp->data;
		tmp->data = right->data;
		right->data = swap;
		tmp = tmp->next;
	}
}
