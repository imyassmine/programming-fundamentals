NAME     = intern
CXX      = g++
CXXFLAGS = -Wall -Wextra -Werror -std=c++98
SRC_DIR  = srcs/
OBJ_DIR  = objs/
INC_DIR  = includes/
SRCS     = $(SRC_DIR)main.cpp \
           $(SRC_DIR)Bureaucrat.cpp \
           $(SRC_DIR)AForm.cpp \
           $(SRC_DIR)ShrubberyCreationForm.cpp \
           $(SRC_DIR)RobotomyRequestForm.cpp \
           $(SRC_DIR)PresidentialPardonForm.cpp \
           $(SRC_DIR)Intern.cpp
OBJS     = $(patsubst $(SRC_DIR)%.cpp,$(OBJ_DIR)%.o,$(SRCS))

all: $(NAME)

$(NAME): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(NAME)

$(OBJ_DIR)%.o: $(SRC_DIR)%.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -I $(INC_DIR) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
