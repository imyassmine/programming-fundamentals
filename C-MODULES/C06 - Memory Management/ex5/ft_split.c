/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yassabda <yassabda@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/08 16:33:47 by yassabda          #+#    #+#             */
/*   Updated: 2026/03/09 18:08:10 by yassabda         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

static int	is_separator(char c, char *charset)
{
	int	i;

	i = -1;
	while (charset[++i])
	{
		if (c == charset[i])
			return (1);
	}
	return (0);
}

static int	count_words(char *str, char *charset)
{
	int	count;

	count = 0;
	while (*str)
	{
		while (*str && is_separator(*str, charset))
			str++;
		if (*str)
		{
			count++;
			while (*str && !is_separator(*str, charset))
				str++;
		}
	}
	return (count);
}

static char	*get_word(char *str, int len)
{
	char	*word;
	int		i;

	word = malloc(len + 1);
	if (!word)
		return (NULL);
	i = -1;
	while (++i < len)
		word[i] = str[i];
	word[i] = '\0';
	return (word);
}

char	**ft_split(char *str, char *charset)
{
	char	**tab;
	int		word_count;
	int		len;

	if (!str || !charset)
		return (NULL);
	word_count = count_words(str, charset);
	tab = malloc(sizeof(char *) * (word_count + 1));
	if (!tab)
		return (NULL);
	tab[word_count] = NULL;
	int (i) = -1;
	while (++i < word_count)
	{
		while (*str && is_separator(*str, charset))
			str++;
		len = 0;
		while (str[len] && !is_separator(str[len], charset))
			len++;
		tab[i] = get_word(str, len);
		if (!tab[i])
			return (NULL);
		str += len;
	}
	return (tab);
}
