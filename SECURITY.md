# Security Policy: NJine IDE

## 🛡️ Our Security Philosophy
NJine IDE is built on a **Pure Python Hybrid Agentic Architecture**. Because this tool is designed to execute Python code and potentially interact with physical hardware (ESP32 controllers, Cow Farm monitoring systems), security is our highest priority. 

We follow a "Security-by-Design" approach, but since this is an IDE, the user is ultimately responsible for the code they execute.

## 📦 Supported Versions
We only provide security patches for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| >= 0.5.x| ✅ Full Support     |
| < 0.5.x | ⚠️ Limited/Personal |

## 🚨 Reporting a Vulnerability
**Do not open a public GitHub Issue for security vulnerabilities.** Publicly disclosing a hole before a patch is ready allows others to exploit the system before it is fixed.

### The 0.5.x Rule
* **If the version is < 0.5.x:** You **MUST** email the lead developer personally at `[your-email@example.com]`. During this early alpha phase, direct communication is the only way to ensure a fast patch. 
* **If the version is >= 0.5.x:** We still recommend personal email for private disclosure, but we will also accept reports via encrypted channels if specified in later updates.

### What to Include in Your Report:
1.  **Vulnerability Type:** (e.g., Remote Code Execution, Path Traversal).
2.  **Reproduction Steps:** A clear guide or a small Python script (Proof of Concept).
3.  **Scope:** Does this affect the TUI, the LiveKit stream, or the Function Calling layer?

## 🛠️ Security Tools We Use
To keep this project solid, we run the following audits on every release:
* **Bandit:** Scans our source code for "Pythonic" security holes (like unsafe `subprocess` calls or `eval()`).
* **Safety:** Checks our `requirements.txt` for dependencies with known vulnerabilities.
* **Manual Audit:** Periodic review of the logic connecting the IDE to the **ESP32** and **LiveKit** cloud.

## 🚜 Physical Safety Warning (Hardware)
**WARNING:** This IDE is designed to control physical hardware (ESP32/Robot Cars). 
* A software security flaw could result in **physical movement** on the farm. 
* We strongly advise all users to implement **physical limit switches** and **emergency stop buttons** on their hardware. 
* The developers of NJine IDE are not responsible for physical damage caused by code execution or security breaches.

## 🚫 Non-Vulnerabilities
The following are considered **intended features**, not security bugs:
1.  **Arbitrary Code Execution:** The user's ability to run any Python code they type into the editor.
2.  **OS Access:** The IDE's ability to access files on the host machine as requested by the user's scripts.
