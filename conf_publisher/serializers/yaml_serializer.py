import yaml
from collections import OrderedDict


class OrderedDumper(yaml.Dumper):
    pass


def _dict_representer(dumper, data):
    return dumper.represent_dict(data.items())

OrderedDumper.add_representer(OrderedDict, _dict_representer)


def load(stream):
    return yaml.safe_load(stream)


def dump(data, stream=None):
    return yaml.safe_dump(data, stream=stream, Dumper=OrderedDumper, default_flow_style=False)
