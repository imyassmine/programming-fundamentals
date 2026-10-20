/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   btree_apply_by_level.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 22:59:01 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/25 12:18:48 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_btree.h"

void	btree_apply_by_level(t_btree *root,
void (*applyf)(void *item, int current_level, int is_first_elem))
{
	if (!root)
		return ;
	t_queue *(queue) = malloc(sizeof(t_queue) * 1000);
	if (!queue)
		return ;
	int (front) = 0;
	int (tail) = 0;
	int (current_lvl) = -1;
	queue[tail++] = (t_queue){root, 0};
	while (front < tail)
	{
		t_queue (current) = queue[front++];
		if (current.level != current_lvl)
		{
			current_lvl = current.level;
			applyf(current.node->item, current_lvl, 1);
		}
		else
			applyf(current.node->item, current_lvl, 0);
		if (current.node->left)
			queue[tail++] = (t_queue){current.node->left, current.level + 1};
		if (current.node->right)
			queue[tail++] = (t_queue){current.node->right, current.level + 1};
	}
	free(queue);
}
