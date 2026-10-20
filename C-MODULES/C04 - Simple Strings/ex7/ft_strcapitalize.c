/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 13:01:31 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/06 14:15:39 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strcapitalize(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (i == 0 || (i && (str[i - 1] < '0' || (str[i - 1] > '9'
						&& str[i - 1] < 'A') || (str[i - 1] > 'Z'
						&& str[i - 1] < 'a') || str[i - 1] > 'z')))
		{
			if (str[i] >= 'a' && str[i] <= 'z')
				str[i] += 'A' - 'a';
		}
		else
		{
			if (str[i] >= 'A' && str[i] <= 'Z')
				str[i] += 'a' - 'A';
		}
		i++;
	}
	return (str);
}

// int	main()
// {
// 	char str[] = "Hello hLKJKJw are you ?";

// 	ft_strcapitalize(str);
// 	printf("%s", str);
// 	return (0);
// }