NAME    = ft_hexdump
CC      = cc
CFLAGS  = -Wall -Wextra -Werror
SRC_DIR = src/
SRCS    = $(SRC_DIR)ft_hexdump.c \
          $(SRC_DIR)utils.c \
          $(SRC_DIR)print_utils.c \
          $(SRC_DIR)print_utils2.c
OBJS    = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

$(SRC_DIR)%.o: $(SRC_DIR)%.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
