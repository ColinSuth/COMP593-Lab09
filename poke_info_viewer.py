from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_pokemon_info


# Create the window
root = Tk()
root.title("Pokemon Stats Viewer")
root.resizable(False, False)

# Add frames to window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, pady=(20, 10))

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky=N)

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, padx=(10, 20), pady=(10, 20))


# Add widgets to frames
# Populate widgets in the Top frame
lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=0, padx=(20, 5), pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

def handel_get_info():

    # get the pokemon name entered by the user
    pokemon_name = ent_name.get()
    if len(pokemon_name) == 0:
        return
    
    # Get the pokemon name from the PokeAPI
    poke_info = get_pokemon_info(pokemon_name)
    if poke_info is None:
        err_msg = f'Unable to fetch information for {pokemon_name.capitalize()} from PokeAPI.'
        messagebox.showinfo(title='Error', message=err_msg, icon='error')

    # Populate the Info frame
    lbl_height_true['text'] = f"{poke_info['height']} dm"
    lbl_weight_true['text'] = f"{poke_info['weight']} hg"
    
    types_list = [t['type']['name'].title() for t in poke_info['types']]
    n = len(types_list)
    # Checks the length of the abilities and then prints it
    if n == 1:
        lbl_type_true['text'] = f"{types_list[0]}"
    
    else:
        types_csl = ', '.join(types_list[:-1])
        lbl_type_true['text'] = f"{types_csl}, {types_list[-1]}"


    # Populate the Stat frame
    bar_hp['value'] = poke_info['stats'][0]['base_stat']
    bar_attack['value'] = poke_info['stats'][1]['base_stat']
    bar_defense['value'] = poke_info['stats'][2]['base_stat']
    bar_spc_attack['value'] = poke_info['stats'][3]['base_stat']
    bar_spc_defense['value'] = poke_info['stats'][4]['base_stat']
    bar_speed['value'] = poke_info['stats'][5]['base_stat']

    return

btn_info = ttk.Button(frm_top, text='Get info', command=handel_get_info)
btn_info.grid(row=0, column=2, padx=10, pady=10)

# Populate widgets in the Info frame
# Pokemon height info
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

lbl_height_true = ttk.Label(frm_btm_left, text='')
lbl_height_true.grid(row=0, column=1, padx=(0, 10), pady=(10,5), sticky=W)


# Pokemon weight info
lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

lbl_weight_true = ttk.Label(frm_btm_left, text='')
lbl_weight_true.grid(row=1, column=1, padx=(0, 10), pady=(10,5), sticky=W)

# Pokemon type info
lbl_type = ttk.Label(frm_btm_left, text='Type')
lbl_type.grid(row=2, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

lbl_type_true = ttk.Label(frm_btm_left, text='')
lbl_type_true.grid(row=2, column=1, padx=(0, 10), pady=(10,5), sticky=W)


# Populate widgets in the Stats frame
# Pokemon HP stats
lbl_hp = ttk.Label(frm_btm_right, text='HP')
lbl_hp.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0, column=1, padx=(0,10), pady=(10, 5))
# bar_hp['value'] = 123

# Pokemon Attack stats

lbl_attack = ttk.Label(frm_btm_right, text='Attack')
lbl_attack.grid(row=1, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_attack.grid(row=1, column=1, padx=(0,10), pady=(10, 5))

# Pokemon Defense stats

lbl_defense = ttk.Label(frm_btm_right, text='Defense')
lbl_defense.grid(row=2, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

bar_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_defense.grid(row=2, column=1, padx=(0,10), pady=(10, 5))


# Pokemon Special Attack stats

lbl_spc_attack = ttk.Label(frm_btm_right, text='Special Attack')
lbl_spc_attack.grid(row=3, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

bar_spc_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_spc_attack.grid(row=3, column=1, padx=(0,10), pady=(10, 5))

# Pokemon Special Defence stats

lbl_spc_defense = ttk.Label(frm_btm_right, text='Special Defense')
lbl_spc_defense.grid(row=4, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

bar_spc_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_spc_defense.grid(row=4, column=1, padx=(0,10), pady=(10, 5))


# Pokemon Speed stats

lbl_speed = ttk.Label(frm_btm_right, text='Speed')
lbl_speed.grid(row=5, column=0, padx=(10, 5), pady=(10, 5), sticky=E)

bar_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_speed.grid(row=5, column=1, padx=(0,10), pady=(10, 5))


# Loop until window is closed
root.mainloop()
