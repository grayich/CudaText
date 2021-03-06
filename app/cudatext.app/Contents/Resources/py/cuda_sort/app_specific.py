import os
from cudatext import *

def get_ini_fn():
    return os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_sort.ini')

def ed_set_text_all(lines):
    ed.set_text_all('\n'.join(lines)+'\n')

def ed_get_text_all():
    n = ed.get_line_count()
    if ed.get_text_line(n-1)=='': n-=1
    return [ed.get_text_line(i) for i in range(n)]    

def ed_insert_to_lines(lines, line1, line2):
    ed.delete(0, line1, 0, line2+1)
    ed.insert(0, line1, '\n'.join(lines)+'\n')
    ed.set_caret(0, line2+1, 0, line1)

def ed_set_tab_title(s):
    ed.set_prop(PROP_TAB_TITLE, s)

def ed_convert_tabs_to_spaces(s):
    return ed.convert(CONVERT_LINE_TABS_TO_SPACES, 0, 0, s)
   
def msg_show_error(s):
    msg_box(s, MB_OK+MB_ICONERROR)

def ed_get_sel_lines():
    return ed.get_sel_lines()
    
