/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cat.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/15 20:50:23 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/16 04:03:51 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <errno.h>

static void	ft_putstr_fd(char *str, int fd)
{
	while (*str)
		write(fd, str++, 1);
}

static void	print_error(char *filename)
{
	ft_putstr_fd("ft_cat: ", 2);
	ft_putstr_fd(filename, 2);
	ft_putstr_fd(": ", 2);
	ft_putstr_fd(strerror(errno), 2);
	write(2, "\n", 1);
}

int	ft_cat(int fd, char *str)
{
	char	buffer[30000];
	int		bytes_read;

	bytes_read = 1;
	while (bytes_read > 0)
	{
		bytes_read = read(fd, buffer, sizeof(buffer));
		if (bytes_read == -1)
			return (print_error(str), 1);
		write(1, buffer, bytes_read);
	}
	return (0);
}

int	main(int argc, char **argv)
{
	int		fd;
	int		i;
	int		has_error;

	if (argc == 1)
		return (ft_cat(0, "stdin"), 0);
	has_error = 0;
	i = 0;
	while (++i < argc)
	{
		fd = open(argv[i], O_RDONLY);
		if (fd == -1)
		{
			print_error(argv[i]);
			has_error = 1;
			continue ;
		}
		if (ft_cat(fd, argv[i]) == 1)
			has_error = 1;
		close (fd);
	}
	return (has_error);
}
