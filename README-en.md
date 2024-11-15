[![en](https://img.shields.io/badge/lang-ko-red.svg)](https://github.com/tkgo11/FakeNewsDetector/blob/main/README-en.md)
<p align="center">
    <img src="icon.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">FAKENEWSDETECTOR</h1></p>
<p align="center">
	<!-- local repository, no metadata badges. --></p>
<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=default&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=default&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/Selenium-43B02A.svg?style=default&logo=Selenium&logoColor=white" alt="Selenium">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=default&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
</p>
<br>

##  Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
	- [Project Index](#project-index)
- [Getting Started](#getting-started)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
	- [Usage](#usage)
- [Project Roadmap](#project-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

##  Overview

Here's a compelling overview of the FakeNewsDetector project:

**Introducing FakeNewsDetector: Empowering Truth-Seekers

In today's digital age, it's crucial to stay informed about current events while avoiding misinformation. That's where FakeNewsDetector comes in – a cutting-edge tool designed to detect and debunk fake news. This innovative project uses AI-powered natural language processing (NLP) techniques to analyze news articles and identify potential fake news.

**Key Features:
Accurate article analysis using KeyBERT model
Real-time comparison with Naver's Open API for related news items
Cosine similarity score calculation for each article

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>The project uses a modular architecture, with separate scripts for accuracy checking, news title generation, and crawling.</li><li>It utilizes natural language processing (NLP) techniques to analyze text and identify relevant phrases.</li><li>The project relies on various APIs, including Naver's Open API and FactCheck SNU website, for data retrieval.</ul> |
| 🔩 | **Code Quality**  | <ul><li>The codebase uses Python as the primary language, with some JavaScript files for the news selector extension.</li><li>It employs popular libraries like pandas, numpy, requests, selenium, and tqdm for data manipulation and processing.</li><li>The project follows best practices for coding standards, with clear variable naming and concise function definitions.</ul> |
| 📄 | **Documentation** | <ul><li>The project has comprehensive documentation, including summaries of each code file and their purposes.</li><li>The documentation is written in Markdown format and includes links to relevant APIs and libraries.</li><li>The project uses Python as the primary language for documentation, with some JavaScript files for the news selector extension.</ul> |
| 🔌 | **Integrations**  | <ul><li>The project integrates with various APIs, including Naver's Open API and FactCheck SNU website, for data retrieval.</li><li>It uses natural language processing (NLP) techniques to analyze text and identify relevant phrases.</li><li>The project relies on web-related modules like requests and selenium for data manipulation and processing.</ul> |
| 💻 | **Tools and Technologies**  | <ul><li>Python as the primary language</li><li>JavaScript for the news selector extension</li><li>pandas, numpy, requests, selenium, and tqdm libraries for data manipulation and processing</li><li>NLP techniques for text analysis</li></ul> |

---

##  Project Structure

```sh
└── FakeNewsDetector/
    ├── accuracy_checker.py
    ├── app.py
    ├── ChromeExt.py
    ├── crawling.py
    ├── data
    │   ├── 논쟁 중.txt
    │   ├── 대체로 사실 아님.txt
    │   ├── 대체로 사실.txt
    │   ├── 사실.txt
    │   ├── 전혀 사실 아님.txt
    │   ├── 절반의 사실.txt
    │   └── 판단 유보.txt
    ├── LICENSE
    ├── main.py
    ├── news-selector
    │   ├── app.js
    │   ├── background.js
    │   ├── icon.png
    │   ├── LICENSE
    │   └── manifest.json
    └── requirements.txt
```


###  Project Index
<details open>
	<summary><b><code>FakeNewsDetector/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/accuracy_checker.py'>accuracy_checker.py</a></b></td>
				<td>- Here is a succinct summary that highlights the main purpose and use of the `accuracy_checker.py` file:

**Summarize**: The script evaluates the accuracy of news articles by comparing their descriptions with keywords extracted from the text<br>- It uses the KeyBERT model to identify relevant phrases, then retrieves related news items from Naver's Open API<br>- The script calculates a cosine similarity score for each article and assigns an accuracy rating based on this score.

**Key Points**: The script processes multiple files, extracts keywords, retrieves descriptions, and calculates scores for each file<br>- It also keeps track of total titles and average cosine similarity for each file.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/app.py'>app.py</a></b></td>
				<td>- Here is a succinct summary that highlights the main purpose and use of the code file:

The `app.py` file generates a selector based on input text by extracting keywords, retrieving related news articles, and calculating their similarity<br>- It uses natural language processing techniques to analyze the text, identify relevant nouns, and retrieve descriptions from Naver News API<br>- The resulting selector is determined by the similarity score between the input text and the retrieved descriptions.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/ChromeExt.py'>ChromeExt.py</a></b></td>
				<td>- Here is a succinct summary that highlights the main purpose and use of the `ChromeExt.py` file:

The script generates news titles from the NewsDataApiClient API and uses OpenAI's GPT-4o-mini model to analyze input text, identifying potential fake news based on provided news titles<br>- The output is written to a file named 'titles.txt'.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/crawling.py'>crawling.py</a></b></td>
				<td>- Here is a succinct summary of the main purpose and use of the `crawling.py` file:

The script crawls the FactCheck SNU website to extract titles from fact-check cards, storing them in text files<br>- It can be run in either single-threaded or multi-threaded modes, with the latter utilizing multiple threads to process pages concurrently<br>- The script also checks the server's status before running and provides a choice for users to select their preferred mode of execution.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/main.py'>main.py</a></b></td>
				<td>- The main purpose of this code file is to manage the execution flow of a project by providing options to run specific scripts based on user input<br>- It serves as an entry point, allowing users to choose between running the main application or an accuracy checker<br>- The code also handles data file integrity checks, ensuring that necessary files exist and are not empty before proceeding with the chosen action.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Facilitates project dependencies by specifying required packages and their versions<br>- This file ensures the correct installation of necessary libraries, including data manipulation tools like pandas and numpy, web-related modules such as requests and selenium, and progress tracking utilities like tqdm.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- news-selector Submodule -->
		<summary><b>news-selector</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/news-selector\app.js'>app.js</a></b></td>
				<td>- Here is a succinct summary of the provided code file:

The `app.js` file enables a news selector feature that highlights and extracts text content from an element on mouse hover or key press, allowing users to generate a unique CSS selector for the selected element<br>- The code achieves this by creating a highlighter div, updating its position and size based on the hovered element, and sending the extracted text value to a backend API to generate the selector.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/news-selector\background.js'>background.js</a></b></td>
				<td>- The `background.js` file serves as the entry point for the news selector project's functionality<br>- It listens for browser actions and executes a script on the target tab when clicked, initiating the setup process<br>- This process enables highlighting, updates the highlight upon mouse movement, captures clicks to grab selectors, and checks for termination keys.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/news-selector\manifest.json'>manifest.json</a></b></td>
				<td>- Here is a summary of the main purpose and use of the `manifest.json` file:

Define the News Selector extension's metadata, permissions, and functionality, enabling users to extract news pages and send them to a server<br>- The file specifies the background service worker, content scripts, and commands for executing actions, as well as icon and title settings.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with FakeNewsDetector, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install FakeNewsDetector using one of the following methods:

**Build from source:**

1. Clone the FakeNewsDetector repository:
```sh
❯ git clone https://github.com/tkgo11/FakeNewsDetector
```

2. Navigate to the project directory:
```sh
❯ cd FakeNewsDetector
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

###  Usage
Run FakeNewsDetector using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python main.py
```

---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Make a crawling code</strike>
- [ ] **`Task 2`**: Change crawling to multi-thread
- [ ] **`Task 3`**: Use Requests library for crawling

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/tkgo11/FakeNewsDetector/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/tkgo11/FakeNewsDetector/issues)**: Submit bugs found or log feature requests for the `FakeNewsDetector` project.
- **💡 [Submit Pull Requests](https://github.com/tkgo11/FakeNewsDetector/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your LOCAL account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone C:\Users\tkgo1\FakeNewsDetector
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to LOCAL**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com/tkgo11/FakeNewsDetector/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=tkgo11/FakeNewsDetector">
   </a>
</p>
</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://github.com/tkgo11/FakeNewsDetector/blob/main/LICENSE) file.

---

##  Acknowledgments

[grab-selector](https://github.com/adam-kov/grab-selector)

---
