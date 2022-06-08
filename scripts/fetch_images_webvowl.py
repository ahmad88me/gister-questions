import os
import shutil
import sys
import traceback


def gather_images(jar_path, opath, template_path):
    """
    :param opath:
    :return:
    """

    oname = opath.split(os.sep)[-1]
    res_path = os.path.join('images', oname)
    webvowl_path = os.path.join(res_path, "webvowl")
    if not os.path.exists(res_path):
        os.mkdir(res_path)

    # if not os.path.exists(webvowl_path):
    #     os.mkdir(webvowl_path)
    if not os.path.exists(webvowl_path):
        shutil.copytree(template_path, webvowl_path)
        print("java -jar -file %s -output %s" % (opath, os.path.join(res_path, "data")))
    else:
        print("Skip %s" % opath)


def workflow(jar_path, ontologies_path, template_path):
    """
    :param ontologies_path:
    :return:
    """
    for opath in os.listdir(ontologies_path):
        try:
            print("processing %s" % opath)
            gather_images(jar_path, os.path.join(ontologies_path, opath), template_path)
        except Exception as e:
            print("unable to generate resources for: %s" % opath)
            print(str(e))
            traceback.print_exc()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        workflow(sys.argv[1], sys.argv[2], sys.argv[3])

# Jar path, ontologies path, template path