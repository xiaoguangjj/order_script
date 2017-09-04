# -*- coding:utf-8 -*-

_missing = object()


class Registry(object):
    """ A registry to store and retrieve schemas and parts of it by a name
    that can be used in validation schemas.

    :param definitions: Optional, initial defintions.
    :type definitions: any :term:`mapping` """

    def __init__(self, definitions={}):
        self._storage = {}
        self.extend(definitions)

    def add(self, name, definition):
        """ Register a definition to the registry. Existing defintions are
        replaced silently.

        :param name: The name which can be used as reference in a validation
                     schema.
        :type name: :class:`str`
        :param definition: The definition.
        :type definition: any :term:`mapping` """
        self._storage[name] = definition

    def all(self):
        """ Returns a :class:`dict` with all registered definitions mapped to
        their name. """
        return self._storage

    def extend(self, definitions):
        """ Add several defintions at once. Existing defintions are
        replaced silently.

        :param definitions: The names and defintions.
        :type definitions: a :term:`mapping` or an :term:`iterable` with
                           two-value :class:`tuple` s """
        for name, definition in dict(definitions).items():
            self.add(name, definition)

    def clear(self):
        """ Purge all defintions in the registry. """
        self._storage.clear()

    def get(self, name, default=None):
        """ Retrieve a defintion from the registry.

        :param name: The reference that points to the defintion.
        :type name: :class:`str`
        :param default: Return value if the reference isn't registered. """
        return self._storage.get(name, default)

    def remove(self, *names):
        """ Unregister definitions from the registry.

        :param names: The names of the defintions that are to be
                      unregistered. """
        for name in names:
            self._storage.pop(name, None)

    def __contains__(self, item):
        return item in self._storage

    def __getattr__(self, item):
        return self.get(item)


class LRUCacheRegistry(Registry):
    # cache
    lru_ttl = 300
