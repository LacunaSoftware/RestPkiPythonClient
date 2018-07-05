class PadesVisualPositioningPresets:
    _cached_presets = dict()

    def __init__(self):
        return

    @staticmethod
    def get_footnote(restpki_client, page_number=None, rows=None):
        url_segment = 'Footnote'

        if page_number is not None:
            url_segment += '?pageNumber=%s' % page_number

        if rows is not None:
            url_segment += '?rows=%s' % rows

        return PadesVisualPositioningPresets._get_preset(restpki_client,
                                                         url_segment)

    @staticmethod
    def get_new_page(restpki_client):
        return PadesVisualPositioningPresets._get_preset(restpki_client,
                                                         'NewPage')

    @staticmethod
    def _get_preset(restpki_client, url_segment):
        if url_segment in PadesVisualPositioningPresets._cached_presets:
            return PadesVisualPositioningPresets._cached_presets[url_segment]

        preset = restpki_client.get(
            'Api/PadesVisualPositioningPresets/%s' % url_segment)
        PadesVisualPositioningPresets._cached_presets[
            url_segment] = preset.json()
        return preset.json()


__all__ = ['PadesVisualPositioningPresets']
