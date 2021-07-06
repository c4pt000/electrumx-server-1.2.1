import setuptools
from server.version import VERSION


setuptools.setup(
    name='electrumx',
    version=VERSION.split()[-1],
    scripts=['electrumx_server.py', 'electrumx_rpc.py'],
    python_requires='>=3.6',
    # via environment variables, in which case I've tested with 15.0.4
    # "x11_hash" package (1.4) is required to sync DASH network.
    install_requires=['aiorpcX[ws]>=0.18.5,<0.19', 'attrs',
                      'plyvel', 'pylru', 'aiohttp>=3.3,<4'],
    extras_require={
        'rapidjson': ['python-rapidjson>=0.4.1,<2.0'],
        'rocksdb': ['python-rocksdb>=0.6.9'],
        'ujson': ['ujson>=2.0.0,<4.0.0'],
        'uvloop': ['uvloop>=0.14'],
        # For various coins
        'blake256': ['blake256>=0.1.1'],
        'crypto': ['pycryptodomex>=3.8.1'],
        'groestl': ['groestlcoin-hash>=1.0.1'],
        'tribushashm': ['tribushashm>=1.0.5'],
        'xevan-hash': ['xevan-hash'],
        'x11-hash': ['x11-hash>=1.4'],
        'zny-yespower-0-5': ['zny-yespower-0-5'],
        'bell-yespower': ['bell-yespower'],
        'cpupower': ['cpupower'],
    },
    packages=setuptools.find_packages(exclude=['tests']),
    description='ElectrumX Server',
    author='Neil Booth',
    author_email='kyuupichan@gmail.com',
    license='MIT Licence',
    url='https://github.com/kyuupichan/electrumx/',
    long_description='Server implementation for the Electrum wallet',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
    ],
)
