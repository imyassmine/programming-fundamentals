/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/08 16:33:32 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/08 22:21:18 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_ultimate_range(int **range, int min, int max)
{
	int	i;
	int	size;
	int	*tab;

	if (min >= max)
	{
		*range = NULL;
		return (0);
	}
	size = max - min;
	tab = malloc((size) * sizeof(int));
	if (!tab)
	{
		*range = NULL;
		return (-1);
	}
	i = -1;
	while (++i < size)
		tab[i] = min + i;
	*range = tab;
	return (size);
}
