import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'json_to_pandas_jabbajabba',
    version = "0.0.1",
    author = "Me",
    author_email = 'jtheHutt@tatooine.gov',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/tianxianglan01/PythonFundamentals.Labs.PipModule.git',
    classifiers = ["Programming Language :: Python:: 3",
                    "License:: OSI :: MIT License",
                    "Operating System :: OS Independent",

    ],

    package_dir= {"": "json_helper"},
    packages=setuptools.find_packages(where = "json_helper"),
    package_requires = ">= 3.9"



)