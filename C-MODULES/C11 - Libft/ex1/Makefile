### VARIABLES ###

NAME = libft.a
CC = cc
FLAGS = -Wall -Wextra -Werror

SRC_PATH = ./srcs/
INC_PATH = ./includes/

SRC_FILES = ft_putchar.c \
			ft_putstr.c \
			ft_strcmp.c \
			ft_strlen.c \
			ft_swap.c

SRC =	$(addprefix $(SRC_PATH), $(SRC_FILES))
OBJ =	$(SRC:.c=.o) main.o

### RULES ###

%.o:			%.c
				$(CC) $(FLAGS) -I $(INC_PATH) -c $< -o $@

$(NAME):		$(OBJ)
				ar rcs $(NAME) $(OBJ)

all:			$(NAME)

clean:
				rm -f $(OBJ)

fclean:			clean
				rm -f $(NAME)

re:				fclean all

.PHONY:			all clean fclean re
