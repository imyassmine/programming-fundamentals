### VARIABLES ###

NAME = ft_display_file
CC = cc
FLAGS = -Wall -Wextra -Werror

SRC_PATH = ./src/

SRC_FILES = ft_display_file.c

SRC = $(addprefix $(SRC_PATH), $(SRC_FILES))
OBJ = $(addprefix $(SRC_PATH), $(SRC_FILES:.c=.o))

### RULES ###

$(SRC_PATH)%.o:	$(SRC_PATH)%.c
				mkdir -p $(dir $@)
				$(CC) $(FLAGS) -c $< -o $@

$(NAME): 		$(OBJ)
				$(CC) $(FLAGS) $(OBJ) -o $(NAME)

all: 			$(NAME)

clean:
				rm -rf $(OBJ)

fclean:			clean
				rm -rf $(NAME)

re:				fclean all

.PHONY:			all clean fclean re