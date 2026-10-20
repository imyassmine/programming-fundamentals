/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   btree_level_count.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 22:59:05 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/23 22:59:06 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_btree.h"

int	btree_level_count(t_btree *root)
{
	int	left_height;
	int	right_height;

	if (root == NULL)
		return (0);
	left_height = btree_level_count(root->left);
	right_height = btree_level_count(root->right);
	if (left_height > right_height)
		return (left_height + 1);
	else
		return (right_height + 1);
}
