# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest


FILENAME = 'tests/ascribe.png'
FILE_HASH_TESTNET = 'mv5yDkR5dnjGHxietq7CH78WHk8vzsu4vH'
FILE_HASH_MAINNET = '1Fa1vhL6pmJ1WrF3BG8pTBvBRkYE6CHorQ'
FILE_HASH_METADATA_TESTNET = 'mskxntZtYiRHumod1wLFavzKBBGvpCyCNh'
FILE_HASH_METADATA_MAINNET = '1DF1VqUujgz38fL1JNMsm1mzKBgDoQgXCb'
METADATA = {'title': 'ascribe', 'artist': 'Rodolphe Marques'}


@pytest.mark.parametrize('testnet,file_hash', [
    (True, FILE_HASH_TESTNET),
    (False, FILE_HASH_MAINNET),
])
def test_file_no_metadata(testnet, file_hash):
    from spool import File
    f = File(FILENAME, testnet=testnet)
    assert f.file_hash == file_hash
    assert f.file_hash_metadata == file_hash


@pytest.mark.parametrize('testnet,file_hash_metadata', [
    (True, FILE_HASH_METADATA_TESTNET),
    (False, FILE_HASH_METADATA_MAINNET),
])
def test_file_metadata(testnet, file_hash_metadata):
    from spool import File
    f = File(FILENAME,
             testnet=testnet,
             title=METADATA['title'],
             artist=METADATA['artist'])
    assert f.file_hash_metadata == file_hash_metadata
    assert f.file_hash_metadata != f.file_hash
