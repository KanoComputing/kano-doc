kano-doc
--------

Documentation tools for Kano OS.

This repository contains scripts and templates to start adding
documentation to other projects. Currently, this only extracts docs for
Python packages.


Initialising a project with docs
--------------------------------

First, ``git clone`` this repository on your machine and let's assume
the following file structure:

    ~/Projects
    ├── my-project
    └── kano-doc

The tools themselves require a ``sudo pip install Sphinx sphinx_rtd_theme``
to generate docs.

To add the docs templates to ``my-project``:

    cd kano-doc
    bin/kano-init ~/Projects/my-project

You can use the ``-h`` option to see all other options.

Include the following targets in ``my-project/Makefile`` (if it doesn't
have one, create one from scratch):

    .PHONY: clean docs

    clean:
        cd docs && make clean

    docs:
        cd docs && make all

Include the following build stage in ``my-project/Jenkinsfile`` (if it
doesn't have one, create one from scratch):

    def repo_name = 'my-project'

    stage ('Docs') {
        build_docs "$repo_name"
    }

Now you can run ``make docs`` from ``~/Projects/my-project`` and perhaps
the following issues might arrise:

-  If the repo contains multiple packages at different locations, add to
   ``~/Projects/my-project/docs/Makefile`` more ``sphinx-apidoc`` with
   paths in where the Py packages will be. Also, add more ``sys.path.insert``
   at the top of the ``~/Projects/my-project/docs/conf.py``
-  Solve any ``ImportErrors`` by adding modules to the
   ``autodoc_mock_imports`` option under ``Options for autodoc`` in
   ``~/Projects/my-project/docs/conf.py``
-  Solve any ``NameErrors`` for ``"_"`` and ``"N_"`` by uncommenting the
   ``kano-i18n`` options under ``Kano OS configuration`` in the same file
-  If you get any other errors that might arrise due to importing a
   package, then ``fix the code for it to be importable!``
-  Finally, make sure to add the package names to
   ``~/Projects/my-project/docs/source/modules.rst``, e.g. if ``my-project``
   has the following Python packages ``my_pkg``, ``other_pkg``, then add
   those names in the file.
-  You can find the main page at
   ``~/Projects/my-project/docs/source/html/index.html``


Quick tips for documenting Python code
--------------------------------------

As a rule of thumb, use Google's guidelines:
https://google.github.io/styleguide/pyguide.html

-  Add ``docstrings`` to functions and classes
-  The package needs to be importable and not run code at import time
-  Get into the habit of checking the docs before submitting a PR

Here is an example of a Google style docstring for a function:

    def is_power_hat_plugged(with_dbus=True, retry_count=5):
        """Check if the Kano PowerHat board is plugged in.

        NOTE: Running this function with_dbus=False must be done when the daemon is
              certainly not running. Otherwise, bad things might happen.

        Args:
            with_dbus (bool): Whether to run the detection through the central dbus
                kano-boards-daemon, or bypass to use the underlying library
            retry_count: See
                :func:`~kano_peripherals.ck2_pro_hat.driver.high_level.get_ck2_pro_hat_interface`

        Returns:
            bool: Whether the PowerHat is plugged in or not
        """
