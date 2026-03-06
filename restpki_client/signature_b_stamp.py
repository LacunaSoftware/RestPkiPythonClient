from .digest_algorithm_and_value import DigestAlgorithmAndValue
from .file_reference import FileReference

class SignatureBStamp:
    def __init__(self, model):
        # None verification for optional fields
        self.document_digests = model.document_digests if model.document_digests else []
        self.index_digests = model.index_digests if model.index_digests else []
        self.index_file = model.index_file
        self.blockchain = model.blockchain.lower() if model.blockchain and model.blockchain in ['bitcoin', 'fabric'] else None
        self.transaction_id = model.transaction_id
        self.block_number = model.block_number
        self.block_date = model.block_date



    # Getters and setters for all fields
    @property
    def document_digests(self):
        return self._document_digests

    @document_digests.setter
    def document_digests(self, value):
        if not isinstance(value, list) or not all(isinstance(item, DigestAlgorithmAndValue) for item in value):
            raise TypeError("document_digests must be a list of DigestAlgorithmAndValueModel objects")
        self._document_digests = value

    @property
    def index_digests(self):
        return self._index_digests

    @index_digests.setter
    def index_digests(self, value):
        if not isinstance(value, list) or not all(isinstance(item, DigestAlgorithmAndValue) for item in value):
            raise TypeError("index_digests must be a list of DigestAlgorithmAndValueModel objects")
        self._index_digests = value

    @property
    def index_file(self):
        return self._index_file

    @index_file.setter
    def index_file(self, value):
        if not isinstance(value, FileReference):
            raise TypeError("index_file must be a FileModel object")
        self._index_file = value

    @property
    def blockchain(self):
        return self._blockchain

    @blockchain.setter
    def blockchain(self, value):
        if not value or value.lower() not in ['bitcoin', 'fabric']:
            raise ValueError("blockchain must be either 'bitcoin' or 'fabric'")
        self._blockchain = value

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value

    @property
    def block_number(self):
        return self._block_number

    @block_number.setter
    def block_number(self, value):
        if not isinstance(value, int):
            raise TypeError("block_number must be an integer")
        self._block_number = value

    @property
    def block_date(self):
        return self._block_date

    @block_date.setter
    def block_date(self, value):
        if not isinstance(value, str):
            raise TypeError("block_date must be a string")
        self._block_date = value

__all__ = ['SignatureBStamp'] 