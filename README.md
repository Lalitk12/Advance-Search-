# Google Advanced Query Generator (OSINT / Security Research Aid)

A Python tool that generates **advanced Google/Bing/DuckDuckGo queries** for **OSINT, security research, and auditing**.  
It provides ready-made query presets (site mapping, leaks, cloud buckets, etc.), supports custom queries, and can export results.  

⚠️ **Disclaimer**  
This tool is for **educational and ethical security research only**.  
Do not use it against systems without proper authorization.  

---

## ✨ Features

- 🔍 **Predefined query presets** for OSINT & security auditing  
- 🌍 Supports **Google, Bing, DuckDuckGo**  
- 📝 Add your own **custom queries**  
- 📅 Date range filtering (`--after`, `--before`)  
- 🧹 Deduplicates queries automatically  
- 📤 Export results to **JSON** or **CSV**  

---

## 📑 Preset Overview

| Preset            | Description                          | Example Query                                   |
|-------------------|--------------------------------------|------------------------------------------------|
| `quick`           | Basic org/domain checks              | `site:example.com`                              |
| `site_mapping`    | Discover subdomains & structure      | `site:*.example.com`                            |
| `public_docs`     | Search for documents & logs          | `site:example.com filetype:pdf`                 |
| `exposed_dirs`    | Look for open directories/backups    | `intitle:"index of" example.com`                |
| `code_sharing`    | Check GitHub/Pastebin leaks          | `site:github.com "Example Corp"`                |
| `login_admin`     | Find login/admin portals             | `site:example.com inurl:admin`                  |
| `public_contacts` | Emails, phones, contact pages        | `"Example Corp" email`                          |
| `leaks_news`      | Mentions of breaches or leaks        | `"Example Corp" "data leak"`                    |
| `cloud_storage`   | Open cloud buckets (S3, Azure, GDrive) | `site:s3.amazonaws.com "Example Corp"`        |

---
## 📦 Installation

Clone the repository and make the script executable:

```bash
git clone https://github.com/yourusername/gquery.git
cd gquery
chmod +x gquery.py
```
---
## ⚡ Usage

Run with organization and domain:

```bash
python3 gquery.py --org "Example Corp" --domain example.com
```
---
## 🔧 Examples

Quick queries (Google):

```bash
python3 gquery.py --org "Example Corp" --domain example.com --preset quick --engine google
```

Site mapping + exposed dirs → JSON export:

```bash
python3 gquery.py --org "Example Corp" --domain example.com --preset site_mapping exposed_dirs --out results.json
```

Custom query:

```bash
python3 gquery.py --org "Example Corp" --domain example.com --custom "site:example.com confidential"
```

---
## 📊 Output
Queries are printed with search engine URLs.

```bash
[GOOGLE] site:example.com
   → https://www.google.com/search?q=site%3Aexample.com
```
---

## 🛡️ License

This project is licensed under the MIT License – free to use, modify, and distribute.

---

👨‍💻 Author

Developed by Lalit kumbhar
GitHub: @Lalitk12

