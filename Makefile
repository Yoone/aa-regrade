MAIN = ./src/main.py
GRADES_FILES = $(foreach cfg, $(shell echo v*.cfg), $(shell echo $(cfg) | sed 's/\.cfg//'))
ITEMS_FILE = items.cfg
PRICES_FILE = prices.cfg
MAKE_NUM = 1000

all: $(GRADES_FILES)

v%: v%.cfg
	@echo "--- Using grade chances from $@ ---"
	@$(MAIN) --grades $^ --prices $(PRICES_FILE) --items $(ITEMS_FILE) --make $(MAKE_NUM)
