/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 20:00:49 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/05 22:01:45 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_ultimate_div_mod(int *a, int *b)
{
	int	tmp;

	tmp = *a;
	*a = tmp / *b;
	*b = tmp % *b;
}

// int	main()
// {
// 	int	a = 4;
// 	int b = 5;

// 	ft_ultimate_div_mod(&a, &b);
// 	printf("%d, %d\n", a, b);
// 	return (0);
// }