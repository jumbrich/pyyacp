#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals




from dtpattern.unicode_translate.translate import string_to_uc_level2, translate, translate_all, uniq_uc
from pyyacp.profiler import ColumnProfiler
from pyjuhelpers.timer import timer

class CharacterSetProfiler(ColumnProfiler):

    def __init__(self):
        super(CharacterSetProfiler, self).__init__('cset', 'cset')

    def result_datatype(self):
        return str

    @timer(key="profile.col_cset")
    def _profile_column(self, column, meta):

        return self._analyse_ColumnPattern(column, meta)


    def _analyse_ColumnPattern(self, column,meta):
        return uniq_uc(column,trans_table=string_to_uc_level2, trans_func=translate)


