/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   btree_insert_data.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/20 23:39:42 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/22 23:08:18 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_btree.h"

void	btree_insert_data(t_btree **root, void *item, int (*cmpf)(void
*, void *))
{
	while (*root)
	{
		if (cmpf(item, (*root)->item) < 0)
			root = &((*root)->left);
		else
			root = &((*root)->right);
	}
	*root = btree_create_node(item);
}
