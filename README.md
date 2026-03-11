# Self-Healing CI Demo

This repository demonstrates a **self-healing CI workflow** using GitHub Actions and Codex.

The project simulates a development workflow where:

1. A pull request triggers CI tests.  
2. If the tests fail, a workflow invokes Codex to automatically analyze the failures.  
3. Codex attempts to fix the code.  
4. The workflow reruns the tests and commits the fix back to the branch.  
4. The new commit triggers **CI and Grade again**.
5. After the second run, a **PR comment is posted summarizing the changes made by the AI agent**.

The goal is to showcase how **AI-assisted automation** can help maintain code quality and speed up debugging in CI pipelines.

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

The pull request is automatically graded based on the following criteria:

Scoring rules:

- **6 pts** → All tests pass  
- **2 pts** → The `tests/` directory was not modified  
- **2 pts** → The `src/` directory was modified 

The workflow posts the score as a comment on the pull request.

------------------------------------------------------------------------


## AI Auto-fix Summary Comment

After the fix is applied and validated, the workflow adds a comment to the Pull Request that includes:

- The **AI-generated commit message**
- The **files modified by the agent**
- A **diff summary showing the changes introduced**
- A short **patch preview of the modifications**

This provides transparency so reviewers can quickly understand **what the AI agent changed and why the CI pipeline passed after the fix**.


------------------------------------------------------------------------

# Purpose of the Project

This repository demonstrates how **AI agents can be integrated into
CI/CD pipelines** to automatically detect and repair issues, creating a
**self-healing development workflow**.

Such systems can help: - reduce debugging time - automate routine
fixes - maintain CI stability - improve developer productivity
