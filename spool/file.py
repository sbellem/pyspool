# -*- coding: utf-8 -*-
"""
File related methods
"""
from __future__ import unicode_literals

import hashlib
from builtins import object, str


import bitcoin


class ExplicitUnicodeLiteral(str):

    def __repr__(self):
        """
        Always return the representation with a prefixed 'u'.

        ..note:: For some reason, using ``super().__repr__()`` would cause
            some tests to fail, somewhat randomly.

        """
        return 'u{}'.format(str.__repr__(self))

urepr = ExplicitUnicodeLiteral


class File(object):

    """
    File utility class.

    Given a file name it calculates the hash of the file and the hash of the file + metadata
    """

    def __init__(self, filename, testnet=False, **kwargs):
        """

        :param filename: Name of the file
        :param testnet: testnet flag. Defaults to False
        :param kwargs: Additional metadata to be encoded with the file.
                       e.g. {'title': 'piece title', 'artist_name': 'artist'}
        :return: File instance
        """

        self.testnet = testnet
        # prefix of the addresses to distinguish between mainnet and testnet
        self._magicbyte = 111 if testnet else 0
        self.file_hash, self.file_hash_metadata = self._calculate_hash(filename, **kwargs)

    @classmethod
    def from_hash(cls, hash):
        """

        :param hash: hash of the file
        :return: File instance
        """

        cls.hash = hash
        return cls

    def _calculate_hash(self, filename, **kwargs):
        """
        Calculates the hash of the file and the hash of the file + metadata (passed on the keywargs)
        """

        # hash to address
        with open(filename, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()

        if kwargs:
            data = str([urepr(v) for v in kwargs.values()] + [file_hash])
        else:
            data = file_hash
        address_piece_with_metadata = str(
            bitcoin.bin_to_b58check(bitcoin.bin_hash160(data.encode()),
                                    magicbyte=self._magicbyte)
        )

        address_piece = str(
            bitcoin.bin_to_b58check(bitcoin.bin_hash160(file_hash.encode()),
                                    magicbyte=self._magicbyte)
        )
        return address_piece, address_piece_with_metadata
