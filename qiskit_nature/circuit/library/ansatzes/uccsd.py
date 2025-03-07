# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""
The UCCSD Ansatz.
"""

from typing import Optional, Tuple

import logging

from qiskit.circuit import QuantumCircuit
from qiskit_nature.operators.second_quantization.qubit_converter import QubitConverter
from .ucc import UCC

logger = logging.getLogger(__name__)


class UCCSD(UCC):
    """The UCCSD Ansatz.

    This is a convenience subclass of the UCC Ansatz. For more information refer to :class:`UCC`.
    """

    def __init__(self, qubit_converter: Optional[QubitConverter] = None,
                 num_particles: Optional[Tuple[int, int]] = None,
                 num_spin_orbitals: Optional[int] = None,
                 reps: int = 1,
                 initial_state: Optional[QuantumCircuit] = None):
        """
        Args:
            qubit_converter: the QubitConverter instance which takes care of mapping a
                :class:`~.SecondQuantizedOp` to a :class:`PauliSumOp` as well as performing all
                configured symmetry reductions on it.
            num_particles: the tuple of the number of alpha- and beta-spin particles.
            num_spin_orbitals: the number of spin orbitals.
            reps: The number of times to repeat the evolved operators.
            initial_state: A `QuantumCircuit` object to prepend to the circuit.
        """
        super().__init__(qubit_converter=qubit_converter,
                         num_particles=num_particles,
                         num_spin_orbitals=num_spin_orbitals,
                         excitations='sd',
                         alpha_spin=True,
                         beta_spin=True,
                         max_spin_excitation=None,
                         reps=reps,
                         initial_state=initial_state)
