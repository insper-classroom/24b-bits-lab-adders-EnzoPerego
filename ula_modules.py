#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a and b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b ^ c
        carry.next = ((not a) & b & c) | (a & (not b) & c) | (a & b & (not c)) | (a & b & c)

    return instances()


@block
def adder2bits(x, y, soma, carry):
    c = Signal(bool(0))
    ha = halfAdder(x[0], y[0], soma[0], c)
    fa = fullAdder(x[1], y[1], c, soma[1], carry)
    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
