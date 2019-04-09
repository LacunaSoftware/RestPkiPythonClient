import six


@six.python_2_unicode_compatible
class ValidationResults(object):

    def __init__(self, model):
        self._errors = None
        self._warnings = None
        self._passed_checks = None

        if model.get('errors', None) is not None:
            self._errors = self._convert_items(model['errors'])

        if model.get('warnings', None) is not None:
            self._warnings = self._convert_items(model['warnings'])

        if model.get('passedChecks', None) is not None:
            self._passed_checks = self._convert_items(model['passedChecks'])

    @property
    def errors(self):
        return self._errors

    @errors.setter
    def errors(self, value):
        self._errors = value

    @property
    def warning(self):
        return self._warnings

    @warning.setter
    def warning(self, value):
        self._warnings = value

    @property
    def passed_checks(self):
        return self._passed_checks

    @passed_checks.setter
    def passed_checks(self, value):
        self._passed_checks = value

    @property
    def is_valid(self):
        return len(self._errors) == 0

    @property
    def checks_performed(self):
        return len(self._errors) + \
               len(self._warnings) + \
               len(self._passed_checks)

    @property
    def has_errors(self):
        return not len(self._errors) == 0

    @property
    def has_warnings(self):
        return not len(self._warnings) == 0

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
                text += ', %s errors' % len(self._errors)
            if self.has_warnings:
                text += ', %s warnings' % len(self._warnings)
            if len(self._passed_checks) > 0:
                if not self.has_errors and not self.has_warnings:
                    text += ', all passed'
                else:
                    text += ', %s passed' % len(self._passed_checks)

        return text

    def __str__(self):
        return self.to_string(0)

    def to_string(self, indentation_level):
        tab = '\t' * indentation_level
        text = ''
        text += self.get_summary(indentation_level)

        if self.has_errors:
            text += '\n%sErrors:\n' % tab
            text += self._join_items(self._errors, indentation_level)

        if self.has_warnings:
            text += '\n%sWarnings:\n' % tab
            text += self._join_items(self._warnings, indentation_level)

        if self._passed_checks is not None:
            text += '\n%sPassed checks:\n' % tab
            text += self._join_items(self._passed_checks, indentation_level)

        return text


class ValidationItem:

    def __init__(self, model):
        self._item_type = model.get('type', None)
        self._message = model.get('message', None)
        self._detail = model.get('detail', None)
        self._inner_validation_results = None

        if model.get('innerValidationResults', None) is not None:
            self._inner_validation_results = ValidationResults(
                model['innerValidationResults'])

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value

    @property
    def inner_validation_results(self):
        return self._inner_validation_results

    @inner_validation_results.setter
    def inner_validation_results(self, value):
        self._inner_validation_results = value

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.to_string(0)

    def to_string(self, indentation_level):
        text = ''
        text += self._message

        if self._detail is not None and len(self._detail) > 0:
            text += ' (%s)' % self._detail

        if self._inner_validation_results is not None:
            text += '\n'
            text += ''
            text += self._inner_validation_results\
                .to_string(indentation_level + 1)

        return text


__all__ = [
    'ValidationResults',
    'ValidationItem'
]
