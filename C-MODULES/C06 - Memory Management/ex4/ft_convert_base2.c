/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_base2.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/08 16:33:42 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/08 22:08:31 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *str)
{
	int	count;

	count = 0;
	while (str[count])
		count++;
	return (count);
}

int	ft_nbrlen(int nbr, char *base)
{
	int		nbr_len;
	int		base_len;
	long	n;

	nbr_len = 0;
	base_len = ft_strlen(base);
	n = nbr;
	if (nbr < 0)
	{
		n = -n;
		nbr_len++;
	}
	while (n >= base_len)
	{
		n /= base_len;
		nbr_len++;
	}
	nbr_len++;
	return (nbr_len);
}

void	putnbr_base(int nbr, char *base, char *str)
{
	int		base_len;
	long	n;
	int		i;
	int		nbr_len;

	base_len = ft_strlen(base);
	nbr_len = ft_nbrlen(nbr, base);
	n = nbr;
	i = 0;
	if (n < 0)
	{
		str[i++] = '-';
		n = -n;
	}
	nbr_len--;
	while (n >= base_len)
	{
		str[nbr_len] = base[n % base_len];
		n = n / base_len;
		nbr_len--;
	}
	if (n < base_len)
		str[i] = base[n];
}
