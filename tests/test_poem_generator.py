"""Unit tests for the sonnet generator."""

import pytest
from src.qpe.poem_generator import SonnetGenerator
from src.qpe.fermion_anaphora import FermionAnaphora
from src.qpe.sanam_nama_bridge import SanamNamaBridge
from src.qpe.utils import extract_pronouns, rhyme_check, syllable_count


class TestSonnetGenerator:
    """Tests for SonnetGenerator class."""

    def test_generate_returns_sonnet(self):
        """Test that generate() returns a sonnet string."""
        gen = SonnetGenerator()
        sonnet = gen.generate()
        assert isinstance(sonnet, str)
        assert len(sonnet) > 0

    def test_sonnet_has_14_lines(self):
        """Test that generated sonnet has 14 lines."""
        gen = SonnetGenerator()
        sonnet = gen.generate()
        lines = sonnet.split("\n")
        assert len(lines) == 14

    def test_generate_batch(self):
        """Test batch sonnet generation."""
        gen = SonnetGenerator()
        sonnets = gen.generate_batch(count=5)
        assert len(sonnets) == 5
        for sonnet in sonnets:
            assert len(sonnet.split("\n")) == 14


class TestFermionAnaphora:
    """Tests for FermionAnaphora class."""

    def test_initialization(self):
        """Test FermionAnaphora initialization."""
        entities = ["moon", "tide", "heart"]
        fa = FermionAnaphora(entities=entities)
        assert fa.entities == entities

    def test_bind_pronoun(self):
        """Test pronoun binding."""
        fa = FermionAnaphora(entities=["the moon"])
        fa.bind("she", "the moon")
        assert fa.bindings["she"] == "the moon"

    def test_resolve(self):
        """Test binding resolution."""
        fa = FermionAnaphora(entities=["moon", "tide"])
        fa.bind("she", "moon")
        fa.bind("it", "tide")
        resolved = fa.resolve()
        assert resolved == {"she": "moon", "it": "tide"}

    def test_coherence_score(self):
        """Test semantic coherence scoring."""
        fa = FermionAnaphora(entities=["moon", "tide"])
        assert fa.coherence_score() == 0.0  # No bindings
        fa.bind("she", "moon")
        assert fa.coherence_score() == 1.0  # All bind to same entity
        fa.bind("it", "tide")
        assert fa.coherence_score() == 1.0  # 2 unique / 2 bindings

    def test_anticommutation_relation(self):
        """Test anticommutation relation computation."""
        fa = FermionAnaphora(entities=["entity1", "entity2"])
        anticomm = fa.anticommutation_relation("entity1", "entity2")
        assert anticomm is not None


class TestSanamNamaBridge:
    """Tests for SanamNamaBridge class."""

    def test_bridge_initialization(self):
        """Test SanamNamaBridge initialization."""
        fa = FermionAnaphora(entities=["moon"])
        bridge = SanamNamaBridge(fa)
        assert bridge.fermion_anaphora is not None

    def test_register_sacred_name(self):
        """Test sacred name registration."""
        bridge = SanamNamaBridge()
        bridge.register_sacred_name("the moon", "Luna's Resonance")
        assert bridge.get_sacred_name("the moon") == "Luna's Resonance"

    def test_generate_resonance_map(self):
        """Test resonance map generation."""
        fa = FermionAnaphora(entities=["moon", "tide"])
        bridge = SanamNamaBridge(fa)
        resonance_map = bridge.generate_resonance_map()
        assert len(resonance_map) == 2
        assert "moon" in resonance_map
        assert "tide" in resonance_map


class TestUtilityFunctions:
    """Tests for utility functions."""

    def test_extract_pronouns(self):
        """Test pronoun extraction."""
        text = "She walked and he followed, then they danced."
        pronouns = extract_pronouns(text)
        assert "she" in pronouns
        assert "he" in pronouns
        assert "they" in pronouns

    def test_rhyme_check(self):
        """Test rhyme checking."""
        line1 = "When time unwinds like thread through cosmic loom,"
        line2 = "And mind becomes a vast and quantum room,"
        assert rhyme_check(line1, line2)

    def test_syllable_count(self):
        """Test syllable counting."""
        text = "hello"
        count = syllable_count(text)
        assert count >= 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
