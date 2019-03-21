class Oids(object):
    # region Digest Algorithms
    MD5 = '1.2.840.113549.2.5'
    SHA1 = '1.3.14.3.2.26'
    # SHA224 = '2.16.840.1.101.3.4.2.4', # RFC 3874 section 4
    SHA256 = '2.16.840.1.101.3.4.2.1'
    SHA384 = '2.16.840.1.101.3.4.2.2'
    SHA512 = '2.16.840.1.101.3.4.2.3'
    SHA3_256 = '2.16.840.1.101.3.4.2.8'
    # endregion

    # region Signature Algorithms
    MD2_WITH_RSA = '1.2.840.113549.1.1.2'
    MD5_WITH_RSA = '1.2.840.113549.1.1.4'
    SHA1_WITH_RSA = '1.2.840.113549.1.1.5'
    SHA256_WITH_RSA = '1.2.840.113549.1.1.11'
    SHA384_WITH_RSA = '1.2.840.113549.1.1.12'
    SHA512_WITH_RSA = '1.2.840.113549.1.1.13'

    SHA1_WITH_DSA = '1.2.840.10040.4.3'           # RFC 3279 section 2.2.2
    # SHA224_WITH_DSA = '2.16.840.1.101.3.4.3.1'  # RFC 5758 section 3.1
    SHA256_WITH_DSA = '2.16.840.1.101.3.4.3.2'    # RFC 5758 section 3.1
    # endregion

    # region Asymmetric Algorithms
    RSA = '1.2.840.113549.1.1.1'  # RFC 3279 section 2.3.1
    DSA = '1.2.840.10040.4.1'     # RFC 3279 section 2.3.2
    # endregion


__all__ = ['Oids']
