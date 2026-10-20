/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tail.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/15 20:50:46 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/16 05:09:02 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include <libgen.h>
#include <stdlib.h>
#include <limits.h>

void	ft_putstr_fd(char *str, int fd);
int		ft_strcmp(char *s1, char *s2);
int		ft_atoi(char *str);
void	print_error(char *filename);

static void	ft_write_ring(char *ring, unsigned long total, unsigned int count)
{
	unsigned int	start;

	if (total == 0)
		return ;
	if (total < count)
		write(1, ring, total);
	else
	{
		start = (unsigned int)(total % count);
		write(1, ring + start, count - start);
		if (start > 0)
			write(1, ring, start);
	}
}

static int	ft_tail(int fd, unsigned int count)
{
	char			*ring;
	char			buffer[4096];
	int				read_bytes;
	int				i;

	if (count == 0)
		return (0);
	ring = malloc(count);
	if (!ring)
		return (-1);
	unsigned long (total) = 0;
	while (1)
	{
		read_bytes = read(fd, buffer, sizeof(buffer));
		if (read_bytes <= 0)
			break ;
		i = 0;
		while (i < read_bytes)
			ring[total++ % count] = buffer[i++];
	}
	if (read_bytes < 0)
		return (free(ring), -1);
	ft_write_ring(ring, total, count);
	free(ring);
	return (0);
}

static void	print_header(char *filename, int need_blank_line)
{
	if (need_blank_line)
		write(1, "\n", 1);
	ft_putstr_fd("==> ", 1);
	ft_putstr_fd(filename, 1);
	ft_putstr_fd(" <==\n", 1);
}

static int	process_files(int argc, char **argv, unsigned int count)
{
	int	fd;
	int	i;
	int	has_error;

	has_error = 0;
	i = 2;
	while (++i < argc)
	{
		fd = open(argv[i], O_RDONLY);
		if (fd == -1)
		{
			print_error(argv[i]);
			has_error = 1;
			continue ;
		}
		if (argc > 4)
			print_header(argv[i], i > 3);
		if (ft_tail(fd, count) == -1)
		{
			print_error(argv[i]);
			has_error = 1;
		}
		close(fd);
	}
	return (has_error);
}

int	main(int argc, char **argv)
{
	unsigned int	count;

	if (argc < 3 || ft_strcmp(argv[1], "-c"))
		return (ft_putstr_fd("usage: ft_tail -c N [file ...]\n", 2), 1);
	count = ft_atoi(argv[2]);
	if (!count && argv[2][0] != '0')
		return (ft_putstr_fd("ft_tail: invalid number of bytes: '", 2),
			ft_putstr_fd(argv[2], 2), ft_putstr_fd("'\n", 2), 1);
	if (argc == 3)
		return (ft_tail(0, count) == -1);
	return (process_files(argc, argv, count));
}
