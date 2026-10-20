/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_utils2.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/17 04:16:39 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/17 04:18:48 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar_fd(char c, int fd);
void	ft_putstr_fd(char *str, int fd);
void	print_hex(unsigned char b);

int	is_printable(unsigned char c)
{
	return (c >= ' ' && c <= '~');
}

void	print_offset(unsigned long n, int width)
{
	char		buf[16];
	char		*base;
	int			i;

	base = "0123456789abcdef";
	i = width - 1;
	while (i >= 0)
	{
		buf[i] = base[n % 16];
		n /= 16;
		i--;
	}
	write(1, buf, width);
}

static void	print_hex_part(unsigned char *buf, int len)
{
	int	i;

	i = -1;
	while (++i < 16)
	{
		if (i < len)
			print_hex(buf[i]);
		else
			ft_putstr_fd("  ", 1);
		if (i == 7)
			ft_putstr_fd("  ", 1);
		else
			ft_putstr_fd(" ", 1);
	}
}

static void	print_ascii_part(unsigned char *buf, int len)
{
	int	i;

	i = -1;
	while (++i < len)
	{
		if (is_printable(buf[i]))
			ft_putchar_fd(buf[i], 1);
		else
			ft_putchar_fd('.', 1);
	}
}

void	print_line(unsigned char *buf, int len, unsigned long offset)
{
	print_offset(offset, 8);
	ft_putstr_fd("  ", 1);
	print_hex_part(buf, len);
	ft_putstr_fd(" |", 1);
	print_ascii_part(buf, len);
	ft_putstr_fd("|\n", 1);
}
