/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_foreach.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 19:44:48 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/19 19:44:49 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

void	ft_list_foreach(t_list *begin_list, void (*f)(void *))
{
	t_list	*tmp;

	if (!begin_list)
		return ;
	tmp = begin_list;
	while (tmp && tmp->next)
	{
		(*f)(tmp->data);
		tmp = tmp->next;
	}
	(*f)(tmp->data);
}
