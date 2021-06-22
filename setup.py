from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='hawser',
    version='0.0.1',
    description='🏷️ Lanyard API Wrapper for Python.',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    url='https://github.com/5elenay/hawser/',
    author='5elenay',
    author_email='',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/5elenay/hawser/issues",
    },
    classifiers=classifiers,
    keywords=["lanyard", "api", "api-wrapper", "wrapper", "lanyard-python", "hawser"],
    packages=find_packages(),
    python_requires='>=3.6.0',
    install_requires=["aiohttp"]
)
