/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_base.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaabdall <yaabdall@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/08 16:33:40 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/09 12:17:48 by yaabdall         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	putnbr_base(int nbr_mid, char *base, char *nbrstr);
int		ft_nbrlen(int nbr, char *base);
int		ft_strlen(char *str);

int	is_valid_base(char *base)
{
	int	i;
	int	j;
	int	len;

	i = -1;
	len = ft_strlen(base);
	if (len <= 1)
		return (0);
	while (++i < len)
	{
		if ((base[i] >= 9 && base[i] <= 13)
			|| base[i] == 32 || base[i] == 43 || base[i] == 45)
			return (0);
		j = i;
		while (++j < len)
		{
			if (base[i] == base[j])
				return (0);
		}
	}
	return (1);
}

int	char_in_base(char a, char *base)
{
	int	i;

	i = -1;
	while (base[++i])
	{
		if (base[i] == a)
			return (i);
	}
	return (-1);
}

int	ft_atoi_base(char *str, char *base)
{
	int	i;
	int	sign;
	int	result;

	i = 0;
	sign = 1;
	result = 0;
	while (str[i] == ' ' || (str[i] >= 9 && str[i] <= 13))
		i++;
	while (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			sign *= -1;
		i++;
	}
	while (str[i] && char_in_base(str[i], base) != -1)
	{
		result = result * ft_strlen(base) + char_in_base(str[i], base);
		i++;
	}
	return (sign * result);
}

char	*ft_convert_base(char *nbr, char *base_from, char *base_to)
{
	char	*fin_nbr;
	int		mid_nbr;
	int		mid_nbr_length;

	if (!nbr || !base_from || !base_to)
		return (0);
	if (!(is_valid_base(base_from)) || !(is_valid_base(base_to)))
		return (0);
	mid_nbr = ft_atoi_base(nbr, base_from);
	mid_nbr_length = ft_nbrlen(mid_nbr, base_to);
	fin_nbr = malloc((mid_nbr_length + 1));
	if (!fin_nbr)
		return (0);
	putnbr_base(mid_nbr, base_to, fin_nbr);
	fin_nbr[mid_nbr_length] = '\0';
	return (fin_nbr);
}
