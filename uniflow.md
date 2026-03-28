# UniFlow ASE Paper — Proje Rehberi

Bu belge, **"Resource-Efficient Multi-Source RAG: Hexagonal Architecture and the 4-bit Quantization Paradox"** makalesinin mevcut durumunu, yazım yaklaşımını, dosya yapısını ve yapılması gerekenleri detaylı şekilde açıklar.

---

## 1. Genel Bilgiler

| Alan | Detay |
|---|---|
| **Hedef Journal** | Automated Software Engineering (Springer, IF: 3.83) |
| **Template** | Springer Nature SN-JNL v3.1, December 2024 |
| **Referans Stili** | `sn-basic` (author-year: "Jones et al. (2020)") |
| **Review Tipi** | Single-blind |
| **Sayfa Sayısı** | 30 sayfa (derlenmiş PDF) |
| **Baz Model** | Qwen2.5-3B-Instruct |
| **Dataset** | SAMSum (16,369) + DialogSum (13,460) = 28,982 örnek |

### Yazarlar

| # | Ad | Rol | Corresponding |
|---|---|---|---|
| 1 | Tunahan Buyukgebiz | Conceptualization, Software, Investigation, Writing – Original Draft | **Evet** |
| 2 | Toprak Necat Gok | Software, Validation, Formal Analysis, Writing – Review & Editing | **Evet** |
| 3 | Suleyman Muhammed Arikan | Methodology, Resources, Writing – Review & Editing | Hayir |
| 4 | Ibrahim Alper Dogru | Supervision, Resources, Writing – Review & Editing, Project Administration | Hayir |

**Kurum:** Gazi University, Department of Computer Engineering, Faculty of Technology, Ankara, Turkey

---

## 2. Dosya Yapisi ve Referanslar

```
uniflow_ase/
├── main.tex                  # Ana makale dosyasi (~1066 satir)
├── main.pdf                  # Derlenmiş PDF ciktisi (30 sayfa)
├── references.bib            # Bibliyografi (~40 aktif referans)
├── uniflow.md                # BU DOSYA — Proje rehberi
├── LATEX_GUIDE.md            # LaTeX derleme komutlari ve hata cozumleri
├── sn-jnl.cls                # Springer Nature document class (degistirilmez)
├── sn-basic.bst              # Bibliography style (degistirilmez)
├── figures/                  # Gorseller (su an PLACEHOLDER)
│   ├── hexagonal-architecture.pdf
│   ├── training-loss-comparison.pdf
│   ├── rag-pipeline.pdf
│   └── query-type-performance.pdf
├── sn-article-template/      # Springer Nature resmi ornek template
│   ├── sn-article.tex        # Ornek makale (referans icin)
│   └── user-manual.pdf       # Template kullanim kilavuzu
└── .cursor/rules/
    ├── paper-rules.mdc       # Yazim kurallari (citation, format, style)
    └── paper-memory.mdc      # Proje baglamı ve kararlar
```

### Onemli Dosyalar

- **`main.tex`** — Makalenin tek kaynak dosyasi. Tum icerik burada. Her section basinda detayli LaTeX comment bloklari ile yazim rehberi mevcut.
- **`references.bib`** — Tum kaynaklar burada. Gruplar halinde organize: Regularization, LLM Models, PEFT, RAG, IR, Architecture, Evaluation, Quantization, vb.
- **`.cursor/rules/paper-rules.mdc`** — Yazim kurallari: forward reference yasagi, citation format (`\cite` vs `\citep`), template uyumluluk (`\botrule`, `\State`, `\bmhead`), writing style (active voice, quantify everything), section uzunluk hedefleri, git commit conventions.
- **`.cursor/rules/paper-memory.mdc`** — Proje baglami: kararlar, tamamlanan bolumler, bilinen sorunlar, session notlari.
- **`LATEX_GUIDE.md`** — Derleme komutlari (`latexmk -pdf main.tex` veya `pdflatex + bibtex + 2x pdflatex`), sik karsilasilan hatalar ve cozumleri.

---

## 3. Citation Kurallari

`sn-basic` stili **author-year** formatindadir. İki farkli citation komutu vardir:

| Komut | Cikti | Kullanim |
|---|---|---|
| `\cite{key}` | Jones et al. (2020) | **Narrative**: Yazar adi cumlenin oznesi |
| `\citep{key}` | (Jones et al., 2020) | **Parenthetical**: Cumle sonunda referans |

**Ornekler:**
- `Sculley et al.~\cite{sculley2015debt} documented...` → Sculley et al. (2015) documented...
- `...violating separation of concerns~\citep{sculley2015debt}.` → ...violating separation of concerns (Sculley et al., 2015).

**Kural:** Yazar adi cumle icinde geciyorsa `\cite`, cumle sonunda parantez icinde kanit olarak veriliyorsa `\citep`.

---

## 4. Makale Yapisi — Section Detaylari

### Section 1: Introduction (`\label{sec:introduction}`)

**Amac:** Okuyucuyu problemle tanistir, bosluklar goster, katkilari sun, makale haritasi ver.

**Yaklasim:** "Hook → Gap → Contributions → Organization" formulu. Tezin 8 sayfalik encyclopedia-style introduction'i yerine kompakt, top-down, contribution-first yaklasim. Active voice, quantify everything, "novel" kelimesinden kacin.

**Yapi:**
1. **Hook** (1 paragraf): Heterojen veri kaynaklari problemi, RAG'in vaat ettigi ama karsilastigi trade-off
2. **Research Gaps** (1 paragraf): UC boluk — (1) quantization RAG'da test edilmemis, (2) 4-bit performans dususu varsayimi test edilmemis, (3) modular RAG mimarisi eksik
3. **RQ Preview** (1 paragraf): 4 RQ ozeti
4. **Contributions** (bullet list): 4 katkı — Quantization Paradox, Hexagonal Architecture, Hybrid Retrieval, Replication Package
5. **Organization** (1 paragraf): Section haritasi

**Tablolar/Sekiller:** Yok (tasarim geregi — Introduction'da tablo/sekil olmaz)

**Referanslar:** ~15 citation (PEFT, quantization, RAG framework'leri, Hexagonal Architecture)

---

### Section 2: Research Questions (`\label{sec:research-questions}`)

**Amac:** Makaleyi ampirik sorusturmalar etrafinda cercevele. ASE hakemleri icin bilimsel titizlik goster.

**Yaklasim:** Shaw'in ICSE'03 taksonomisi kullanildi — her RQ bir soru tipine sahip:
- **RQ1 [Generalization]**: Quantization seviyelerinde memory-performance trade-off nedir?
- **RQ2 [Feasibility]**: Hexagonal Architecture multi-source RAG icin uygulanabilir mi?
- **RQ3 [Characterization]**: 4-bit quantization implicit regularization saglar mi?
- **RQ4 [Evaluation]**: Hybrid retrieval tek stratejilere gore nasil performans gosterir?

**Yapi:** Her RQ icin: Bold label + italik soru + olculebilir degiskenler + baglamsal aciklama. Sub-question yok (kullanici tercihi). Paragraf formati (listeleme degil).

**Onemli Karar:** Forward reference yasagi — RQ'larda "Table X'te gorecegimiz gibi" gibi ifadeler yok.

---

### Section 3: Related Work (`\label{sec:related-work}`)

**Amac:** Calismamizi literaturdeki bosluklar uzerinden konumlandir.

**Yaklasim:** Ansiklopedik survey degil, **critical positioning**. Her alt bolum su pattern'i izler:
> "While [Paper X] demonstrates [contribution], their approach [limitation]. In contrast, our work [how we address it]."

**Alt Bolumler:**
1. **3.1 Parameter-Efficient Fine-Tuning** — Adapters → LoRA → QLoRA, PEFT tarihcesi. Bosluk: QLoRA generic benchmark'larda test edilmis, RAG'da degil.
2. **3.2 Retrieval-Augmented Generation** — REALM → RETRO → Atlas → RAG frameworks (LangChain, LlamaIndex, Haystack). Bosluk: Monolithic mimari, tek modalite.
3. **3.3 Hybrid Information Retrieval** — BM25, DPR, ColBERT, Sentence-BERT, RRF. Bosluk: Tek-domain benchmark'lar, query tipi analizi yok.
4. **3.4 Software Architecture for ML Systems** — Hexagonal Architecture, DDD, MLOps. Bosluk: ML sistemlerinde mimari pattern'ler kavramsal kalıyor.
5. **3.5 Positioning Summary** — 3 temel fark ozetlenir.

**Potansiyel Eksiklikler:**
- 2024-2025 tarihli guncel RAG calismalari eksik (orn: GraphRAG, Adaptive RAG)
- Alternatif quantization yontemleri (GPTQ, AWQ) karsilastirmasi zayif
- Related work comparison table eklenebilir (feature matrix)

---

### Section 4: Research Method (`\label{sec:method}`)

**Amac:** Metodolojimizi RQ-driven ve reproducibility-first acikla.

**Yaklasim:** Her alt bolum "To address RQX..." ile baslar. Past tense (yapilan is) + present tense (tasarim gerekceleri). Karar gerekceleri ("We chose X over Y because Z").

**Alt Bolumler:**

1. **4.1 System Architecture: Hexagonal Design** — 12 adapter taksonomisi (4 input, 5 processing, 3 infrastructure), port tipleri (IInputAdapter, IProcessingAdapter, IInfrastructureAdapter), DAG-based orchestration (LangGraph), kalite ozellikleri (modularity, extensibility, performance).
   - **Figure 1** (`fig:hexagonal-architecture`): Hexagonal Architecture diyagrami — **PLACEHOLDER, OLUSTURULMALI**

2. **4.2 Fine-Tuning Methodology** — Dataset (SAMSum + DialogSum = 28,982), preprocessing, QLoRA + LoRA implementasyonu, v1/v2/v3 karsilastirmasi.
   - **Table 1** (`tab:hyperparameters`): v1/v2/v3 hyperparameter karsilastirmasi

3. **4.3 Hybrid Retrieval Pipeline** — BM25 + Semantic Search + RRF. Algorithm 1 (RRF pseudocode). BM25Retriever (rank-bm25) + Qdrant + bge-small-en-v1.5.
   - **Algorithm 1** (`alg:rrf`): RRF pseudocode
   - **Figure 2** (`fig:rag-pipeline`): Hybrid retrieval pipeline diyagrami — **PLACEHOLDER, OLUSTURULMALI**

4. **4.4 Evaluation Design** — 10 metrik, 4 RQ ile eslestirilmis. 500-query test set, 3 annotator (Fleiss' kappa=0.78). Baselines ve istatistiksel testler.
   - **Table 2** (`tab:evaluation-metrics`): RQ-metrik eslestirme tablosu

5. **4.5 Implementation Details** — Hardware (RTX 4090), software stack, random seed, MLflow tracking.

---

### Section 5: Results and Discussion (`\label{sec:results}`)

**Amac:** Her RQ icin bulgu → kanit → tartisma → cikarimlari sun.

**Yaklasim:** Her alt bolum su sablonu izler:
1. RQ'yu yeniden belirt (1 cumle, italik)
2. **Finding** headline (bold, kantitatif)
3. Tablo/sekil referansi ile kanit
4. Mekanizma tartismasi (neden bu sonuc?)
5. Onceki calismalara karsilastirma
6. Pratik cikarimlar

**Alt Bolumler:**

1. **5.1 RQ1: Quantization-Performance Trade-offs** — 4-bit en dusuk loss (0.38 vs 0.52), %75 memory azalma, 2.1x hizlanma. Istatistiksel testler (p=0.0003, Cohen's d=0.9). Maliyet analizi (cloud + consumer GPU). Manual evaluation (accuracy %89).
   - **Table 3** (`tab:version-comparison`): v1/v2/v3 metrik karsilastirma
   - **Figure 3** (`fig:training-loss`): Training loss egrileri — **PLACEHOLDER, OLUSTURULMALI**

2. **5.2 RQ2: Hexagonal Architecture Effectiveness** — 65ms overhead (%16 toplam), coupling coefficient 0.15, cyclomatic complexity 3.2, %95 code coverage. ArXiv adapter 4 saatte eklendi vs LangChain'de 2-3 gun.
   - **Table 4** (`tab:latency-breakdown`): Latency breakdown tablosu

3. **5.3 RQ3: Implicit Regularization** — Gradient norm %50 azalma (2.4→1.2), ROUGE-L %6 iyilesme (0.48→0.51), train-val gap sabit (0.06). Stochastic rounding → gradient noise injection mekanizmasi. Dropout ile karsilastirma.
   - **Table 5** (`tab:regularization-evidence`): ROUGE/gradient norm tablosu

4. **5.4 RQ4: Hybrid Retrieval Superiority** — P@5=0.81, R@10=0.94, %15-30 iyilesme. Multi-hop query'lerde %70 kazanc. RRF vs learned fusion karsilastirmasi.
   - **Table 6** (`tab:retrieval-comparison`): Strateji karsilastirma tablosu
   - **Table 7** (`tab:query-type-breakdown`): Query tipi bazinda P@5 performansi

5. **5.5 Summary of Findings** — 4 RQ sentezi, quantization paradox vurgusu, validity threat'lere gecis.

**Potansiyel Eksiklikler:**
- Query type performance bar chart eksik (`figures/query-type-performance.pdf` placeholder var)
- Ablation study eksik (orn: LoRA rank degistirmenin etkisi)
- Confusion matrix veya hata analizi eklenebilir

---

### Section 6: Threats to Validity (`\label{sec:threats}`)

**Amac:** Sinirlamalarin farkindaligini goster, metodik titizligi kanitla.

**Yaklasim:** Wohlin et al. (2012) framework'u. Her threat icin: **Threat** → **Mitigation** → **Residual Risk** formati. 9 threat, 4 kategori.

**Kategoriler:**
- **Construct Validity** (Threat 1-2): ROUGE sinirlamalari, dataset temsil gucu
- **Internal Validity** (Threat 3-4): Random seed varyasyonu, hyperparameter tuning
- **External Validity** (Threat 5-7): Model-specific, dil yanliligi, hardware-specific
- **Conclusion Validity** (Threat 8-9): Sample size, corpus boyutu

---

### Section 7: Replication Package (`\label{sec:replication}`)

**Amac:** Toplulugun sonuclari dogrulamasini sagla.

**Yaklasim:** ACM Artifact Evaluation kilavuzlarina uygun. Kompakt, 2 paragraflik prose formati (daha once checklist formati vardi, kaldirildi — journal'larda standart degil).

**Icerik:** GitHub repo + HuggingFace Hub + pip requirements + Docker + seed'ler + hardware gereksinimleri + maliyet tahmini.

---

### Section 8: Conclusion and Future Work (`\label{sec:conclusion}`)

**Amac:** Katkilari ozetle, arastirma ve pratik icin cikarimlari sun, gelecek yonelimler belirle.

**Yaklasim:** Forward-looking, impact-focused. Tezin 4 sayfalik tekrarlayici ozetinin yerine 3 alt bolumlu kompakt yapi.

**Alt Bolumler:**
1. **8.1 Summary of Contributions** — 4 RQ'nun birer cumlelik ozeti + quantization paradox vurgusu
2. **8.2 Implications for Research and Practice** — ML araştırmacıları, SE araştırmacıları, pratisyenler icin ayri paragraflar
3. **8.3 Future Directions** — Short-term (validity threat'leri adresle), Medium-term (multimodal embedding, cross-encoder reranking), Long-term (PAC-Bayes teorik analiz, 1-bit quantization, agentic RAG)

---

### Back Matter

Springer Nature formati geregi asagidaki declarations mevcut:
- **Acknowledgements** — Gazi Universitesi, danisman tesekkurleri, open-source araclar
- **Data Availability** — GitHub + HuggingFace linkleri
- **Funding** — "No specific grant..."
- **Competing Interests** — "No competing interests."
- **Ethics Approval / Consent to Participate / Consent for Publication** — "Not applicable."
- **Code Availability** — GitHub linki
- **Author Contributions** — CRediT formatinda

---

## 5. Tablolar ve Sekiller Ozeti

### Tablolar (7 adet)

| # | Label | Section | Icerik |
|---|---|---|---|
| T1 | `tab:hyperparameters` | 4.2 | v1/v2/v3 fine-tuning hyperparametreleri |
| T2 | `tab:evaluation-metrics` | 4.4 | RQ-metrik eslestirmesi (10 metrik, 4 RQ) |
| T3 | `tab:version-comparison` | 5.1 | Quantization seviye karsilastirmasi (loss, memory, speed) |
| T4 | `tab:latency-breakdown` | 5.2 | DAG-based orchestration latency breakdown |
| T5 | `tab:regularization-evidence` | 5.3 | ROUGE + gradient norm + train-val gap |
| T6 | `tab:retrieval-comparison` | 5.4 | Retrieval strateji karsilastirmasi (P@k, R@k, MRR, NDCG) |
| T7 | `tab:query-type-breakdown` | 5.4 | Query tipi bazinda P@5 performansi |

### Sekiller (3 adet — hepsi PLACEHOLDER)

| # | Dosya | Section | Icerik | Oncelik |
|---|---|---|---|---|
| F1 | `figures/hexagonal-architecture.pdf` | 4.1 | 12 adapter, 3 port tipi, domain core, DAG-based orchestration | **KRITIK** |
| F2 | `figures/training-loss-comparison.pdf` | 5.1 | 3 loss egrisi (v1/v2/v3), 1000 step, hata bantlari (3 seed) | **KRITIK** |
| F3 | `figures/rag-pipeline.pdf` | 4.3 | BM25 + Semantic → RRF → Context → LLM akis diyagrami | **KRITIK** |

### Opsiyonel Ek Sekil

| # | Dosya | Section | Icerik | Oncelik |
|---|---|---|---|---|
| F4 | `figures/query-type-performance.pdf` | 5.4 | Bar chart: P@5 by query type x strateji | ORTA |

### Algoritmalar (1 adet)

| # | Label | Section | Icerik |
|---|---|---|---|
| A1 | `alg:rrf` | 4.3 | Reciprocal Rank Fusion pseudocode |

---

## 6. YAPILMASI GEREKENLER

### Kritik (Submission Oncesi Zorunlu)

- [ ] **Figure 1 olustur** (`figures/hexagonal-architecture.pdf`): UniFlow Hexagonal Architecture diyagrami. Merkezdeki domain core, etrafinda 3 halka (input, processing, infrastructure adapter'lari). Her adapter ismi ve gorevi gorulmeli. Draw.io, Figma, TikZ veya benzeri aracla olusturulabilir.

- [ ] **Figure 2 olustur** (`figures/training-loss-comparison.pdf`): X ekseni: training steps (0-1000), Y ekseni: training loss. 3 cizgi: v1 full-precision (mavi, 0.52'de biter), v2 8-bit (yesil, 0.45'te biter), v3 4-bit (kirmizi, 0.38'de biter). Hata bantlari (std dev across 3 seeds). Matplotlib veya benzer aracla olusturulabilir.

- [ ] **Figure 3 olustur** (`figures/rag-pipeline.pdf`): Sol tarafta kullanici sorgusu, paralel olarak BM25 ve Semantic Search'e gider, ikisinin sonuclari RRF Fusion'da birlesir, top-5 dokuman context olarak LLM'e gider, cevap uretilir. Flowchart formati.

### Yuksek Oncelik

- [ ] **Guncel referanslar ekle** (2024-2025): RAG alaninda GraphRAG (Microsoft), Adaptive RAG, alternatif quantization (GPTQ, AWQ) calismalari. Related Work'te bu bosluk hakem tarafindan fark edilebilir.

- [ ] **(Opsiyonel) Figure 4 olustur** (`figures/query-type-performance.pdf`): Grouped bar chart — 3 grup (Factual, Conceptual, Multi-hop), her grupta 3 bar (BM25, Semantic, Hybrid). Veriler `tab:query-type-breakdown`'dan alinir.

### Orta Oncelik

- [ ] **Related Work'e comparison table** ekle: RAG frameworks (LangChain, LlamaIndex, Haystack, UniFlow) feature matrix — multi-source, modular, quantized, hybrid retrieval.

- [ ] **Ablation study** ekle (Section 5): LoRA rank degistirmenin etkisi, RRF constant c degerinin etkisi.

### Dusuk Oncelik

- [ ] Section 5 hafif kisaltma — bazi paragraflar tekrar iceriyor (ozellikle implications/recommendations). Hedef: ~200-220 satir.
- [ ] Hata analizi / failure case ornekleri eklenmesi (Section 5.4 sonuna).
- [ ] `colorlinks=false` yapmak camera-ready versiyonda (review icin sorun degil).

---

## 7. Derleme Talimatlari

```bash
# Tam derleme (referanslar dahil)
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

# Hizli derleme (referanslar zaten resolve ise)
latexmk -pdf main.tex

# Temizlik
rm -f main.aux main.bbl main.blg main.out main.log main.fls main.fdb_latexmk
```

---

## 8. Springer Nature Template Ozel Notlari

| Konu | Dogru Kullanim | Yanlis Kullanim |
|---|---|---|
| Tablo alt cizgi | `\botrule` | `\bottomrule` |
| Algoritma state | `\State` | `\STATE` |
| Acknowledgements | `\bmhead{Acknowledgements}` | `\begin{acknowledgements}` |
| Abstract sirasi | `\abstract{}` → `\keywords{}` → `\maketitle` | `\maketitle` → `\abstract{}` |
| Bib style | `\bibliography{references}` (otomatik stil) | `\bibliographystyle{sn-basic}` (duplicate hata) |

---

## 9. Temel Metrikler

| Metrik | v1 (Full) | v2 (8-bit) | v3 (4-bit) |
|---|---|---|---|
| Training Loss | 0.52 | 0.45 | **0.38** |
| Validation Loss | 0.58 | 0.51 | **0.44** |
| GPU Memory (train) | 18.2 GB | 8.1 GB | **4.5 GB** |
| Inference Speed | 45 tok/s | 72 tok/s | **95 tok/s** |
| ROUGE-L | 0.48 | 0.49 | **0.51** |
| Training Time | 18h | 12h | **8h** |

| Retrieval Strategy | P@5 | R@10 | MRR |
|---|---|---|---|
| BM25 Only | 0.58 | 0.74 | 0.76 |
| Semantic Only | 0.74 | 0.87 | 0.75 |
| **Hybrid (RRF)** | **0.81** | **0.94** | **0.83** |
