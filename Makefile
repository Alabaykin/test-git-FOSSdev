.DEFAULT_GOAL := help
help:
	@echo "This makefile for repo"

create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Creating practice"
	mkdir -p $(PRACTICE)
	cp PracticeMakefile $(PRACTICE)/Makefile

remove-practice:
	rm -fr $(PRACTICE)

# mkdir demo-practice/
# mkdir demo-practice/src
# mkdir demo-practice/tests
# mkdir demo-practice/docs
# mkdir demo-practice/README.md
