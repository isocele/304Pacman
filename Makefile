##
## EPITECH PROJECT, 2018
## makefile
## File description:
## makefile
##

RM	=	rm -f

all:
		cp 304pacman.py 304pacman

clean:
		$(RM) 304pacman

fclean:		clean

re:		fclean all
