# Rule-Based AI Logic Engine (v1.0)

A deterministic, high-efficiency "White Box" AI Chatbot interface built on the Input-Process-Output (IPO) model. [cite_start]This system represents the fundamental architectural control layer used in modern AI guardrail frameworks (such as NVIDIA NeMo and Llama Guard) to filter, sanitize, and control probabilistic outputs.

---

## 🧠 Architectural Overview

Before managing the unpredictability of a generative probability engine, an AI engineer must master the precision of a logic engine. This project intentionally avoids linear `if-elif` conditional ladders—which suffer from structural instability and $O(n)$ time complexity —and implements a highly scalable **Hash Map / Dictionary** configuration operating at **$O(1)$ constant time complexity**

The engineering pipeline follows a transparent, hardcoded **Input-Process-Output (IPO) Architecture** ensuring 100% safety and zero hallucination risk

1. **Input & Sanitization (Phase 1):** Takes raw text feed and standardizes it using case-folding and whitespace removal (`.lower().strip()`) to eliminate data entry inconsistencies.
2. **Process / Logic Skeleton (Phase 2):** Performs an instantaneous intent matching operation against a hardcoded knowledge base.
3. **Output & Fallback Protection (Phase 3):** Serves exact-match responses via an atomic lookup query, instantly returning a safe, predefined fallback response if the user query is unmapped.

---

## 🛠️ Tech Stack & Skills Showcased

* **Language:** Python 3.x
* **GUI Framework:** Tkinter (scrolledtext widgets, custom key bindings)
* **Data Structures:** Python Dictionaries (Hash Maps) 
* **Design Patterns:** Input-Process-Output (IPO) Model, Event-Driven Architecture, Deterministic Guardrails 
* **Algorithmic Efficiency:** $O(1)$ Constant lookup execution time 

---
