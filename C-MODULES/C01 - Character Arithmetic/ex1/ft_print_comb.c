/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/04 17:06:46 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/04 21:25:48 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

static void	print_tab(int *tab)
{
	int		i;
	char	c;

	i = -1;
	while (++i < 3)
	{
		c = tab[i] + '0';
		write(1, &c, 1);
	}
}

void	ft_print_comb(void)
{
	int	tab[3];
	int	i;
	int	pos;

	i = -1;
	while (++i < 3)
		tab[i] = i;
	while (1)
	{
		print_tab(tab);
		if (tab[0] == 7)
			break ;
		write(1, ", ", 2);
		pos = 2;
		while (pos >= 0 && tab[pos] == 10 - (3 - pos))
			pos--;
		tab[pos]++;
		while (pos + 1 < 3)
		{
			tab[pos + 1] = tab[pos] + 1;
			pos++;
		}
	}
}

// int	main()
// {
// 	ft_print_comb();
// 	return (0);
// }