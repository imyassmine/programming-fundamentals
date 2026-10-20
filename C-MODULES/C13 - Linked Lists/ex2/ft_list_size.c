/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_size.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 19:44:26 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/19 19:44:27 by yassabda         ###   ########.fr       */
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
