/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/04 18:28:29 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/04 21:28:11 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

static void	ft_putnbr(int nb)
{
	char	c;
	long	n;

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

void	ft_print_comb2(void)
{
	size_t	i;
	size_t	j;

	i = -1;
	while (++i < 99)
	{
		j = i;
		while (++j < 100)
		{
			if (i < 10)
				write(1, "0", 1);
			ft_putnbr(i);
			write(1, " ", 1);
			if (j < 10)
				write(1, "0", 1);
			ft_putnbr(j);
			if (!(i == 98 && j == 99))
				write(1, ", ", 2);
		}
	}
}

// int	main()
// {
// 	ft_print_comb2();
// 	return (0);
// }