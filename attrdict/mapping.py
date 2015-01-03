"""
An implementation of MutableAttr
"""
from collections import Mapping

from attrdict.mixins import MutableAttr


class AttrMap(MutableAttr):
    """
    An implementation of MutableAttr.
    """
    def __init__(self, items=None, sequence_type=tuple):
        if items is None:
            items = {}
        elif not isinstance(items, Mapping):
            items = dict(items)

        self.__setattr__('_sequence_type', sequence_type, force=True)
        self.__setattr__('_mapping', items, force=True)
        self.__setattr__('_allow_invalid_attributes', False, force=True)

    def _configuration(self):
        """
        The configuration for an attrmap instance.
        """
        return self._sequence_type

    def __getitem__(self, key):
        """
        Access a value associated with a key.
        """
        return self._mapping[key]

    def __setitem__(self, key, value):
        """
        Add a key-value pair to the instance.
        """
        self._mapping[key] = value

    def __delitem__(self, key):
        """
        Delete a key-value pair
        """
        del self._mapping[key]

    def __len__(self):
        """
        Check the length of the mapping.
        """
        return len(self._mapping)

    def __iter__(self):
        """
        Iterated through the keys.
        """
        return iter(self._mapping)

    def __repr__(self):
        """
        Return a string representation of the object
        """
        return u"a{0}".format(repr(self._mapping))

    def __getstate__(self):
        """
        Serialize the object.
        """
        return (
            self._mapping,
            self._sequence_type,
            self._allow_invalid_attributes
        )

    def __setstate__(self, state):
        """
        Deserialize the object.
        """
        mapping, sequence_type, allow_invalid_attributes = state
        self.__setattr__('_mapping', mapping, force=True)
        self.__setattr__('_sequence_type', sequence_type, force=True)
        self.__setattr__(
            '_allow_invalid_attributes',
            allow_invalid_attributes,
            force=True
        )

    @classmethod
    def _constructor(cls, mapping, configuration):
        """
        A standardized constructor.
        """
        return cls(mapping, sequence_type=configuration)