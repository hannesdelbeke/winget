"""
sample code to get winget package manifest data
"""

from winget import WinGetPackage


def print_package_from_repo():
    winget_package = WinGetPackage(id_='Python.Python.3.8')
    print(winget_package)  # <WinGetPackage('Python.Python.3.8')>
    print(winget_package.id)   # Python.Python.3.8
    print(winget_package.name)  # Python.3.8
    print(winget_package.publisher)  # Python
    print(winget_package.versions)  # {'3.8.7', '3.8.3', '3.8.2', '3.8.4', '3.8.0', '3.8.5', '3.8.9', '3.8.1', '3.8.8', '3.8.10', '3.8.6'}

    pkg_version = winget_package['3.8.10']
    if pkg_version:
        print(pkg_version)  # <WinGetPackageVersion('Python.Python.3.8': '3.8.10')>
        print(pkg_version.name)  # Python.3.8
        print(pkg_version.version)  # 3.8.10
        print(pkg_version.publisher)  # Python
        print(pkg_version.id)  # Python.Python.3.8
        print(pkg_version.api_url)  # https://api.github.com/repos/microsoft/winget-pkgs/contents/manifests/p/Python/Python/3/8/3.8.10
        print(pkg_version.api_contents)  # [{'name': 'Python.Python.3.8.installer.yaml', 'path': 'manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.installer.yaml', 'sha': 'ecaa0592dac48e2cfc74ccfd4b9b79b5adaec952', 'size': 1142, 'url': 'https://api.github.com/repos/microsoft/winget-pkgs/contents/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.installer.yaml?ref=master', 'html_url': 'https://github.com/microsoft/winget-pkgs/blob/master/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.installer.yaml', 'git_url': 'https://api.github.com/repos/microsoft/winget-pkgs/git/blobs/ecaa0592dac48e2cfc74ccfd4b9b79b5adaec952', 'download_url': 'https://raw.githubusercontent.com/microsoft/winget-pkgs/master/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.installer.yaml', 'type': 'file', '_links': {'self': 'https://api.github.com/repos/microsoft/winget-pkgs/contents/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.installer.yaml?ref=master', 'git': 'https://api.github.com/repos/microsoft/winget-pkgs/git/blobs/ecaa0592dac48e2cfc74ccfd4b9b79b5adaec952', 'html': 'https://github.com/microsoft/winget-pkgs/blob/master/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.installer.yaml'}}, {'name': 'Python.Python.3.8.locale.en-US.yaml', 'path': 'manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.locale.en-US.yaml', 'sha': '854eb5a8b077c96455f2e75828848d182921c296', 'size': 637, 'url': 'https://api.github.com/repos/microsoft/winget-pkgs/contents/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.locale.en-US.yaml?ref=master', 'html_url': 'https://github.com/microsoft/winget-pkgs/blob/master/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.locale.en-US.yaml', 'git_url': 'https://api.github.com/repos/microsoft/winget-pkgs/git/blobs/854eb5a8b077c96455f2e75828848d182921c296', 'download_url': 'https://raw.githubusercontent.com/microsoft/winget-pkgs/master/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.locale.en-US.yaml', 'type': 'file', '_links': {'self': 'https://api.github.com/repos/microsoft/winget-pkgs/contents/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.locale.en-US.yaml?ref=master', 'git': 'https://api.github.com/repos/microsoft/winget-pkgs/git/blobs/854eb5a8b077c96455f2e75828848d182921c296', 'html': 'https://github.com/microsoft/winget-pkgs/blob/master/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.locale.en-US.yaml'}}, {'name': 'Python.Python.3.8.yaml', 'path': 'manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.yaml', 'sha': '19a8c5fa88c96c157109876b2491ab83152e6050', 'size': 215, 'url': 'https://api.github.com/repos/microsoft/winget-pkgs/contents/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.yaml?ref=master', 'html_url': 'https://github.com/microsoft/winget-pkgs/blob/master/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.yaml', 'git_url': 'https://api.github.com/repos/microsoft/winget-pkgs/git/blobs/19a8c5fa88c96c157109876b2491ab83152e6050', 'download_url': 'https://raw.githubusercontent.com/microsoft/winget-pkgs/master/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.yaml', 'type': 'file', '_links': {'self': 'https://api.github.com/repos/microsoft/winget-pkgs/contents/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.yaml?ref=master', 'git': 'https://api.github.com/repos/microsoft/winget-pkgs/git/blobs/19a8c5fa88c96c157109876b2491ab83152e6050', 'html': 'https://github.com/microsoft/winget-pkgs/blob/master/manifests/p/Python/Python/3/8/3.8.10/Python.Python.3.8.yaml'}}]

        # todo, manifests are never set, this currently fails
        #  pkg_version.parse_manifests()
        print(pkg_version.manifests)  # {}
        print(pkg_version.version_manifest)  # None
        print(pkg_version.default_locale_manifest)  # None

        # todo, can we have something like this:
        #  print(pkg_version.install_location)  # C:\Program Files\Python38


if __name__ == "__main__":
    print_package_from_repo()
