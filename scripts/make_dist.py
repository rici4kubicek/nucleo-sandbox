Import("env")

from zipfile import ZipFile, ZIP_DEFLATED
from os.path import join, basename, exists
from os import mkdir
import shutil

from utils import extract_version

TARGETDIR = "dist/"

def after_build(source, target, env):
    version = extract_version(env)

    if not exists(TARGETDIR):
        mkdir(TARGETDIR)

    target_zip = env.File(join("$BUILD_DIR", f"$PROGNAME-{version}.zip"))
    with ZipFile(target_zip.rstr(), 'w', compression=ZIP_DEFLATED) as z:
        target_hex = env.File(join("$BUILD_DIR", "${PROGNAME}.hex")).rstr()
        z.write(target_hex, basename(target_hex))

    shutil.copy(target_zip.rstr(), TARGETDIR)


env.AddPostAction(
    "buildprog",
    env.VerboseAction(
        after_build,
        "Generating zip bundle"
    )
)