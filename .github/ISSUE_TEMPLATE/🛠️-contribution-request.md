---
name: "\U0001F6E0️ Contribution Request"
about: Use this to propose a fix or a specific change you want to work on.
title: ''
labels: ''
assignees: ''

---

name: 🛠️ Contribution Request
description: Request to work on a bug fix, improvement, or specific task.
title: "[CONTRIB]: "
labels: ["contribution-request"]
body:
  - type: markdown
    attributes:
      value: |
        ## 🛡️ PurePy IDE Developer Portal
        Use this form to request permission to work on a specific part of the codebase. 
        **Note:** Do not start coding until this request is approved to ensure it aligns with the Pure Python vision.

  - type: input
    id: developer_name
    attributes:
      label: Full Name / GitHub Handle
      placeholder: e.g., @python_master_99
    validations:
      required: true

  - type: dropdown
    id: contrib_type
    attributes:
      label: What are you contributing?
      options:
        - Bug Fix
        - UI/TUI Polishing
        - Documentation
        - Performance Optimization
        - Refactoring
    validations:
      required: true

  - type: textarea
    id: proposal
    attributes:
      label: Detailed Proposal
      description: What specific part of the IDE are you planning to touch?
      placeholder: I want to optimize the syntax highlighting engine...
    validations:
      required: true

  - type: input
    id: dependencies
    attributes:
      label: New Dependencies?
      description: Will this add any new Python packages? (Remember: NO non-Python libs allowed).
      placeholder: e.g., None or 'rich-pixels'
    validations:
      required: false

  - type: checkboxes
    id: terms
    attributes:
      label: Development Standards
      options:
        - label: I confirm this code is 100% Pure Python.
          required: true
        - label: I have read the SECURITY.md regarding version < 0.5.x.
          required: true
        - label: I acknowledge this work will be licensed under AGPL v3.0.
          required: true
        - label: I will run 'Bandit' and 'Safety' checks before submitting a PR.
          required: true
