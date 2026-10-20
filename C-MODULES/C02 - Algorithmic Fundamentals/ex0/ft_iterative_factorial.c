/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 14:05:38 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/05 17:50:33 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_factorial(int nb)
{
	int	f;
	int	i;

	if (nb < 0)
		return (0);
	f = 1;
	i = 1;
	while (i <= nb)
	{
		f *= i;
		i++;
	}
	return (f);
}
