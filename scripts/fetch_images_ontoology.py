import os
import shutil
import sys


def gather_images(opath):
    """
    :param opath:
    :return:
    """
    oname = opath.split(os.sep)[-1]
    res_path = os.path.join('images', oname)
    if not os.path.exists(res_path):
        os.mkdir(res_path)
    oimage = oname+".png"

    src_path = os.path.join(opath, 'diagrams', 'ar2dtool-class', oimage)
    dest = os.path.join(res_path, "acla"+oimage)
    if not os.path.exists(dest):
        shutil.copyfile(src_path, dest)

    src_path = os.path.join(opath, 'diagrams', 'ar2dtool-taxonomy', oimage)
    dest = os.path.join(res_path, "atax"+oimage)
    if not os.path.exists(dest):
        shutil.copyfile(src_path, dest)

    src_path = os.path.join(opath, 'documentation', 'webvowl')
    dest = os.path.join(res_path, "webvowl")
    if not os.path.exists(dest):
        shutil.copytree(src_path, dest)


def workflow(ontologies_path):
    """
    :param ontologies_path:
    :return:
    """
    for opath in os.listdir(ontologies_path):
        try:
            print("copying %s" % opath)
            gather_images(os.path.join(ontologies_path, opath))
        except Exception as e:
            print("unable to generate resources for: %s" % opath)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        workflow(sys.argv[1])

