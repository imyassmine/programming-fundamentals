/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_show_tab.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 14:04:28 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/26 20:50:16 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_stock_str.h"
#include <unistd.h>

void	ft_putnbr(int nb)
{
	long	n;
	char	c;

	n = nb;
	if (n < 0)
	{
		write(1, "-", 1);
		n = -n;
	}
	if (n >= 10)
		ft_putnbr(n / 10);
	c = n % 10 + '0';
	write(1, &c, 1);
}

void	ft_show_tab(struct s_stock_str *par)
{
	int	i;

	while (par->str)
	{
		i = -1;
		while (par->str[++i])
			write(1, &par->str[i], 1);
		write(1, "\n", 1);
		ft_putnbr(par->size);
		write(1, "\n", 1);
		i = -1;
		while (par->copy[++i])
			write(1, &par->copy[i], 1);
		write(1, "\n", 1);
		par++;
	}
}
