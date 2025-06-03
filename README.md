# System Zarządzania Projektami

Aplikacja desktopowa stworzona w Pythonie z użyciem **PyQt5**, **MongoDB** i **Matplotlib**, służąca do przeglądania, eksportowania i wizualizacji danych projektowych.

---

## 📌 Funkcjonalności

- ✅ Graficzny interfejs (PyQt5)
- ✅ Pobieranie danych z MongoDB
- ✅ Tabela z informacjami o projektach
- ✅ Eksport do pliku CSV
- ✅ Wykres słupkowy z postępem projektów

---

## 🛠 Wymagania

```bash
pip install -r requirements.txt
---

## 🗃 Struktura danych MongoDB

```json
{
  "nazwa": "Projekt Alpha",
  "status": "W toku",
  "termin": "2024-12-31",
  "postep": 60,
  "budzet": 100000,
  "wydatki": 45000
}

---

### ▶️ Sekcja: Uruchomienie
```markdown
---

## ▶️ Uruchomienie

```bash
python main.py

---

### 📂 Sekcja: Pliki w repozytorium
```markdown
---

## 📂 Zawartość repozytorium

| Plik                            | Opis                                   |
|---------------------------------|----------------------------------------|
| `main.py`                       | Główna aplikacja z GUI                 |
| `projekty.csv`                  | Przykładowy eksport danych             |
| `requirements.txt`              | Lista wymaganych bibliotek             |
| `System zarządzania...MZ 206.py`| Wersja alternatywna/testowa            |
| `Aplikacja_z_MongoDB_...docx`   | Opis projektu i dokumentacja           |
---

## 👤 Autor

**Piotr Krasowski**  
Projekt zaliczeniowy / portfolio – 2024
