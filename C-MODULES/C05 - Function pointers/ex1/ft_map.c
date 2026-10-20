/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_map.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/07 20:16:39 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/07 20:23:03 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_map(int *tab, int length, int (*f)(int))
{
	int	i;
	int	*new_tab;

	new_tab = malloc(sizeof(int) * length);
	if (!new_tab)
		return (NULL);
	i = -1;
	while (++i < length)
		new_tab[i] = (f)(tab[i]);
	return (new_tab);
}
