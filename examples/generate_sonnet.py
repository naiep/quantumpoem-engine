"""Demo script: Generate quantum sonnets with sanam-nama integration."""

import sys
sys.path.insert(0, '../')

from src.qpe.poem_generator import SonnetGenerator
from src.qpe.fermion_anaphora import FermionAnaphora
from src.qpe.sanam_nama_bridge import SanamNamaBridge


def main():
    """Generate and display quantum sonnets."""
    print("\n" + "="*70)
    print("✨ QUANTUM POEM ENGINE - Sonnet Generation Demo ✨".center(70))
    print("="*70 + "\n")

    # Initialize the sonnet generator
    generator = SonnetGenerator()

    # Generate and display sonnets
    print("Generating 2 quantum sonnets...\n")
    for i in range(2):
        sonnet = generator.generate()
        print(f"--- Sonnet {i+1} ---")
        print(sonnet)
        print()

    # Demo fermionic anaphora + sanam-nama bridge
    print("\n" + "-"*70)
    print("Fermionic Anaphora + Sanam-Nama Integration Demo".center(70))
    print("-"*70 + "\n")

    fa = FermionAnaphora(entities=["the moon", "the tide", "the heart"])
    fa.bind("she", "the moon")
    fa.bind("it", "the tide")
    fa.bind("her", "the moon")

    print(f"Fermionic State: {fa}\n")
    print(f"Pronoun Bindings (resolved): {fa.resolve()}")
    print(f"Semantic Coherence Score: {fa.coherence_score():.3f}\n")

    # Initialize sanam-nama bridge
    bridge = SanamNamaBridge(fa)
    bridge.register_sacred_name("the moon", "Luna's Resonance")
    bridge.register_sacred_name("the tide", "Ocean's Pulse")
    bridge.register_sacred_name("the heart", "Aether's Echo")

    print("Sacred Resonance Mapping:")
    for entity, resonance in bridge.generate_resonance_map().items():
        alignment = bridge.compute_semantic_alignment("she", entity)
        print(f"  {entity:15} → {resonance:25} [alignment: {alignment:.3f}]")

    print("\n" + "-"*70)
    print("Anticommutation Relations:".center(70))
    print("-"*70)
    print(
        f"{{a_moon, a†_tide}} = {fa.anticommutation_relation('the moon', 'the tide')}"
    )
    print(
        f"{{a_moon, a†_moon}} = {fa.anticommutation_relation('the moon', 'the moon')}"
    )
    print()


if __name__ == "__main__":
    main()
