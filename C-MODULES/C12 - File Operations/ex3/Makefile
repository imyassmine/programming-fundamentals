### VARIABLES ###

NAME = ft_hexdump
CC = cc
FLAGS = -Wall -Wextra -Werror

SRC_PATH = ./src/

SRC_FILES = ft_hexdump.c \
			utils.c \
			print_utils.c \
			print_utils2.c

SRC = $(addprefix $(SRC_PATH), $(SRC_FILES))
OBJ = $(addprefix $(SRC_PATH), $(SRC_FILES:.c=.o))

### RULES ###

$(SRC_PATH)%.o: $(SRC_PATH)%.c
				$(CC) $(FLAGS) -c $< -o $@

$(NAME):		$(OBJ)
				$(CC) $(FLAGS) -o $(NAME) $(OBJ)

all: $(NAME)

clean:
				rm -rf $(OBJ)

fclean:			clean
				rm -f $(NAME)

re:				fclean all

.PHONY:			all clean fclean re