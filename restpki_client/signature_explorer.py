from abc import ABCMeta

from .file_result import FileResult
from .file_reference import FileReference


class SignatureExplorer(object):
    __metaclass__ = ABCMeta

    def __init__(self, client):
        self._client = client
        self._signature_file = None

        self.__validate = None
        self.__security_context_id = None
        self.__default_signature_policy_id = None
        self.__acceptable_explicit_policies = None
        self.__ignore_revocation_status_unknown = False

    # region "client" accessors

    @property
    def client(self):
        return self.__get_client()

    def __get_client(self):
        return self._client

    @client.setter
    def client(self, value):
        self.__set_client(value)

    def __set_client(self, value):
        if value is None:
            raise Exception('The provided "client" is not valid')
        self._client = value

    # endregion

    # region "signature_file" accessors

    @property
    def signature_file(self):
        return self.__get_signature_file()

    def __get_signature_file(self):
        return self._signature_file.file_desc

    @signature_file.setter
    def signature_file(self, value):
        self.__set_signature_file(value)

    def __set_signature_file(self, value):
        if value is None:
            raise Exception('The provided "signature_file" is not valid')
        self._signature_file = FileReference.from_file(value)

    # endregion

    # region "signature_file_path" accessors

    @property
    def signature_file_path(self):
        return self.__get_signature_file_path()

    def __get_signature_file_path(self):
        return self._signature_file.path

    @signature_file_path.setter
    def signature_file_path(self, value):
        self.__set_signature_file_path(value)

    def __set_signature_file_path(self, value):
        if value is None:
            raise Exception('The provided "signature_file_path" is not valid')
        self._signature_file = FileReference.from_path(value)

    # endregion

    # region "signature_file_raw" accessors

    @property
    def signature_file_raw(self):
        return self.__get_signature_file_raw()

    def __get_signature_file_raw(self):
        return self._signature_file.content_raw

    @signature_file_raw.setter
    def signature_file_raw(self, value):
        self.__set_signature_file_raw(value)

    def __set_signature_file_raw(self, value):
        if value is None:
            raise Exception('The provided "signature_file_raw" is not valid')
        self._signature_file = FileReference.from_content_raw(value)

    # endregion

    # region "signature_file_base64" accessors

    @property
    def signature_file_base64(self):
        return self.__get_signature_file_base64()

    def __get_signature_file_base64(self):
        return self._signature_file.content_base64

    @signature_file_base64.setter
    def signature_file_base64(self, value):
        self.__set_signature_file_base64(value)

    def __set_signature_file_base64(self, value):
        if value is None:
            raise Exception('The provided "signature_file_base64" is not valid')
        self._signature_file_base64 = FileReference.from_content_base64(value)

    # endregion

    # region "signature_file_blob_token" accessors

    @property
    def signature_file_blob_token(self):
        return self.__get_signature_file_blob_token()

    def __get_signature_file_blob_token(self):
        return self._signature_file.blob_token

    @signature_file_blob_token.setter
    def signature_file_blob_token(self, value):
        self.__set_signature_file_blob_token(value)

    def __set_signature_file_blob_token(self, value):
        if value is None:
            raise Exception('The provided "signature_file_blob_token" is not '
                            'valid')
        self._signature_file = FileReference.from_blob(value)

    # endregion

    # region "signature_file_result" accessors

    @property
    def signature_file_result(self):
        return self.__get_signature_file_result()

    def __get_signature_file_result(self):
        result = FileResult(self._client, self._signature_file.content_base64)
        return result

    @signature_file_result.setter
    def signature_file_result(self, value):
        self.__set_signature_file_result(value)

    def __set_signature_file_result(self, value):
        if value is None:
            raise Exception('The provided "signature_file_result" is not valid')
        self._signature_file = FileReference.from_result(value)

    # endregion

    # region "validate" accessors

    @property
    def validate(self):
        return self.__get_validate()

    def __get_validate(self):
        return self.__validate

    @validate.setter
    def validate(self, value):
        self.__set_validate(value)

    def __set_validate(self, value):
        if value is None:
            raise Exception('The provided "validate" is not valid')
        self.__validate = value

    # endregion

    # region "security_context_id" accessors

    @property
    def security_context_id(self):
        return self.__get_security_context_id()

    def __get_security_context_id(self):
        return self.__security_context_id

    @security_context_id.setter
    def security_context_id(self, value):
        self.__set_security_context_id(value)

    def __set_security_context_id(self, value):
        if value is None:
            raise Exception('The provided "security_context_id" is not valid')
        self.__security_context_id = value

    # endregion

    # region "default_signature_policy_id" accessors

    @property
    def default_signature_policy_id(self):
        return self.__get_default_signature_policy_id()

    def __get_default_signature_policy_id(self):
        return self.__default_signature_policy_id

    @default_signature_policy_id.setter
    def default_signature_policy_id(self, value):
        self.__set_default_signature_policy_id(value)

    def __set_default_signature_policy_id(self, value):
        if value is None:
            raise Exception('The provided "default_signature_policy_id" is not '
                            'valid')
        self.__default_signature_policy_id = value

    # endregion

    # region "acceptable_explicit_policies" accessors

    @property
    def acceptable_explicit_policies(self):
        return self.__get_acceptable_explicit_policies()

    def __get_acceptable_explicit_policies(self):
        return self.__acceptable_explicit_policies

    @acceptable_explicit_policies.setter
    def acceptable_explicit_policies(self, value):
        self.__set_acceptable_explicit_policies(value)

    def __set_acceptable_explicit_policies(self, value):
        if value is None:
            raise Exception('The provided "acceptable_explicit_policies" is not'
                            ' valid')
        self.__acceptable_explicit_policies = value

    # endregion

    # region "ignore_revocation_status_unknown" accessors

    @property
    def ignore_revocation_status_unknown(self):
        return self.__get_ignore_revocation_status_unknown()

    def __get_ignore_revocation_status_unknown(self):
        return self.__ignore_revocation_status_unknown

    @ignore_revocation_status_unknown.setter
    def ignore_revocation_status_unknown(self, value):
        self.__set_ignore_revocation_status_unknown(value)

    def __set_ignore_revocation_status_unknown(self, value):
        if value is None:
            raise Exception('The provided "ignore_revocation_status_unknown" is'
                            ' not valid')
        self.__ignore_revocation_status_unknown = value

    # endregion

    def _fill_request(self, request):
        request['validate'] = self.__validate
        request['defaultSignaturePolicyId'] = self.__default_signature_policy_id
        request['securityContextId'] = self.__security_context_id
        request['ignoreRevocationStatusUnknown'] = \
            self.__ignore_revocation_status_unknown
        if self.__acceptable_explicit_policies is not None:
            policy_ids = [policy.id for policy in
                          self.__acceptable_explicit_policies.policies]
            request['acceptableExplicitPolicies'] = policy_ids
        request['file'] = \
            self._signature_file.upload_or_reference(self._client)


__all__ = ['SignatureExplorer']
