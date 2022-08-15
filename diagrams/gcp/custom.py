from . import _GCP


class Custom(_GCP):
    _type = "custom"
    _icon_dir = "resources/gcp/custom"


class Eventarc(_Custom):
    _icon = "eventarc.png"
