/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_clear.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 19:44:39 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/19 19:44:40 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

void	ft_list_clear(t_list *begin_list, void (*free_fct)(void *))
{
	t_list	*tmp;

	if (!begin_list)
		return ;
	while (begin_list && begin_list->next)
	{
		free_fct(begin_list->data);
		tmp = begin_list->next;
		free(begin_list);
		begin_list = tmp;
	}
	free_fct(begin_list->data);
	free(begin_list);
}
