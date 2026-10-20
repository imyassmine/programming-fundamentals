NAME    = ft_tail
CC      = cc
CFLAGS  = -Wall -Wextra -Werror
SRC_DIR = src/
SRCS    = $(SRC_DIR)ft_tail.c \
          $(SRC_DIR)utils.c
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
