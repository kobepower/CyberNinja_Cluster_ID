import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import customtkinter as ctk
import json
import os
from pathlib import Path
from PIL import Image, ImageTk
import webbrowser

# ==========================
# CyberNinja Theme Settings
# ==========================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Custom colors
CYBER_CYAN = "#00ffff"
CYBER_GREEN = "#00ff00"
CYBER_MAGENTA = "#ff00ff"
CYBER_DARK = "#0a0a0f"
CYBER_PANEL = "#12121a"
CYBER_ACCENT = "#00ffcc"
CYBER_RED = "#ff0066"
CYBER_YELLOW = "#ffcc00"

class LuxuryClusterGuide(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🔧 CyberNinja Cluster ID - Professional Edition")
        self.geometry("1400x900")
        self.minsize(1200, 800)
        self.configure(fg_color=CYBER_DARK)

        # Database & folders
        self.db_file = "cluster_database.json"
        self.images_dir = "Cluster_Images"
        
        os.makedirs(self.images_dir, exist_ok=True)
        
        self.load_or_create_db()
        self.current_image_path = None
        
        self.build_ui()

    # =======================
    # Database Handling
    # =======================
    def load_or_create_db(self):
        if not os.path.exists(self.db_file):
            default_db = {
                "Audi": {
                    "A3": {
                        "2015-2020": {
                            "clusters": ["8V0920940A", "8V0920860E", "8V0920860G", "8V0920860N", "8V0920860P", 
                                       "8V0920861", "8V0920861A", "8V0920861H", "8V0920861N", "8V0920870H", 
                                       "8V0920872B", "8V0920960A", "8V0920960B", "8V0920960H", "8V0920960M", "8V0920961C"],
                            "cluster_removal": "Required",
                            "bcm_location": "Dashboard - requires partial removal",
                            "special_notes": "Gateway module programming required. Cluster must be bench programmed.",
                            "xhorse_adapters": ["VVDI Prog Audi BCM2 Adapter", "Dashboard Programmer"],
                            "key_type": "8V0 959 754",
                            "programming_method": "OBDII + Bench (Cluster)",
                            "difficulty": "Advanced"
                        }
                    },
                    "A4": {
                        "2017-2025": {
                            "clusters": ["8W0920xxx series"],
                            "cluster_removal": "Required for some",
                            "bcm_location": "Dashboard center",
                            "special_notes": "BCM2 system. May require gateway unlock.",
                            "xhorse_adapters": ["VVDI Prog BCM2 Adapter"],
                            "key_type": "8W0 959 754",
                            "programming_method": "OBDII preferred",
                            "difficulty": "Intermediate"
                        },
                        "2009-2016": {
                            "clusters": [],
                            "cluster_removal": "Not typically required",
                            "bcm_location": "Dashboard",
                            "special_notes": "Older system, easier programming",
                            "xhorse_adapters": ["Standard OBDII"],
                            "key_type": "8K0 959 754",
                            "programming_method": "OBDII",
                            "difficulty": "Basic"
                        }
                    },
                    "Q5": {
                        "2018-2025": {
                            "clusters": ["80A920xxx series"],
                            "cluster_removal": "Required",
                            "bcm_location": "Behind dashboard",
                            "special_notes": "BCM2 programming required. Gateway may need unlock.",
                            "xhorse_adapters": ["VVDI Prog BCM2 Adapter", "MLB Platform Adapter"],
                            "key_type": "80A 959 754",
                            "programming_method": "Bench + OBDII",
                            "difficulty": "Advanced"
                        }
                    },
                    "Q7": {
                        "2020-2025": {
                            "clusters": [],
                            "cluster_removal": "Required - MLB Platform",
                            "bcm_location": "Behind dashboard - MLB",
                            "special_notes": "MLB platform requires special adapter. Very complex programming.",
                            "xhorse_adapters": ["VVDI Prog MLB Adapter", "BCM2 Adapter"],
                            "key_type": "4M0 959 754 (MLB)",
                            "programming_method": "Bench programming mandatory",
                            "difficulty": "Expert"
                        }
                    }
                },
                "BMW": {
                    "3 Series": {
                        "2019-2025": {
                            "clusters": ["G20/G21 series"],
                            "cluster_removal": "Rarely required",
                            "bcm_location": "FEM Module - Behind glove box",
                            "special_notes": "FEM (Footwell Electronics Module) programming. ISN code required. CAN FD system.",
                            "xhorse_adapters": ["BMW FEM/BDC Adapter", "CAS4+ Adapter"],
                            "key_type": "8723604-01",
                            "programming_method": "OBDII with ISN",
                            "difficulty": "Advanced",
                            "system_type": "FEM/BDC (2016+)",
                            "can_program": "Yes - with proper tools"
                        },
                        "2012-2018": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "CAS3/CAS4 module - Behind glove box",
                            "special_notes": "CAS4/CAS4+ programming. May need to read ISN from CAS module.",
                            "xhorse_adapters": ["BMW CAS3/CAS4 Adapter"],
                            "key_type": "YGOHUF5767",
                            "programming_method": "OBDII",
                            "difficulty": "Intermediate",
                            "system_type": "CAS4/CAS4+ (2008-2015)",
                            "can_program": "Yes"
                        },
                        "2006-2011": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "CAS3 module - Behind glove box",
                            "special_notes": "CAS3 system. Easier to program than CAS4.",
                            "xhorse_adapters": ["BMW CAS3 Adapter", "AK90+ Key Programmer"],
                            "key_type": "LX8FZV / KR55WK49127",
                            "programming_method": "OBDII",
                            "difficulty": "Basic",
                            "system_type": "CAS3 (2004-2011)",
                            "can_program": "Yes"
                        },
                        "2001-2005": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "CAS2 module",
                            "special_notes": "CAS2 system. Older and easier programming.",
                            "xhorse_adapters": ["BMW CAS2 Adapter", "AK90+"],
                            "key_type": "LX8FZV",
                            "programming_method": "OBDII",
                            "difficulty": "Basic",
                            "system_type": "CAS2 (2001-2005)",
                            "can_program": "Yes"
                        }
                    },
                    "5 Series": {
                        "2017-2025": {
                            "clusters": [],
                            "cluster_removal": "Rarely required",
                            "bcm_location": "FEM module",
                            "special_notes": "FEM/BDC system. Complex security. ISN required.",
                            "xhorse_adapters": ["BMW FEM/BDC Adapter"],
                            "key_type": "8723604-01",
                            "programming_method": "OBDII with ISN",
                            "difficulty": "Advanced",
                            "system_type": "FEM/BDC (2016+)",
                            "can_program": "Yes - with proper tools"
                        },
                        "2011-2016": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "CAS4/CAS4+ module",
                            "special_notes": "CAS4+ programming. ISN may be needed.",
                            "xhorse_adapters": ["BMW CAS4+ Adapter"],
                            "key_type": "YGOHUF5767",
                            "programming_method": "OBDII",
                            "difficulty": "Intermediate",
                            "system_type": "CAS4+ (2011-2015)",
                            "can_program": "Yes"
                        },
                        "2004-2010": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "CAS3 module",
                            "special_notes": "CAS3 system. Standard programming.",
                            "xhorse_adapters": ["BMW CAS3 Adapter"],
                            "key_type": "LX8FZV",
                            "programming_method": "OBDII",
                            "difficulty": "Basic",
                            "system_type": "CAS3 (2004-2011)",
                            "can_program": "Yes"
                        }
                    },
                    "7 Series": {
                        "2016-2025": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "FEM module",
                            "special_notes": "FEM system. High security. May require dealer support for certain functions.",
                            "xhorse_adapters": ["BMW FEM/BDC Adapter"],
                            "key_type": "8723604-01",
                            "programming_method": "OBDII with ISN",
                            "difficulty": "Expert",
                            "system_type": "FEM/BDC (2016+)",
                            "can_program": "Yes - but complex"
                        },
                        "2009-2015": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "CAS4 module",
                            "special_notes": "CAS4 system. ISN programming required.",
                            "xhorse_adapters": ["BMW CAS4 Adapter"],
                            "key_type": "YGOHUF5767",
                            "programming_method": "OBDII",
                            "difficulty": "Advanced",
                            "system_type": "CAS4 (2008-2015)",
                            "can_program": "Yes"
                        }
                    },
                    "X3": {
                        "2018-2025": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "FEM module",
                            "special_notes": "FEM programming required.",
                            "xhorse_adapters": ["BMW FEM/BDC Adapter"],
                            "key_type": "8723604-01",
                            "programming_method": "OBDII",
                            "difficulty": "Advanced",
                            "system_type": "FEM/BDC (2016+)",
                            "can_program": "Yes"
                        },
                        "2011-2017": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "CAS4 module",
                            "special_notes": "CAS4 programming.",
                            "xhorse_adapters": ["BMW CAS4 Adapter"],
                            "key_type": "YGOHUF5767",
                            "programming_method": "OBDII",
                            "difficulty": "Intermediate",
                            "system_type": "CAS4 (2008-2015)",
                            "can_program": "Yes"
                        }
                    },
                    "X5": {
                        "2019-2025": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "FEM module",
                            "special_notes": "FEM programming. Complex security system.",
                            "xhorse_adapters": ["BMW FEM/BDC Adapter"],
                            "key_type": "8723604-01",
                            "programming_method": "OBDII",
                            "difficulty": "Advanced",
                            "system_type": "FEM/BDC (2016+)",
                            "can_program": "Yes"
                        },
                        "2014-2018": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "CAS4+ module",
                            "special_notes": "CAS4+ system.",
                            "xhorse_adapters": ["BMW CAS4+ Adapter"],
                            "key_type": "YGOHUF5767",
                            "programming_method": "OBDII",
                            "difficulty": "Intermediate",
                            "system_type": "CAS4+ (2011-2015)",
                            "can_program": "Yes"
                        },
                        "2007-2013": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "CAS3 module",
                            "special_notes": "CAS3 system. Standard programming.",
                            "xhorse_adapters": ["BMW CAS3 Adapter"],
                            "key_type": "LX8FZV",
                            "programming_method": "OBDII",
                            "difficulty": "Basic",
                            "system_type": "CAS3 (2004-2011)",
                            "can_program": "Yes"
                        }
                    }
                },
                "Mercedes-Benz": {
                    "C-Class": {
                        "2022-2025": {
                            "clusters": [],
                            "cluster_removal": "Not typically required",
                            "bcm_location": "SAM module - Various locations",
                            "special_notes": "FBS4 system. Online SCN coding REQUIRED. Cannot be programmed without dealer support or online access. IR key programming only for existing keys.",
                            "xhorse_adapters": ["MB IR Key Programmer", "VVDI MB BGA Tool (limited)"],
                            "key_type": "IYZDC12K",
                            "programming_method": "Dealer/Online ONLY (FBS4)",
                            "difficulty": "Expert",
                            "system_type": "FBS4 (2018+)",
                            "can_program": "NO - Dealer Only for new keys"
                        },
                        "2015-2021": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module - Behind dashboard",
                            "special_notes": "FBS3 system. IR programming possible. Some models may need online verification.",
                            "xhorse_adapters": ["MB IR Programmer", "VVDI MB BGA Tool"],
                            "key_type": "IYZDC07",
                            "programming_method": "IR programming + OBDII",
                            "difficulty": "Intermediate",
                            "system_type": "FBS3 (2000-2018)",
                            "can_program": "Yes - IR programming works"
                        },
                        "2008-2014": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module",
                            "special_notes": "FBS3 system. Standard IR programming.",
                            "xhorse_adapters": ["MB IR Programmer"],
                            "key_type": "IYZ3312",
                            "programming_method": "IR programming",
                            "difficulty": "Basic",
                            "system_type": "FBS3 (2000-2018)",
                            "can_program": "Yes"
                        }
                    },
                    "E-Class": {
                        "2021-2025": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module",
                            "special_notes": "FBS4 system. DEALER ONLY. Online authorization REQUIRED. Cannot program keys independently.",
                            "xhorse_adapters": ["N/A - Dealer equipment required"],
                            "key_type": "IYZDC12K",
                            "programming_method": "Dealer Only (FBS4)",
                            "difficulty": "Expert",
                            "system_type": "FBS4 (2018+)",
                            "can_program": "NO - Must go to dealer"
                        },
                        "2017-2020": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module",
                            "special_notes": "FBS3/FBS4 transition. 2017-2019 may be FBS3 (programmable). 2020+ is FBS4 (dealer only). Check VIN.",
                            "xhorse_adapters": ["MB IR Programmer (FBS3 only)", "VVDI MB BGA Tool"],
                            "key_type": "IYZDC07 / IYZDC12K",
                            "programming_method": "IR (FBS3) / Dealer (FBS4)",
                            "difficulty": "Advanced",
                            "system_type": "FBS3/FBS4 Transition",
                            "can_program": "Check VIN - FBS3=Yes, FBS4=No"
                        },
                        "2010-2016": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module",
                            "special_notes": "FBS3 system. IR programming works well.",
                            "xhorse_adapters": ["MB IR Programmer"],
                            "key_type": "IYZ3312",
                            "programming_method": "IR programming",
                            "difficulty": "Basic",
                            "system_type": "FBS3 (2000-2018)",
                            "can_program": "Yes"
                        }
                    },
                    "S-Class": {
                        "2021-2025": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "Multiple SAM modules",
                            "special_notes": "FBS4 system. DEALER ONLY. Most complex Mercedes system. Online SCN coding mandatory. Do NOT accept these jobs for AKL.",
                            "xhorse_adapters": ["N/A - Dealer only"],
                            "key_type": "IYZDC12K",
                            "programming_method": "Dealer Only",
                            "difficulty": "Expert",
                            "system_type": "FBS4 (2018+)",
                            "can_program": "NO - Dealer Only"
                        },
                        "2014-2020": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM modules",
                            "special_notes": "FBS3 system. Complex but programmable with IR. 2018+ may be FBS4 - verify first.",
                            "xhorse_adapters": ["MB IR Programmer", "VVDI MB BGA Tool"],
                            "key_type": "IYZDC07",
                            "programming_method": "IR programming (FBS3 only)",
                            "difficulty": "Advanced",
                            "system_type": "FBS3 (verify year)",
                            "can_program": "FBS3=Yes, FBS4=No"
                        },
                        "2007-2013": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module",
                            "special_notes": "FBS3 system. Standard IR programming.",
                            "xhorse_adapters": ["MB IR Programmer"],
                            "key_type": "IYZ3312",
                            "programming_method": "IR programming",
                            "difficulty": "Intermediate",
                            "system_type": "FBS3 (2000-2018)",
                            "can_program": "Yes"
                        }
                    },
                    "GLC": {
                        "2020-2025": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module",
                            "special_notes": "FBS4 system. Dealer only for new key programming.",
                            "xhorse_adapters": ["N/A"],
                            "key_type": "IYZDC12K",
                            "programming_method": "Dealer Only",
                            "difficulty": "Expert",
                            "system_type": "FBS4 (2018+)",
                            "can_program": "NO"
                        },
                        "2016-2019": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module",
                            "special_notes": "FBS3 system. IR programming works.",
                            "xhorse_adapters": ["MB IR Programmer"],
                            "key_type": "IYZDC07",
                            "programming_method": "IR programming",
                            "difficulty": "Intermediate",
                            "system_type": "FBS3 (2000-2018)",
                            "can_program": "Yes"
                        }
                    },
                    "GLE": {
                        "2020-2025": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module",
                            "special_notes": "FBS4 system. DEALER ONLY. Cannot program independently.",
                            "xhorse_adapters": ["N/A"],
                            "key_type": "IYZDC12K",
                            "programming_method": "Dealer Only",
                            "difficulty": "Expert",
                            "system_type": "FBS4 (2018+)",
                            "can_program": "NO - Dealer Only"
                        },
                        "2016-2019": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module",
                            "special_notes": "FBS3 system. IR programming possible.",
                            "xhorse_adapters": ["MB IR Programmer", "VVDI MB BGA Tool"],
                            "key_type": "IYZDC07",
                            "programming_method": "IR programming",
                            "difficulty": "Intermediate",
                            "system_type": "FBS3 (2000-2018)",
                            "can_program": "Yes"
                        },
                        "2012-2015": {
                            "clusters": [],
                            "cluster_removal": "Not required",
                            "bcm_location": "SAM module",
                            "special_notes": "FBS3 system. Standard IR programming.",
                            "xhorse_adapters": ["MB IR Programmer"],
                            "key_type": "IYZ3312",
                            "programming_method": "IR programming",
                            "difficulty": "Basic",
                            "system_type": "FBS3 (2000-2018)",
                            "can_program": "Yes"
                        }
                    }
                }
            }
            with open(self.db_file, 'w') as f:
                json.dump(default_db, f, indent=4)
            self.db = default_db
        else:
            with open(self.db_file, 'r') as f:
                self.db = json.load(f)

    def save_db(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.db, f, indent=4)

    # =======================
    # UI Building
    # =======================
    def build_ui(self):
        # Title Bar
        title_frame = ctk.CTkFrame(self, fg_color=CYBER_PANEL, height=80)
        title_frame.pack(fill="x", padx=10, pady=(10, 5))
        title_frame.pack_propagate(False)
        
        title_left = ctk.CTkFrame(title_frame, fg_color="transparent")
        title_left.pack(side="left", padx=20, pady=10)
        
        ctk.CTkLabel(title_left, text="🔧 CYBERNINJA CLUSTER ID", 
                     font=("Consolas", 26, "bold"), text_color=CYBER_CYAN).pack(anchor="w")
        ctk.CTkLabel(title_left, text="BMW • Audi • Mercedes-Benz | System Identification Tool", 
                     font=("Consolas", 11), text_color="#666").pack(anchor="w")

        # Warning banner
        warning_frame = ctk.CTkFrame(self, fg_color="#331100", height=40)
        warning_frame.pack(fill="x", padx=10, pady=5)
        warning_frame.pack_propagate(False)
        
        ctk.CTkLabel(warning_frame, text="⚠️ HIGH-END VEHICLE GUIDE - Always verify cluster removal requirements before starting work", 
                     font=("Consolas", 11, "bold"), text_color=CYBER_YELLOW).pack(pady=10)

        # Main content
        main = ctk.CTkFrame(self, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=10, pady=5)

        # Left panel - Vehicle Selection
        left = ctk.CTkFrame(main, fg_color=CYBER_PANEL, width=400)
        left.pack(side="left", fill="both", expand=False, padx=(0, 5))

        ctk.CTkLabel(left, text="📋 VEHICLE SELECTION", font=("Consolas", 16, "bold"), 
                     text_color=CYBER_ACCENT).pack(pady=(15, 10))

        # Selection form
        form = ctk.CTkFrame(left, fg_color="transparent")
        form.pack(padx=20, pady=10, fill="x")

        # Make
        ctk.CTkLabel(form, text="Make:", font=("Consolas", 12, "bold")).pack(anchor="w", pady=(10, 5))
        self.make_var = ctk.StringVar()
        self.make_cb = ctk.CTkComboBox(form, width=340, height=40, font=("Consolas", 13),
                                        values=[""] + sorted(self.db.keys()), variable=self.make_var,
                                        command=self.update_models)
        self.make_cb.pack(pady=5)

        # Model
        ctk.CTkLabel(form, text="Model:", font=("Consolas", 12, "bold")).pack(anchor="w", pady=(10, 5))
        self.model_var = ctk.StringVar()
        self.model_cb = ctk.CTkComboBox(form, width=340, height=40, font=("Consolas", 13),
                                         values=[], variable=self.model_var, command=self.update_years)
        self.model_cb.pack(pady=5)

        # Year Range
        ctk.CTkLabel(form, text="Year Range:", font=("Consolas", 12, "bold")).pack(anchor="w", pady=(10, 5))
        self.year_var = ctk.StringVar()
        self.year_cb = ctk.CTkComboBox(form, width=340, height=40, font=("Consolas", 13),
                                        values=[], variable=self.year_var, command=self.display_info)
        self.year_cb.pack(pady=5)

        # Search button
        ctk.CTkButton(form, text="🔍 SHOW INFORMATION", width=340, height=50,
                      fg_color=CYBER_GREEN, hover_color="#00cc00", text_color="#000",
                      font=("Consolas", 14, "bold"), command=self.display_info).pack(pady=20)

        # Quick stats
        stats_frame = ctk.CTkFrame(left, fg_color="#1a1a2e", corner_radius=10)
        stats_frame.pack(padx=20, pady=10, fill="x")
        
        ctk.CTkLabel(stats_frame, text="📊 Database Stats", font=("Consolas", 12, "bold"),
                     text_color=CYBER_ACCENT).pack(pady=10)
        
        total_makes = len(self.db)
        total_models = sum(len(models) for models in self.db.values())
        
        ctk.CTkLabel(stats_frame, text=f"Makes: {total_makes} | Models: {total_models}",
                     font=("Consolas", 11), text_color="#aaa").pack(pady=(0, 10))

        # Right panel - Information Display
        right = ctk.CTkFrame(main, fg_color=CYBER_PANEL)
        right.pack(side="right", fill="both", expand=True, padx=(5, 0))

        ctk.CTkLabel(right, text="📖 VEHICLE INFORMATION", font=("Consolas", 16, "bold"),
                     text_color=CYBER_ACCENT).pack(pady=(15, 10))

        # Scrollable info frame
        self.info_scroll = ctk.CTkScrollableFrame(right, fg_color="#0a0a15", corner_radius=10)
        self.info_scroll.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Initial message
        self.show_initial_message()

        # Bottom toolbar
        bottom = ctk.CTkFrame(self, fg_color=CYBER_PANEL, height=60)
        bottom.pack(fill="x", pady=(5, 10), padx=10)
        
        ctk.CTkButton(bottom, text="📚 Edit Database", width=140, height=40,
                      fg_color=CYBER_MAGENTA, hover_color="#cc00cc",
                      command=self.open_db_editor).pack(side="left", padx=15, pady=10)
        
        ctk.CTkButton(bottom, text="➕ Add New Entry", width=140, height=40,
                      fg_color=CYBER_CYAN, hover_color="#00cccc", text_color="#000",
                      command=self.add_new_entry).pack(side="left", padx=5, pady=10)
        
        ctk.CTkButton(bottom, text="🌐 Xhorse Website", width=140, height=40,
                      command=lambda: webbrowser.open("https://www.xhorsetool.com")).pack(side="left", padx=5, pady=10)
        
        ctk.CTkLabel(bottom, text="CyberNinja Cluster ID - Professional Edition v1.0",
                     font=("Consolas", 10), text_color="#666").pack(side="right", padx=20)

    def show_initial_message(self):
        """Display initial welcome message"""
        for widget in self.info_scroll.winfo_children():
            widget.destroy()
        
        welcome = ctk.CTkFrame(self.info_scroll, fg_color="transparent")
        welcome.pack(pady=50)
        
        ctk.CTkLabel(welcome, text="👋 Welcome to CyberNinja Cluster ID",
                     font=("Consolas", 18, "bold"), text_color=CYBER_CYAN).pack(pady=10)
        ctk.CTkLabel(welcome, text="Select a vehicle to identify the security system,\ncluster requirements, and determine if you can program it.",
                     font=("Consolas", 12), text_color="#aaa").pack(pady=10)
        ctk.CTkLabel(welcome, text="📌 Supported: Audi • BMW (CAS2/3/4/FEM) • Mercedes (FBS3/FBS4)",
                     font=("Consolas", 11), text_color=CYBER_ACCENT).pack(pady=20)

    # =======================
    # Event Handlers
    # =======================
    def update_models(self, *args):
        make = self.make_var.get()
        self.model_cb.set("")
        self.year_cb.set("")
        self.year_cb.configure(values=[])
        
        if make and make in self.db:
            models = sorted(self.db[make].keys())
            self.model_cb.configure(values=models)

    def update_years(self, *args):
        make = self.make_var.get()
        model = self.model_var.get()
        self.year_cb.set("")
        
        if make and model and model in self.db.get(make, {}):
            years = sorted(self.db[make][model].keys(), reverse=True)
            self.year_cb.configure(values=years)

    # =======================
    # New Helper Methods (from ChatGPT suggestions)
    # =======================
    def create_expandable_section(self, title, content_widget, color=CYBER_CYAN):
        """Creates a clickable expandable section with custom content widget inside"""
        section_frame = ctk.CTkFrame(self.info_scroll, fg_color="#1a1a2e", corner_radius=8)
        section_frame.pack(fill="x", pady=5, padx=10)
        
        header = ctk.CTkButton(section_frame, text=f"▶ {title}", font=("Consolas", 12, "bold"),
                               fg_color=color, hover_color="#00cccc", text_color="#000",
                               corner_radius=8, height=40, anchor="w")
        header.pack(fill="x", padx=5, pady=5)
        
        content_frame = ctk.CTkFrame(section_frame, fg_color="#0a0a15", corner_radius=8)
        content_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        content_widget(content_frame)
        
        # Start collapsed
        content_frame.pack_forget()
        
        def toggle():
            if content_frame.winfo_ismapped():
                content_frame.pack_forget()
                header.configure(text=header.cget("text").replace("▼", "▶"))
            else:
                content_frame.pack(fill="x", padx=10, pady=(0, 10))
                header.configure(text=header.cget("text").replace("▶", "▼"))
        
        header.configure(command=toggle)
        return section_frame

    def create_tooltip(self, widget, text):
        """Simple hover tooltip using Toplevel"""
        tooltip = None
        
        def enter(event):
            nonlocal tooltip
            x = widget.winfo_rootx() + widget.winfo_width() + 5
            y = widget.winfo_rooty() + widget.winfo_height() // 2
            tooltip = tk.Toplevel(widget)
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{x}+{y}")
            label = tk.Label(tooltip, text=text, background="#333333", foreground="#ffffff",
                             font=("Consolas", 10), padx=8, pady=4, relief="solid", borderwidth=1)
            label.pack()
        
        def leave(event):
            nonlocal tooltip
            if tooltip:
                tooltip.destroy()
                tooltip = None
        
        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)

    def copy_to_clipboard(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
        messagebox.showinfo("Copied", "Text copied to clipboard!")

    def display_info(self, *args):
        """Display vehicle information with all new interactive features"""
        make = self.make_var.get()
        model = self.model_var.get()
        year_range = self.year_var.get()
        
        if not all([make, model, year_range]):
            messagebox.showwarning("Selection Required", "Please select Make, Model, and Year Range")
            return
        
        if year_range not in self.db.get(make, {}).get(model, {}):
            return
        
        data = self.db[make][model][year_range]
        
        # Clear previous content
        for widget in self.info_scroll.winfo_children():
            widget.destroy()
        
        # Vehicle Header
        header = ctk.CTkFrame(self.info_scroll, fg_color="#1a2a3a", corner_radius=10)
        header.pack(fill="x", pady=(10, 20), padx=10)
        
        ctk.CTkLabel(header, text=f"{make} {model} ({year_range})",
                     font=("Consolas", 20, "bold"), text_color=CYBER_CYAN).pack(pady=15)
        
        # Difficulty Badge with tooltip
        difficulty = data.get("difficulty", "Unknown")
        diff_colors = {
            "Basic": CYBER_GREEN,
            "Intermediate": CYBER_YELLOW,
            "Advanced": "#ff8800",
            "Expert": CYBER_RED
        }
        diff_color = diff_colors.get(difficulty, "#888")
        
        diff_frame = ctk.CTkFrame(header, fg_color=diff_color, corner_radius=5)
        diff_frame.pack(pady=(0, 10))
        diff_label = ctk.CTkLabel(diff_frame, text=f"  Difficulty: {difficulty}  ",
                                  font=("Consolas", 11, "bold"), text_color="#000")
        diff_label.pack(padx=10, pady=5)
        self.create_tooltip(diff_label, "Complexity level of key programming job")

        # System Type Badge
        system_type = data.get("system_type", "Unknown")
        sys_frame = ctk.CTkFrame(header, fg_color=CYBER_CYAN, corner_radius=5)
        sys_frame.pack(pady=(0, 10))
        sys_label = ctk.CTkLabel(sys_frame, text=f"  System: {system_type}  ",
                                 font=("Consolas", 11, "bold"), text_color="#000")
        sys_label.pack(padx=10, pady=5)
        self.create_tooltip(sys_label, "Immobilizer system type")

        # CAN PROGRAM Badge
        can_program = data.get("can_program", "Unknown")
        can_color = CYBER_GREEN if "Yes" in can_program else CYBER_RED
        can_frame = ctk.CTkFrame(header, fg_color=can_color, corner_radius=5)
        can_frame.pack(pady=(0, 15))
        can_label = ctk.CTkLabel(can_frame, text=f"  CAN YOU PROGRAM: {can_program.upper()}  ",
                                 font=("Consolas", 12, "bold"), text_color="#000")
        can_label.pack(padx=15, pady=8)
        self.create_tooltip(can_label, "Whether third-party tools can program keys")

        # Reference Image (clickable to open full size)
        img_key = f"{make}_{model}_{year_range}".replace(" ", "_").replace("/", "-")
        img_path = f"{self.images_dir}/{img_key}.jpg"
        
        if os.path.exists(img_path):
            img_frame = ctk.CTkFrame(self.info_scroll, fg_color="#1a1a2e", corner_radius=8)
            img_frame.pack(fill="x", pady=10, padx=10)
            
            ctk.CTkLabel(img_frame, text="📷 Reference Image (click to open full size):",
                         font=("Consolas", 12, "bold"), text_color=CYBER_CYAN).pack(anchor="w", padx=15, pady=(10, 5))
            
            try:
                img = Image.open(img_path)
                img.thumbnail((600, 400))
                photo = ImageTk.PhotoImage(img)
                img_label = ctk.CTkLabel(img_frame, image=photo, text="")
                img_label.image = photo
                img_label.pack(padx=15, pady=10)
                img_label.bind("<Button-1>", lambda e: os.startfile(img_path))
            except Exception as e:
                ctk.CTkLabel(img_frame, text=f"Error loading image: {e}").pack(pady=10)

        # Simple sections (non-expandable for brevity)
        self.create_section("⚠️ CLUSTER REMOVAL", data.get("cluster_removal", "Unknown"), CYBER_RED)
        self.create_section("📍 BCM/Control Module Location", data.get("bcm_location", "Unknown"), CYBER_CYAN)
        self.create_section("🔧 Programming Method", data.get("programming_method", "Unknown"), CYBER_ACCENT)

        # Key Type with copy button
        key_frame = ctk.CTkFrame(self.info_scroll, fg_color="#1a1a2e", corner_radius=8)
        key_frame.pack(fill="x", pady=5, padx=10)
        ctk.CTkLabel(key_frame, text="🔑 Key FCC/Part Number:", font=("Consolas", 12, "bold"),
                     text_color=CYBER_GREEN).pack(anchor="w", padx=15, pady=(10, 5))
        key_text = data.get("key_type", "Unknown")
        key_label = ctk.CTkLabel(key_frame, text=key_text, font=("Consolas", 12), text_color="#fff")
        key_label.pack(anchor="w", padx=15)
        ctk.CTkButton(key_frame, text="📋 Copy", width=100, height=30,
                      command=lambda: self.copy_to_clipboard(key_text)).pack(pady=(5, 10), anchor="e", padx=15)

        # Expandable: Locked Clusters
        if data.get("clusters"):
            def clusters_content(parent):
                ctk.CTkLabel(parent, text="📋 Locked Cluster Part Numbers:", font=("Consolas", 11, "bold"),
                             text_color=CYBER_YELLOW).pack(anchor="w", padx=10, pady=(10, 5))
                clusters_text = ctk.CTkTextbox(parent, height=120, font=("Consolas", 10))
                clusters_text.pack(fill="x", padx=10, pady=(0, 10))
                cluster_list = ", ".join(data["clusters"])
                clusters_text.insert("1.0", cluster_list)
                clusters_text.configure(state="disabled")
                ctk.CTkButton(parent, text="📋 Copy All Clusters", width=180,
                              command=lambda: self.copy_to_clipboard(cluster_list)).pack(pady=(0, 10))
            self.create_expandable_section("📋 Locked Clusters", clusters_content, CYBER_YELLOW)

        # Expandable: Xhorse Adapters (clickable links)
        if data.get("xhorse_adapters"):
            def adapters_content(parent):
                ctk.CTkLabel(parent, text="🔌 Required Xhorse Adapters:", font=("Consolas", 12, "bold"),
                             text_color=CYBER_GREEN).pack(anchor="w", padx=10, pady=(10, 5))
                for adapter in data["xhorse_adapters"]:
                    btn = ctk.CTkButton(parent, text=adapter, fg_color="#3333ff", hover_color="#5555ff", height=35,
                                        command=lambda a=adapter: webbrowser.open(f"https://www.google.com/search?q=Xhorse+{a.replace(' ', '+')}"))
                    btn.pack(fill="x", padx=10, pady=5)
            self.create_expandable_section("🔌 Required Xhorse Adapters", adapters_content, CYBER_GREEN)

        # Expandable: Special Notes
        if data.get("special_notes"):
            def notes_content(parent):
                notes_text = ctk.CTkTextbox(parent, height=120, font=("Consolas", 11), wrap="word")
                notes_text.pack(fill="x", padx=10, pady=10)
                notes_text.insert("1.0", data["special_notes"])
                notes_text.configure(state="disabled")
            self.create_expandable_section("📝 Special Notes & Warnings", notes_content, CYBER_YELLOW)

    def create_section(self, title, content, color):
        """Helper to create simple non-expandable info sections"""
        section = ctk.CTkFrame(self.info_scroll, fg_color="#1a1a2e", corner_radius=8)
        section.pack(fill="x", pady=5, padx=10)
        
        ctk.CTkLabel(section, text=title, font=("Consolas", 11, "bold"),
                    text_color=color).pack(anchor="w", padx=15, pady=(10, 5))
        ctk.CTkLabel(section, text=content, font=("Consolas", 12),
                    text_color="#fff", wraplength=700, justify="left").pack(anchor="w", padx=15, pady=(0, 10))

    # =======================
    # Database Management
    # =======================
    def open_db_editor(self):
        editor = DatabaseEditor(self)
        self.wait_window(editor)
        self.load_or_create_db()
        self.make_cb.configure(values=[""] + sorted(self.db.keys()))

    def add_new_entry(self):
        add_window = AddEntryWindow(self)
        self.wait_window(add_window)


# =======================
# Database Editor Window
# =======================
class DatabaseEditor(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("📚 Edit Cluster ID Database")
        self.geometry("1000x700")
        self.configure(fg_color=CYBER_DARK)
        self.build_ui()

    def build_ui(self):
        ctk.CTkLabel(self, text="🔧 CLUSTER DATABASE EDITOR", font=("Consolas", 20, "bold"),
                     text_color=CYBER_CYAN).pack(pady=15)
        
        ctk.CTkLabel(self, text="Edit the JSON below to add/modify vehicle information",
                     font=("Consolas", 11), text_color="#666").pack()

        frame = ctk.CTkFrame(self, fg_color=CYBER_PANEL)
        frame.pack(fill="both", expand=True, padx=20, pady=15)

        self.text = ctk.CTkTextbox(frame, font=("Consolas", 10), fg_color="#0a0a15",
                                    text_color=CYBER_GREEN)
        self.text.pack(fill="both", expand=True, padx=10, pady=10)

        btns = ctk.CTkFrame(self, fg_color="transparent")
        btns.pack(fill="x", pady=15, padx=20)
        
        ctk.CTkButton(btns, text="✅ Save & Close", width=150, height=40,
                      fg_color=CYBER_GREEN, text_color="#000", font=("Consolas", 12, "bold"),
                      command=self.save).pack(side="right", padx=10)
        
        ctk.CTkButton(btns, text="❌ Cancel", width=100, height=40,
                      fg_color="#444", command=self.destroy).pack(side="right", padx=10)
        
        ctk.CTkButton(btns, text="🔄 Format JSON", width=120, height=40,
                      command=self.format_json).pack(side="left", padx=10)

        pretty = json.dumps(self.parent.db, indent=4, sort_keys=True)
        self.text.insert("end", pretty)

    def format_json(self):
        try:
            data = json.loads(self.text.get("1.0", "end"))
            self.text.delete("1.0", "end")
            self.text.insert("end", json.dumps(data, indent=4, sort_keys=True))
        except json.JSONDecodeError as e:
            messagebox.showerror("JSON Error", f"Invalid JSON:\n{e}")

    def save(self):
        try:
            new_db = json.loads(self.text.get("1.0", "end"))
            self.parent.db = new_db
            self.parent.save_db()
            messagebox.showinfo("Saved", "Database updated successfully!")
            self.destroy()
        except json.JSONDecodeError as e:
            messagebox.showerror("JSON Error", f"Invalid JSON:\n{e}")


# =======================
# Add Entry Window
# =======================
class AddEntryWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("➕ Add New Vehicle Entry")
        self.geometry("800x900")
        self.configure(fg_color=CYBER_DARK)
        self.current_image = None
        self.build_ui()

    def build_ui(self):
        ctk.CTkLabel(self, text="➕ ADD NEW VEHICLE", font=("Consolas", 20, "bold"),
                     text_color=CYBER_CYAN).pack(pady=15)

        scroll = ctk.CTkScrollableFrame(self, fg_color=CYBER_PANEL)
        scroll.pack(fill="both", expand=True, padx=20, pady=10)

        # Form fields
        fields = [
            ("Make", "make"),
            ("Model", "model"),
            ("Year Range (e.g., 2015-2020)", "year_range"),
            ("Cluster Removal (Required/Not Required/Varies)", "cluster_removal"),
            ("BCM Location", "bcm_location"),
            ("Key FCC/Part Number", "key_type"),
            ("Programming Method", "programming_method"),
            ("Difficulty (Basic/Intermediate/Advanced/Expert)", "difficulty")
        ]

        self.entries = {}
        for label, key in fields:
            ctk.CTkLabel(scroll, text=label + ":", font=("Consolas", 11, "bold"),
                        text_color=CYBER_ACCENT).pack(anchor="w", padx=20, pady=(10, 5))
            entry = ctk.CTkEntry(scroll, width=700, height=35, font=("Consolas", 11))
            entry.pack(padx=20, pady=5)
            self.entries[key] = entry

        # Cluster Part Numbers
        ctk.CTkLabel(scroll, text="Locked Cluster Part Numbers (comma separated):",
                    font=("Consolas", 11, "bold"), text_color=CYBER_ACCENT).pack(anchor="w", padx=20, pady=(10, 5))
        self.clusters_text = ctk.CTkTextbox(scroll, width=700, height=80, font=("Consolas", 10))
        self.clusters_text.pack(padx=20, pady=5)

        # Xhorse Adapters
        ctk.CTkLabel(scroll, text="Required Xhorse Adapters (one per line):",
                    font=("Consolas", 11, "bold"), text_color=CYBER_ACCENT).pack(anchor="w", padx=20, pady=(10, 5))
        self.adapters_text = ctk.CTkTextbox(scroll, width=700, height=80, font=("Consolas", 10))
        self.adapters_text.pack(padx=20, pady=5)

        # Special Notes
        ctk.CTkLabel(scroll, text="Special Notes & Warnings:",
                    font=("Consolas", 11, "bold"), text_color=CYBER_ACCENT).pack(anchor="w", padx=20, pady=(10, 5))
        self.notes_text = ctk.CTkTextbox(scroll, width=700, height=100, font=("Consolas", 10))
        self.notes_text.pack(padx=20, pady=5)

        # Image attachment
        img_frame = ctk.CTkFrame(scroll, fg_color="#1a1a2e", corner_radius=10)
        img_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(img_frame, text="📷 Reference Image:", font=("Consolas", 11, "bold"),
                    text_color=CYBER_CYAN).pack(pady=10)
        
        self.image_preview = ctk.CTkLabel(img_frame, text="No Image", width=200, height=150,
                                          fg_color="#0a0a15", corner_radius=8)
        self.image_preview.pack(pady=10)
        
        ctk.CTkButton(img_frame, text="📁 Attach Image", width=150, height=35,
                     fg_color=CYBER_MAGENTA, command=self.attach_image).pack(pady=10)

        # Save button
        ctk.CTkButton(scroll, text="💾 SAVE ENTRY", width=300, height=50,
                     fg_color=CYBER_GREEN, text_color="#000", font=("Consolas", 14, "bold"),
                     command=self.save_entry).pack(pady=30)

    def attach_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Reference Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All Files", "*.*")]
        )
        
        if file_path:
            self.current_image = file_path
            try:
                img = Image.open(file_path)
                img.thumbnail((200, 150))
                photo = ImageTk.PhotoImage(img)
                self.image_preview.configure(image=photo, text="")
                self.image_preview.image = photo
            except Exception as e:
                messagebox.showerror("Image Error", f"Could not load image:\n{e}")

    def save_entry(self):
        # Validate required fields
        make = self.entries["make"].get().strip()
        model = self.entries["model"].get().strip()
        year_range = self.entries["year_range"].get().strip()
        
        if not all([make, model, year_range]):
            messagebox.showwarning("Missing Data", "Please fill in Make, Model, and Year Range")
            return
        
        # Parse clusters
        clusters_raw = self.clusters_text.get("1.0", "end").strip()
        clusters = [c.strip() for c in clusters_raw.split(",") if c.strip()] if clusters_raw else []
        
        # Parse adapters
        adapters_raw = self.adapters_text.get("1.0", "end").strip()
        adapters = [a.strip() for a in adapters_raw.split("\n") if a.strip()] if adapters_raw else []
        
        # Build entry
        entry_data = {
            "clusters": clusters,
            "cluster_removal": self.entries["cluster_removal"].get().strip(),
            "bcm_location": self.entries["bcm_location"].get().strip(),
            "special_notes": self.notes_text.get("1.0", "end").strip(),
            "xhorse_adapters": adapters,
            "key_type": self.entries["key_type"].get().strip(),
            "programming_method": self.entries["programming_method"].get().strip(),
            "difficulty": self.entries["difficulty"].get().strip()
        }
        
        # Add to database
        if make not in self.parent.db:
            self.parent.db[make] = {}
        if model not in self.parent.db[make]:
            self.parent.db[make][model] = {}
        
        self.parent.db[make][model][year_range] = entry_data
        self.parent.save_db()
        
        # Save image if attached
        if self.current_image:
            try:
                img_key = f"{make}_{model}_{year_range}".replace(" ", "_").replace("/", "-")
                dest_path = f"{self.parent.images_dir}/{img_key}.jpg"
                img = Image.open(self.current_image)
                if img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                img.thumbnail((1920, 1920), Image.Resampling.LANCZOS)
                img.save(dest_path, "JPEG", quality=85)
            except Exception as e:
                messagebox.showwarning("Image Error", f"Could not save image:\n{e}")
        
        messagebox.showinfo("Success", f"Added {make} {model} ({year_range}) to database!")
        self.destroy()


# =======================
# Main Entry Point
# =======================
if __name__ == "__main__":
    import subprocess
    import sys
    
    required = ["customtkinter", "Pillow"]
    missing = []
    
    for pkg in required:
        try:
            __import__(pkg.replace("-", "_"))
        except ImportError:
            missing.append(pkg)
    
    if missing:
        print(f"Installing missing packages: {missing}")
        for pkg in missing:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
    
    app = LuxuryClusterGuide()
    app.mainloop()
