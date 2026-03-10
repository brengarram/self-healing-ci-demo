# Self-Healing CI Demo

This repository demonstrates a **self-healing CI workflow** using GitHub
Actions and Codex.

The project simulates a development workflow where: 1. A pull request
triggers CI tests. 2. If the tests fail, a workflow can invoke **Codex**
to automatically analyze the failures. 3. Codex attempts to fix the
code. 4. The workflow reruns the tests and commits the fix back to the
branch. 5. A grading workflow evaluates the pull request based on
predefined criteria.

The goal is to showcase how **AI-assisted automation** can help maintain
code quality and speed up debugging in CI pipelines.

------------------------------------------------------------------------

# Repository Components

This repo contains three main workflows:

### CI Workflow

Runs automatically on pull requests and executes the test suite.

### Codex Auto-fix Workflow

A manually triggered workflow that attempts to automatically repair
failing functions using Codex.

### Grade Workflow

Evaluates pull requests and assigns a score based on test results and
code quality constraints.

------------------------------------------------------------------------

# Project Structure

    src/
        contact_utils.py

    tests/
        test_contact_utils.py

    .codex/
        commands/
            fix-ci.md

    .github/workflows/
        ci.yml
        codex-autofix.yml
        grade.yml

------------------------------------------------------------------------

# Run Tests Locally

Install dependencies and run tests:

``` bash
uv sync
uv run pytest -q
```

------------------------------------------------------------------------

# Run CI

Open a pull request.\
The CI workflow runs automatically and executes the test suite.

------------------------------------------------------------------------

# Run Auto-fix Workflow

If a pull request contains failing tests, the **Codex Auto-fix
workflow** can attempt to repair the code.

Steps:

1.  Push a failing branch.
2.  Go to **GitHub → Actions**.
3.  Select **Codex Auto-fix**.
4.  Click **Run workflow**.
5.  Enter the branch name.
6.  Run it.

The workflow will:

-   run the tests
-   analyze failures
-   call Codex with a repair command
-   apply code fixes
-   rerun the tests
-   commit and push the patch to the branch

If the fix succeeds, the CI pipeline should turn green.

------------------------------------------------------------------------

# How Grading Works

The **grade workflow** runs automatically on pull request updates and
calculates a score.

Scoring rules:

-   **6 points** if tests pass
-   **2 points** if the `tests/` folder was not modified
-   **2 points** if the code diff remains small

The workflow posts the score as a comment on the pull request.

------------------------------------------------------------------------

# Purpose of the Project

This repository demonstrates how **AI agents can be integrated into
CI/CD pipelines** to automatically detect and repair issues, creating a
**self-healing development workflow**.

Such systems can help: - reduce debugging time - automate routine
fixes - maintain CI stability - improve developer productivity
