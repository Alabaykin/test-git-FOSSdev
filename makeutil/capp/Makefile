.PHONY: another-app
#not all targets are listed in phony

# Might be correct, but "build" and "app" are different 
build:
	gcc main.c -o app

# Correct on phony
app: main.c
	gcc main.c -o app

# Inorrect: listed in phony
another-app: main.c
	gcc main.c -o another-app
