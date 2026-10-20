/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_combn.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/04 17:12:35 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/04 21:37:29 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

static void	print_tab(int *tab, int n)
{
	int		i;
	char	c;

	i = -1;
	while (++i < n)
	{
		c = tab[i] + '0';
		write(1, &c, 1);
	}
}

void	ft_print_combn(int n)
{
	int	tab[10];
	int	i;
	int	pos;

	if (n < 1 || n > 9)
		return ;
	i = -1;
	while (++i < n)
		tab[i] = i;
	while (1)
	{
		print_tab(tab, n);
		if (tab[0] == 10 - n)
			break ;
		write(1, ", ", 2);
		pos = n - 1;
		while (pos >= 0 && tab[pos] == 10 - (n - pos))
			pos--;
		tab[pos]++;
		while (pos + 1 < n)
		{
			tab[pos + 1] = tab[pos] + 1;
			pos++;
		}
	}
}

// int	main()
// {
// 	ft_print_combn(9);
// 	return (0);
// }