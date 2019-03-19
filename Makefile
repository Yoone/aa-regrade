MAIN = ./src/main.py
GRADES_FILES = $(foreach cfg, $(shell echo v*.cfg), $(shell echo $(cfg) | sed 's/\.cfg//'))
ITEMS_FILE = items.cfg
PRICES_FILE = prices.cfg
MAKE_NUM = 1000

.PHONY: all print_make_num

all: $(GRADES_FILES)

print_make_num: # Prints only once
	@echo "Making $(MAKE_NUM) of each item."

v%: print_make_num v%.cfg
	@echo "\n--- Grade chances from $@ ---\n"
	@$(MAIN) --grades $$(echo $^ | grep -o 'v.\+\.cfg') --prices $(PRICES_FILE) --items $(ITEMS_FILE) --make $(MAKE_NUM)
