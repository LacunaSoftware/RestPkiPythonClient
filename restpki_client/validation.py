import six


@six.python_2_unicode_compatible
class ValidationResults:
    errors = None
    warnings = None
    passed_checks = None

    def __init__(self, model):
        self.errors = self._convert_items(model['errors'])
        self.warnings = self._convert_items(model['warnings'])
        self.passed_checks = self._convert_items(model['passedChecks'])

    @property
    def is_valid(self):
        return len(self.errors) == 0

    @property
    def checks_performed(self):
        return len(self.errors) + len(self.warnings) + len(self.passed_checks)

    @property
    def has_errors(self):
        return not len(self.errors) == 0

    @property
    def has_warnings(self):
        return not len(self.warnings) == 0

    @staticmethod
    def _convert_items(items):
        converted = list()
        for item in items:
            converted.append(ValidationItem(item))

        return converted

    @staticmethod
    def _join_items(items, indentation_level):
        text = ''
        is_first = True
        tab = '\t' * indentation_level

        for item in items:
            if is_first:
                is_first = False
            else:
                text += '\n'

            text += '%s- ' % tab
            text += item.to_string(indentation_level)

        return text

    @property
    def summary(self):
        return self.get_summary(0)

    def get_summary(self, indentation_level=0):
        tab = '\t' * indentation_level
        text = '%sValidation results: ' % tab

        if self.checks_performed == 0:
            text += 'no checks performed'
        else:
            text += '%s checks performed' % self.checks_performed

            if self.has_errors:
                text += ', %s errors' % len(self.errors)
            if self.has_warnings:
                text += ', %s warnings' % len(self.warnings)
            if len(self.passed_checks) > 0:
                if not self.has_errors and not self.has_warnings:
                    text += ', all passed'
                else:
                    text += ', %s passed' % len(self.passed_checks)

        return text

    def __str__(self):
        return self.to_string(0)

    def to_string(self, indentation_level):
        tab = '\t' * indentation_level
        text = ''
        text += self.get_summary(indentation_level)

        if self.has_errors:
            text += '\n%sErrors:\n' % tab
            text += self._join_items(self.errors, indentation_level)

        if self.has_warnings:
            text += '\n%sWarnings:\n' % tab
            text += self._join_items(self.warnings, indentation_level)

        if self.passed_checks is not None:
            text += '\n%sPassed checks:\n' % tab
            text += self._join_items(self.passed_checks, indentation_level)

        return text


class ValidationItem:
    itemType = None
    message = ''
    detail = ''
    innerValidationResults = None

    def __init__(self, model):
        self.itemType = model['type']
        self.message = model['message']
        self.detail = model['detail']

        if model['innerValidationResults'] is not None:
            self.innerValidationResults = ValidationResults(
                model['innerValidationResults'])

    def __unicode__(self):
        return self.to_string(0)

    def to_string(self, indentation_level):
        text = ''
        text += self.message

        if self.detail is not None and len(self.detail) > 0:
            text += ' (%s)' % self.detail

        if self.innerValidationResults is not None:
            text += '\n'
            text += ''
            text += self.innerValidationResults.to_string(indentation_level + 1)

        return text


__all__ = ['ValidationResults', 'ValidationItem']
