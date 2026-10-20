/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_push_strs.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 19:44:36 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/19 19:44:37 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

t_list	*ft_list_push_strs(int size, char **strs)
{
	t_list	*head;
	t_list	*new;
	int		i;

	head = NULL;
	i = -1;
	while (++i < size)
	{
		new = ft_create_elem(strs[i]);
		if (!new)
			return (NULL);
		new->next = head;
		head = new;
	}
	return (head);
}
