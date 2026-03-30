import argparse
from typing import Any, Callable, Generic, Iterator, Iterable, Optional, TypeVar

T = TypeVar('T')


class Manual(argparse.Action):
    def __init__(
        self,
        option_strings,
        dest=argparse.SUPPRESS,
        default=argparse.SUPPRESS,
        help=None
    ):
        super().__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help
        )

    def __call__(self, parser, namespace, values, option_string=None):
        parser.print_manual()
        parser.exit()


class LazyChoices(argparse.Action, Generic[T]):
    def __init__(
        self,
        *args,
        getter: Callable[[], Iterable[T]],
        help_formatter: Optional[Callable[[T, bool], str]] = None,
        sort: bool = False,
        cache: bool = True,
        isolation_mode: bool = False,
        **kwargs
    ) -> None:
        self.getter = getter
        self.help_formatter = help_formatter
        self.sort = sort
        self.cache = cache
        self.isolation_mode = isolation_mode
        self._help: Optional[str] = None
        self._help_resolved: bool = False
        self._obj: Optional[Iterable[T]] = None
        super().__init__(*args, **kwargs)
        self.choices = self

    def load(self) -> T:
        if self._obj is None or not self.cache:
            self._obj = self.getter()

        assert self._obj is not None
        return self._obj

    def _resolve_help(self) -> Optional[str]:
        """Compute and cache the formatted help string by calling the getter.

        This is intentionally separate from the ``help`` property so that
        ``getter`` is only called when help text is *actually* needed (i.e.
        when ``--help`` is passed), not during parser construction.

        Python 3.14 added a ``_check_help()`` call inside
        ``ArgumentParser.add_argument()`` that accesses ``action.help`` while
        building the parser.  Previously only ``parse_args(['--help'])``
        triggered help formatting.  Without this guard, ``getter`` would be
        called eagerly — breaking the lazy evaluation contract and failing the
        test that asserts ``getter`` is not called until ``--help`` is used.
        """
        if not self._help_resolved and self.help_formatter is not None:
            self._help = self.help_formatter(
                self.load(),
                isolation_mode=self.isolation_mode
            )
            self._help_resolved = True
        return self._help

    @property
    def help(self) -> Optional[str]:
        # Return the already-resolved string if available, but do NOT call
        # _resolve_help() here.  The actual resolution is deferred until the
        # formatter explicitly asks for it (see format_help / format_usage
        # paths that call _expand_help → action.help after _resolve_help has
        # been invoked, or until the user passes --help).
        return self._help

    @help.setter
    def help(self, value: Any) -> None:
        self._help = value
        # Mark as resolved when argparse sets help directly (e.g. during
        # _check_help in Python 3.14) so we don't overwrite it later.
        if value is not None:
            self._help_resolved = True

    def __contains__(self, item: Any) -> bool:
        return item in self.load()

    def __iter__(self) -> Iterator[T]:
        if self.sort:
            return iter(sorted(self.load()))
        else:
            return iter(self.load())

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)
