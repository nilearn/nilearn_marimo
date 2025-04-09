# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "marimo",
#     "git+https://github.com/nilearn/nilearn.git",
#     "plotly",
# ]
# ///

import marimo

__generated_with = "0.12.0"
app = marimo.App(width="full", app_title="nilearn stable")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Using nilearn in a marimo notebook

        This notebook is mostly for nilearn developers
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
    mo.md(
        r"""
        /// attention | running on dev

        This notebook is meant to run on the main branch of nilearn

        ///
        """
    )
    return


@app.cell
def _(mo):
    from nilearn import __version__

    mo.md(f"Running Nilearn {__version__}")
    return (__version__,)


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
    import numpy as np
    from nilearn.datasets import load_fsaverage, load_fsaverage_data
    from nilearn.plotting import plot_surf_stat_map
    from nilearn.surface import SurfaceImage

    fsaverage_meshes = load_fsaverage()

    motor_activation_surface_image = SurfaceImage.from_volume(
        mesh=fsaverage_meshes["pial"],
        volume_img=motor_activation_image,
    )

    curv_sign = load_fsaverage_data(data_type="curvature")

    fig = plot_surf_stat_map(
        stat_map=motor_activation_surface_image,
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
        motor_activation_surface_image,
        np,
        plot_surf_stat_map,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Interactive surface viewing""")
    return


@app.cell
def _(curv_sign, fsaverage_meshes, motor_activation_surface_image):
    from nilearn.plotting import view_surf

    view_surf(
        surf_mesh=fsaverage_meshes["inflated"],
        surf_map=motor_activation_surface_image,
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Masker reports""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### NiftiMasker""")
    return


@app.cell
def _(motor_activation_image):
    from nilearn.datasets import fetch_development_fmri
    from nilearn.maskers import NiftiMasker

    nifti_masker = NiftiMasker(
        standardize="zscore_sample",
        mask_strategy="epi",
        memory="nilearn_cache",
        memory_level=2,
        smoothing_fwhm=8,
        cmap="gray",
    )

    nifti_masker.fit(motor_activation_image)
    report = nifti_masker.generate_report()
    report
    return NiftiMasker, fetch_development_fmri, nifti_masker, report


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### NiftiLabelsMasker""")
    return


@app.cell
def _(motor_activation_image):
    from nilearn.datasets import fetch_atlas_schaefer_2018
    from nilearn.maskers import NiftiLabelsMasker

    atlas_schaefer_2018 = fetch_atlas_schaefer_2018()

    try:
        nifti_labels_masker = NiftiLabelsMasker(
            atlas_schaefer_2018.maps,
            labels=atlas_schaefer_2018.labels,
        )
        nifti_labels_masker.fit(motor_activation_image)
        label_report = nifti_labels_masker.generate_report()
    except ValueError as e:
        print(e)
        label_report = None
    label_report
    return (
        NiftiLabelsMasker,
        atlas_schaefer_2018,
        fetch_atlas_schaefer_2018,
        label_report,
        nifti_labels_masker,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### SurfaceLabelsMasker""")
    return


@app.cell
def _(SurfaceImage, fsaverage_meshes, motor_activation_surface_image):
    from nilearn.datasets import fetch_atlas_surf_destrieux
    from nilearn.maskers import SurfaceLabelsMasker

    atlas_surf_destrieux = fetch_atlas_surf_destrieux()

    labels_img = SurfaceImage(
        mesh=fsaverage_meshes["inflated"],
        data={
            "left": atlas_surf_destrieux["map_left"],
            "right": atlas_surf_destrieux["map_right"],
        },
    )

    labels_masker = SurfaceLabelsMasker(labels_img, lut=atlas_surf_destrieux.lut).fit()
    labels_masker.transform(motor_activation_surface_image)
    labels_masker_report = labels_masker.generate_report()
    labels_masker_report
    return (
        SurfaceLabelsMasker,
        atlas_surf_destrieux,
        fetch_atlas_surf_destrieux,
        labels_img,
        labels_masker,
        labels_masker_report,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### SurfaceMapsMasker""")
    return


@app.cell
def _(SurfaceImage, fsaverage_meshes, motor_activation_surface_image):
    from nilearn.datasets import fetch_atlas_msdl, load_nki
    from nilearn.maskers import SurfaceMapsMasker

    atlas_msdl = fetch_atlas_msdl()

    surf_atlas = SurfaceImage.from_volume(volume_img=atlas_msdl.maps, mesh=fsaverage_meshes["pial"])

    surface_map_masker = SurfaceMapsMasker(surf_atlas).fit()
    surface_map_masker.transform(motor_activation_surface_image)

    try:
        report_mpl = surface_map_masker.generate_report(engine="matplotlib")
    # not only implemented for nilearn > 0.11.1
    except AttributeError as e:
        print(e)
        report_mpl = None
    report_mpl
    return (
        SurfaceMapsMasker,
        atlas_msdl,
        fetch_atlas_msdl,
        load_nki,
        report_mpl,
        surf_atlas,
        surface_map_masker,
    )


@app.cell
def _(surface_map_masker):
    try:
        report_plotly = surface_map_masker.generate_report(engine="plotly")
    # not only implemented for nilearn > 0.11.1
    except AttributeError as e:
        print(e)
        report_plotly = None
    report_plotly
    return (report_plotly,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## GLM reports""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### First level model report""")
    return


@app.cell
def _():
    from nilearn.datasets import fetch_ds000030_urls, fetch_openneuro_dataset, select_from_index

    def fetch_bids_data():
        _, urls = fetch_ds000030_urls()

        exclusion_patterns = [
            "*group*",
            "*phenotype*",
            "*mriqc*",
            "*parameter_plots*",
            "*physio_plots*",
            "*space-fsaverage*",
            "*space-T1w*",
            "*dwi*",
            "*beh*",
            "*task-bart*",
            "*task-rest*",
            "*task-scap*",
            "*task-task*",
        ]
        urls = select_from_index(urls, exclusion_filters=exclusion_patterns, n_subjects=1)

        data_dir, _ = fetch_openneuro_dataset(urls=urls)

        return data_dir

    return (
        fetch_bids_data,
        fetch_ds000030_urls,
        fetch_openneuro_dataset,
        select_from_index,
    )


@app.cell
def _(fetch_bids_data):
    from pathlib import Path

    from nilearn.glm.first_level import first_level_from_bids
    from nilearn.interfaces.fsl import get_design_from_fslmat

    data_dir = fetch_bids_data()

    task_label = "stopsignal"
    space_label = "MNI152NLin2009cAsym"
    derivatives_folder = "derivatives/fmriprep"
    (
        models,
        models_run_imgs,
        _,
        _,
    ) = first_level_from_bids(
        data_dir,
        task_label,
        space_label,
        smoothing_fwhm=5.0,
        derivatives_folder=derivatives_folder,
        slice_time_ref=0.0,
    )

    flm = models[0]

    imgs = models_run_imgs[0]

    fsl_design_matrix_path = (
        Path(data_dir)
        / "derivatives"
        / "task"
        / f"sub-{flm.subject_label}"
        / "stopsignal.feat"
        / "design.mat"
    )
    design_matrices = get_design_from_fslmat(fsl_design_matrix_path, column_names=None)
    design_columns = [f"cond_{int(i):02}" for i in range(len(design_matrices.columns))]
    design_columns[0] = "Go"
    design_columns[4] = "StopSuccess"
    design_matrices.columns = design_columns
    return (
        Path,
        data_dir,
        derivatives_folder,
        design_columns,
        design_matrices,
        first_level_from_bids,
        flm,
        fsl_design_matrix_path,
        get_design_from_fslmat,
        imgs,
        models,
        models_run_imgs,
        space_label,
        task_label,
    )


@app.cell
def _(design_matrices, flm, imgs):
    flm.fit(imgs, design_matrices=design_matrices)
    return


@app.cell
def _(flm):
    flm_report = flm.generate_report(
        contrasts="StopSuccess - Go",
        title="FLM Bids Features Stat maps",
        cluster_threshold=3,
        plot_type="glass",
    )
    return (flm_report,)


@app.cell
def _(flm_report):
    flm_report
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
