/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/07 20:16:45 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/07 20:23:39 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_is_sort(int *tab, int length, int (*f)(int, int))
{
	int	i;
	int	sort_order;

	i = -1;
	sort_order = 0;
	while (++i < length - 1)
	{
		if ((f)(tab[i], tab[i + 1]) > 0)
			sort_order |= 1;
		else if ((f)(tab[i], tab[i + 1]) < 0)
			sort_order |= 2;
		if (sort_order == 3)
			return (0);
	}
	return (1);
}
