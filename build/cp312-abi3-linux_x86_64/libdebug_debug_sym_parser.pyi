from collections.abc import Iterable, Iterator
from typing import overload


class ElfInfo:
    """Information about an ELF file"""

    @property
    def build_id(self) -> str:
        """The build ID of the ELF file"""

    @property
    def debuglink(self) -> str:
        """The debug link of the ELF file"""

    @property
    def symbols(self) -> SymbolVector:
        """The symbols of the ELF file"""

class SymbolInfo:
    """Symbol information"""

    @property
    def name(self) -> str:
        """The name of the symbol"""

    @property
    def low_pc(self) -> int:
        """The low address of the symbol"""

    @property
    def high_pc(self) -> int:
        """The high address of the symbol"""

class SymbolVector:
    """A vector of symbols"""

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: SymbolVector) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[SymbolInfo], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[SymbolInfo]: ...

    @overload
    def __getitem__(self, arg: int, /) -> SymbolInfo: ...

    @overload
    def __getitem__(self, arg: slice, /) -> SymbolVector: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: SymbolInfo, /) -> None:
        """Append `arg` to the end of the list."""

    def insert(self, arg0: int, arg1: SymbolInfo, /) -> None:
        """Insert object `arg1` before index `arg0`."""

    def pop(self, index: int = -1) -> SymbolInfo:
        """Remove and return item at `index` (default last)."""

    def extend(self, arg: SymbolVector, /) -> None:
        """Extend `self` by appending elements from `arg`."""

    @overload
    def __setitem__(self, arg0: int, arg1: SymbolInfo, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: SymbolVector, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

def collect_external_symbols(debug_file_path: str, debug_info_level: int) -> SymbolVector:
    """
    Collect the external symbols from a debug file

    Args:
        debug_file_path (str): The path to the debug file
        debug_info_level (int): The debug info level for parsing.

    Returns:
        list: A list of external symbols
    """

def read_elf_info(elf_file_path: str, debug_info_level: int) -> ElfInfo:
    """
    Read the symbol table and the build ID from an ELF file

    Args:
        elf_file_path (str): The path to the ELF file
        debug_info_level (int): The debug info level for parsing.

    Returns:
        tuple: A tuple containing the symbol table, the build ID and the debug file path
    """
