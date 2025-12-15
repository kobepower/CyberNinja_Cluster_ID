# CyberNinja_Cluster_ID
Audi, BWM, Benz, Key programing, GUI. 

# 🔧 CyberNinja Cluster ID

A professional desktop application for automotive locksmiths and key programmers to identify luxury vehicle security systems, cluster removal requirements, and programming capabilities. Designed specifically for BMW (CAS2/3/4/FEM), Audi (BCM2), and Mercedes-Benz (FBS3/FBS4) vehicles.

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🎯 Purpose

**Know before you go.** When a customer calls about a luxury vehicle key programming job, CyberNinja Cluster ID instantly tells you:

- ✅ **Can you program it?** (YES/NO with clear reasoning)
- 🔧 **What system is it?** (CAS2/3/4/FEM for BMW, FBS3/FBS4 for Mercedes, BCM2 for Audi)
- ⚠️ **Cluster removal required?** (Critical for Audi BCM2 systems)
- 📍 **Where is the BCM/SAM/CAS module?**
- 🔌 **What Xhorse adapters are needed?**
- 📝 **Special warnings and procedures**

**Stop accepting jobs you can't complete.** Mercedes FBS4 (2018+) requires dealer equipment - this app will warn you immediately.

## ✨ Key Features

### 🚗 System Identification
- **BMW CAS Systems** - Identifies CAS2 (2001-2005), CAS3 (2004-2011), CAS4/CAS4+ (2008-2015), FEM/BDC (2016+)
- **Mercedes FBS Systems** - Identifies FBS3 (programmable) vs FBS4 (dealer only)
- **Audi BCM2 Systems** - Tracks locked cluster part numbers that require removal

### 🎨 Professional Interface
- **Dark cyberpunk theme** - Easy on the eyes during long work sessions
- **Color-coded difficulty** - Green (Basic), Yellow (Intermediate), Orange (Advanced), Red (Expert)
- **CAN PROGRAM badge** - Instant YES/NO indicator in green or red
- **System type badges** - Clearly shows which CAS/FBS/BCM system

### 📋 Comprehensive Database
- **Pre-loaded with common vehicles** - BMW 3/5/7 Series, X3/X5, Mercedes C/E/S Class, GLC/GLE, Audi A3/A4/Q5/Q7
- **Locked cluster tracking** - Complete list of Audi cluster part numbers requiring removal
- **Xhorse adapter recommendations** - Exact adapters needed for each job
- **Year-specific data** - Know exactly which years you can handle

### 🛠️ Database Management
- **Fully editable** - Add your own vehicles and procedures
- **JSON-based** - Human-readable, easy to backup
- **Image attachments** - Add photos of clusters, BCMs, adapters
- **Quick add interface** - Form-based entry for new vehicles

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/cyberninja-cluster-id.git
cd cyberninja-cluster-id
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install customtkinter Pillow
```

3. **Run the application**
```bash
python cluster_id.py
```

The application will automatically:
- Create `cluster_database.json` with pre-loaded vehicle data
- Create `Cluster_Images` folder for reference photos
- Load the professional cyberpunk-themed interface

## 📖 Usage Guide

### Looking Up a Vehicle

1. **Select Make** - Choose BMW, Audi, or Mercedes-Benz
2. **Select Model** - Pick the specific model (3 Series, C-Class, etc.)
3. **Select Year Range** - Choose the year range
4. **Click "SHOW INFORMATION"** or the info loads automatically

### Understanding the Results

#### CAN YOU PROGRAM Badge
- 🟢 **YES** - You have the tools and ability to program this vehicle
- 🔴 **NO - Dealer Only** - Do NOT accept this job, requires dealer equipment
- 🟡 **Check VIN** - Transition years, verify FBS3/FBS4 before accepting

#### System Type Badge
- **CAS2** (2001-2005) - Easy, basic programming
- **CAS3** (2004-2011) - Standard OBDII programming
- **CAS4/CAS4+** (2008-2015) - May need ISN reading
- **FEM/BDC** (2016+) - Complex but doable with proper tools
- **FBS3** (2000-2018) - IR programming works
- **FBS4** (2018+) - DEALER ONLY, online SCN coding required

#### Difficulty Levels
- 🟢 **Basic** - Standard OBDII programming, minimal risk
- 🟡 **Intermediate** - Some complexity, ISN may be needed
- 🟠 **Advanced** - Bench programming, complex procedures
- 🔴 **Expert** - High risk, may require dealer support

### Critical Information Displayed

**Cluster Removal**
- Shows if the instrument cluster must be removed from the vehicle
- Lists specific locked cluster part numbers for Audi vehicles
- Critical for quoting time and pricing

**BCM/SAM/CAS Location**
- Exact location of the control module
- Helps with access and removal planning

**Required Xhorse Adapters**
- Complete list of adapters needed for the job
- Direct links to Xhorse website for purchasing

**Special Notes & Warnings**
- Critical procedures and requirements
- Common pitfalls to avoid
- Gateway unlock requirements
- Online coding requirements

### Adding New Vehicles

#### Method 1: Quick Add Form
1. Click **"➕ Add New Entry"** button
2. Fill in the form fields:
   - Make, Model, Year Range
   - Cluster removal requirements
   - BCM location
   - Key FCC/Part number
   - Programming method
   - Difficulty level
3. Add cluster part numbers (comma-separated)
4. Add required Xhorse adapters (one per line)
5. Add special notes and warnings
6. Optionally attach a reference image
7. Click **"💾 SAVE ENTRY"**

#### Method 2: Direct JSON Editing
1. Click **"📚 Edit Database"** button
2. Edit the JSON structure directly
3. Click **"🔄 Format JSON"** to validate and format
4. Click **"✅ Save & Close"**

**JSON Structure:**
```json
{
  "Make": {
    "Model": {
      "Year-Range": {
        "clusters": ["part1", "part2"],
        "cluster_removal": "Required/Not Required",
        "bcm_location": "Location details",
        "special_notes": "Important warnings",
        "xhorse_adapters": ["Adapter 1", "Adapter 2"],
        "key_type": "FCC code",
        "programming_method": "OBDII/Bench/IR",
        "difficulty": "Basic/Intermediate/Advanced/Expert",
        "system_type": "CAS3/FBS3/etc",
        "can_program": "Yes/No"
      }
    }
  }
}
```

### Attaching Reference Images

Images help identify clusters, BCMs, and adapters at a glance.

1. When adding a new entry, click **"📁 Attach Image"**
2. Select an image file (PNG, JPG, GIF, BMP)
3. Image is automatically saved with the vehicle entry
4. Images display when viewing vehicle information

Images are stored in `Cluster_Images` folder with naming format:
`Make_Model_YearRange.jpg`

## 🎯 Real-World Usage Scenarios

### Scenario 1: Customer Calls About 2022 Mercedes C-Class
1. Look up: Mercedes-Benz → C-Class → 2022-2025
2. **Result**: 🔴 **NO - Dealer Only** - FBS4 system
3. **Action**: Politely decline or refer to dealer

### Scenario 2: Customer Calls About 2016 BMW X5
1. Look up: BMW → X5 → 2014-2018
2. **Result**: 🟢 **YES** - CAS4+ system
3. **Difficulty**: Intermediate
4. **Adapters**: BMW CAS4+ Adapter
5. **Action**: Accept job, quote accordingly

### Scenario 3: Customer Calls About 2018 Mercedes E-Class
1. Look up: Mercedes-Benz → E-Class → 2017-2020
2. **Result**: 🟡 **Check VIN** - FBS3/FBS4 transition
3. **Action**: Check VIN first. If FBS3 = accept, if FBS4 = decline

### Scenario 4: Customer Calls About 2019 Audi A3
1. Look up: Audi → A3 → 2015-2020
2. **Result**: 🟠 **Advanced** - Cluster removal REQUIRED
3. **Shows**: List of 15+ locked cluster part numbers
4. **Adapters**: VVDI Prog Audi BCM2 Adapter, Dashboard Programmer
5. **Action**: Quote higher price for cluster removal and bench work

## 🔐 BMW System Reference

### CAS2 (2001-2005)
- ✅ **Programmable**: Yes
- **Difficulty**: Basic
- **Method**: OBDII
- **Notes**: Older system, straightforward programming

### CAS3 (2004-2011)
- ✅ **Programmable**: Yes
- **Difficulty**: Basic to Intermediate
- **Method**: OBDII
- **Common vehicles**: E90 3 Series, E60 5 Series, E70 X5
- **Notes**: Most common system, well-documented

### CAS4/CAS4+ (2008-2015)
- ✅ **Programmable**: Yes
- **Difficulty**: Intermediate
- **Method**: OBDII, may need ISN reading
- **Common vehicles**: F30 3 Series, F10 5 Series
- **Notes**: ISN code may be required, slightly more complex

### FEM/BDC (2016+)
- ✅ **Programmable**: Yes with proper tools
- **Difficulty**: Advanced
- **Method**: OBDII with ISN, CAN FD
- **Common vehicles**: G20 3 Series, G30 5 Series, G05 X5
- **Notes**: Most complex BMW system, requires FEM/BDC adapter

## 🔐 Mercedes-Benz System Reference

### FBS3 (2000-2018)
- ✅ **Programmable**: Yes
- **Difficulty**: Basic to Intermediate
- **Method**: IR programming + OBDII
- **Common vehicles**: W204 C-Class, W212 E-Class, W221 S-Class
- **Tools**: MB IR Programmer, VVDI MB BGA Tool
- **Notes**: Standard IR programming works well

### FBS4 (2018+)
- ❌ **Programmable**: NO - Dealer Only
- **Difficulty**: Expert (Impossible without dealer)
- **Method**: Online SCN coding required
- **Common vehicles**: W206 C-Class (2022+), W213 E-Class (2021+), W223 S-Class (2021+)
- **Tools**: Requires dealer equipment and online authorization
- **Notes**: **DO NOT ACCEPT THESE JOBS** - Cannot be programmed independently

### Transition Years (2017-2020)
- ⚠️ **Important**: Check VIN to determine FBS3 vs FBS4
- **2017-2019**: Often still FBS3 (programmable)
- **2020+**: Usually FBS4 (dealer only)
- **Always verify** before accepting the job

## 🔐 Audi BCM2 System Reference

### BCM2 Locked Clusters
Certain Audi cluster part numbers are "locked" and MUST be removed from the vehicle for bench programming:

**A3 (8V) Common Locked Clusters:**
- 8V0920940A, 8V0920860E, 8V0920860G, 8V0920860N, 8V0920860P
- 8V0920861/A/H/N, 8V0920870H, 8V0920872B
- 8V0920960A/B/H/M, 8V0920961C

**Programming Requirements:**
- Cluster MUST be removed from dashboard
- Bench programming with VVDI Prog + BCM2 Adapter
- Gateway module may need programming
- Dashboard must be partially disassembled

**Difficulty**: Advanced - Always quote extra time for cluster removal

## 📁 File Structure

```
cyberninja-cluster-id/
├── cluster_id.py                   # Main application
├── cluster_database.json           # Vehicle database (auto-generated)
├── Cluster_Images/                 # Reference images folder
│   ├── BMW_3Series_2019-2025.jpg
│   ├── Mercedes-Benz_C-Class_2022-2025.jpg
│   └── ...
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🎨 Customization

### Changing the Color Theme

Edit the color constants at the top of `cluster_id.py`:

```python
CYBER_CYAN = "#00ffff"      # Main accent color
CYBER_GREEN = "#00ff00"     # Success/Yes indicators
CYBER_MAGENTA = "#ff00ff"   # Action buttons
CYBER_DARK = "#0a0a0f"      # Background
CYBER_PANEL = "#12121a"     # Panel background
CYBER_ACCENT = "#00ffcc"    # Secondary accent
CYBER_RED = "#ff0066"       # Warning/No indicators
CYBER_YELLOW = "#ffcc00"    # Caution indicators
```

### Adding Your Own Branding

Modify the title and footer text in the `build_ui()` function:

```python
ctk.CTkLabel(title_left, text="YOUR COMPANY NAME", ...)
ctk.CTkLabel(bottom, text="Your Company - Professional Edition v1.0", ...)
```

## 🛠️ Technical Details

### Built With
- **CustomTkinter** - Modern, themeable UI framework
- **Pillow (PIL)** - Image processing and display
- **JSON** - Lightweight, human-readable database format
- **Tkinter** - Base GUI framework (included with Python)

### Database Format
- **JSON structure** - Easy to read, edit, and backup
- **Hierarchical organization** - Make → Model → Year Range
- **Extensible** - Add any fields you need

### Image Storage
- **Format**: JPEG (auto-converted from any format)
- **Size**: Auto-resized to max 1920px
- **Transparency**: Auto-converted to white background
- **Quality**: 85% JPEG quality (good balance)

## 🐛 Troubleshooting

### Application won't start
- Ensure Python 3.8+ is installed: `python --version`
- Install dependencies: `pip install customtkinter Pillow`
- Check for error messages in terminal

### Database errors
- Validate JSON at [jsonlint.com](https://jsonlint.com)
- Use the **"🔄 Format JSON"** button in the database editor
- Delete `cluster_database.json` to regenerate default database

### Images not displaying
- Ensure Pillow is installed: `pip install Pillow`
- Check image format (PNG, JPG, GIF, BMP supported)
- Verify image file exists in `Cluster_Images` folder

### "Can Program" shows incorrect information
- Edit the specific vehicle entry
- Update the `can_program` field
- Verify `system_type` is correct

## ⚠️ Important Warnings

### Mercedes FBS4 Systems
**DO NOT ACCEPT** programming jobs for 2018+ Mercedes vehicles without verifying the system type first. FBS4 requires:
- Dealer-level equipment
- Online SCN coding authorization
- Cannot be completed with aftermarket tools

If you accept an FBS4 job, you **cannot complete it** and will lose money.

### Audi Locked Clusters
Some Audi clusters **MUST** be removed from the vehicle for programming. Always:
- Check if cluster removal is required
- Quote extra time for dashboard disassembly
- Have proper bench programming equipment (VVDI Prog + BCM2 Adapter)

### BMW FEM Systems
2016+ BMW vehicles with FEM/BDC require:
- Proper FEM/BDC programming adapter
- ISN code reading capability
- Advanced knowledge of CAN FD systems

## 📝 License

This project is licensed under the MIT License:

```
MIT License

Copyright (c) 2024 CyberNinja Tools

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🤝 Contributing

Contributions welcome! Here's how:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/NewManufacturer`)
3. **Commit your changes** (`git commit -m 'Add Porsche support'`)
4. **Push to the branch** (`git push origin feature/NewManufacturer`)
5. **Open a Pull Request**

### Ideas for Contributions
- Add more vehicle manufacturers (Porsche, Jaguar, Land Rover details)
- Expand year ranges for existing vehicles
- Add more locked cluster part numbers
- Improve system identification algorithms
- Add video tutorial links
- Multi-language support

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/cyberninja-cluster-id/issues)
- **Xhorse Tools**: [https://www.xhorsetool.com](https://www.xhorsetool.com)
- **Email**: support@example.com

## 🙏 Acknowledgments

- **Xhorse** - For developing professional key programming tools
- **Automotive Locksmith Community** - For sharing system identification knowledge
- **CustomTkinter** - For the excellent modern UI framework

## 📊 Roadmap

### Version 1.1 (Planned)
- [ ] Add more Audi models and locked clusters
- [ ] Expand BMW model coverage
- [ ] Add Porsche support
- [ ] VIN decoder integration
- [ ] Export vehicle info to PDF

### Version 1.2 (Future)
- [ ] Land Rover system identification
- [ ] Jaguar support
- [ ] Video tutorial links for complex procedures
- [ ] Cost calculator for quoting jobs
- [ ] Time estimate calculator

### Version 2.0 (Future)
- [ ] Cloud sync for database
- [ ] Mobile companion app
- [ ] Automatic updates for new vehicles
- [ ] Integration with key cutting databases
- [ ] Customer job tracking

---

**Made with 🔑 for professional automotive locksmiths**

*Know Your System. Quote Accurately. Complete Every Job.* 🚗✨
