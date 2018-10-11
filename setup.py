from setuptools import setup,find_packages

setup(
  name = 'soundcloud_dl',
  version = '0.1.19',
  description = 'A tool to download tracks from soundcloud.com',
  packages = ['','downloader'],
  author = 'Suyash Behera',
  author_email = 'sne9x@outlook.com',
  url = 'https://github.com/Suyash458/soundcloud-dl', 
  download_url = 'https://github.com/Suyash458/soundcloud-dl/archive/master.zip', 
  keywords = ['Downloader', 'Python', 'soundcloud'],
  install_requires = ['soundcloud','requests','mutagen', 'six', 'halo', 'tqdm'],
  entry_points = {
        'console_scripts': ['soundcloud-dl=soundcloud_dl:main',
        'sc-dl=soundcloud_dl:main'],
  },
  classifiers=[
   'Development Status :: 5 - Production/Stable',
  ],
)