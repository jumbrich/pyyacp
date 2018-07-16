from dtpattern.unicode_translate.pattern_detection_print import pattern_to_string
from dtpattern.unicode_translate.translate import higher_level
from dtpattern.value_pattern_detection import pattern, uc_agg
from pyyacp.profiler import ColumnProfiler
from pyjuhelpers.timer import timer

class ColumnPatternProfiler(ColumnProfiler):

    def __init__(self):
        super(ColumnPatternProfiler, self).__init__('cpp','pattern')

    def result_datatype(self):
        return str

    @timer(key="profile.col_pattern")
    def _profile_column(self, values, meta) -> str:

        res = pattern(values, pf=uc_agg)
        #print(res)
        hl = higher_level(res)
        #print(res)

        hl_str = pattern_to_string(hl, collapse_level=2)
        #print(hl_str)
        return hl_str



