# 🎬 Film Tracker

Profesionální Python aplikace pro sledování filmů s grafickým rozhraním (GUI) postaveným na **tkinter**.

## Spuštění

```bash
python3 film_tracker.py
```

> Vyžaduje Python 3.8+ s modulem `tkinter` (součást standardní knihovny Pythonu).

## Funkce

### Hlavní rozhraní
- **Levý panel** – navigace mezi sekcemi: Dashboard, Moje filmy, Watchlist, Oblíbené, Statistiky, Nastavení
- **Horní lišta** – vyhledávací pole, tlačítko „+ Přidat film", profil, statistiky
- **Tabulka filmů** – řazení dle libovolného sloupce kliknutím na záhlaví
- **Filtry** – filtrovat dle názvu, roku, žánru a počtu zobrazených záznamů
- **Detail panel** – po výběru filmu zobrazí kompletní informace, hodnocení a ovládací tlačítka
- **Stavový řádek** – celkový počet filmů, počet zobrazených, sledovaných a oblíbených

### Správa filmů
- Přidání nového filmu (Ctrl+N nebo tlačítko)
- Úprava existujícího filmu (dvojklik nebo F2)
- Smazání filmu (klávesa Delete nebo kontextové menu)
- Přidání do oblíbených / watchlistu
- Označení jako sledované

### GUI funkce
- 🌑 **Tmavé téma** s kontrastními zelenými akcenty
- 🖱️ **Pravé kliknutí** na film otevře kontextové menu s akcemi
- ⌨️ **Klávesové zkratky**: Ctrl+N (nový film), Ctrl+F (hledat), Ctrl+Q (ukončit),
  F2 (upravit), F5 (obnovit), Delete (smazat), Escape (reset filtrů), Ctrl+±️ (velikost písma)
- 🔤 **Nastavitelná velikost písma** v tabulce
- ↔️ **Přetahovatelný oddělovač** mezi tabulkou a panelem detailů
- 📊 **Statistiky** – přehled sbírky, průměrné hodnocení, celkový čas sledování, top 5 filmů

### Vzorová data
Aplikace obsahuje 152 předvyplněných filmů pro okamžitou demonstraci.

## Struktura kódu

| Třída / funkce | Popis |
|----------------|-------|
| `FilmTrackerApp` | Hlavní aplikační okno, layout, menu, akce |
| `FilmDialog` | Modální dialog pro přidání/úpravu filmu |
| `StatisticsDialog` | Okno se statistikami sbírky |
| `AboutDialog` | Dialog „O aplikaci" s přehledem zkratek |
| `make_button()` | Pomocná funkce pro stylizovaná tlačítka |
| `SAMPLE_FILMS` | Vzorová data (152 filmů) |

## Technologie

- **Python 3** – standardní knihovna, žádné závislosti třetích stran
- **tkinter** – vestavěný GUI framework
- **ttk** – stylizované widgety (Treeview, Combobox)
