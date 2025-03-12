import json
import pyblish.api
from pathlib import Path
import tempfile

from quadpype.hosts.tvpaint.api.lib import (
    execute_george_through_file
)

class ExtractTempWorkfile(pyblish.api.InstancePlugin):
    label = "Extract Temp Workfile"
    order = pyblish.api.ExtractorOrder - 0.48
    hosts = ["tvpaint"]
    families = ["workfile"]

    def process(self, instance):
        repres = instance.data["representations"]
        for repre in repres:
            dirpath = self._create_temp_workfile(repre.get("files"))
            repre.update({"stagingDir": dirpath})
            instance.context.data["cleanupFullPaths"].append(dirpath)

        self.log.info("Updated temp workfile instance: {}".format(
            json.dumps(instance.data["representations"], indent=4)
        ))

    @staticmethod
    def _create_temp_workfile(filename):
        """Create a temporary saved workfile.
        It is important in case the user doesn't save before publish to have
        the exact same file in the published workfile and the working workfile

        Return: the new staging_dir"""

        staging_dir = (
            tempfile.mkdtemp(prefix="tvpaint_render_")
        ).replace("\\", "/")

        temp_wofkfile_path = Path(staging_dir) / filename
        george_script = u"tv_SaveProject '{}'".format(str(temp_wofkfile_path))

        execute_george_through_file(george_script)
        return staging_dir
