"""QuantumPoem Engine (QPE) - Quantum-inspired poetry generation."""

__version__ = "0.1.0"
__author__ = "Umair Siddiquie"
__description__ = "Quantum-inspired poetic structure engine using fermionic anaphora and sanam-nama modeling"

from .poem_generator import SonnetGenerator
from .fermion_anaphora import FermionAnaphora
from .sanam_nama_bridge import SanamNamaBridge

__all__ = ["SonnetGenerator", "FermionAnaphora", "SanamNamaBridge"]
