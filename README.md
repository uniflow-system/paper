# UniFlow — ASE Journal Paper

**Resource-Efficient Multi-Source RAG: Hexagonal Architecture and the 4-bit Quantization Paradox**

Automated Software Engineering (Springer) journal submission icin LaTeX kaynak dosyalari.

---

## Hizli Baslangic

```bash
# Repo'yu klonla
git clone https://github.com/tunahanbg/uniflow_ase.git
cd uniflow_ase

# PDF derle (tam derleme — referanslar dahil)
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

# veya tek komutla
latexmk -pdf main.tex
```

Cikti: `main.pdf` (30 sayfa)

---

## Kilit Dosyalar

| Dosya | Aciklama |
|---|---|
| `main.tex` | Ana makale. Tum icerik burada. Her section basinda detayli yazim rehberi yorumlari mevcut. |
| `references.bib` | Bibliyografi. Gruplar halinde organize (~40 aktif referans). |
| `uniflow.md` | **Proje rehberi.** Section detaylari, yazim yaklasimi, eksikler, TODO listesi — **ilk bu dosyayi oku.** |
| `LATEX_GUIDE.md` | Derleme komutlari, sik karsilasilan LaTeX hatalari ve cozumleri. |
| `figures/` | Gorseller. Su an placeholder PDF'ler var — gercek figurlerin olusturulmasi gerekiyor. |

## Kurallar ve Conventions

| Dosya | Aciklama |
|---|---|
| `.cursor/rules/paper-rules.mdc` | Yazim kurallari: citation format, template uyumluluk, style guide, section uzunluk hedefleri. |
| `.cursor/rules/paper-memory.mdc` | Proje baglami: alinan kararlar, tamamlanan bolumler, session notlari. |

## Template (Referans)

| Dosya | Aciklama |
|---|---|
| `sn-article-template/sn-article.tex` | Springer Nature resmi ornek makale. LaTeX komut ornekleri icin buraya bak. |
| `sn-article-template/user-manual.pdf` | Template kullanim kilavuzu. |
| `sn-jnl.cls` | Springer Nature document class (degistirme). |
| `sn-basic.bst` | Bibliography style (degistirme). |

---

## Oncelikli Yapilacaklar

Detayli liste `uniflow.md` icerisinde. Ozet:

1. **3 figure olustur** (su an placeholder):
   - `figures/hexagonal-architecture.pdf` — 12 adapter mimarisi diyagrami
   - `figures/training-loss-comparison.pdf` — v1/v2/v3 loss egrileri grafigi
   - `figures/rag-pipeline.pdf` — Hybrid retrieval akis diyagrami

2. **Guncel referanslar** ekle (2024-2025 RAG/quantization calismalari)

3. **Son okuma** ve derleme kontrolu

---

## Citation Kurali

Template author-year stili kullaniyor (`sn-basic`):

- **`\cite{key}`** → Yazar adi cumle icinde: *"Sculley et al. (2015) documented..."*
- **`\citep{key}`** → Parantez icinde referans: *"...technical debt (Sculley et al., 2015)."*

---

## Yazarlar

| Ad | Rol | Corresponding |
|---|---|---|
| Tunahan Buyukgebiz | Conceptualization, Software, Investigation, Writing | ✓ |
| Toprak Necat Gok | Software, Validation, Formal Analysis, Writing | ✓ |
| Suleyman Muhammed Arikan | Methodology, Resources, Writing | |
| Ibrahim Alper Dogru | Supervision, Resources, Project Administration | |

**Kurum:** Gazi University, Department of Computer Engineering, Ankara, Turkey
