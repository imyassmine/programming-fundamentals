/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_find.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 19:44:56 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/19 19:44:57 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

t_list	*ft_list_find(t_list *begin_list,
	void *data_ref, int (*cmp)(void *, void *))
{
	t_list	*tmp;

	if (!begin_list)
		return (NULL);
	tmp = begin_list;
	while (tmp && tmp->next)
	{
		if ((*cmp)(tmp->data, data_ref) == 0)
			return (tmp);
		tmp = tmp->next;
	}
	if ((*cmp)(tmp->data, data_ref) == 0)
		return (tmp);
	return (NULL);
}
