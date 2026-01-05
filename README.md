## Overview
This tool generates structured XML entries for hardpoints for the game Empire at War: Forces of Corruption.
The intent is to streamline the task of creating of multiple hardpoints that follow a similar naming convention.

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
1. Setup & Template

       Download: Run the .exe from the latest [Releases] section.
       
       Load Template: Paste an existing hardpoint XML into the top field to autofill the generator, or fill the fields manually.
       
       The "00" Rule: For any field you want to be numbered (e.g., HP_Star_Destroyer_TL_00), ensure the string ends in or contains 00. The program will replace this with 01, 02, etc.

3. Supported Numbering Fields

       The program scans for 00 in the following tags:
       
       Hardpoint Name
       
       Model To Attach & Collision Mesh
       
       Attachment, Turret, & Barrel Bones
       
       Fire Bones (A, B, and C)
       
       Damage Decals & Particles

3. Generation Settings
   
       Start Value: Set the starting number (default is 1).
       
       Every Other: Toggles increments of 2 (useful for port/starboard separation).
       
       Force Consecutive: When enabled for the "Hardpoint Name," names will always increase by 1, even if other fields use different logic.
       
       Manual List: Enter specific suffixes (separated by commas or spaces) to replace 00 with custom values.

5. Output
   
       Generate XML: Click this to populate the output box.
       
       Copy Output: Copies the full XML blocks ready for your Hardpoints.xml.
       
       Copy Names: Copies only the <Hardpoint_Name> strings, ready to be pasted into a unit's <HardPoints> tag.

## License

Copyright (c) 2025 Bryson Cotton
This software is free for personal use only.
Redistribution, modification, or resale is prohibited.


You do not need to file anything to use this software for personal purposes. Any use beyond that requires explicit permission from the copyright holder.

## Author
Bryson Cotton
