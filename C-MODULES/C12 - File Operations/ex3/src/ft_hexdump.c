/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_hexdump.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/15 20:58:20 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/18 22:43:18 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <errno.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>

void	print_offset(unsigned long n, int width);
void	print_hex(unsigned char b);
void	ft_putstr_fd(char *str, int fd);
void	print_error(char *file_name);
void	ft_putchar_fd(char c, int fd);
int		ft_strcmp(char *s1, char *s2);
int		is_printable(unsigned char c);
void	print_line(unsigned char *buf, int len, unsigned long offset);
void	init_state(unsigned long tab[4]);

/*
state[0] = offset -> position totale dans le flux (tout fichier confondu)
state[1] = line_len -> nombre d'octets stockes dans line[]
state[2] = has_prev -> si previous line est valide
state[3] = -> si on est deja en train d'afficher *
*/

static void	process_full_line(unsigned char *line,
	unsigned char *prev_line, unsigned long *state)
{
	int	j;
	int	same;

	same = state[2];
	j = -1;
	while (same && ++j < 16)
	{
		if (line[j] != prev_line[j])
			same = 0;
	}
	if (same)
	{
		if (!state[3])
			ft_putstr_fd("*\n", 1);
		state[3] = 1;
	}
	else
		(print_line(line, 16, state[0]), state[3] = 0);
	j = -1;
	while (++j < 16)
		prev_line[j] = line[j];
	state[2] = 1;
	state[0] += 16;
	state[1] = 0;
}

static int	read_and_process_fd(int fd, unsigned char *line,
	unsigned char *prev_line, unsigned long *state)
{
	unsigned char	buf[1024];
	long			read_bytes;
	int				i;

	read_bytes = read(fd, buf, sizeof(buf));
	while (read_bytes > 0)
	{
		i = 0;
		while (i < read_bytes)
		{
			line[state[1]] = buf[i++];
			state[1]++;
			if (state[1] == 16)
				process_full_line(line, prev_line, state);
		}
		read_bytes = read(fd, buf, sizeof(buf));
	}
	if (read_bytes < 0)
		return (-1);
	return (0);
}

static void	print_last_line(unsigned char *line, unsigned long *state)
{
	if (state[1] > 0)
	{
		print_line(line, state[1], state[0]);
		state[0] += state[1];
	}
	if (state[0] > 0)
		(print_offset(state[0], 8), ft_putstr_fd("\n", 1));
}

static void	call_read_process(int fd, unsigned char *line,
	unsigned long state[4], char *str)
{
	static unsigned char	prev_line[16];

	if (read_and_process_fd(fd, line, prev_line, state) < 0)
		print_error(str);
}

int	main(int argc, char **argv)
{
	unsigned long	state[4];
	unsigned char	line[16];
	int				fd;
	int				i;

	init_state(state);
	if (argc < 2 || ft_strcmp(argv[1], "-C") != 0)
		return (ft_putstr_fd("usage: ft_hexdump -C [file] [...]\n", 2), 1);
	if (argc == 2)
		call_read_process(0, line, state, "stdin");
	i = 1;
	while (++i < argc)
	{
		fd = open(argv[i], O_RDONLY);
		if (fd == -1)
		{
			print_error(argv[i]);
			continue ;
		}
		call_read_process(fd, line, state, argv[i]);
		close(fd);
	}
	print_last_line(line, state);
	return (0);
}
