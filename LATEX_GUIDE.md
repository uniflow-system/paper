# UniFlow ASE - LaTeX Geliştirme Rehberi

Bu dosya, Springer Nature `sn-jnl` template'i ile `main.tex` üzerinde çalışırken dikkat edilmesi gereken noktaları içerir.

---

## Template Bilgileri

- **Template:** Springer Nature SN-JNL (Version 3.1, December 2024)
- **Document Class:** `sn-jnl` with `sn-basic` reference style
- **Journal:** Automated Software Engineering
- **Kaynak:** [Springer Nature LaTeX Templates](https://www.springernature.com/gp/authors/campaigns/latex-author-support)

---

## Derleme Komutları

### Hızlı Derleme
```bash
latexmk -pdf main.tex
```

### Tam Derleme (bibliyografi dahil)
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Temizlik + Yeniden Derleme
```bash
rm -f main.aux main.bbl main.blg main.out main.log
latexmk -pdf main.tex
```

---

## Proje Yapısı

```
uniflow_ase/
├── main.tex              # Ana LaTeX dosyası
├── references.bib        # Bibliyografi veritabanı
├── sn-jnl.cls           # Springer Nature document class
├── sn-basic.bst         # Springer Nature bibliography style
├── main.pdf             # Derlenmiş PDF çıktısı
├── LATEX_GUIDE.md       # Bu dosya
├── sn-article-template/ # Orijinal template (referans için)
│   ├── sn-article.tex   # Örnek makale
│   ├── sn-article.pdf   # Örnek PDF
│   ├── user-manual.pdf  # Kullanım kılavuzu
│   └── bst/             # Tüm bibliyografi stilleri
└── .vscode/
    └── settings.json    # VS Code/Cursor LaTeX ayarları
```

---

## Springer Nature Formatı: Önemli Komutlar

### Document Class
```latex
\documentclass[pdflatex,sn-basic]{sn-jnl}
```

Diğer stil seçenekleri:
- `sn-mathphys-num` - Matematik/Fizik (numaralı)
- `sn-mathphys-ay` - Matematik/Fizik (yazar-yıl)
- `sn-nature` - Nature dergisi
- `sn-vancouver-num` - Vancouver (numaralı)

### Yazar Formatı
```latex
\author*[1]{\fnm{First} \sur{Last}}\email{email@domain.com}  % * = corresponding
\author[1,2]{\fnm{Second} \sur{Author}}\email{author@domain.com}

\affil*[1]{\orgdiv{Department}, 
           \orgname{University}, 
           \orgaddress{\city{City}, \postcode{12345}, \country{Country}}}
```

### Abstract ve Keywords
```latex
\abstract{Abstract metni burada...}
\keywords{Keyword1, Keyword2, Keyword3}
\maketitle  % Abstract ve keywords'ten SONRA gelir
```

### Back Matter (Acknowledgements vb.)
```latex
\backmatter

\bmhead{Acknowledgements}
Teşekkür metni...

\bmhead{Data Availability}
Veri erişilebilirlik beyanı...

\bmhead{Competing Interests}
The authors declare no competing interests.

\bmhead{Author Contributions}
Yazar katkıları...

\bibliography{references}  % bibliographystyle otomatik ayarlanır
```

### Tablo Formatı
```latex
\begin{table}[h]
\caption{Tablo başlığı}\label{tab:label}
\begin{tabular}{@{}lcc@{}}
\toprule
Sütun 1 & Sütun 2 & Sütun 3 \\
\midrule
Veri 1 & Veri 2 & Veri 3 \\
\botrule  % NOT: \bottomrule değil \botrule!
\end{tabular}
\end{table}
```

### Algoritma Formatı (algpseudocode)
```latex
\begin{algorithm}[tb]
\caption{Algoritma başlığı}
\label{alg:label}
\begin{algorithmic}[1]
    \Require Girdiler
    \Ensure Çıktılar
    \State $x \gets$ değer
    \For{each item}
        \State İşlem
    \EndFor
    \State \Return sonuç \Comment{Açıklama}
\end{algorithmic}
\end{algorithm}
```

**Dikkat:** Eski `algorithmic` paketi (`\STATE`, `\FOR`, `\ENDFOR`) değil, yeni `algpseudocode` paketi (`\State`, `\For`, `\EndFor`) kullanılıyor!

---

## Sık Karşılaşılan Hatalar

### Hata 1: `\bottomrule` undefined
**Çözüm:** `\botrule` kullanın (sn-jnl class farklı tanım kullanıyor)

### Hata 2: `\STATE` undefined
**Çözüm:** `\State` kullanın (algpseudocode paketi)

### Hata 3: `acknowledgements` environment undefined
**Çözüm:** `\begin{acknowledgements}` yerine `\bmhead{Acknowledgements}` kullanın

### Hata 4: Duplicate \bibstyle
**Çözüm:** Manuel `\bibliographystyle{...}` komutunu kaldırın - sn-jnl class otomatik ayarlar

### Hata 5: Abstract `\maketitle`'dan sonra
**Çözüm:** Springer Nature formatında sıra:
1. `\title`, `\author`, `\affil`
2. `\abstract{...}`
3. `\keywords{...}`
4. `\maketitle`

---

## Citation Formatı

sn-basic stili author-year formatı kullanır:
```latex
\cite{hu2022lora}           % (Hu et al. 2022)
\citep{hu2022lora}          % (Hu et al. 2022)  
\citet{hu2022lora}          % Hu et al. (2022)
```

---

## Yardımcı Kaynaklar

- `sn-article-template/user-manual.pdf` - Detaylı kullanım kılavuzu
- `sn-article-template/sn-article.tex` - Örnek makale
- [Springer Nature Author Guidelines](https://www.springer.com/gp/authors-editors)
- [Automated Software Engineering Journal](https://www.springer.com/journal/10515)

---

*Son güncelleme: Ocak 2026 - Springer Nature SN-JNL v3.1*
