# Self-Healing CI Demo

This repository demonstrates a **self-healing CI workflow** using GitHub Actions and Codex.

The project simulates a development workflow where:
1. A pull request triggers CI tests.
2. If the tests fail, a workflow can invoke **Codex** to automatically analyze the failures.
3. Codex attempts to fix the code.
4. The workflow reruns the tests and commits the fix back to the branch.
5. A grading workflow evaluates the pull request based on predefined criteria.

The goal is to showcase how **AI-assisted automation** can help maintain code quality and speed up debugging in CI pipelines.

---

# Repository Components

This repo contains three main workflows:

### CI Workflow
Runs automatically on pull requests and executes the test suite.

### Codex Auto-fix Workflow
A manually triggered workflow that attempts to automatically repair failing tests using Codex.

### Grade Workflow
Evaluates pull requests and assigns a score based on test results and code quality constraints.

---

# Project Structure
