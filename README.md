🌍 Climate Disclosure Analysis with Text Mining (Data Science)

📌 Overview:
This repository contains the code and data of the manuscript:
Assessment of TCFD voluntary disclosure compliance in the Spanish energy sector: A text mining approach to climate change financial disclosures.

📌 General description: 
This study investigates the voluntary implementation of the Task Force on Cli-mate-related Financial Disclosures (TCFD) framework in 64 annual sustainability re-ports (2020-2024) of six Spanish energy companies listed on IBEX-35. The methodology includes advanced text mining (TM) techniques, such as named entity recognition (NER) and full-text searches (FTS), to ensure a comprehensive analysis. We evaluated the 11 recommended disclosures to assess their quality, extent, and relevance, as well as 70 specific concepts based on TM analyses and previous report evaluations, to con-struct an index of TCFD compliance. The results show year-on-year improvements in compliance with the TCFD. The TM technique reveals that Iberdrola and Repsol lead governance and risk disclosure, whereas Enagás and REE show inconsistencies in re-silience and emissions, posing reputational risks. Significant progress has been made in 11 aspects of reporting quality, scope, and relevance to stakeholders. The index shows disclosure inequality for 70 specific concepts. The conclusions are that the energy sec-tor drives political-social change against climate change, progress in opportunities and challenges remains, and reinforces the need for mandatory climate financial reporting standards. Future research will analyze the TCFD framework to assess intangible business assets and the impact of regulatory implementation on sustainability reports using TM. The originality, implications, and empirical evidence provide a multidisci-plinary perspective using text mining, revealing key patterns, and promoting trans-parency for stakeholders

🏗 Repository structure
│─── *,txt files of examples of processed files (preprocessed, dirty and clean text for example).
│── *.py files to execute different parts of the methodology
│─── *.PDF files examples of reports discussed
│─── requirements.txt / como ejecutarlo.txt # Python dependencies
│─── README.md # This file
📁 data/ – (or the name of your folder - Not included) Place corporate reports here before running the notebook.
📁 results/ – (or the name of your folder - Not included )Stores generated figures and tables from the analysis.

🚀 Getting Started
1️⃣ Clone this repository
2️⃣ Install dependencies
Ensure you have Python 3.8+ installed. Then, install the required packages:
pip install -r requirements.txt / como ejecutarlo.txt
3️⃣ Prepare the data
Download corporate sustainability reports from:
The analyzed PDF reports were obtained from six corporate website officials of the companies studied.
Web site Enagás: https://www.enagas.es/es/
Web site Endesa: https://www.endesa.com/
Web site Iberdrola: https://www.iberdrola.es/
Web site Naturgy: https://www.naturgy.com/
Web site Redaia: https://www.redaia.com/
Web site Repsol: https://www.repsol.com/es/index.cshtml
Place PDF reports inside the data/ folder (or the name of your folder)
4️⃣ Run the program
Run the notebook step by step to reproduce the analysis.

⚙ Features & Methods
1. Definition and Objectives: This study investigated whether the analyzed companies
comply with the TCFD framework using TM in the financial reporting of annual and sustainability reports.
We collected and preprocessed 64 reports from six publicly.
traded companies in the Spanish energy sector of IBEX-35 between 2020 and 2023.
3. Tools and Resources used: Reports were manually downloaded in PDF format and hosted in a shared Microsoft OneDrive space. They were sorted and formatted using Adobe Pro X and converted into Microsoft Word format. The software used was, Python v. 3.11  Python-docx v.1.1.2, and pdfplumber v.0.11.4 libraries were used to read the documents, whereas the spaCy v.3.8.4 library facilitated tokenization. Whoosh v.2.7.4 was employed for full-text searches. Microsoft Excel was used to compile and analyze the results. The phrase consists of a series of commands used in a programming environment, specifically Python, to install libraries and download a natural language processing model

📊 Key findings:
Continuous improvements in compliance with the TCFD.
Differences in the quality of disclosures.
Climate change potential of the sector.

📜 License
This repository is licensed under the MIT License. See LICENSE for details.

🤝 Contributing
Feel free to contribute! Open an issue or pull request if you have suggestions for improvements.

📬 Contact
For questions or collaboration inquiries, contact:
📧 [matiasdo@ucm.es]]
