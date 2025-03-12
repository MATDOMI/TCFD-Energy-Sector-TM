This repository contains the code and data of the manuscript:
Assessment of TCFD voluntary disclosure compliance in the Spanish energy sector: A text mining approach to climate change financial disclosures.

📌 General description: 
This study investigates the voluntary implementation of the Task Force on Cli-mate-related Financial Disclosures (TCFD) framework in 64 annual sustainability re-ports (2020-2023) of six Spanish energy companies listed on IBEX-35. The methodology includes advanced text mining (TM) techniques, such as named entity recognition (NER) and full-text searches (FTS), to ensure a comprehensive analysis. We evaluated the 11 recommended disclosures to assess their quality, extent, and relevance, as well as 70 specific concepts based on TM analyses and previous report evaluations, to con-struct an index of TCFD compliance. The results show year-on-year improvements in compliance with the TCFD. The TM technique reveals that Iberdrola and Repsol lead governance and risk disclosure, whereas Enagás and REE show inconsistencies in re-silience and emissions, posing reputational risks. Significant progress has been made in 11 aspects of reporting quality, scope, and relevance to stakeholders. The index shows disclosure inequality for 70 specific concepts. The conclusions are that the energy sec-tor drives political-social change against climate change, progress in opportunities and challenges remains, and reinforces the need for mandatory climate financial reporting standards. Future research will analyze the TCFD framework to assess intangible business assets and the impact of regulatory implementation on sustainability reports using TM. The originality, implications, and empirical evidence provide a multidisci-plinary perspective using text mining, revealing key patterns, and promoting trans-parency for stakeholders

🏗 Repository structure
_1.Journal_DATA.docx # Basis for the document in 'PAPER' format from the journal DATA, published by MDPI.
world-3533625.pdf # Submitted to MDPI publisher at Journal World : Paper PDF
│─── *,txt files of examples of processed files (preprocessed, dirty and clean text for example).
│── *.py files to execute different parts of the methodology
│─── *.PDF files examples of reports discussed
│─── requirements.txt / how to run it # Python dependencies
│─── README.md # This file

⚙ Features & Methods
1. Definition and Objectives: This study investigated whether the analyzed companies 263
comply with the TCFD framework using TM in the financial reporting of annual and 264
sustainability reports. We collected and preprocessed 64 reports from six publicly 265
traded companies in the Spanish energy sector of IBEX-35 between 2020 and 2023. 266
2. Tools and Resources used: Reports were manually downloaded in PDF format and 267
hosted in a shared Microsoft OneDrive space. They were sorted and formatted using 268
Adobe Pro X and converted into Microsoft Word format. Python v. 3.11, and the Py- 269
thon-docx v.1.1.2 and pdfplumber v.0.11.4 libraries were used to read the documents, 270
whereas the spaCy v.3.8.4 library facilitated tokenization. Whoosh v.2.7.4 was em- 271
ployed for full-text searches. Microsoft Excel was used to compile and analyze the 272
results.
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
