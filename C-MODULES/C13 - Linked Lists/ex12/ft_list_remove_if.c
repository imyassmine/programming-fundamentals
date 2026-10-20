/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_remove_if.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 19:44:59 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/19 19:45:00 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

void	ft_list_remove_if(t_list **begin_list, void *data_ref,
	int (*cmp)(void *, void *), void (*free_fct)(void *))
{
	t_list	*tmp;
	t_list	*prev;
	t_list	*next;

	if (!begin_list || !cmp || !free_fct)
		return ;
	prev = NULL;
	tmp = *begin_list;
	while (tmp)
	{
		next = tmp->next;
		if ((*cmp)(tmp->data, data_ref) == 0)
		{
			(*free_fct)(tmp->data);
			free(tmp);
			if (prev)
				prev->next = next;
			else
				*begin_list = next;
		}
		else
			prev = tmp;
		tmp = next;
	}
}
