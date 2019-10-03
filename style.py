import pandas as pd
from matplotlib.colors import hsv_to_rgb
from collections import OrderedDict

qtl_color_s = pd.Series({
    'eqtl_dark':  hsv_to_rgb([0.55, 0.8, 0.6]),
    'eqtl':       hsv_to_rgb([0.55, 0.8, 0.8]),
    'sqtl_dark':  hsv_to_rgb([0.05, 0.8, 0.6]),
    'sqtl':       hsv_to_rgb([0.05, 0.8, 0.8]),
    'eqtl_trans': hsv_to_rgb([0.10, 0.8, 0.9 ]),
})

finemap_color_s = pd.Series(OrderedDict([
    ('top_evariant', hsv_to_rgb([0,       0, 0.4])),
    ('caveman',      hsv_to_rgb([0.5,   0.8, 0.7])),
    ('caviar',       hsv_to_rgb([0.025, 0.8, 0.8])),
    ('dap-g' ,       hsv_to_rgb([0.1,   0.8, 0.9])),
    ('consensus',    hsv_to_rgb([0.3,  0.99, 0.7])),
    ('caveman_dark', hsv_to_rgb([0.5,   0.4, 0.7])),
    ('caviar_dark',  hsv_to_rgb([0.025, 0.4, 0.8])),
    ('dap-g_dark' ,  hsv_to_rgb([0.1,   0.4, 0.9])),
]))

colors_df = pd.read_csv('data/gtex_colors.txt', sep='\t', index_col=0)
