/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_non_printable.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 13:01:55 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/06 13:28:29 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

static void	ft_puthex(unsigned char c)
{
	char	*base;

	base = "0123456789abcdef";
	write(1, &base[c / 16], 1);
	write(1, &base[c % 16], 1);
}

void	ft_putstr_non_printable(char *str)
{
	while (*str)
	{
		if (*str < ' ' || *str > '~')
		{
			write(1, "\\", 1);
			ft_puthex((unsigned char)*str);
		}
		else
			write(1, str, 1);
		str++;
	}
}

// int	main()
// {
// 	ft_putstr_non_printable("Hello\nHow are you ?");
// 	return (0);
// }