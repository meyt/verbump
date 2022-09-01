import re


def bump(content: str, pattern: str, part: int) -> tuple:
    current_version = None
    new_version = None

    def replacer(m):
        nonlocal current_version, new_version

        version = m.group(1)
        if not version:
            raise ValueError("The regex pattern has no group")

        full_span = m.span(0)
        span = m.span(1)
        current_version = version
        version = list(map(int, version.split(".")))
        for k in range(len(version)):
            if k == part:
                version[k] += 1

            elif k > part:
                version[k] = 0

        new_version = ".".join(map(str, version))
        return (
            content[full_span[0] : span[0]]
            + new_version
            + content[span[1] : full_span[1]]
        )

    new_content = re.sub(pattern, replacer, content)

    if new_content == content:
        raise ValueError("Cannot find version string")

    return new_content, current_version, new_version
