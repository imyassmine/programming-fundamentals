#!/bin/sh

NAME="libft.a"
CC="cc"
CFLAGS="-Wall -Wextra -Werror"
SRC="ft_putchar.c ft_swap.c ft_putstr.c ft_strlen.c ft_strcmp.c"
OBJ="ft_putchar.o ft_swap.o ft_putstr.o ft_strlen.o ft_strcmp.o"

$CC $CFLAGS -c $SRC
ar rcs $NAME $OBJ
rm -f $OBJ
