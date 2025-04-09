"""Marimo demo."""

import marimo

__generated_with = "0.12.0"
app = marimo.App(width="medium", app_title="Intro to Marimo notebooks")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Introduction to marimo notebooks""")
    return


@app.cell
def _(mo):
    a = 2

    mo.md(f"""
    ## Improve reproducibility - part 1 : DAG

    Value from one cell...
    ```
    a = {a}
    ```
    """)
    return (a,)


@app.cell
def cell_2(a, mo):
    b = a + 5

    mo.md(f"""
    ... will change in all other cells...
    ```
    b = a + 2 = {a} + 2 = {a + 2}
    ```
    """)
    return (b,)


@app.cell
def _(a, b, mo):
    c = a + b

    mo.md(f"""
    ... ALL other cells
    ```
    c = a + b = {a} + {b} = {a + b}
    ```
    """)
    return (c,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This all based on a Directed Acyclic Graph.

        Viewable in the side panel ⬅️
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        So your cells will always be executed in the correct order,
        no matter the order of your cells.

        You can totally have your imports [at the end](#imports).
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Side effect

        Variables cannot be redefined.

        Try renaming the following variable from `_a` to `a` and run the cell.
        """
    )
    return


@app.cell(disabled=True)
def _():
    _a = "2"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Qualite of life improvements: it's just python !!""")
    return


@app.cell(hide_code=True)
def _(mo, show_intro_nb):
    mo.md(show_intro_nb())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""All cells are just function with `app.cell()` decorator.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        You can also just do:

        ```bash
        python notebooks/mo_intro.py
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    from nilearn.datasets import load_mni152_template
    from nilearn.plotting import plot_img, show

    template = load_mni152_template()
    fig = plot_img(template)
    show()

    mo.md("""
    ## Improve reproducibility - part 2 : dependency tracking

    This cell imports things from nilearn
    but if I have not declared in my dependencies (in a requirements.txt, pyproject.toml...)
    which version of of nilearn I am using
    the results of my notebook may vary.

    So let's rerun the notebook but in 'sandbox' mode:

    ```bash
    marimo edit --sandbox notebooks/mo_intro.py
    ```

    This will create a virtual environment with uv and installed the required dependencies.

    ```
    Running in a sandbox: uv run --isolated --no-project --with-requirements /tmp/tmpu9dq4o5f.txt --refresh marimo edit mo_intro.py
    Installed 35 packages in 32ms
    ```

    You will then be prompted to install any missing dependencies.

    This will also detect optional dependencies required for some import.
    Here you will also get an extra prompt to install matplotlib as it is required for nilearn plotting.
    """)
    return fig, load_mni152_template, plot_img, show, template


@app.cell(hide_code=True)
def _(mo, show_intro_nb):
    mo.vstack(
        [
            mo.md(
                """
        Notice how the beginning of the notebook was updated
        with toml-like definition of the dependencies of the notebook.
        """
            ),
            mo.md(show_intro_nb("@app")),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Cells can be tested !!!!""")
    return


@app.cell
def function_to_test():
    def function_to_test(a):
        return a + 1

    return (function_to_test,)


@app.cell
def test_function(function_to_test):
    assert function_to_test(3) == 4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Name cells that contain a "test_..." and run pytest on your notebook.

        ```bash
        $ pytest notebooks/mo_intro.py

        ================================================== test session starts ===================================================
        platform linux -- Python 3.12.9, pytest-8.3.4, pluggy-1.5.0 -- /home/remi-gau/miniconda3/bin/python3
        cachedir: .pytest_cache
        Using --randomly-seed=252202663
        rootdir: /home/remi-gau/github/poia
        configfile: pyproject.toml
        plugins: reporter-0.5.3, cov-6.0.0, timeout-2.3.1, anyio-4.9.0, xdist-3.6.1, reporter-html1-0.9.2, nbmake-1.5.5, randomly-3.16.0, csv-3.0.0
        collected 1 item

        mo_intro.py::test_function PASSED

        =================================================== 1 passed in 0.39s ====================================================
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        /// attention | BUG

        Testing with pytest directly would sometimes fail for marimo >= 0.12.1.

        [Bug reported](https://github.com/marimo-team/marimo/issues/4440) and should be fixed in next release.

        ///
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Rich display of dataframes

        Interactive table with easily accessible 'transform' operations.
        """
    )
    return


@app.cell
def _():
    from nilearn.glm.tests._testing import modulated_event_paradigm

    events = modulated_event_paradigm()
    events
    return events, modulated_event_paradigm


@app.cell
def _(events, mo):
    transformed_df = mo.ui.dataframe(events)
    transformed_df
    return (transformed_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Plotting and interactive UI""")
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(start=0, stop=7, step=1, label="Threshold", value=2)
    return (slider,)


@app.cell
def _(slider):
    slider
    return


@app.cell
def _(slider):
    from nilearn.datasets import load_sample_motor_activation_image
    from nilearn.plotting import view_img

    stat_map = load_sample_motor_activation_image()

    view_img(stat_map, threshold=slider.value)
    return load_sample_motor_activation_image, stat_map, view_img


@app.cell
def _():
    import marimo as mo

    mo.md("""
    ## Imports
    """)
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Helper functions""")
    return


@app.cell(hide_code=True)
def _(mo):
    def show_intro_nb(break_condition: str = "def cell_2(") -> str:
        try:
            with (mo.notebook_location() / "mo_intro.py").open("r") as f:
                lines = f.readlines()
        except Exception:
            return ""

        intro = []
        for l in lines:
            intro.append(l)
            if l.startswith(break_condition):
                break
        return (
            f"""
    {"`" * 3}python
    """
            + " ".join(intro)
            + f"""
    {"`" * 3}"""
        )

    return (show_intro_nb,)


if __name__ == "__main__":
    app.run()
