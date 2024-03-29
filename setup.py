from setuptools import setup

setup(
    author='CryptoGu1',
    author_email='Kriptoairdrop9@gmail.com',
    name='Dory',
    version='0.0.1',
    description='A simple package for https://app.tea.xyz/. Example Dory1 - https://github.com/CryptoGu1/Dorytea1.git and tea-Dory2 - https://github.com/CryptoGu1/Dorytea2.git',
    url='https://github.com/CryptoGu1/Dorytea.git',
    project_urls={
        'Homepage': 'https://github.com/CryptoGu1/Dorytea.git',
        'Source': 'https://github.com/CryptoGu1/Dorytea.git',
    },
    py_modules=['hi_tea'],
    entry_points={
        'console_scripts': [
            'hi-tea=hi_tea:hello_tea_xyz'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=[
        'Dorytea1',
        'Dorytea2',
        # add your projects
    ],
)
