# Copyright (c) 2025 Bryson Cotton
# This software is free for personal use only.
# Redistribution, modification, or resale is prohibited.

import tkinter as tk
from tkinter import ttk
import xml.etree.ElementTree as ET
import re


def generate_hardpoints(num_entries, values, step, start_value, manual_list=None, force_consecutive=False):
    xml_template = """    <HardPoint Name="{HardPoint_Name}">
        <Type> {Type} </Type>
        <Tooltip_Text>{Tooltip_Text}</Tooltip_Text>
        <Is_Targetable>{Is_Targetable}</Is_Targetable>
        <Is_Destroyable>{Is_Destroyable}</Is_Destroyable>
        <Health>{Health}</Health>
        <Death_Explosion_Particles>{Death_Explosion_Particles}</Death_Explosion_Particles>
        <Death_Explosion_SFXEvent>{Death_Explosion_SFXEvent}</Death_Explosion_SFXEvent>

        <Model_To_Attach>{Model_To_Attach}</Model_To_Attach>
        <Attachment_Bone>{Attachment_Bone}</Attachment_Bone>
        <Collision_Mesh>{Collision_Mesh}</Collision_Mesh>
        <Damage_Decal>{Damage_Decal}</Damage_Decal>
        <Damage_Particles>{Damage_Particles}</Damage_Particles>

        <Is_Turret> {Is_Turret} </Is_Turret>
        <Turret_Rest_Angle> {Turret_Rest_Angle} </Turret_Rest_Angle>
        <Turret_Rotation_Offset> {Turret_Rotation_Offset} </Turret_Rotation_Offset>
        <Turret_Rotate_Speed> {Turret_Rotate_Speed} </Turret_Rotate_Speed>
        <Turret_Rotate_Extent_Degrees> {Turret_Rotate_Extent_Degrees} </Turret_Rotate_Extent_Degrees>
        <Turret_Elevate_Extent_Degrees> {Turret_Elevate_Extent_Degrees} </Turret_Elevate_Extent_Degrees>
        <Turret_Bone_Name> {Turret_Bone_Name} </Turret_Bone_Name>
        <Barrel_Bone_Name> {Barrel_Bone_Name} </Barrel_Bone_Name>

        <Death_Breakoff_Prop>{Death_Breakoff_Prop}</Death_Breakoff_Prop>

        <Damage_Type> {Damage_Type} </Damage_Type>

        <Fire_Bone_A>{Fire_Bone_A}</Fire_Bone_A>
        <Fire_Bone_B>{Fire_Bone_B}</Fire_Bone_B>
        <Fire_Bone_C>{Fire_Bone_C}</Fire_Bone_C>
        <Fire_Cone_Width>{Fire_Cone_Width}</Fire_Cone_Width>
        <Fire_Cone_Height>{Fire_Cone_Height}</Fire_Cone_Height>
        <Fire_Projectile_Type>{Fire_Projectile_Type}</Fire_Projectile_Type>
        <Fire_Min_Recharge_Seconds>{Fire_Min_Recharge_Seconds}</Fire_Min_Recharge_Seconds>
        <Fire_Max_Recharge_Seconds>{Fire_Max_Recharge_Seconds}</Fire_Max_Recharge_Seconds>
        <Fire_Pulse_Count>{Fire_Pulse_Count}</Fire_Pulse_Count>
        <Fire_Pulse_Delay_Seconds>{Fire_Pulse_Delay_Seconds}</Fire_Pulse_Delay_Seconds>
        <Fire_Range_Distance>{Fire_Range_Distance}</Fire_Range_Distance>
        <Fire_SFXEvent>{Fire_SFXEvent}</Fire_SFXEvent>

        <Fire_Inaccuracy_Distance> Fighter, {Fire_Inaccuracy_Fighter} </Fire_Inaccuracy_Distance>
        <Fire_Inaccuracy_Distance> Bomber, {Fire_Inaccuracy_Bomber} </Fire_Inaccuracy_Distance>
        <Fire_Inaccuracy_Distance> Transport, {Fire_Inaccuracy_Transport} </Fire_Inaccuracy_Distance>
        <Fire_Inaccuracy_Distance> Corvette, {Fire_Inaccuracy_Corvette} </Fire_Inaccuracy_Distance>
        <Fire_Inaccuracy_Distance> Frigate, {Fire_Inaccuracy_Frigate} </Fire_Inaccuracy_Distance>
        <Fire_Inaccuracy_Distance> Capital, {Fire_Inaccuracy_Capital} </Fire_Inaccuracy_Distance>
        <Fire_Inaccuracy_Distance> Super, {Fire_Inaccuracy_Super} </Fire_Inaccuracy_Distance>
        <Allow_Opportunity_Fire_When_Idle>{Allow_Opportunity_Fire_When_Idle}</Allow_Opportunity_Fire_When_Idle>
        <Allow_Opportunity_Fire_When_Targeting>{Allow_Opportunity_Fire_When_Targeting}</Allow_Opportunity_Fire_When_Targeting>
    </HardPoint>"""

    complete_xml = ''
    replaceable_tags = {
        'Fire_Bone_A', 'Fire_Bone_B', 'Fire_Bone_C',
        'Attachment_Bone', 'Collision_Mesh', 'Model_To_Attach',
        'Damage_Decal', 'Damage_Particles' , 'Turret_Bone_Name', 'Barrel_Bone_Name'
    }

    if manual_list:
        target_numbers = manual_list
    else:
        target_numbers = [f"{(start_value + (i * step)):02d}" for i in range(num_entries)]

    for idx, current_num_str in enumerate(target_numbers):
        current_values = values.copy()

        if force_consecutive:
            name_num = f"{(start_value + idx):02d}"
        else:
            try:
                name_num = f"{int(current_num_str):02d}"
            except ValueError:
                name_num = current_num_str

        if "00" in current_values['HardPoint_Name']:
            current_values['HardPoint_Name'] = current_values['HardPoint_Name'].replace("00", name_num)

        for key in replaceable_tags:
            val = current_values.get(key)
            if val and "00" in val:
                try:
                    formatted_num = f"{int(current_num_str):02d}"
                except ValueError:
                    formatted_num = current_num_str
                current_values[key] = val.replace("00", formatted_num)

        formatted_entry = xml_template.format(**{k: v if v else '' for k, v in current_values.items()})
        complete_xml += f"{formatted_entry}\n\n"

    return complete_xml.strip()


def parse_xml_to_fields():
    xml_text = xml_input.get("1.0", tk.END).strip()
    if not xml_text: return

    result_text.delete(1.0, tk.END)

    for entry in list(entry_fields.values()) + [entry_hardpoint_name, entry_tooltip_text, entry_inacc_fighter,
                                                entry_inacc_bomber,
                                                entry_inacc_transport, entry_inacc_corvette, entry_inacc_frigate,
                                                entry_inacc_capital,
                                                entry_inacc_super]:
        entry.delete(0, tk.END)

    name_match = re.search(r'Name\s*=\s*["\']([^"\']+)["\']', xml_text)
    if name_match:
        entry_hardpoint_name.insert(0, name_match.group(1))

    for tag_name, entry_obj in entry_fields.items():
        pattern = rf'<{tag_name}>(.*?)</{tag_name}>'
        tag_match = re.search(pattern, xml_text, re.DOTALL)
        if tag_match:
            val = tag_match.group(1).strip()
            entry_obj.insert(0, val)

    tooltip_match = re.search(r'<Tooltip_Text>(.*?)</Tooltip_Text>', xml_text, re.DOTALL)
    if tooltip_match: entry_tooltip_text.insert(0, tooltip_match.group(1).strip())

    inacc_matches = re.findall(r'<Fire_Inaccuracy_Distance>\s*([^,]+),\s*([^<]+)\s*</Fire_Inaccuracy_Distance>',
                               xml_text)
    mapping = {
        "Fighter": entry_inacc_fighter, "Bomber": entry_inacc_bomber,
        "Transport": entry_inacc_transport, "Corvette": entry_inacc_corvette,
        "Frigate": entry_inacc_frigate, "Capital": entry_inacc_capital, "Super": entry_inacc_super
    }
    for ship_type, val in inacc_matches:
        ship_type = ship_type.strip()
        if ship_type in mapping:
            mapping[ship_type].insert(0, val.strip())

    result_text.insert(tk.END, "XML Scraped Successfully.")


def clear_xml_box():
    xml_input.delete(1.0, tk.END)


def generate_xml():
    try:
        manual_input = entry_manual.get().strip()
        manual_list = [x.strip() for x in manual_input.split(",") if x.strip()] if manual_input else None

        if not manual_list:
            num_entries_str = entry_count.get().strip()
            num_entries = int(num_entries_str) if num_entries_str else 0
        else:
            num_entries = len(manual_list)

        start_val = int(entry_start.get() or 1)
        step = 2 if var_step.get() else 1

        values = {k: v.get() for k, v in entry_fields.items()}
        values.update({
            'HardPoint_Name': entry_hardpoint_name.get(),
            'Tooltip_Text': entry_tooltip_text.get(),
            'Fire_Inaccuracy_Fighter': entry_inacc_fighter.get(),
            'Fire_Inaccuracy_Bomber': entry_inacc_bomber.get(),
            'Fire_Inaccuracy_Transport': entry_inacc_transport.get(),
            'Fire_Inaccuracy_Corvette': entry_inacc_corvette.get(),
            'Fire_Inaccuracy_Frigate': entry_inacc_frigate.get(),
            'Fire_Inaccuracy_Capital': entry_inacc_capital.get(),
            'Fire_Inaccuracy_Super': entry_inacc_super.get()
        })

        result = generate_hardpoints(num_entries, values, step, start_val, manual_list, var_force_consecutive.get())
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e}")


def copy_output():
    root.clipboard_clear()
    root.clipboard_append(result_text.get("1.0", tk.END).strip())


def copy_hardpoint_names():
    out = result_text.get("1.0", tk.END).strip()
    names = [l.split('Name="')[1].split('"')[0] for l in out.split('\n') if '<HardPoint Name="' in l]
    if names:
        # Formats as "Name,\nName,\nName"
        formatted_names = ",\n".join(names)
        root.clipboard_clear()
        root.clipboard_append(formatted_names)


def clear_fields():
    for e in list(entry_fields.values()) + [entry_hardpoint_name, entry_tooltip_text, entry_inacc_fighter,
                                            entry_inacc_bomber,
                                            entry_inacc_transport, entry_inacc_corvette, entry_inacc_frigate,
                                            entry_inacc_capital,
                                            entry_inacc_super, entry_count, entry_manual]:
        e.delete(0, tk.END)
    entry_start.delete(0, tk.END)
    entry_start.insert(0, "1")
    xml_input.delete(1.0, tk.END)
    result_text.delete(1.0, tk.END)
    var_step.set(False)
    var_force_consecutive.set(False)


# --- GUI ---
root = tk.Tk()
root.title("HardPoint XML Generator")
root.geometry("1100x850")

top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=10, pady=5)
top_frame.columnconfigure(6, weight=1)

tk.Label(top_frame, text="Entries:").grid(row=0, column=0)
entry_count = tk.Entry(top_frame, width=5)
entry_count.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Start:").grid(row=0, column=2)
entry_start = tk.Entry(top_frame, width=5)
entry_start.grid(row=0, column=3, padx=5)
entry_start.insert(0, "1")

var_step = tk.BooleanVar()
tk.Checkbutton(top_frame, text="Every Other", variable=var_step).grid(row=0, column=4, padx=5)

tk.Label(top_frame, text="Manual List:").grid(row=0, column=5, padx=(10, 2))
entry_manual = tk.Entry(top_frame)
entry_manual.grid(row=0, column=6, sticky="ew")

tk.Label(root, text="Paste XML to auto-fill:").pack(anchor="w", padx=10)
xml_input = tk.Text(root, height=4)
xml_input.pack(fill="x", padx=10, pady=2)

xml_btn_frame = tk.Frame(root)
xml_btn_frame.pack(pady=2)
tk.Button(xml_btn_frame, text="Load XML", command=parse_xml_to_fields).pack(side="left", padx=5)
tk.Button(xml_btn_frame, text="Clear XML Box", command=clear_xml_box).pack(side="left", padx=5)

input_frame = ttk.Frame(root)
input_frame.pack(fill="both", expand=True, padx=10)
canvas = tk.Canvas(input_frame)
scrollbar = ttk.Scrollbar(input_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.columnconfigure(1, weight=1)
scrollable_frame.columnconfigure(3, weight=1)
scrollable_frame.columnconfigure(5, weight=1)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas_win = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.bind('<Configure>', lambda e: canvas.itemconfigure(canvas_win, width=e.width))
canvas.configure(yscrollcommand=scrollbar.set)

entry_fields = {}
fields = [
    ("HardPoint Name", "entry_hardpoint_name", ""), ("Type", "entry_type", "Type"),
    ("Tooltip Text", "entry_tooltip_text", ""), ("Is Targetable", "entry_targetable", "Is_Targetable"),
    ("Is Destroyable", "entry_destroyable", "Is_Destroyable"), ("Health", "entry_health", "Health"),
    ("Death Particles", "entry_explosion_particles", "Death_Explosion_Particles"),
    ("Death SFX", "entry_explosion_sfx", "Death_Explosion_SFXEvent"),
    ("Model Attach", "entry_model", "Model_To_Attach"), ("Attach Bone", "entry_attachment_bone", "Attachment_Bone"),
    ("Collision Mesh", "entry_collision_mesh", "Collision_Mesh"),
    ("Damage Decal", "entry_damage_decal", "Damage_Decal"),
    ("Damage Particles", "entry_damage_particles", "Damage_Particles"), ("Is Turret", "entry_is_turret", "Is_Turret"),
    ("Rest Angle", "entry_rest_angle", "Turret_Rest_Angle"),
    ("Rot Offset", "entry_rotation_offset", "Turret_Rotation_Offset"),
    ("Rot Speed", "entry_rotate_speed", "Turret_Rotate_Speed"),
    ("Rot Extent", "entry_rotate_extent", "Turret_Rotate_Extent_Degrees"),
    ("Elev Extent", "entry_elevate_extent", "Turret_Elevate_Extent_Degrees"),
    ("Turret Bone", "entry_turret_bone", "Turret_Bone_Name"),
    ("Barrel Bone", "entry_barrel_bone", "Barrel_Bone_Name"),
    ("Breakoff Prop", "entry_breakoff_prop", "Death_Breakoff_Prop"),
    ("Damage Type", "entry_damage_type", "Damage_Type"), ("Fire Bone A", "entry_fire_bone_a", "Fire_Bone_A"),
    ("Fire Bone B", "entry_fire_bone_b", "Fire_Bone_B"), ("Fire Bone C", "entry_fire_bone_c", "Fire_Bone_C"),
    ("Cone Width", "entry_cone_width", "Fire_Cone_Width"), ("Cone Height", "entry_cone_height", "Fire_Cone_Height"),
    ("Proj Type", "entry_projectile_type", "Fire_Projectile_Type"),
    ("Min Recharge", "entry_min_recharge", "Fire_Min_Recharge_Seconds"),
    ("Max Recharge", "entry_max_recharge", "Fire_Max_Recharge_Seconds"),
    ("Pulse Count", "entry_pulse_count", "Fire_Pulse_Count"),
    ("Pulse Delay", "entry_pulse_delay", "Fire_Pulse_Delay_Seconds"),
    ("Range Dist", "entry_range_distance", "Fire_Range_Distance"),
    ("Fire SFX", "entry_fire_sfx", "Fire_SFXEvent"), ("Inacc Fighter", "entry_inacc_fighter", ""),
    ("Inacc Bomber", "entry_inacc_bomber", ""), ("Inacc Transport", "entry_inacc_transport", ""),
    ("Inacc Corvette", "entry_inacc_corvette", ""), ("Inacc Frigate", "entry_inacc_frigate", ""),
    ("Inacc Capital", "entry_inacc_capital", ""), ("Inacc Super", "entry_inacc_super", ""),
    ("Opp Fire Idle", "entry_opp_fire_idle", "Allow_Opportunity_Fire_When_Idle"),
    ("Opp Fire Target", "entry_opp_fire_target", "Allow_Opportunity_Fire_When_Targeting")
]

for i, (label, var_name, xml_tag) in enumerate(fields):
    row, col = i % 15, (i // 15) * 2
    tk.Label(scrollable_frame, text=f"{label}:").grid(row=row, column=col, sticky="w", padx=5)

    if label == "HardPoint Name":
        name_subframe = tk.Frame(scrollable_frame)
        name_subframe.grid(row=row, column=col + 1, sticky="ew", pady=2, padx=5)
        name_subframe.columnconfigure(0, weight=1)
        globals()[var_name] = tk.Entry(name_subframe)
        globals()[var_name].grid(row=0, column=0, sticky="ew")
        var_force_consecutive = tk.BooleanVar()
        tk.Checkbutton(name_subframe, text="Force Consecutive", variable=var_force_consecutive).grid(row=0, column=1,
                                                                                                     padx=5)
    else:
        globals()[var_name] = tk.Entry(scrollable_frame)
        globals()[var_name].grid(row=row, column=col + 1, sticky="ew", pady=2, padx=5)

    if xml_tag: entry_fields[xml_tag] = globals()[var_name]

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

btn_frame = ttk.Frame(root)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Generate XML", command=generate_xml).pack(side="left", padx=5)
tk.Button(btn_frame, text="Copy Output", command=copy_output).pack(side="left", padx=5)
tk.Button(btn_frame, text="Copy Names", command=copy_hardpoint_names).pack(side="left", padx=5)
tk.Button(btn_frame, text="Clear All Fields", command=clear_fields).pack(side="left", padx=5)

result_text = tk.Text(root, height=12)
result_text.pack(fill="both", expand=True, padx=10, pady=5)

root.mainloop()