
Quickstart guide
================

After following the :ref:`installation` instructions, you can either `run remotely`_ in the cloud, or `run locally`_ on your machine. The run instructions below will use :ref:`asic_demo`, a simple design run in an ASIC flow, using the :ref:`skywater130` PDK (set up from  :ref:`installation`).

.. _run remotely:

Remote Run
-----------
SiliconCompiler supports running jobs in the cloud on either :ref:`private <private-server>` or `public`_ servers. We are currently running a public beta server which anybody can use. To see the details of how remote processing works, see :ref:`here <remote processing>`.


.. _public:

Public Cloud Access
^^^^^^^^^^^^^^^^^^^^

By default, SiliconCompiler will send remote jobs to our public beta servers, after printing a brief reminder that the job is being uploaded to a public server. You can run a quick self-test to verify that SiliconCompiler was installed successfully::

    sc -target asic_demo -remote

The job should only take a few minutes to run if the servers aren't too busy. Skip to `remote run results`_ to see the expected output.

You do not need to configure anything to use the :ref:`remote` flag with these public servers, but you can use the :ref:`sc-configure` command to specify where SiliconCompiler should send remote jobs. For more information, see the :ref:`Configuring a Different Remote Server` section.

Remote Run Results
^^^^^^^^^^^^^^^^^^

.. include:: quickstart/quickstart_banner.rst

As run goes through each step of the flow, a message will be printed to the screen every 30 seconds.

Then, at the end of the run, a summary table will be printed similar to the one show below:

.. image:: ../_images/summary_table.png

All design outputs are located in ``build/<design>/<jobname>``. When running remote, you will not get all the tool-specific output that you would with a local run, but you will be able to find a screenshot of the demo design ``heartbeat.png`` and a summary report in ``report.html``:

.. image:: ../_images/selftest_screenshot.png


.. _run locally:

Local Run
----------

If you wish to run locally, you will need to install some external tool dependencies to start. Take a look at :ref:`External Tools` for a list of tools which you may want to have.

.. note::

   The minimum set of tools required for an ASIC flow are: :ref:`Surelog <surelog>`, :ref:`Yosys <yosys>`, :ref:`OpenROAD <openroad>`, and :ref:`KLayout <klayout>`. Links to individual tool installation instructions and platform
   limitations can be found in the :ref:`Tools directory`.

Once you have these tools installed, try compiling a simple design:

.. code-block:: bash

    (venv) cd $SCPATH/../examples/heartbeat
    (venv) sc -target asic_demo


.. include:: quickstart/quickstart_banner.rst

Then, at the end of the run, a summary table will be printed similar to the one show below:

.. image:: ../_images/summary_table.png


By default, only the summary of each step is printed, in order to not clutter up the screen with tool-specific output. If you wish to see the output from each tool, you can find the log files associated with each tool in: ``build/<design>/<jobname>/<step>/<index>/<step>.log``

If you wish to see all the tool-specific information printed onto the screen, you can turn the :ref:`quiet` option off.

View Design
^^^^^^^^^^^^
For viewing IC layout files (DEF, GDSII) we recommend installing the open source multi-platform :ref:`Klayout viewer <klayout>`  (available for Windows, Linux, and macOS). Installation instructions for Klayout can be found in the :ref:`tools directory <klayout>`.


If you have Klayout installed, at the end of your run, a window should have popped up with your completed design.

If you have closed that window and want to reference it again, you can view the output from the :ref:`asicflow` by
by calling :ref:`sc-show` directly from the command line as shown below:

.. code-block:: bash

   (venv) sc-show -design heartbeat

.. image:: _images/heartbeat.png

What Next?
-----------

Now that you've quickly run a simple example, you can proceed to a larger example like :ref:`building your own soc`, or you can dive deeper into the SiliconCompiler build flow  you ran from this quickstart (`asic_demo <https://github.com/siliconcompiler/siliconcompiler/blob/main/siliconcompiler/targets/asic_demo.py>`_) by looking through how the flow is constructed with :ref:`execution model`, :ref:`data model`, and :ref:`programming model` in the Flow Basics section.
