# Workflow-Tutorial

[![Test C++](https://github.com/InnocentBug/workflow-tutorial/actions/workflows/test_cpp.yml/badge.svg)](https://github.com/InnocentBug/workflow-tutorial/actions/workflows/test_cpp.yml)
[![Test Python](https://github.com/InnocentBug/workflow-tutorial/actions/workflows/test_python.yml/badge.svg)](https://github.com/InnocentBug/workflow-tutorial/actions/workflows/test_python.yml)
[![Trunk](https://github.com/InnocentBug/workflow-tutorial/actions/workflows/trunk.yml/badge.svg)](https://github.com/InnocentBug/workflow-tutorial/actions/workflows/trunk.yml)

This is a tutorial repository that demonstrates how to set up a GitHub workflow for two independent projects, one in Python and the other in C++.

## C++ Project

The C++ project is located in the [`src`](src/) directory. The project uses CMake for building, and tests are included via CMake as well.

You can check the workflow file for this project at [`.github/workflows/test_cpp.yml`](.github/workflows/test_cpp.yml).

## Python Project

The Python project is located in [`magic_python`](magic_python/) and is fully set up as a module. Tests are run using `pytest`.

You can check the workflow file for this project at [`.github/workflows/test_python.yml`](.github/workflows/test_python.yml).

### Jupyter Notebooks

Python project may be accompanied by jupyter notebooks, usually we want to make sure that these notebooks do not break during the development of the project.
So an automated test of the notebooks is a good idea.

You can check the workflow file that automatically runs a jupyter notebooks here [`.github/workflows/test_jupyter.yml`](.github/workflows/test_jupyter.yml).

## Trunk

We use [trunk.io](https://trunk.io) to manage formatting and software engineering. It is free for open-source projects; please refer to their website for more details.

You can check the workflow file for this project at [`.github/workflows/trunk.yml`](.github/workflows/trunk.yml). This workflow ensures that everything is up to standard.

## Notes

Extra notes for the process are included below. These can be ignored.

1. Create a repository, set it to public, apply MIT license, add a Python gitignore, and clone it.
2. Protect the `main` branch via `Settings > Branches > Add Protection Rule`. The settings should include requiring a PR, requiring approvals (optional), dismissing stale pull request reviews, requiring status checks, and requiring the branch to be up-to-date.
3. Add labels to PR, assign yourself to PR, squash and merge PR.
4. Add the C++ program, but not the test. Push and open a PR.
5. Add a simple workflow to test.
6. Add CMake to build and test.
7. Create badges via `Actions > workflow name > [...] > create status badge > add text`.
