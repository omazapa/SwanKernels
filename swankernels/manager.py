

from jupyter_client.kernelspec import KernelSpecManager, KernelSpec, NoSuchKernel
import os
from traitlets import Unicode, Bool

class SwanKernelSpecManager(KernelSpecManager):
    project_path = Unicode("", config=True, allow_none=False,
                         help="SWAN Project path")
    def __init__(self, **kwargs):
        super(SwanKernelSpecManager, self).__init__(**kwargs)

    def set_project_kernel_path(self):
        os.environ["JUPYTER_PATH"]=self.project_path+"/.local/"

    def find_kernel_specs(self, skip_base=True):
        """ Returns a dict mapping kernel names to resource directories.
            The update process also adds the resource dir for the conda
            environments.
        """
        self.set_project_kernel_path()
        kspecs = super(SwanKernelSpecManager, self).find_kernel_specs()
        return kspecs

    def get_kernel_spec(self, kernel_name):
        """ Returns a :class:`KernelSpec` instance for the given kernel_name.
            Additionally, conda kernelspecs are generated on the fly
            accordingly with the detected envitonments.
        """

        self.set_project_kernel_path()
        return super(SwanKernelSpecManager, self).get_kernel_spec(kernel_name)

    def get_all_specs(self):
        """ Returns a dict mapping kernel names to dictionaries with two
            entries: "resource_dir" and "spec". This was added to fill out
            the full public interface to KernelManagerSpec.
        """
        res = {}
        for name, resource_dir in self.find_kernel_specs().items():
            try:
                spec = self.get_kernel_spec(name)
                res[name] = {'resource_dir': resource_dir,
                             'spec': spec.to_dict()}
            except NoSuchKernel:
                self.log.warning("Error loading kernelspec %r", name, exc_info=True)
        return res