/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaabdall <yaabdall@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/08 16:33:36 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/09 12:25:06 by yaabdall         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

static int	ft_strlen(char *str)
{
	int	count;

	count = 0;
	while (str[count])
		count++;
	return (count);
}

static int	ft_total_len(int size, char **strs, char *sep)
{
	int	total;
	int	i;

	total = 0;
	i = -1;
	while (++i < size)
	{
		total += ft_strlen(strs[i]);
		if (i < size - 1)
			total += ft_strlen(sep);
	}
	return (total);
}

static char	*ft_empty_str(void)
{
	char	*s;

	s = malloc(1);
	if (!s)
		return (NULL);
	s[0] = '\0';
	return (s);
}

static void	ft_strcpy(char *dst, char *src, int *pos)
{
	int	i;

	i = -1;
	while (src[++i])
	{
		dst[*pos] = src[i];
		(*pos)++;
	}
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*result;
	int		total;
	int		pos;
	int		i;

	if (size < 0)
		return (NULL);
	if (size == 0)
		return (ft_empty_str());
	if (!strs || !sep)
		return (NULL);
	total = ft_total_len(size, strs, sep);
	result = malloc(total + 1);
	if (!result)
		return (NULL);
	pos = 0;
	i = -1;
	while (++i < size)
	{
		ft_strcpy(result, strs[i], &pos);
		if (i < size - 1)
			ft_strcpy(result, sep, &pos);
	}
	result[pos] = '\0';
	return (result);
}
