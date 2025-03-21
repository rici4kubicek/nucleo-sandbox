Import("env")

from os.path import join

target_elf = join("$BUILD_DIR", "${PROGNAME}.elf")
target_hex = env.ElfToHex(join("$BUILD_DIR", "${PROGNAME}"), target_elf)

env.Depends("buildprog", target_hex)
