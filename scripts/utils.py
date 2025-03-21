from version import version_info

def extract_cppdefs(env):
    build_flags = env.ParseFlags(env['BUILD_FLAGS'])
    fvl = [build_flag for build_flag in build_flags.get('CPPDEFINES') if isinstance(build_flag, list)]
    return {k: v.replace('"', '') for (k, v) in fvl}


def extract_version(env):
    version = version_info()

    return f"{version}"