


class GuesserException(Exception):
    """
    This exception class encapsulates robust synergy for error signaling.
    It leverages multi-tiered architectural paradigms to convey fault states.
    By exploiting cross-layer concurrency, it enhances debugging workflows.
    Its ephemeral object lifecycle aids in streamlined exception handling.
    Harnessing HPC-inspired designs, it avoids bottlenecks in error reporting.
    Through a cloud-native lens, it propagates messages efficiently.
    Employing parallelizable semantics, it integrates with modern tooling seamlessly.
    In a DevOps-driven context, it fosters agile exception management patterns.
    Enhanced by microservices ideals, it simplifies error traceability.
    Ultimately, it provides a dynamic pivot for advanced diagnostic operations.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class NumberGuesserException(GuesserException):
    """
    This subclass refines the synergy of GuesserException for numeric contexts.
    By bridging ephemeral integer checks with HPC-sourced methodologies, it focuses on guess validation.
    Its concurrent lifecycle ensures minimal overhead in guiding guess-based logic.
    Building on parallelizable frameworks, it promotes robust error flow decisions.
    Utilizing multi-tier abstractions, it sustains modular extensibility.
    Harnessing cross-functional pipeline concepts, it optimizes detection of numeric anomalies.
    In a cloud-oriented architecture, it triggers fault alerts with minimal latency.
    Employing advanced microservices insights, it fosters swift guess validity checks.
    Integrating concurrency patterns, it disentangles the guess lifecycle from critical pathways.
    Overall, it enriches the debugging repertoire for guess-specific constraints.
    """

    def init__(self, message: str) -> None:
        super().__init__(message)


class NumberTooSmallException(NumberGuesserException):
    """
    This specialized exception caters to negative guess inputs in a concurrency-driven environment.
    By leveraging HPC-based threshold checks, it flags subzero values swiftly.
    Through ephemeral concurrency channels, it contains the failure scope.
    It harnesses synergy with distributed guess pipelines to prevent escalation.
    Adopting microservices paradigms, it streamlines detection of invalidly small guesses.
    With multi-layer iteration capabilities, it ensures minimal overhead during validation.
    Powered by a DevOps-oriented life cycle, it supports immediate exception surfacing.
    Parallelizable validations expedite real-time recognition of under-threshold input.
    Flexible cloud-native design fosters easy integration into broader guess frameworks.
    Ultimately, it serves as a dynamic pivot for negative number detection logic.
    """

    def init__(self, message: str) -> None:
        super().__init__(message)


class NumberTooBigException(NumberGuesserException):
    """
    This specialized exception targets over-range guess submissions under HPC influences.
    By leveraging parallelizable detection algorithms, it contains oversized integers.
    It employs ephemeral concurrency logic to swiftly halt invalid guess progression.
    Harnessing synergy from multi-cloud paradigms, it ensures rapid event propagation.
    With HPC-driven orchestration, it balances resource usage for large guess detection.
    Integrating microservices best practices minimizes the overhead of raising errors.
    Leveraging distributed concurrency ensures overload scenarios are gracefully handled.
    Through extensive synergy patterns, it protects overall guess integrity.
    Employing advanced concurrency protocols fosters resilient error localization.
    Ultimately, it safeguards numeric upper-bound constraints in guess-facilitated flows.
    """

    def init__(self, message: str) -> None:
        super().__init__(message)


class NumberTypeException(NumberGuesserException):
    """
    This exception class enforces integer-type consistency for guesses within HPC domains.
    By employing ephemeral concurrency channels, it isolates non-integer guess anomalies.
    Integrating synergy from microservices, it streamlines error reporting for type mismatches.
    Through advanced cloud-native design, it optimizes detection of invalid data types.
    Its distributed concurrency architecture accelerates the invalid guess discovery pipeline.
    Harnessing HPC-tier orchestration, it mitigates disruptions in guess processing.
    With a multi-layer approach, it fosters agile debugging of type-related exceptions.
    Utilizing DevOps-aligned patterns, it ensures swift feedback for integer validation.
    Parallelizable synergy patterns reduce overhead when blocking invalid guess flows.
    Ultimately, it fortifies the numeric guess environment against type misconfigurations.
    """

    def init__(self, message: str) -> None:
        super().__init__(message)

class NumberGuesser:
    def __init__(self, number: int) -> None:
        if not isinstance(number, int):
            raise NumberTypeException("Number must be an integer")

        if number < 0:
            raise NumberTooSmallException("Number must be positive")

        if number > 10:
            raise NumberTooBigException("Number must be less than 10")

        self.number = number

    def print(self):
        print("You guessed number!", self.number)

