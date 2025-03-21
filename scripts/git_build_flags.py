from version import version_info

Import("env")

version = version_info()

env.Append(CPPDEFINES=[
    ("SW_VERSION_MAJOR", version.major + (128 * int(version.dirty))),
    ("SW_VERSION_MINOR", version.minor),
    ("SW_VERSION_USER", version.user),
])