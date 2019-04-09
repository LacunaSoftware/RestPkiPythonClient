class PadesVisualPositioningPresets(object):
    cached_presets = dict()

    @staticmethod
    def get_footnote(client, page_number=None, rows=None):

        url_segment = 'Footnote'
        if page_number:
            url_segment += '?pageNumber=%s' % page_number

        if rows:
            url_segment += '&' if page_number else '?'
            url_segment += 'rows=%s' % rows

        return PadesVisualPositioningPresets.__get_preset(client, url_segment)

    @staticmethod
    def get_new_page(client):
        return PadesVisualPositioningPresets.__get_preset(client,
                                                          'NewPage')

    @staticmethod
    def __get_preset(client, url_segment):
        if url_segment in PadesVisualPositioningPresets.cached_presets:
            return PadesVisualPositioningPresets.cached_presets[url_segment]

        preset = client.get(
            'Api/PadesVisualPositioningPresets/%s' % url_segment)

        PadesVisualPositioningPresets.cached_presets[url_segment] = preset
        return preset


__all__ = ['PadesVisualPositioningPresets']
