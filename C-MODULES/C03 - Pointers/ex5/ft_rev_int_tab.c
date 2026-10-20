/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 20:04:06 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/05 22:04:26 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_rev_int_tab(int *tab, int size)
{
	int	i;
	int	tmp;

	i = -1;
	while (++i < size / 2)
	{
		tmp = tab[size - i - 1];
		tab[size - i - 1] = tab [i];
		tab[i] = tmp;
	}
}

// int	main()
// {
// 	int	tab[5]= {5, 3, 9, 1, 8};

// 	ft_rev_int_tab(tab, 5);
// 	printf("%d, %d, %d, %d, %d\n", tab[0], tab[1], tab[2], tab[3], tab[4]);
// 	return (0);
// }