from pbr.version import VersionInfo

package_name='hello_pypi'
info = VersionInfo(package_name)

version = info.version_string()

if __name__ == '__main__':
	print(version)
