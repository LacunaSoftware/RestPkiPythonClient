class PadesVisualPositioningPresets(object):
    cached_presets = dict()

    def __init__(self):
        pass

    @classmethod
    def get_footnote(cls, client, page_number=None, rows=None):

        url_segment = 'Footnote'
        if page_number:
            url_segment += '?pageNumber=%s' % page_number

        if rows:
            url_segment += '&' if page_number else '?'
            url_segment += 'rows=%s' % rows

        return PadesVisualPositioningPresets._get_preset(client, url_segment)

    @classmethod
    def get_new_page(cls, client):
        return PadesVisualPositioningPresets._get_preset(client,
                                                         'NewPage')

    @classmethod
    def _get_preset(cls, client, url_segment):
        if url_segment in PadesVisualPositioningPresets.cached_presets:
            return PadesVisualPositioningPresets.cached_presets[url_segment]

        preset = client.get(
            'Api/PadesVisualPositioningPresets/%s' % url_segment)

        PadesVisualPositioningPresets.cached_presets[url_segment] = preset
        return preset


__all__ = ['PadesVisualPositioningPresets']
