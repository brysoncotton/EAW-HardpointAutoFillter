## Overview
This tool generates structured XML entries for hardpoints for the game Empire at War: Forces of Corruption.
The intent is to streamline the task of creating of multiple hardpoints that follow a similar naming convention.

## Getting Started
1. Download the provided .exe under the releases section

2. Fill out all necessary fields for your hardpoints. (You can paste existing hardpoint code into the top field to use as a template.)

3. Replace the name of the hardpoint with YOUR_hardpoint_NAME_00 (e.g., HP_MC80_TB_00).

4. The program searches for 00 in the following fields and replaces it with consecutive values (01, 02, ... 09, 10, etc.):

       Hardpoint Name

       Model To Attach
  
       Attachment Bone
  
       Collision Mesh
  
       Damage_Decal
  
       Damage_Particles
 
       Fire Bone A
  
       Fire Bone B
 
       Fire Bone C

       Turret_Bone_Name

       Barrel_Bone_Name
  
6. Click "Generate XML".

7. Verify the generated XML is correct.

8. Click "Copy Output" and paste it into your hardpoint .xml file.
9. 
10. Click "Copy Names" to copy the names of the generated hardpoints for convenient pasting into your unit .xml file.


The generator can:
- Produce multiple hardpoint XML entries with incremental naming and values.
- Load and parse existing hardpoint XML snippets to autofill input fields.
- Copy the generated XML or just the hardpoint names to your clipboard.
- Customize key properties of each hardpoint through the GUI.

Features
- Batch Generation: Generate multiple entries with automatic numbering.
- Smart Replacement: Replace specific tags in each entry based on a numbering system.
- XML Parsing: Load an existing hardpoint XML snippet to populate fields automatically.
- Clipboard Support: Copy full XML output or just the hardpoint names.
- Flexible Input: Customize values for all relevant hardpoint properties.

## Usage Instructions
1. Enter the number of entries you want to generate.
2. Set the start value (default is `1`).
3. Toggle 'Every Other' if you want to increment numbers by 2 instead of 1.
4. Manual List lets you add specific hardpoints; just type the values of the hardpoints that will replace the 00 throughout the hardpoint XML code
5. Paste existing hardpoint XML into the text box if you want to autofill the fields.
6. Fill in or adjust the input fields as needed.
7. Force Consecutive next to the "Hardpoint Name" tag forces the 00 in that specific tag to increase by increments of 1 starting at the value defined in the "start" dialogue above
8. Click Generate XML to produce the output.
9. Click Copy Output to copy the XML to your clipboard, or Copy Names to copy just the hardpoint names.
10. Clear Fields resets everything for a fresh start.

## License

```
Copyright (c) 2025 Bryson Cotton
This software is free for personal use only.
Redistribution, modification, or resale is prohibited.
```

You do not need to file anything to use this software for personal purposes. Any use beyond that requires explicit permission from the copyright holder.

## Author
Bryson Cotton
