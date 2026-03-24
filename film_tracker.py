#!/usr/bin/env python3
"""
Film Tracker - Profesionální aplikace pro sledování filmů
Verze: 1.0.0
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import datetime

# ── Barevné schéma ───────────────────────────────────────────────────────────
BG_DARK      = "#2e1a1a"   # hlavní pozadí
BG_SIDEBAR   = "#3e1616"   # postranní panel
BG_CARD      = "#600f0f"   # karta / panel
BG_TABLE     = "#3a1e1e"   # tabulka
BG_ROW_ODD   = "#452525"
BG_ROW_EVEN  = "#3a1e1e"
BG_ROW_SEL   = "#600f0f"

ACCENT_GREEN  = "#4ecca3"   # primární akcent (zelená)
ACCENT_GREEN2 = "#3aaa87"   # tmavší zelená pro hover
ACCENT_WINE   = "#833353"   # sekundární akcent
ACCENT_RED    = "#e94560"   # nebezpečná akce
ACCENT_YELLOW = "#f5a623"   # upozornění / hodnocení

FG_PRIMARY   = "#eaeaea"
FG_SECONDARY = "#c0a0a0"
FG_DISABLED  = "#806060"
FG_BUTTON    = "#000000"

FONT_TITLE   = ("Segoe UI", 18, "bold")
FONT_HEADING = ("Segoe UI", 11, "bold")
FONT_NORMAL  = ("Segoe UI", 10)
FONT_SMALL   = ("Segoe UI", 9)
FONT_MONO    = ("Consolas", 9)

# ── Vzorová data ──────────────────────────────────────────────────────────────
SAMPLE_FILMS = [
    {"id": 1,  "nazev": "Inception",               "rok": 2010, "zanr": "Sci-Fi / Thriller",    "hodnoceni": 9.2, "delka": 148, "reziser": "Christopher Nolan",  "popis": "Zloděj, který krade firemní tajemství pomocí technologie sdílení snů, dostane inverz… zasadit myšlenku do mysli cíle.", "sledovano": True,  "oblibene": True,  "watchlist": False},
    {"id": 2,  "nazev": "The Dark Knight",          "rok": 2008, "zanr": "Akční / Drama",         "hodnoceni": 9.0, "delka": 152, "reziser": "Christopher Nolan",  "popis": "Batman, komisař Gordon a státní zástupce Harvey Dent musí spolupracovat, aby zničili organizovaný zločin v Gothamu.", "sledovano": True,  "oblibene": True,  "watchlist": False},
    {"id": 3,  "nazev": "Interstellar",             "rok": 2014, "zanr": "Sci-Fi / Drama",        "hodnoceni": 8.7, "delka": 169, "reziser": "Christopher Nolan",  "popis": "Tým průzkumníků cestuje skrze červí díru ve vesmíru, aby zajistil přežití lidstva.", "sledovano": True,  "oblibene": True,  "watchlist": False},
    {"id": 4,  "nazev": "Pulp Fiction",             "rok": 1994, "zanr": "Krimi / Drama",         "hodnoceni": 8.9, "delka": 154, "reziser": "Quentin Tarantino", "popis": "Životy dvou gangsterů, boxera, manželky gangstera a dvojice lupičů se proplétají ve čtyřech příbězích násilí a vykoupení.", "sledovano": True,  "oblibene": False, "watchlist": False},
    {"id": 5,  "nazev": "The Matrix",               "rok": 1999, "zanr": "Sci-Fi / Akční",        "hodnoceni": 8.7, "delka": 136, "reziser": "Wachowski Sisters","popis": "Programátor zjišťuje, že realita, ve které žije, je simulace vytvořená strojní inteligencí.", "sledovano": True,  "oblibene": True,  "watchlist": False},
    {"id": 6,  "nazev": "Fight Club",               "rok": 1999, "zanr": "Drama / Thriller",      "hodnoceni": 8.8, "delka": 139, "reziser": "David Fincher",     "popis": "Nespokojenec a výřečný prodavač mýdla zakládají podzemní bojový klub, který se změní v něco mnohem temnějšího.", "sledovano": True,  "oblibene": False, "watchlist": False},
    {"id": 7,  "nazev": "Forrest Gump",             "rok": 1994, "zanr": "Drama / Romantika",     "hodnoceni": 8.8, "delka": 142, "reziser": "Robert Zemeckis",   "popis": "Příběh muže s nízkým IQ, jehož život zasahuje do klíčových historických událostí 20. století.", "sledovano": False, "oblibene": True,  "watchlist": True},
    {"id": 8,  "nazev": "The Shawshank Redemption", "rok": 1994, "zanr": "Drama / Krimi",         "hodnoceni": 9.3, "delka": 142, "reziser": "Frank Darabont",    "popis": "Dva uvěznění muži si vybudují přátelství a najdou naději ve věznici Shawshank.", "sledovano": False, "oblibene": True,  "watchlist": True},
    {"id": 9,  "nazev": "Goodfellas",               "rok": 1990, "zanr": "Krimi / Drama",         "hodnoceni": 8.7, "delka": 146, "reziser": "Martin Scorsese",   "popis": "Příběh Henryho Hilla a jeho vzestupu a pádu v newyorské mafii.", "sledovano": True,  "oblibene": False, "watchlist": False},
    {"id": 10, "nazev": "Schindler's List",         "rok": 1993, "zanr": "Drama / Historie",      "hodnoceni": 9.0, "delka": 195, "reziser": "Steven Spielberg",  "popis": "Příběh Oskara Schindlera, který zachránil životy více než tisíce polských Židů během holocaustu.", "sledovano": False, "oblibene": False, "watchlist": True},
    {"id": 11, "nazev": "The Godfather",            "rok": 1972, "zanr": "Krimi / Drama",         "hodnoceni": 9.2, "delka": 175, "reziser": "Francis F. Coppola","popis": "Stárnoucí patriarcha organizovaného zločinného klanu přenáší kontrolu nad svým říší na svého neochotného syna.", "sledovano": True,  "oblibene": True,  "watchlist": False},
    {"id": 12, "nazev": "Avengers: Endgame",        "rok": 2019, "zanr": "Akční / Sci-Fi",        "hodnoceni": 8.4, "delka": 181, "reziser": "Russo Brothers",    "popis": "Po ničivých událostech se Avengers znovu shromáždí, aby zvrátili činy Thanose a obnovili řád ve vesmíru.", "sledovano": True,  "oblibene": False, "watchlist": False},
    {"id": 13, "nazev": "Parasite",                 "rok": 2019, "zanr": "Thriller / Drama",      "hodnoceni": 8.6, "delka": 132, "reziser": "Bong Joon-ho",      "popis": "Chudá rodina se infiltruje do bohatého domácího prostředí a jejich plán má nečekané důsledky.", "sledovano": False, "oblibene": False, "watchlist": True},
    {"id": 14, "nazev": "Blade Runner 2049",        "rok": 2017, "zanr": "Sci-Fi / Noir",         "hodnoceni": 8.0, "delka": 164, "reziser": "Denis Villeneuve",  "popis": "Nový blade runner odkrývá tajemství, které by mohlo uvěznit společnost do chaosu.", "sledovano": True,  "oblibene": True,  "watchlist": False},
    {"id": 15, "nazev": "Dune",                     "rok": 2021, "zanr": "Sci-Fi / Dobrodružství","hodnoceni": 8.0, "delka": 155, "reziser": "Denis Villeneuve",  "popis": "Paul Atreides, génius, je na cestě k vesmírné planetě Arrakis a jejímu vzácnému koření.", "sledovano": False, "oblibene": False, "watchlist": True},
    {"id": 16, "nazev": "1917",                     "rok": 2019, "zanr": "Válečný / Drama",       "hodnoceni": 8.3, "delka": 119, "reziser": "Sam Mendes",        "popis": "Dva britští vojáci dostanou zdánlivě nemožný rozkaz – doručit zprávu, která může zachránit 1600 mužů.", "sledovano": True,  "oblibene": False, "watchlist": False},
    {"id": 17, "nazev": "Joker",                    "rok": 2019, "zanr": "Drama / Thriller",      "hodnoceni": 8.4, "delka": 122, "reziser": "Todd Phillips",     "popis": "Arthur Fleck, muž bojující s duševní nemocí, se transformuje v ikonického Jokera.", "sledovano": True,  "oblibene": False, "watchlist": False},
    {"id": 18, "nazev": "Spider-Man: No Way Home",  "rok": 2021, "zanr": "Akční / Sci-Fi",        "hodnoceni": 8.2, "delka": 148, "reziser": "Jon Watts",         "popis": "Peter Parker žádá Doctora Stranga o kouzlo, které změní jeho osud – s nebezpečnými důsledky.", "sledovano": False, "oblibene": False, "watchlist": True},
    {"id": 19, "nazev": "The Revenant",             "rok": 2015, "zanr": "Dobrodružství / Drama",  "hodnoceni": 8.0, "delka": 156, "reziser": "Alejandro G. Iñárritu","popis": "Lovec přežije útok medvěda a vydá se na cestu pomsty za smrt svého syna.", "sledovano": True,  "oblibene": False, "watchlist": False},
    {"id": 20, "nazev": "Mad Max: Fury Road",       "rok": 2015, "zanr": "Akční / Sci-Fi",        "hodnoceni": 8.1, "delka": 120, "reziser": "George Miller",     "popis": "V post-apokalyptické pustině se Max spojí s rebelskou Furiosa, aby utekl před tyranem.", "sledovano": False, "oblibene": True,  "watchlist": False},
]

# Přidáme dalších 132 filmů pro celkový počet 152
EXTRA_NAMES = [
    "Bohemian Rhapsody", "La La Land", "Whiplash", "The Social Network",
    "Gone Girl", "Arrival", "Hereditary", "Midsommar", "Get Out", "Us",
    "Once Upon a Time in Hollywood", "Knives Out", "The Irishman",
    "Marriage Story", "Little Women", "Portrait of a Lady on Fire",
    "Uncut Gems", "The Lighthouse", "Tenet", "Soul",
    "Nomadland", "Minari", "Sound of Metal", "The Father", "Judas and the Black Messiah",
    "News of the World", "Promising Young Woman", "Mank", "The Trial of the Chicago 7",
    "One Night in Miami", "Ma Rainey's Black Bottom", "Wolfwalkers",
    "CODA", "The Power of the Dog", "No Time to Die", "Shang-Chi",
    "Eternals", "Black Widow", "Luca", "The Suicide Squad",
    "Titane", "Memoria", "The Worst Person in the World",
    "Drive My Car", "Parallel Mothers", "Petite Maman",
    "After Love", "Flee", "Encounter", "Mass",
    "The Tender Bar", "Being the Ricardos", "House of Gucci",
    "Licorice Pizza", "C'mon C'mon", "King Richard",
    "tick, tick... BOOM!", "Encanto", "The Mitchells vs the Machines",
    "Raya and the Last Dragon", "Jungle Cruise", "Black Widow",
    "Snake Eyes", "F9", "Space Jam: A New Legacy",
    "The Suicide Squad", "Mortal Kombat", "Army of the Dead",
    "Zack Snyder's Justice League", "Godzilla vs. Kong",
    "The Conjuring: The Devil Made Me Do It", "A Quiet Place Part II",
    "Coming 2 America", "Without Remorse", "The Tomorrow War",
    "Gunpowder Milkshake", "The Dig", "Malcolm & Marie",
    "The Harder They Fall", "The Guilty", "Sweet Girl",
    "Thunder Force", "Thunder Force 2", "Army of Thieves",
    "Red Notice", "The Starling", "The Midnight Sky",
    "Outside the Wire", "The White Tiger", "Pieces of a Woman",
    "Finding 'Ohana", "To All the Boys: Always and Forever",
    "Yes Day", "The Mitchells vs. the Machines", "Fear Street Part One: 1994",
    "Fear Street Part Two: 1978", "Fear Street Part Three: 1666",
    "Oxygen", "The Wasteland", "Stowaway",
    "Those Who Wish Me Dead", "Wrath of Man", "Mortal Kombat",
    "Riders of Justice", "Violation", "Land",
    "The Dig", "News of the World", "Penguin Bloom",
    "The Marksman", "Outside the Wire", "Locked Down",
    "Synchronic", "The Empty Man", "Possessor",
    "The Night House", "Saint Maud", "I'm Thinking of Ending Things",
    "The Platform", "His House", "Underwater",
    "Color Out of Space", "Doctor Sleep", "Midsommar",
    "The Lighthouse", "Cats", "Little Women",
    "Marriage Story", "Ford v Ferrari", "Richard Jewell",
    "Judy", "Jojo Rabbit", "Knives Out",
    "Parasite", "Joker", "Once Upon a Time in Hollywood",
    "The Farewell", "Us", "Avengers: Endgame",
    "Spider-Man: Far from Home", "John Wick: Chapter 3",
    "Rocketman", "Booksmart", "Long Shot",
]

GENRES = [
    "Akční", "Drama", "Komedie", "Sci-Fi", "Thriller", "Horor",
    "Romantika", "Dobrodružství", "Animace", "Dokumentární",
    "Krimi", "Historie", "Muzikál", "Rodinný", "Mysteriózní",
]

for i, name in enumerate(EXTRA_NAMES[:132], start=21):
    SAMPLE_FILMS.append({
        "id": i,
        "nazev": name,
        "rok": random.randint(1990, 2023),
        "zanr": random.choice(GENRES),
        "hodnoceni": round(random.uniform(6.0, 9.5), 1),
        "delka": random.randint(80, 200),
        "reziser": "Různí",
        "popis": "Popis tohoto filmu zatím nebyl přidán.",
        "sledovano": random.choice([True, False]),
        "oblibene": random.choice([True, False]),
        "watchlist": random.choice([True, False]),
    })


# ── Pomocné widgety ───────────────────────────────────────────────────────────

def make_button(parent, text, command=None, color=ACCENT_GREEN, fg=FG_BUTTON,
                width=None, padx=12, pady=6, font=FONT_NORMAL):
    """Vytvoří stylizované tlačítko s hover efektem."""
    btn = tk.Button(
        parent, text=text, command=command,
        bg=color, fg=fg, activebackground=ACCENT_GREEN2, activeforeground=fg,
        relief="flat", cursor="hand2", font=font,
        padx=padx, pady=pady, bd=0,
    )
    if width:
        btn.config(width=width)
    btn.bind("<Enter>", lambda e: btn.config(bg=ACCENT_GREEN2))
    btn.bind("<Leave>", lambda e: btn.config(bg=color))
    return btn


def make_label(parent, text, font=FONT_NORMAL, fg=FG_PRIMARY, bg=None, **kw):
    return tk.Label(parent, text=text, font=font, fg=fg,
                    bg=bg or BG_DARK, **kw)


def separator(parent, bg=BG_CARD, height=1, pady=4):
    f = tk.Frame(parent, bg=bg, height=height)
    f.pack(fill="x", pady=pady)
    return f


# ── Dialogy ───────────────────────────────────────────────────────────────────

class FilmDialog(tk.Toplevel):
    """Modální dialog pro přidání nebo úpravu filmu."""

    def __init__(self, parent, film=None, on_save=None, films=None):
        super().__init__(parent)
        self.on_save = on_save
        self.result = None
        self._original = film
        self._all_films = films or SAMPLE_FILMS

        title_text = "Upravit film" if film else "Přidat nový film"
        self.title(title_text)
        self.resizable(False, False)
        self.configure(bg=BG_DARK)
        self.grab_set()

        self._build(film or {})
        self.transient(parent)
        self.update_idletasks()
        # Vystředit na rodiče
        px = parent.winfo_rootx() + (parent.winfo_width() - self.winfo_width()) // 2
        py = parent.winfo_rooty() + (parent.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{px}+{py}")

    # ── Layout ──
    def _build(self, film):
        # Záhlaví
        header = tk.Frame(self, bg=BG_CARD, pady=12)
        header.pack(fill="x")
        icon = "✏️" if self._original else "🎬"
        title_text = f"{icon}  {'Upravit film' if self._original else 'Přidat nový film'}"
        make_label(header, title_text, font=FONT_TITLE, bg=BG_CARD).pack(padx=20)

        # Formulář
        form = tk.Frame(self, bg=BG_DARK, padx=24, pady=16)
        form.pack(fill="both", expand=True)

        self._vars = {}

        fields = [
            ("Název filmu *",         "nazev",      "entry",    None),
            ("Rok vydání",            "rok",         "entry",    None),
            ("Žánr",                  "zanr",        "combo",    GENRES),
            ("Hodnocení (0–10)",      "hodnoceni",   "entry",    None),
            ("Délka (minuty)",        "delka",       "entry",    None),
            ("Režisér",               "reziser",     "entry",    None),
            ("Popis",                 "popis",       "text",     None),
        ]

        for row_idx, (label_text, key, widget_type, options) in enumerate(fields):
            lbl = make_label(form, label_text, fg=ACCENT_GREEN, font=FONT_SMALL)
            lbl.grid(row=row_idx * 2, column=0, sticky="w", pady=(8, 1))

            if widget_type == "entry":
                var = tk.StringVar(value=str(film.get(key, "")))
                self._vars[key] = var
                e = tk.Entry(form, textvariable=var, bg=BG_CARD, fg=FG_PRIMARY,
                             insertbackground=FG_PRIMARY, relief="flat",
                             font=FONT_NORMAL, width=40)
                e.grid(row=row_idx * 2 + 1, column=0, sticky="ew", ipady=6)

            elif widget_type == "combo":
                var = tk.StringVar(value=str(film.get(key, "")))
                self._vars[key] = var
                cb = ttk.Combobox(form, textvariable=var, values=options,
                                  font=FONT_NORMAL, width=38)
                cb.grid(row=row_idx * 2 + 1, column=0, sticky="ew")

            elif widget_type == "text":
                self._vars[key] = None  # zpracujeme zvlášť
                frame = tk.Frame(form, bg=BG_CARD)
                frame.grid(row=row_idx * 2 + 1, column=0, sticky="ew")
                self._text_popis = tk.Text(frame, height=5, bg=BG_CARD,
                                           fg=FG_PRIMARY, insertbackground=FG_PRIMARY,
                                           relief="flat", font=FONT_NORMAL, width=40,
                                           wrap="word")
                self._text_popis.pack(fill="x")
                self._text_popis.insert("1.0", film.get("popis", ""))

        # Checkboxy
        self._var_sledovano = tk.BooleanVar(value=film.get("sledovano", False))
        self._var_oblibene  = tk.BooleanVar(value=film.get("oblibene", False))
        self._var_watchlist = tk.BooleanVar(value=film.get("watchlist", False))

        checks = tk.Frame(form, bg=BG_DARK)
        checks.grid(row=len(fields) * 2, column=0, sticky="w", pady=(12, 0))

        for text, var in [("✓ Sledováno", self._var_sledovano),
                          ("♥ Oblíbené",  self._var_oblibene),
                          ("⊕ Watchlist", self._var_watchlist)]:
            cb = tk.Checkbutton(checks, text=text, variable=var,
                                bg=BG_DARK, fg=FG_PRIMARY, selectcolor=BG_CARD,
                                activebackground=BG_DARK, activeforeground=ACCENT_GREEN,
                                font=FONT_NORMAL, cursor="hand2")
            cb.pack(side="left", padx=(0, 16))

        form.columnconfigure(0, weight=1)

        # Tlačítka
        btn_frame = tk.Frame(self, bg=BG_DARK, padx=24, pady=12)
        btn_frame.pack(fill="x")

        make_button(btn_frame, "💾  Uložit",   command=self._save,   color=ACCENT_GREEN).pack(side="left", padx=(0, 8))
        make_button(btn_frame, "✗  Zrušit",    command=self.destroy, color=ACCENT_RED,  fg=FG_PRIMARY).pack(side="left")

    def _save(self):
        data = {}
        for key, var in self._vars.items():
            if var is not None:
                data[key] = var.get().strip()
            else:
                data[key] = self._text_popis.get("1.0", "end-1c").strip()

        if not data.get("nazev"):
            messagebox.showerror("Chyba", "Název filmu je povinný!", parent=self)
            return

        # Konverze typů
        try:
            data["rok"]        = int(data["rok"]) if data["rok"] else datetime.date.today().year
            data["hodnoceni"]  = float(data["hodnoceni"].replace(",", ".")) if data["hodnoceni"] else 0.0
            data["delka"]      = int(data["delka"]) if data["delka"] else 0
        except ValueError as e:
            messagebox.showerror("Chyba", f"Neplatná hodnota: {e}", parent=self)
            return

        data["sledovano"] = self._var_sledovano.get()
        data["oblibene"]  = self._var_oblibene.get()
        data["watchlist"] = self._var_watchlist.get()

        if self._original:
            data["id"] = self._original["id"]
        else:
            data["id"] = max((f["id"] for f in self._all_films), default=0) + 1

        self.result = data
        if self.on_save:
            self.on_save(data)
        self.destroy()


class AboutDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("O aplikaci")
        self.configure(bg=BG_DARK)
        self.resizable(False, False)
        self.grab_set()

        make_label(self, "🎬 Film Tracker", font=FONT_TITLE).pack(pady=(24, 4))
        make_label(self, "Verze 1.0.0", fg=FG_SECONDARY).pack()
        make_label(self, "Profesionální aplikace pro sledování filmů",
                   fg=FG_SECONDARY).pack(pady=(8, 4))
        separator(self, bg=BG_CARD)
        make_label(self, "Klávesové zkratky:", font=FONT_HEADING, fg=ACCENT_GREEN).pack(pady=(8, 4))
        shortcuts = [
            ("Ctrl+N", "Nový film"),
            ("Ctrl+F", "Vyhledat"),
            ("Ctrl+Q", "Ukončit"),
            ("Delete",  "Smazat vybraný film"),
            ("F5",      "Obnovit tabulku"),
            ("Enter",   "Detail vybraného filmu"),
        ]
        for key, desc in shortcuts:
            row = tk.Frame(self, bg=BG_DARK)
            row.pack(fill="x", padx=32, pady=1)
            make_label(row, key, font=FONT_MONO, fg=ACCENT_GREEN,
                       bg=BG_CARD, padx=6, pady=2).pack(side="left")
            make_label(row, f"  {desc}", fg=FG_PRIMARY).pack(side="left")

        make_button(self, "Zavřít", command=self.destroy).pack(pady=20)
        self.transient(parent)
        self.update_idletasks()
        px = parent.winfo_rootx() + (parent.winfo_width() - self.winfo_width()) // 2
        py = parent.winfo_rooty() + (parent.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{px}+{py}")


class StatisticsDialog(tk.Toplevel):
    def __init__(self, parent, films):
        super().__init__(parent)
        self.title("Statistiky")
        self.configure(bg=BG_DARK)
        self.grab_set()
        self.resizable(True, True)
        self.geometry("600x500")

        self._build(films)
        self.transient(parent)

    def _build(self, films):
        make_label(self, "📊 Statistiky", font=FONT_TITLE).pack(pady=(20, 12))

        total     = len(films)
        watched   = 0
        favs      = 0
        watchlist = 0
        sum_rat   = 0.0
        sum_len   = 0
        for f in films:
            if f.get("sledovano"):  watched += 1
            if f.get("oblibene"):   favs += 1
            if f.get("watchlist"):  watchlist += 1
            sum_rat += f["hodnoceni"]
            sum_len += f["delka"]
        avg_rat   = sum_rat / total if total else 0
        avg_len   = sum_len / total if total else 0
        total_min = sum_len

        stats = [
            ("Celkem filmů",         str(total)),
            ("Sledováno",            f"{watched} ({watched/total*100:.0f} %)" if total else "0"),
            ("Oblíbené",             str(favs)),
            ("Watchlist",            str(watchlist)),
            ("Průměrné hodnocení",   f"{avg_rat:.2f} / 10"),
            ("Průměrná délka",       f"{avg_len:.0f} min"),
            ("Celkový čas sledování",f"{total_min // 60} h {total_min % 60} min"),
        ]

        frame = tk.Frame(self, bg=BG_CARD, padx=24, pady=16)
        frame.pack(fill="x", padx=24)

        for i, (label, value) in enumerate(stats):
            r = tk.Frame(frame, bg=BG_CARD if i % 2 == 0 else BG_TABLE)
            r.pack(fill="x", pady=1)
            make_label(r, label, fg=FG_SECONDARY, bg=r["bg"]).pack(side="left", padx=8, pady=4)
            make_label(r, value, fg=ACCENT_GREEN,  bg=r["bg"], font=FONT_HEADING).pack(side="right", padx=8, pady=4)

        # Top 5 filmů
        make_label(self, "🏆 Top 5 filmů dle hodnocení",
                   font=FONT_HEADING, fg=ACCENT_GREEN).pack(pady=(16, 4))

        top5_frame = tk.Frame(self, bg=BG_CARD, padx=16, pady=8)
        top5_frame.pack(fill="x", padx=24)

        top5 = sorted(films, key=lambda f: f["hodnoceni"], reverse=True)[:5]
        for i, f in enumerate(top5, 1):
            row = tk.Frame(top5_frame, bg=BG_CARD)
            row.pack(fill="x", pady=2)
            make_label(row, f"{i}. {f['nazev']}", bg=BG_CARD).pack(side="left", padx=4)
            stars = "★" * int(f["hodnoceni"] / 2) + "☆" * (5 - int(f["hodnoceni"] / 2))
            make_label(row, f"{f['hodnoceni']}  {stars}",
                       fg=ACCENT_YELLOW, bg=BG_CARD, font=FONT_HEADING).pack(side="right", padx=4)

        make_button(self, "Zavřít", command=self.destroy).pack(pady=20)


# ── Hlavní okno ───────────────────────────────────────────────────────────────

class FilmTrackerApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("🎬 Film Tracker")
        self.geometry("1400x800")
        self.minsize(1100, 650)
        self.configure(bg=BG_DARK)

        self._films = list(SAMPLE_FILMS)
        self._filtered = list(self._films)
        self._active_section = "moje"
        self._detail_film = None

        # Stav pro přizpůsobení zobrazení
        self._font_size = tk.IntVar(value=10)
        self._show_details = tk.BooleanVar(value=True)

        self._apply_ttk_style()
        self._build_menu()
        self._build_layout()
        self._bind_shortcuts()
        # Select initial section after full layout is built
        self._select_section("moje")
        self._refresh_table()
        self._update_status()

    # ── Styl ──────────────────────────────────────────────────────────────────

    def _apply_ttk_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview",
                        background=BG_TABLE, fieldbackground=BG_TABLE,
                        foreground=FG_PRIMARY, rowheight=28,
                        borderwidth=0, font=FONT_NORMAL)
        style.configure("Treeview.Heading",
                        background=BG_CARD, foreground=ACCENT_GREEN,
                        font=FONT_HEADING, relief="flat")
        style.map("Treeview",
                  background=[("selected", BG_ROW_SEL)],
                  foreground=[("selected", FG_PRIMARY)])
        style.configure("TCombobox",
                        fieldbackground=BG_CARD, background=BG_CARD,
                        foreground=FG_PRIMARY, selectbackground=BG_ROW_SEL)

    # ── Hlavní menu ───────────────────────────────────────────────────────────

    def _build_menu(self):
        menubar = tk.Menu(self, bg=BG_DARK, fg=FG_PRIMARY,
                          activebackground=BG_CARD, activeforeground=ACCENT_GREEN,
                          relief="flat", bd=0)

        # Soubor
        file_menu = tk.Menu(menubar, tearoff=0, bg=BG_DARK, fg=FG_PRIMARY,
                            activebackground=BG_CARD, activeforeground=ACCENT_GREEN)
        file_menu.add_command(label="➕  Přidat film",   command=self._open_add_dialog,
                              accelerator="Ctrl+N")
        file_menu.add_command(label="📥  Importovat...", command=self._placeholder("Import dat"))
        file_menu.add_command(label="📤  Exportovat...", command=self._placeholder("Export dat"))
        file_menu.add_separator()
        file_menu.add_command(label="⚙️  Nastavení",    command=self._open_settings)
        file_menu.add_separator()
        file_menu.add_command(label="🚪  Ukončit",       command=self.quit,
                              accelerator="Ctrl+Q")
        menubar.add_cascade(label="Soubor", menu=file_menu)

        # Zobrazení
        view_menu = tk.Menu(menubar, tearoff=0, bg=BG_DARK, fg=FG_PRIMARY,
                            activebackground=BG_CARD, activeforeground=ACCENT_GREEN)
        view_menu.add_checkbutton(label="Zobrazit detail",
                                  variable=self._show_details,
                                  command=self._toggle_details)
        view_menu.add_separator()
        view_menu.add_command(label="Zvětšit písmo",  command=self._increase_font,
                              accelerator="Ctrl++")
        view_menu.add_command(label="Zmenšit písmo",  command=self._decrease_font,
                              accelerator="Ctrl+-")
        view_menu.add_command(label="Výchozí písmo",  command=self._reset_font)
        menubar.add_cascade(label="Zobrazení", menu=view_menu)

        # Filmy
        films_menu = tk.Menu(menubar, tearoff=0, bg=BG_DARK, fg=FG_PRIMARY,
                             activebackground=BG_CARD, activeforeground=ACCENT_GREEN)
        films_menu.add_command(label="🔍  Vyhledat",      command=self._focus_search,
                               accelerator="Ctrl+F")
        films_menu.add_command(label="🗑️  Smazat vybraný", command=self._delete_selected,
                               accelerator="Delete")
        films_menu.add_command(label="✏️  Upravit",        command=self._open_edit_dialog,
                               accelerator="F2")
        films_menu.add_separator()
        films_menu.add_command(label="⭐ Přidat do oblíbených", command=self._toggle_favorite)
        films_menu.add_command(label="📋  Přidat na watchlist",  command=self._toggle_watchlist)
        menubar.add_cascade(label="Filmy", menu=films_menu)

        # Nápověda
        help_menu = tk.Menu(menubar, tearoff=0, bg=BG_DARK, fg=FG_PRIMARY,
                            activebackground=BG_CARD, activeforeground=ACCENT_GREEN)
        help_menu.add_command(label="📊  Statistiky",  command=self._open_statistics)
        help_menu.add_separator()
        help_menu.add_command(label="ℹ️  O aplikaci", command=lambda: AboutDialog(self))
        menubar.add_cascade(label="Nápověda", menu=help_menu)

        self.config(menu=menubar)

    # ── Rozložení ─────────────────────────────────────────────────────────────

    def _build_layout(self):
        # Horní lišta
        self._build_topbar()
        # Hlavní kontejner (sidebar + obsah)
        main = tk.Frame(self, bg=BG_DARK)
        main.pack(fill="both", expand=True)
        # PanedWindow před sidebarem, abychom měli paned dříve
        self._paned = tk.PanedWindow(main, orient="horizontal",
                                     bg=BG_DARK, sashwidth=6,
                                     sashrelief="flat", sashpad=2)
        # Nejprve sestavíme obsah (filtry), pak sidebar (který volá _apply_filters)
        self._build_content()
        self._build_detail_panel()
        self._build_sidebar(main)
        self._paned.pack(side="left", fill="both", expand=True, padx=(0, 0))
        # Stavový řádek
        self._build_statusbar()

    # ── Horní lišta ──────────────────────────────────────────────────────────

    def _build_topbar(self):
        bar = tk.Frame(self, bg=BG_CARD, height=52)
        bar.pack(fill="x")
        bar.pack_propagate(False)

        # Logo
        make_label(bar, "🎬 Film Tracker", font=("Segoe UI", 14, "bold"),
                   fg=ACCENT_GREEN, bg=BG_CARD).pack(side="left", padx=(16, 24))

        # Vyhledávání
        search_frame = tk.Frame(bar, bg=BG_TABLE, padx=2, pady=2)
        search_frame.pack(side="left", padx=8)
        make_label(search_frame, "🔍", bg=BG_TABLE, fg=FG_SECONDARY).pack(side="left", padx=(6, 2))
        self._search_var = tk.StringVar()
        self._search_var.trace_add("write", lambda *_: self._apply_filters())
        self._search_entry = tk.Entry(
            search_frame, textvariable=self._search_var,
            bg=BG_TABLE, fg=FG_PRIMARY, insertbackground=FG_PRIMARY,
            relief="flat", font=FONT_NORMAL, width=30,
        )
        self._search_entry.pack(side="left", ipady=6, padx=(0, 8))
        self._search_entry.insert(0, "Hledat filmy...")
        self._search_entry.config(fg=FG_DISABLED)
        self._search_entry.bind("<FocusIn>",  self._search_focus_in)
        self._search_entry.bind("<FocusOut>", self._search_focus_out)

        # Tlačítka vpravo
        btn_frame = tk.Frame(bar, bg=BG_CARD)
        btn_frame.pack(side="right", padx=16)

        make_button(btn_frame, "+ Přidat film", command=self._open_add_dialog,
                    padx=16, pady=8).pack(side="left", padx=4)
        make_button(btn_frame, "👤 Profil",
                    command=self._placeholder("Profil uživatele"),
                    color=BG_TABLE, fg=FG_PRIMARY, padx=12, pady=8).pack(side="left", padx=4)
        make_button(btn_frame, "📊 Statistiky",
                    command=self._open_statistics,
                    color=ACCENT_WINE, fg=FG_PRIMARY, padx=12, pady=8).pack(side="left", padx=4)

    def _search_focus_in(self, event):
        if self._search_entry.get() == "Hledat filmy...":
            self._search_entry.delete(0, "end")
            self._search_entry.config(fg=FG_PRIMARY)

    def _search_focus_out(self, event):
        if not self._search_entry.get():
            self._search_entry.insert(0, "Hledat filmy...")
            self._search_entry.config(fg=FG_DISABLED)

    # ── Postranní menu ────────────────────────────────────────────────────────

    def _build_sidebar(self, parent):
        sidebar = tk.Frame(parent, bg=BG_SIDEBAR, width=200)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        make_label(sidebar, "MENU", font=("Segoe UI", 8, "bold"),
                   fg=FG_DISABLED, bg=BG_SIDEBAR).pack(anchor="w", padx=16, pady=(16, 4))

        sections = [
            ("🏠", "Dashboard",  "dashboard"),
            ("🎬", "Moje filmy", "moje"),
            ("📋", "Watchlist",  "watchlist"),
            ("❤️",  "Oblíbené",  "oblibene"),
            ("📊", "Statistiky", "statistiky"),
            ("⚙️",  "Nastavení",  "nastaveni"),
        ]
        self._sidebar_buttons = {}

        for icon, label, key in sections:
            btn = tk.Button(
                sidebar, text=f"  {icon}  {label}",
                command=lambda k=key: self._select_section(k),
                bg=BG_SIDEBAR, fg=FG_PRIMARY,
                activebackground=BG_CARD, activeforeground=ACCENT_GREEN,
                relief="flat", anchor="w", font=FONT_NORMAL,
                padx=8, pady=10, cursor="hand2",
            )
            btn.pack(fill="x", padx=8, pady=1)
            self._sidebar_buttons[key] = btn

        separator(sidebar, bg=BG_CARD, pady=8)

        make_label(sidebar, "FILTROVAT", font=("Segoe UI", 8, "bold"),
                   fg=FG_DISABLED, bg=BG_SIDEBAR).pack(anchor="w", padx=16, pady=(0, 4))

        filter_options = [("Vše", None), ("Sledováno", "sledovano"),
                          ("Nesledováno", "nesledovano")]
        self._filter_watched = tk.StringVar(value="Vše")
        for text, val in filter_options:
            rb = tk.Radiobutton(
                sidebar, text=f"  {text}",
                variable=self._filter_watched, value=text,
                command=self._apply_filters,
                bg=BG_SIDEBAR, fg=FG_SECONDARY,
                activebackground=BG_CARD, activeforeground=ACCENT_GREEN,
                selectcolor=BG_CARD, relief="flat",
                font=FONT_SMALL, cursor="hand2",
            )
            rb.pack(anchor="w", padx=16)

        separator(sidebar, bg=BG_CARD, pady=8)

        # Přidat film – malé tlačítko
        make_button(sidebar, "+ Přidat film",
                    command=self._open_add_dialog,
                    padx=12, pady=6).pack(padx=16, pady=4, fill="x")

        make_button(sidebar, "🚪 Ukončit",
                    command=self.quit,
                    color=ACCENT_RED, fg=FG_PRIMARY,
                    padx=12, pady=6).pack(padx=16, pady=4, fill="x", side="bottom")

    def _select_section(self, key):
        for k, btn in self._sidebar_buttons.items():
            btn.config(bg=BG_CARD if k == key else BG_SIDEBAR,
                       fg=ACCENT_GREEN if k == key else FG_PRIMARY)
        self._active_section = key

        if key == "statistiky":
            self._open_statistics()
        elif key == "nastaveni":
            self._open_settings()
        elif key == "dashboard":
            self._show_dashboard()
        else:
            self._apply_filters()

    # ── Hlavní obsah (tabulka + filtry) ──────────────────────────────────────

    def _build_content(self):
        content = tk.Frame(self._paned, bg=BG_DARK)
        self._paned.add(content, minsize=500, stretch="always")

        # Záhlaví sekce
        header = tk.Frame(content, bg=BG_DARK, pady=8)
        header.pack(fill="x", padx=16)
        self._section_title = make_label(
            header, "🎬 Moje filmy", font=FONT_TITLE, fg=FG_PRIMARY)
        self._section_title.pack(side="left")
        make_label(header, "Klikněte na film pro detail  |  Pravý klik pro akce",
                   fg=FG_DISABLED, font=FONT_SMALL).pack(side="right", pady=4)

        # Filtry
        self._build_filters(content)
        separator(content, bg=BG_CARD)

        # Tabulka
        table_frame = tk.Frame(content, bg=BG_DARK)
        table_frame.pack(fill="both", expand=True, padx=16, pady=(0, 8))

        cols = ("nazev", "rok", "zanr", "hodnoceni", "delka", "stav")
        self._tree = ttk.Treeview(
            table_frame, columns=cols, show="headings",
            selectmode="extended", style="Treeview",
        )

        col_cfg = [
            ("nazev",     "Název",          280, "w"),
            ("rok",       "Rok vydání",      70, "center"),
            ("zanr",      "Žánr",           160, "w"),
            ("hodnoceni", "Hodnocení",        80, "center"),
            ("delka",     "Délka (min)",      80, "center"),
            ("stav",      "Stav",             90, "center"),
        ]
        for col, heading, width, anchor in col_cfg:
            self._tree.heading(col, text=heading,
                               command=lambda c=col: self._sort_by(c))
            self._tree.column(col, width=width, anchor=anchor, minwidth=40)

        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical",
                                  command=self._tree.yview)
        self._tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self._tree.pack(fill="both", expand=True)

        # Události tabulky
        self._tree.bind("<<TreeviewSelect>>", self._on_film_select)
        self._tree.bind("<Double-1>",         self._open_edit_dialog)
        self._tree.bind("<Return>",           self._open_edit_dialog)
        self._tree.bind("<Delete>",           lambda e: self._delete_selected())
        self._tree.bind("<Button-3>",         self._show_context_menu)

        # Kontextové menu
        self._ctx_menu = tk.Menu(self, tearoff=0,
                                 bg=BG_DARK, fg=FG_PRIMARY,
                                 activebackground=BG_CARD,
                                 activeforeground=ACCENT_GREEN)
        self._ctx_menu.add_command(label="✏️  Upravit film",    command=self._open_edit_dialog)
        self._ctx_menu.add_command(label="⭐ Přidat do oblíbených", command=self._toggle_favorite)
        self._ctx_menu.add_command(label="📋  Přidat na watchlist",  command=self._toggle_watchlist)
        self._ctx_menu.add_command(label="✓  Označit jako sledované", command=self._mark_watched)
        self._ctx_menu.add_separator()
        self._ctx_menu.add_command(label="🗑️  Smazat",            command=self._delete_selected)

    def _build_filters(self, parent):
        fframe = tk.Frame(parent, bg=BG_CARD, padx=16, pady=10)
        fframe.pack(fill="x", padx=16)

        make_label(fframe, "Filtry:", font=FONT_HEADING, fg=ACCENT_GREEN,
                   bg=BG_CARD).grid(row=0, column=0, sticky="w", padx=(0, 12))

        # Filtr: Název
        make_label(fframe, "Název:", fg=FG_SECONDARY, bg=BG_CARD).grid(
            row=0, column=1, sticky="w")
        self._filter_name = tk.StringVar()
        self._filter_name.trace_add("write", lambda *_: self._apply_filters())
        tk.Entry(fframe, textvariable=self._filter_name, bg=BG_TABLE,
                 fg=FG_PRIMARY, insertbackground=FG_PRIMARY, relief="flat",
                 font=FONT_NORMAL, width=16).grid(row=0, column=2, padx=(4, 16), ipady=4)

        # Filtr: Rok
        make_label(fframe, "Rok:", fg=FG_SECONDARY, bg=BG_CARD).grid(
            row=0, column=3, sticky="w")
        self._filter_year = tk.StringVar()
        self._filter_year.trace_add("write", lambda *_: self._apply_filters())
        tk.Entry(fframe, textvariable=self._filter_year, bg=BG_TABLE,
                 fg=FG_PRIMARY, insertbackground=FG_PRIMARY, relief="flat",
                 font=FONT_NORMAL, width=8).grid(row=0, column=4, padx=(4, 16), ipady=4)

        # Filtr: Žánr
        make_label(fframe, "Žánr:", fg=FG_SECONDARY, bg=BG_CARD).grid(
            row=0, column=5, sticky="w")
        self._filter_genre = tk.StringVar(value="Vše")
        genre_cb = ttk.Combobox(fframe, textvariable=self._filter_genre,
                                values=["Vše"] + sorted(GENRES),
                                font=FONT_SMALL, width=14)
        genre_cb.grid(row=0, column=6, padx=(4, 16))
        genre_cb.bind("<<ComboboxSelected>>", lambda e: self._apply_filters())

        # Filtr: Počet zobrazených
        make_label(fframe, "Zobrazit:", fg=FG_SECONDARY, bg=BG_CARD).grid(
            row=0, column=7, sticky="w")
        self._filter_count = tk.StringVar(value="Vše")
        count_cb = ttk.Combobox(fframe, textvariable=self._filter_count,
                                values=["Vše", "10", "25", "50", "100"],
                                font=FONT_SMALL, width=6)
        count_cb.grid(row=0, column=8, padx=(4, 16))
        count_cb.bind("<<ComboboxSelected>>", lambda e: self._apply_filters())

        # Tlačítko reset
        make_button(fframe, "✗ Reset", command=self._reset_filters,
                    color=BG_TABLE, fg=FG_PRIMARY,
                    padx=8, pady=4).grid(row=0, column=9, padx=8)

    # ── Detail panel ─────────────────────────────────────────────────────────

    def _build_detail_panel(self):
        self._detail_frame = tk.Frame(self._paned, bg=BG_SIDEBAR, width=320)
        self._paned.add(self._detail_frame, minsize=260, stretch="never")
        self._detail_frame.pack_propagate(False)

        self._render_empty_detail()

    def _render_empty_detail(self):
        for w in self._detail_frame.winfo_children():
            w.destroy()
        make_label(self._detail_frame, "ℹ️ Detail filmu",
                   font=FONT_HEADING, fg=ACCENT_GREEN,
                   bg=BG_SIDEBAR).pack(pady=(24, 4))
        make_label(self._detail_frame,
                   "Vyberte film v tabulce\npro zobrazení detailů.",
                   fg=FG_DISABLED, bg=BG_SIDEBAR,
                   justify="center").pack(pady=8)

    def _render_detail(self, film):
        for w in self._detail_frame.winfo_children():
            w.destroy()

        # Název
        header = tk.Frame(self._detail_frame, bg=BG_CARD, pady=12)
        header.pack(fill="x")
        make_label(header, film["nazev"], font=FONT_HEADING,
                   fg=ACCENT_GREEN, bg=BG_CARD, wraplength=280).pack(padx=12)

        # Hodnocení hvězdičky
        stars_val = film["hodnoceni"]
        filled = int(stars_val / 2)
        stars = "★" * filled + "☆" * (5 - filled)
        make_label(header, f"{stars_val}  {stars}",
                   fg=ACCENT_YELLOW, bg=BG_CARD, font=FONT_HEADING).pack(padx=12, pady=4)

        # Informace
        info_frame = tk.Frame(self._detail_frame, bg=BG_SIDEBAR, padx=12, pady=8)
        info_frame.pack(fill="x")

        info_rows = [
            ("🗓️  Rok vydání:",  str(film["rok"])),
            ("🎭  Žánr:",        film["zanr"]),
            ("🎬  Režisér:",     film.get("reziser", "—")),
            ("⏱️  Délka:",       f"{film['delka']} min"),
        ]
        for label, value in info_rows:
            row = tk.Frame(info_frame, bg=BG_SIDEBAR)
            row.pack(fill="x", pady=2)
            make_label(row, label, fg=FG_SECONDARY, bg=BG_SIDEBAR,
                       font=FONT_SMALL).pack(side="left")
            make_label(row, value, fg=FG_PRIMARY, bg=BG_SIDEBAR,
                       font=FONT_SMALL).pack(side="right")

        separator(self._detail_frame, bg=BG_CARD)

        # Stav
        stav_frame = tk.Frame(self._detail_frame, bg=BG_SIDEBAR, padx=12, pady=4)
        stav_frame.pack(fill="x")

        badges = []
        if film.get("sledovano"):  badges.append(("✓ Sledováno", ACCENT_GREEN))
        if film.get("oblibene"):   badges.append(("❤ Oblíbené",  ACCENT_RED))
        if film.get("watchlist"):  badges.append(("📋 Watchlist", ACCENT_WINE))
        if not badges:             badges.append(("— Bez štítku", FG_DISABLED))

        for badge_text, color in badges:
            make_label(stav_frame, badge_text, fg=color, bg=BG_SIDEBAR,
                       font=FONT_SMALL).pack(side="left", padx=(0, 8))

        separator(self._detail_frame, bg=BG_CARD)

        # Popis
        make_label(self._detail_frame, "📝 Popis:",
                   fg=ACCENT_GREEN, font=FONT_SMALL,
                   bg=BG_SIDEBAR).pack(anchor="w", padx=12, pady=(4, 2))
        desc = tk.Text(self._detail_frame, height=6, bg=BG_SIDEBAR,
                       fg=FG_SECONDARY, font=FONT_SMALL,
                       relief="flat", wrap="word", cursor="arrow",
                       state="normal", padx=12, pady=4)
        desc.pack(fill="x", padx=0)
        desc.insert("1.0", film.get("popis", "Popis není k dispozici."))
        desc.config(state="disabled")

        separator(self._detail_frame, bg=BG_CARD)

        # Akční tlačítka
        btn_frame = tk.Frame(self._detail_frame, bg=BG_SIDEBAR, padx=12, pady=8)
        btn_frame.pack(fill="x")
        make_button(btn_frame, "✏️ Upravit",
                    command=self._open_edit_dialog,
                    padx=10, pady=5).pack(side="left", padx=(0, 6))
        make_button(btn_frame, "❤ Oblíbené",
                    command=self._toggle_favorite,
                    color=ACCENT_RED, fg=FG_PRIMARY,
                    padx=10, pady=5).pack(side="left", padx=(0, 6))
        make_button(btn_frame, "🗑️",
                    command=self._delete_selected,
                    color=BG_TABLE, fg=FG_PRIMARY,
                    padx=10, pady=5).pack(side="left")

    # ── Stavový řádek ─────────────────────────────────────────────────────────

    def _build_statusbar(self):
        bar = tk.Frame(self, bg=BG_CARD, height=26)
        bar.pack(fill="x", side="bottom")
        bar.pack_propagate(False)

        self._status_label = make_label(
            bar, "", fg=FG_SECONDARY, font=FONT_SMALL, bg=BG_CARD)
        self._status_label.pack(side="left", padx=12, pady=4)

        make_label(bar, "Film Tracker v1.0.0  |  Python + tkinter",
                   fg=FG_DISABLED, font=FONT_SMALL, bg=BG_CARD).pack(side="right", padx=12)

    def _update_status(self):
        total   = len(self._films)
        visible = len(self._filtered)
        watched = sum(1 for f in self._films if f.get("sledovano"))
        favs    = sum(1 for f in self._films if f.get("oblibene"))
        self._status_label.config(
            text=f"Stavový řádek: {total} filmů celkem  |  "
                 f"Zobrazeno: {visible}  |  "
                 f"Sledováno: {watched}  |  "
                 f"Oblíbené: {favs}"
        )

    # ── Data a filtry ─────────────────────────────────────────────────────────

    def _apply_filters(self, *_):
        # Guard: filter widgets may not yet exist during startup
        if not hasattr(self, "_filter_watched"):
            return
        section = self._active_section
        films = list(self._films)

        # Filtr podle sekce
        if section == "watchlist":
            films = [f for f in films if f.get("watchlist")]
        elif section == "oblibene":
            films = [f for f in films if f.get("oblibene")]

        # Filtr sledováno/nesledováno
        watched_filter = self._filter_watched.get()
        if watched_filter == "Sledováno":
            films = [f for f in films if f.get("sledovano")]
        elif watched_filter == "Nesledováno":
            films = [f for f in films if not f.get("sledovano")]

        # Vyhledávání
        search = self._search_var.get().strip().lower()
        if search and search != "hledat filmy...":
            films = [f for f in films
                     if search in f["nazev"].lower()
                     or search in f["zanr"].lower()
                     or search in str(f.get("reziser", "")).lower()]

        # Filtr název
        name_f = self._filter_name.get().strip().lower()
        if name_f:
            films = [f for f in films if name_f in f["nazev"].lower()]

        # Filtr rok
        year_f = self._filter_year.get().strip()
        if year_f:
            films = [f for f in films if str(f["rok"]).startswith(year_f)]

        # Filtr žánr
        genre_f = self._filter_genre.get()
        if genre_f and genre_f != "Vše":
            films = [f for f in films if genre_f.lower() in f["zanr"].lower()]

        # Počet zobrazených
        count_f = self._filter_count.get()
        if count_f != "Vše":
            try:
                films = films[:int(count_f)]
            except ValueError:
                pass

        self._filtered = films
        self._refresh_table()
        self._update_status()

        # Aktualizovat nadpis sekce
        titles = {
            "moje":       "🎬 Moje filmy",
            "watchlist":  "📋 Watchlist",
            "oblibene":   "❤️  Oblíbené filmy",
            "dashboard":  "🏠 Dashboard",
            "statistiky": "📊 Statistiky",
            "nastaveni":  "⚙️  Nastavení",
        }
        self._section_title.config(text=titles.get(section, "🎬 Filmy"))

    def _refresh_table(self):
        self._tree.delete(*self._tree.get_children())
        for i, film in enumerate(self._filtered):
            stars = "★" * int(film["hodnoceni"] / 2)
            stav_parts = []
            if film.get("sledovano"):  stav_parts.append("✓")
            if film.get("oblibene"):   stav_parts.append("❤")
            if film.get("watchlist"):  stav_parts.append("📋")
            stav = " ".join(stav_parts) if stav_parts else "—"

            tag = "odd" if i % 2 == 0 else "even"
            self._tree.insert(
                "", "end", iid=str(film["id"]),
                values=(
                    film["nazev"],
                    film["rok"],
                    film["zanr"],
                    f"{film['hodnoceni']}  {stars}",
                    film["delka"],
                    stav,
                ),
                tags=(tag,),
            )

        self._tree.tag_configure("odd",  background=BG_ROW_ODD)
        self._tree.tag_configure("even", background=BG_ROW_EVEN)

    def _reset_filters(self):
        self._filter_name.set("")
        self._filter_year.set("")
        self._filter_genre.set("Vše")
        self._filter_count.set("Vše")
        self._filter_watched.set("Vše")
        self._search_var.set("")
        self._apply_filters()

    def _sort_by(self, col):
        """Řazení tabulky podle sloupce."""
        reverse = getattr(self, "_sort_reverse", False)
        key_map = {
            "nazev":     lambda f: f["nazev"].lower(),
            "rok":       lambda f: f["rok"],
            "zanr":      lambda f: f["zanr"].lower(),
            "hodnoceni": lambda f: f["hodnoceni"],
            "delka":     lambda f: f["delka"],
            "stav":      lambda f: (f.get("sledovano", False), f.get("oblibene", False)),
        }
        key_fn = key_map.get(col, lambda f: "")
        self._filtered.sort(key=key_fn, reverse=reverse)
        self._sort_reverse = not reverse
        self._refresh_table()

    # ── Akce ─────────────────────────────────────────────────────────────────

    def _on_film_select(self, event=None):
        sel = self._tree.selection()
        if not sel:
            self._render_empty_detail()
            return
        film_id = int(sel[0])
        film = next((f for f in self._films if f["id"] == film_id), None)
        if film:
            self._detail_film = film
            self._render_detail(film)

    def _get_selected_film(self):
        sel = self._tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Vyberte film v tabulce.", parent=self)
            return None
        film_id = int(sel[0])
        return next((f for f in self._films if f["id"] == film_id), None)

    def _open_add_dialog(self, event=None):
        def on_save(data):
            self._films.append(data)
            self._apply_filters()
            self._status_label.config(fg=ACCENT_GREEN)
            self.after(2000, lambda: self._status_label.config(fg=FG_SECONDARY))
        FilmDialog(self, on_save=on_save, films=self._films)

    def _open_edit_dialog(self, event=None):
        film = self._get_selected_film()
        if not film:
            return
        def on_save(data):
            idx = next((i for i, f in enumerate(self._films) if f["id"] == data["id"]), None)
            if idx is not None:
                self._films[idx] = data
            self._apply_filters()
            self._render_detail(data)
        FilmDialog(self, film=film, on_save=on_save, films=self._films)

    def _delete_selected(self, event=None):
        film = self._get_selected_film()
        if not film:
            return
        if messagebox.askyesno(
            "Smazat film",
            f"Opravdu chcete smazat film\n\"{film['nazev']}\"?",
            parent=self,
        ):
            self._films = [f for f in self._films if f["id"] != film["id"]]
            self._render_empty_detail()
            self._apply_filters()

    def _toggle_favorite(self, event=None):
        film = self._get_selected_film()
        if not film:
            return
        film["oblibene"] = not film.get("oblibene", False)
        self._apply_filters()
        if self._detail_film and self._detail_film["id"] == film["id"]:
            self._render_detail(film)

    def _toggle_watchlist(self, event=None):
        film = self._get_selected_film()
        if not film:
            return
        film["watchlist"] = not film.get("watchlist", False)
        self._apply_filters()
        if self._detail_film and self._detail_film["id"] == film["id"]:
            self._render_detail(film)

    def _mark_watched(self, event=None):
        film = self._get_selected_film()
        if not film:
            return
        film["sledovano"] = True
        self._apply_filters()
        if self._detail_film and self._detail_film["id"] == film["id"]:
            self._render_detail(film)

    def _show_context_menu(self, event):
        row = self._tree.identify_row(event.y)
        if row:
            self._tree.selection_set(row)
            self._ctx_menu.post(event.x_root, event.y_root)

    # ── Speciální obrazovky ───────────────────────────────────────────────────

    def _show_dashboard(self):
        self._section_title.config(text="🏠 Dashboard")
        total   = len(self._films)
        watched = sum(1 for f in self._films if f.get("sledovano"))
        favs    = sum(1 for f in self._films if f.get("oblibene"))
        wl      = sum(1 for f in self._films if f.get("watchlist"))
        messagebox.showinfo(
            "Dashboard",
            f"📊 Přehled knihovny\n\n"
            f"🎬 Celkem filmů:   {total}\n"
            f"✓  Sledováno:      {watched}\n"
            f"❤  Oblíbené:       {favs}\n"
            f"📋 Watchlist:      {wl}\n"
            f"📽  Nesledováno:   {total - watched}\n\n"
            f"Průměrné hodnocení: "
            f"{sum(f['hodnoceni'] for f in self._films) / total:.2f} / 10" if total else "N/A",
            parent=self,
        )

    def _open_statistics(self):
        StatisticsDialog(self, self._films)

    def _open_settings(self):
        win = tk.Toplevel(self)
        win.title("Nastavení")
        win.configure(bg=BG_DARK)
        win.geometry("480x400")
        win.grab_set()
        win.transient(self)

        make_label(win, "⚙️  Nastavení", font=FONT_TITLE).pack(pady=(20, 12))

        frame = tk.Frame(win, bg=BG_CARD, padx=24, pady=16)
        frame.pack(fill="x", padx=24)

        # Velikost písma
        make_label(frame, "Velikost písma tabulky:", fg=ACCENT_GREEN,
                   bg=BG_CARD).pack(anchor="w", pady=(0, 4))
        fs_frame = tk.Frame(frame, bg=BG_CARD)
        fs_frame.pack(fill="x")
        for size, label in [(9, "Malé"), (10, "Střední"), (12, "Velké"), (14, "XL")]:
            tk.Radiobutton(
                fs_frame, text=label, variable=self._font_size, value=size,
                command=self._apply_font_size,
                bg=BG_CARD, fg=FG_PRIMARY, selectcolor=BG_TABLE,
                activebackground=BG_CARD, activeforeground=ACCENT_GREEN,
                font=FONT_NORMAL, cursor="hand2",
            ).pack(side="left", padx=8)

        separator(frame, bg=BG_TABLE)

        # Zobrazit detail
        tk.Checkbutton(
            frame, text="Zobrazit panel s detailem",
            variable=self._show_details, command=self._toggle_details,
            bg=BG_CARD, fg=FG_PRIMARY, selectcolor=BG_TABLE,
            activebackground=BG_CARD, activeforeground=ACCENT_GREEN,
            font=FONT_NORMAL, cursor="hand2",
        ).pack(anchor="w", pady=8)

        separator(frame, bg=BG_TABLE)
        make_label(frame, "Téma:", fg=ACCENT_GREEN, bg=BG_CARD).pack(anchor="w", pady=(8, 4))
        make_label(frame, "Tmavé téma (výchozí) – další témata brzy k dispozici",
                   fg=FG_DISABLED, font=FONT_SMALL, bg=BG_CARD).pack(anchor="w")

        make_button(win, "Zavřít", command=win.destroy).pack(pady=20)

    def _toggle_details(self):
        if self._show_details.get():
            self._paned.add(self._detail_frame)
        else:
            self._paned.remove(self._detail_frame)

    def _apply_font_size(self):
        size = self._font_size.get()
        style = ttk.Style(self)
        style.configure("Treeview", font=("Segoe UI", size), rowheight=size + 18)

    def _increase_font(self, event=None):
        if self._font_size.get() < 18:
            self._font_size.set(self._font_size.get() + 1)
            self._apply_font_size()

    def _decrease_font(self, event=None):
        if self._font_size.get() > 7:
            self._font_size.set(self._font_size.get() - 1)
            self._apply_font_size()

    def _reset_font(self):
        self._font_size.set(10)
        self._apply_font_size()

    # ── Klávesové zkratky ─────────────────────────────────────────────────────

    def _bind_shortcuts(self):
        self.bind("<Control-n>", self._open_add_dialog)
        self.bind("<Control-N>", self._open_add_dialog)
        self.bind("<Control-q>", lambda e: self.quit())
        self.bind("<Control-Q>", lambda e: self.quit())
        self.bind("<Control-f>", lambda e: self._focus_search())
        self.bind("<Control-F>", lambda e: self._focus_search())
        self.bind("<Control-plus>",  self._increase_font)
        self.bind("<Control-minus>", self._decrease_font)
        self.bind("<F5>",   lambda e: self._apply_filters())
        self.bind("<F2>",   self._open_edit_dialog)
        self.bind("<Escape>", lambda e: self._reset_filters())
        # Pravé kliknutí na stavový řádek
        self._status_label.bind("<Button-3>", self._statusbar_context)

    def _focus_search(self):
        self._search_entry.focus_set()
        self._search_entry.select_range(0, "end")

    def _statusbar_context(self, event):
        menu = tk.Menu(self, tearoff=0, bg=BG_DARK, fg=FG_PRIMARY,
                       activebackground=BG_CARD, activeforeground=ACCENT_GREEN)
        menu.add_command(label="📊 Statistiky",  command=self._open_statistics)
        menu.add_command(label="🔄 Obnovit",      command=self._apply_filters)
        menu.add_separator()
        menu.add_command(label="🚪 Ukončit",      command=self.quit)
        menu.post(event.x_root, event.y_root)

    # ── Zástupné akce ─────────────────────────────────────────────────────────

    def _placeholder(self, feature):
        def handler(event=None):
            messagebox.showinfo(
                "Funkce v přípravě",
                f"Funkce \"{feature}\" bude dostupná v příští verzi.",
                parent=self,
            )
        return handler


# ── Vstupní bod ───────────────────────────────────────────────────────────────

def main():
    app = FilmTrackerApp()
    app.mainloop()


if __name__ == "__main__":
    main()
