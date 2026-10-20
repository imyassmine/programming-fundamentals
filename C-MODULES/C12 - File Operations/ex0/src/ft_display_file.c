/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_display_file.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/15 20:50:17 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/16 03:18:50 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <fcntl.h>

void	ft_putendl_fd(char *str, int fd)
{
	while (*str)
		write(fd, str++, 1);
	write(fd, "\n", 1);
}

int	main(int argc, char **argv)
{
	int		fd;
	char	buffer[4096];
	int		bytes_read;

	if (argc == 1)
		return (ft_putendl_fd("File name missing.", 2), 1);
	if (argc > 2)
		return (ft_putendl_fd("Too many arguments.", 2), 1);
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
		return (ft_putendl_fd("Cannot read file.", 2), 1);
	bytes_read = 1;
	while (bytes_read > 0)
	{
		bytes_read = read(fd, buffer, 4096);
		if (bytes_read == -1)
			return (ft_putendl_fd("Cannot read file.", 2), 1);
		buffer[bytes_read] = '\0';
		write(1, buffer, bytes_read);
	}
	close(fd);
	return (0);
}
