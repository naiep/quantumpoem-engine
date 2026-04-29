"""Core sonnet generation engine."""

import random
from typing import List


class SonnetGenerator:
    """Generates Shakespearean sonnets with quantum-inspired structure."""

    def __init__(self):
        """Initialize the sonnet generator with thematic quatrains and couplet."""
        self.quatrains = [
            [
                "When time unwinds like thread through cosmic loom,",
                "And stars recall the verse they once sang true,",
                "The mind becomes a vast and quantum room,",
                "Where every thought both false and real is new.",
            ],
            [
                "The logic gates collapse to fermi states,",
                "And meaning flows through anticommuting space,",
                "Where pronouns bind to what the heart creates,",
                "And anaphora reveals the truth we chase.",
            ],
            [
                "Yet in the silence, patterns start to form,",
                "Like operators aligned in sacred dance,",
                "The quantum poem, born of form and storm,",
                "Grants consciousness a fleeting second glance.",
            ],
        ]

        self.couplet = [
            "Thus meaning blooms where logic dares not tread,",
            "A poem born where fermions hold the thread.",
        ]

    def generate(self) -> str:
        """Generate a complete Shakespearean sonnet.

        Returns:
            str: A 14-line sonnet with ABAB CDCD EFEF GG rhyme scheme.
        """
        lines = []

        # Select two random quatrains
        selected_quatrains = random.sample(self.quatrains, 2)
        for quatrain in selected_quatrains:
            lines.extend(quatrain)

        # Add the couplet
        lines.extend(self.couplet)

        return "\n".join(lines)

    def generate_batch(self, count: int = 3) -> List[str]:
        """Generate multiple sonnets.

        Args:
            count: Number of sonnets to generate.

        Returns:
            List of sonnet strings.
        """
        return [self.generate() for _ in range(count)]
