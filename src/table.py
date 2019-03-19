# -*- coding: utf-8 -*-

def pp(tab):
    col_lengths = {}

    # Determining column lengths
    for line in tab:
        for i, col in enumerate(line):
            col_len = len(str(col))
            if col_len > col_lengths.get(i, 0):
                col_lengths[i] = col_len

    # Printing header
    th = []
    th_sep = []
    for i, col in enumerate(tab[0]):
        th.append(('{:' + str(col_lengths[i]) + '}').format(col))
        th_sep.append(('{:-<' + str(col_lengths[i]) + '}').format(''))
    print(' | '.join(th))
    print('-|-'.join(th_sep))

    # Printing body
    for line in tab[1:]:
        th = []
        for i, col in enumerate(line):
            th.append(('{:' + str(col_lengths[i]) + '}').format(col))
        print(' | '.join(th))
