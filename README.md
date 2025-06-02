# Ref2DOI
### 🔍 What does it do?

**Ref2DOI** extracts the DOI and title of each reference from a plain text reference list (copied from one or more academic papers). It uses text analysis tools to process the references and outputs three text files:

* `dois.txt` – Contains the extracted DOIs
* `titles.txt` – Contains the extracted titles
* `differences.txt` – A list of references that might not have been correctly identified (so you can manually verify them)

You can use the `dois.txt` file with this free tool to generate a `.RIS` file for easy import into EndNote, Zotero, or Mendeley:
👉 [CitationChaser](https://estech.shinyapps.io/citationchaser)

This tool is especially helpful when dealing with reference lists from **unpublished** theses or articles. For already published papers, the website above can often extract references automatically.

---

### 🧰 Requirements (for Windows):

1. **Install Python**
   [Download Python 3.10.11](https://www.python.org/downloads/release/python-31011/)
   ⚠️ Make sure to check "Add Python to PATH" during installation.

2. **Install Ruby**
   [Download RubyInstaller 3.4.4-2 (x64)](https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.4.4-2/rubyinstaller-devkit-3.4.4-2-x64.exe)
   ⚠️ After installation, follow the MSYS2 setup (`ridk install`) and install all three suggested items.

3. **Install dependencies**

   * Install `anystyle-cli` (used for citation parsing):

     ```bash
     gem install anystyle-cli
     ```

---

### 🚀 How to use

1. Run the `Ref2DOI.bat` file (double-click or run via CMD).
2. Paste your reference list into the prompt:
   * One reference per line
   * No empty lines between references
   * Format-check your list in VSCode if needed

3. Hit Enter — processing begins.
4. After a short while, the output files will be saved in a folder named `exports`.

   * Input example:
     ```bash
      1.	Araujo C, Silva T, Ogliari F, Meireles S, Piva E, Demarco F. Microleakage of seven adhesive systems in enamel and dentin. J Contemp Dent Pract. 2006;7(5):26-33.
      2.	Takamizawa T, Barkmeier WW, Tsujimoto A, Berry TP, Watanabe H, Erickson RL, et al. Influence of different etching modes on bond strength and fatigue strength to dentin using universal adhesive systems. Dental Materials. 2016;32(2):e9-e21.
      3.	Imai A, Takamizawa T, Sai K, Tsujimoto A, Nojiri K, Endo H, et al. Influence of application method on surface free‐energy and bond strength of universal adhesive systems to enamel. European Journal of Oral Sciences. 2017;125(5):385-95.
      4.	Ferracane JL. Resin composite—state of the art. Dental materials. 2011;27(1):29-38.
      5.	Grégoire G, Guignes P, Nasr K. Effects of dentine moisture on the permeability of total-etch and one-step self-etch adhesives. journal of dentistry. 2009;37(9):691-9.
      6.	Shin TP, Yao X, Huenergardt R, Walker MP, Wang Y. Morphological and chemical characterization of bonding hydrophobic adhesive to dentin using ethanol wet bonding technique. Dental Materials. 2009;25(8):1050-7.
     ```
     * output:
     ```bash
      Extracted Titles:
      1. Microleakage of seven adhesive systems in enamel and dentin
      2. Influence of different etching modes on bond strength and fatigue strength to dentin using universal adhesive systems
      3. Influence of application method on surface free‐energy and bond strength of universal adhesive systems to enamel
      4. Resin composite—state of the art
      5. Effects of dentine moisture on the permeability of total-etch and one-step self-etch adhesives
      6. Morphological and chemical characterization of bonding hydrophobic adhesive to dentin using ethanol wet bonding technique

      DOIs:
      10.5005/jcdp-7-5-26, 10.1016/j.dental.2015.11.005, 10.1111/eos.12361, 10.1016/j.dental.2010.10.020, 10.1016/j.jdent.2009.05.010, 10.1016/j.dental.2009.03.006
     ```

---

### 💡 Additional Notes

* The tool is tested on **Windows**, but it can also run on **macOS** and **Linux** — just make sure to install the appropriate versions of Python and Ruby and run the script manually (since `.bat` files only work on Windows).
