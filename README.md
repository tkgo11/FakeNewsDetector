[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/tkgo11/FakeNewsDetector/blob/main/README-en.md)
<p align="center">
    <img src="icon.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">FAKENEWSDETECTOR</h1></p>
<p align="center">
	<!-- 로컬 저장소, 메타데이터 배지 없음. --></p>
<p align="center">이 도구와 기술로 제작됨:</p>
<p align="center">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=default&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=default&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/Selenium-43B02A.svg?style=default&logo=Selenium&logoColor=white" alt="Selenium">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=default&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=default&logo=pandas&logoColor=white" alt="pandas">
</p>
<br>

## 목차

- [목차](#목차)
- [개요](#개요)
- [기능](#기능)
- [프로젝트 구조](#프로젝트-구조)
  - [프로젝트 인덱스](#프로젝트-인덱스)
- [시작하기](#시작하기)
  - [필수 조건](#필수-조건)
  - [설치](#설치)
  - [사용법](#사용법)
- [프로젝트 로드맵](#프로젝트-로드맵)
- [기여하기](#기여하기)
- [라이선스](#라이선스)
- [감사의 말](#감사의-말)

---

## 개요

FakeNewsDetector 프로젝트에 대한 개요:

**FakeNewsDetector 소개: 진실을 찾는 사람들을 위한 도구

오늘날의 디지털 시대에는 현재 사건에 대한 정보를 얻으면서도 잘못된 정보를 피하는 것이 중요합니다. FakeNewsDetector는 바로 그런 역할을 합니다. 이 혁신적인 도구는 AI 기반 자연어 처리(NLP) 기술을 사용하여 뉴스 기사를 분석하고 잠재적인 가짜 뉴스를 식별합니다.

**주요 기능:
KeyBERT 모델을 사용한 정확한 기사 분석
Naver의 Open API와의 실시간 비교를 통한 관련 뉴스 항목 확인
각 기사에 대한 코사인 유사도 점수 계산

---

## 기능

|      | 기능         | 요약       |
| :--- | :---:           | :---          |
| ⚙️  | **아키텍처**  | <ul><li>프로젝트는 정확도 검사, 뉴스 제목 생성, 크롤링을 위한 별도의 스크립트를 사용하여 모듈식 아키텍처를 사용합니다.</li><li>텍스트를 분석하고 관련 구문을 식별하기 위해 자연어 처리(NLP) 기술을 활용합니다.</li><li>데이터 검색을 위해 Naver의 Open API 및 FactCheck SNU 웹사이트를 포함한 다양한 API를 사용합니다.</ul> |
| 🔩 | **코드 품질**  | <ul><li>코드베이스는 Python을 주요 언어로 사용하며, 뉴스 선택기 확장을 위한 일부 JavaScript 파일을 포함합니다.</li><li>데이터 조작 및 처리를 위해 pandas, numpy, requests, selenium, tqdm과 같은 인기 있는 라이브러리를 사용합니다.</li><li>코딩 표준에 대한 모범 사례를 따르며, 명확한 변수 명명 및 간결한 함수 정의를 제공합니다.</ul> |
| 📄 | **문서화** | <ul><li>프로젝트는 각 코드 파일의 요약 및 목적을 포함한 포괄적인 문서를 제공합니다.</li><li>문서는 Markdown 형식으로 작성되었으며 관련 API 및 라이브러리에 대한 링크를 포함합니다.</li><li>프로젝트는 문서화를 위해 Python을 주요 언어로 사용하며, news selector 확장을 위한 일부 JavaScript 파일을 포함합니다.</ul> |
| 🔌 | **통합**  | <ul><li>프로젝트는 데이터 검색을 위해 Naver의 Open API 및 FactCheck SNU 웹사이트를 포함한 다양한 API와 통합됩니다.</li><li>텍스트를 분석하고 관련 구문을 식별하기 위해 자연어 처리(NLP) 기술을 사용합니다.</li><li>데이터 조작 및 처리를 위해 requests 및 selenium과 같은 웹 관련 모듈을 사용합니다.</ul> |
| 💻 | **도구 및 기술**  | <ul><li>Python을 주요 언어로 사용</li><li>뉴스 선택기 확장을 위한 JavaScript</li><li>데이터 조작 및 처리를 위한 pandas, numpy, requests, selenium, tqdm 라이브러리</li><li>텍스트 분석을 위한 NLP 기술</li></ul> |

---

## 프로젝트 구조

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

### 프로젝트 인덱스
<details open>
	<summary><b><code>FakeNewsDetector/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/accuracy_checker.py'>accuracy_checker.py</a></b></td>
				<td>- `accuracy_checker.py` 파일의 주요 목적과 사용을 강조하는 간결한 요약:

**요약**: 이 스크립트는 텍스트에서 추출한 키워드와 설명을 비교하여 뉴스 기사의 정확성을 평가합니다<br>- KeyBERT 모델을 사용하여 관련 구문을 식별한 후 Naver의 Open API에서 관련 뉴스 항목을 검색합니다<br>- 각 기사에 대한 코사인 유사도 점수를 계산하고 이 점수를 기반으로 정확도 등급을 부여합니다.

**주요 포인트**: 이 스크립트는 여러 파일을 처리하고, 키워드를 추출하고, 설명을 검색하고, 각 파일에 대한 점수를 계산합니다<br>- 또한 각 파일에 대한 총 제목 수와 평균 코사인 유사도를 추적합니다.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/app.py'>app.py</a></b></td>
				<td>- 코드 파일의 주요 목적과 사용을 강조하는 간결한 요약:

`app.py` 파일은 입력 텍스트를 기반으로 선택기를 생성하여 키워드를 추출하고 관련 뉴스 기사를 검색하며 유사성을 계산합니다<br>- 텍스트를 분석하고 관련 명사를 식별하며 Naver 뉴스 API에서 설명을 검색하기 위해 자연어 처리 기술을 사용합니다<br>- 결과 선택기는 입력 텍스트와 검색된 설명 간의 유사도 점수에 의해 결정됩니다.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/ChromeExt.py'>ChromeExt.py</a></b></td>
				<td>- `ChromeExt.py` 파일의 주요 목적과 사용을 강조하는 간결한 요약:

이 스크립트는 NewsDataApiClient API에서 뉴스 제목을 생성하고 OpenAI의 GPT-4o-mini 모델을 사용하여 입력 텍스트를 분석하여 제공된 뉴스 제목을 기반으로 잠재적인 가짜 뉴스를 식별합니다<br>- 출력은 'titles.txt'라는 파일에 기록됩니다.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/crawling.py'>crawling.py</a></b></td>
				<td>- `crawling.py` 파일의 주요 목적과 사용에 대한 간결한 요약:

이 스크립트는 FactCheck SNU 웹사이트를 크롤링하여 팩트체크 카드에서 제목을 추출하고 이를 텍스트 파일에 저장합니다<br>- 단일 스레드 또는 멀티 스레드 모드로 실행할 수 있으며, 후자는 여러 스레드를 사용하여 페이지를 동시에 처리합니다<br>- 스크립트는 실행 전에 서버의 상태를 확인하고 사용자가 선호하는 실행 모드를 선택할 수 있는 옵션을 제공합니다.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/main.py'>main.py</a></b></td>
				<td>- 이 코드 파일의 주요 목적은 사용자 입력에 따라 특정 스크립트를 실행할 수 있는 옵션을 제공하여 프로젝트의 실행 흐름을 관리하는 것입니다<br>- 메인 애플리케이션 또는 정확도 검사기를 실행할 수 있는 진입점 역할을 합니다<br>- 코드 또한 데이터 파일 무결성 검사를 처리하여 필요한 파일이 존재하고 비어 있지 않은지 확인한 후 선택한 작업을 진행합니다.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- 필요한 패키지와 버전을 지정하여 프로젝트 종속성을 관리합니다<br>- 이 파일은 pandas 및 numpy와 같은 데이터 조작 도구, requests 및 selenium과 같은 웹 관련 모듈, tqdm과 같은 진행 추적 유틸리티를 포함한 필수 라이브러리의 올바른 설치를 보장합니다.</td>
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
				<td>- 제공된 코드 파일의 간결한 요약:

`app.js` 파일은 마우스 오버 또는 키 누름 시 요소에서 텍스트 콘텐츠를 강조하고 추출하여 사용자가 선택한 요소에 대한 고유한 CSS 선택기를 생성할 수 있는 뉴스 선택기 기능을 활성화합니다<br>- 이 코드는 하이라이터 div를 생성하고, 마우스 오버된 요소에 따라 위치와 크기를 업데이트하며, 추출된 텍스트 값을 백엔드 API로 보내 선택기를 생성합니다.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/news-selector\background.js'>background.js</a></b></td>
				<td>- `background.js` 파일은 뉴스 선택기 프로젝트의 기능을 위한 진입점 역할을 합니다<br>- 브라우저 동작을 수신하고 클릭 시 대상 탭에서 스크립트를 실행하여 설정 프로세스를 시작합니다<br>- 이 프로세스는 강조 표시를 활성화하고, 마우스 이동 시 강조 표시를 업데이트하며, 클릭을 캡처하여 선택기를 가져오고 종료 키를 확인합니다.</td>
			</tr>
			<tr>
				<td><b><a href='C:\Users\tkgo1\FakeNewsDetector/blob/master/news-selector\manifest.json'>manifest.json</a></b></td>
				<td>- `manifest.json` 파일의 주요 목적과 사용에 대한 요약:

뉴스 페이지를 추출하여 서버로 보내는 기능을 제공하는 뉴스 선택기 확장의 메타데이터, 권한 및 기능을 정의합니다<br>- 파일은 백그라운드 서비스 워커, 콘텐츠 스크립트 및 작업 실행을 위한 명령을 지정하며, 아이콘 및 제목 설정을 포함합니다.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 시작하기

### 필수 조건

FakeNewsDetector를 시작하기 전에 실행 환경이 다음 요구 사항을 충족하는지 확인하세요:

- **프로그래밍 언어:** Python
- **패키지 관리자:** Pip

### 설치

다음 방법 중 하나를 사용하여 FakeNewsDetector를 설치하세요:

**소스에서 빌드:**

1. FakeNewsDetector 저장소를 클론합니다:
```sh
❯ git clone https://github.com/tkgo11/FakeNewsDetector
```

2. 프로젝트 디렉토리로 이동합니다:
```sh
❯ cd FakeNewsDetector
```

3. 라이브러리를 설치합니다:


**`pip` 사용** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

### 사용법
다음 명령을 사용하여 FakeNewsDetector를 실행하세요:
**`pip` 사용** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python main.py
```

---
## 프로젝트 로드맵

- [X] **`Task 1`**: <strike>크롤링 코드 만들기</strike>
- [ ] **`Task 2`**: 크롤링을 멀티 스레드로 변경하기
- [ ] **`Task 3`**: 크롤링에 Requests 라이브러리 사용하기

---

## 기여하기

- **💬 [Discussions 참여하기](https://github.com/tkgo11/FakeNewsDetector/discussions)**: 인사이트를 공유하고, 피드백을 제공하거나 질문하세요.
- **🐛 [Issues 보고하기](https://github.com/tkgo11/FakeNewsDetector/issues)**: `FakeNewsDetector` 프로젝트에 대한 버그를 제출하거나 기능 요청을 기록하세요.
- **💡 [Pull requests 제출하기](https://github.com/tkgo11/FakeNewsDetector/pulls)**: 열린 PR을 검토하고, 자신의 PR을 제출하세요.

<details closed>
<summary>기여 가이드라인</summary>

1. **저장소 포크하기**: 프로젝트 저장소를 자신의 계정으로 포크하세요.
2. **로컬로 클론하기**: git 클라이언트를 사용하여 포크한 저장소를 로컬 머신에 클론하세요.
   ```sh
   git clone C:\Users\tkgo1\FakeNewsDetector
   ```
3. **새 브랜치 생성하기**: 항상 새 브랜치에서 작업하고, 설명적인 이름을 부여하세요.
   ```sh
   git checkout -b new-feature-x
   ```
4. **변경 사항 적용하기**: 로컬에서 변경 사항을 개발하고 테스트하세요.
5. **변경 사항 커밋하기**: 업데이트를 설명하는 명확한 메시지로 커밋하세요.
   ```sh
   git commit -m '새 기능 x 구현.'
   ```
6. **로컬로 푸시하기**: 포크한 저장소로 변경 사항을 푸시하세요.
   ```sh
   git push origin new-feature-x
   ```
7. **풀 리퀘스트 제출하기**: 원래 프로젝트 저장소에 대해 PR을 생성하세요. 변경 사항과 그 동기를 명확히 설명하세요.
8. **검토**: PR이 검토되고 승인되면 메인 브랜치에 병합됩니다. 기여를 축하합니다!
</details>

<details closed>
<summary>기여자 그래프</summary>
<br>
<p align="left">
   <a href="https://github.com/tkgo11/FakeNewsDetector/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=tkgo11/FakeNewsDetector">
   </a>
</p>
</details>

---

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 보호됩니다. 자세한 내용은 [LICENSE](https://github.com/tkgo11/FakeNewsDetector/blob/main/LICENSE) 파일을 참조하세요.

---

## 감사의 말

[grab-selector](https://github.com/adam-kov/grab-selector)

---
