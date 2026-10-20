/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 19:58:53 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/05 22:04:20 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}

// int	main()
// {
// 	int	a = 4;
// 	int b = 5;
// 	int div;
// 	int mod;

// 	ft_div_mod(a, b, &div, &mod);
// 	printf("%d, %d\n", div, mod);
// 	return (0);
// }