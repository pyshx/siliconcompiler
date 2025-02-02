'''
Xyce is a high performance SPICE-compatible circuit simulator
capable capable of solving extremely large circuit problems by
supporting large-scale parallel computing platforms. It also
supports serial execution on all common desktop platforms,
and small-scale parallel runs on Unix-like systems.

Documentation: https://xyce.sandia.gov/documentation-tutorials/

Sources: https://github.com/Xyce/Xyce

Installation: https://xyce.sandia.gov/documentation-tutorials/building-guide/

Status: SC integration WIP
'''

import os

################################
# Setup Tool (pre executable)
################################
def setup(chip):

     tool = 'xyce'
     step = chip.get('arg','step')
     index = chip.get('arg','index')
     task = chip._get_task(step, index)

     clobber = False

     chip.set('tool', tool, 'exe', tool)
     chip.set('tool', tool, 'version', '0.0', clobber=clobber)
     chip.set('tool', tool, 'task', task, 'threads', os.cpu_count(), step=step, index=index, clobber=clobber)

##################################################
if __name__ == "__main__":

    chip = make_docs()
    chip.write_manifest("xyce.json")
