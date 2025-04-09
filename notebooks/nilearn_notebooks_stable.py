# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "marimo",
#     "matplotlib",
#     "nilearn==0.11.1",
#     "numpy==2.2.4",
# ]
# ///

import marimo

__generated_with = "0.12.0"
app = marimo.App(width="medium", app_title="nilearn stable")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Using nilearn in a marimo notebook

        This notebook is mostly for nilearn developpers
        to make sure nilearn functionalities run well
        in a marimo notebook.

        But this can serve as an starting point
        for anyone to start using nilearn
        in a marimo notebook.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Volume plotting""")
    return


@app.cell
def _(mo):
    from nilearn.datasets import load_mni152_template
    from nilearn.plotting import plot_img, show

    template = load_mni152_template()
    img_fig = plot_img(template)
    show()

    mo.md("Basic plotting of template.")
    return img_fig, load_mni152_template, plot_img, show, template


@app.cell
def _(mo, show):
    from nilearn.datasets import load_sample_motor_activation_image
    from nilearn.plotting import plot_stat_map

    motor_activation_image = load_sample_motor_activation_image()
    stat_map_fig = plot_stat_map(motor_activation_image)
    show()

    mo.md("Basic plotting of statistical map.")
    return (
        load_sample_motor_activation_image,
        motor_activation_image,
        plot_stat_map,
        stat_map_fig,
    )


@app.cell
def _(mo, motor_activation_image, show):
    from nilearn.plotting import plot_glass_brain

    plot_glass_brain(motor_activation_image, threshold=3)
    show()

    mo.md("Basic plotting of a glass brain.")
    return (plot_glass_brain,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Interactive image ⬇️""")
    return


@app.cell
def _(motor_activation_image):
    from nilearn.plotting import view_img
    html_fig = view_img(motor_activation_image)
    html_fig
    return html_fig, view_img


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Surface plotting""")
    return


@app.cell
def _(mo, motor_activation_image, show):
    from nilearn.datasets import load_fsaverage
    from nilearn.surface import SurfaceImage
    import numpy as np
    from nilearn.plotting import plot_surf_stat_map
    from nilearn.datasets import load_fsaverage_data

    fsaverage_meshes = load_fsaverage()

    surface_image = SurfaceImage.from_volume(
        mesh=fsaverage_meshes["pial"],
        volume_img=motor_activation_image,
    )

    curv_sign = load_fsaverage_data(data_type="curvature")

    fig = plot_surf_stat_map(
        stat_map=surface_image,
        surf_mesh=fsaverage_meshes["inflated"],
        title="Surface with matplotlib",
        threshold=1.0,
        bg_map=curv_sign,
    )
    show()

    mo.md("Basic surface plotting.")
    return (
        SurfaceImage,
        curv_sign,
        fig,
        fsaverage_meshes,
        load_fsaverage,
        load_fsaverage_data,
        np,
        plot_surf_stat_map,
        surface_image,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Interactive surface viewing""")
    return


@app.cell
def _(curv_sign, fsaverage_meshes, surface_image):
    from nilearn.plotting import view_surf

    view_surf(
        surf_mesh=fsaverage_meshes["inflated"],
        surf_map=surface_image,
        threshold="90%",
        bg_map=curv_sign,
        title="3D visualization in a web browser",
    )
    return (view_surf,)


@app.cell
def _(motor_activation_image):
    from nilearn.plotting import view_img_on_surf

    view_img_on_surf(motor_activation_image, threshold="90%")
    return (view_img_on_surf,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
