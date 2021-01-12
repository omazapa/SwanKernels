
import os
from distutils.dir_util import copy_tree
from swankernels.config import get_templates_path


def create_kernel_from_template(repo, stack, platform, source, kernel, output_path):
    kernel_path = repo+"_"+stack+"_"+platform+"_"+kernel
    generated_path = output_path+"/"+kernel_path
    template_path = get_templates_path()
    if "python" in kernel: #in templates it is python, but it can appaer in the config like python2 or python3, I am just setting it to python
        template_path += "python"
    else:
        template_path += kernel

    os.makedirs(generated_path, exist_ok=True)
    copy_tree(template_path, generated_path)
    kernel_data = ""
    with open(generated_path+'/kernel.json', 'r') as f:
        kernel_data = f.read()
        if repo == "SFT":  # default for LCG is python2 unleast python3 is in the name
            if "python3" in stack:
                kernel_data = kernel_data.replace("#", "3")
            else:
                kernel_data = kernel_data.replace("#", "2")

        if repo == "CMS":
            if "python3" == kernel:  # usually python 2/3 are available in CMS with can set both
                kernel_data = kernel_data.replace("#", "3")
            else:
                kernel_data = kernel_data.replace("#", "2")

        kernel_data = kernel_data.replace("REPO", repo)
        kernel_data = kernel_data.replace("STACK", stack)
        kernel_data = kernel_data.replace("PLATFORM", platform)
        kernel_data = kernel_data.replace("SOURCE", source)

    with open(generated_path+'/kernel.json', 'w') as f:
        f.write(kernel_data)


# def create_kernels(data,output_path):
#     for repo in data.keys():
#         for item in data[repo]:
#             for stack in item['STACKS']:
#                 for platform in item['PLATFORMS']:
#                     for kernel in item['KERNELS']:
#                         kernel_full=repo+"_"+stack+"_"+platform+"_"+kernel
#                         print("GENERATING = "+kernel_full)
#                         create_kernel_from_template(repo,stack,platform,kernel,output_path)