from typing import List, Optional, Tuple
from manim import VGroup, Text, MathTex, RIGHT, DOWN, WHITE, GRAY_C

class Hashmap:
    """
    A class to create and display hashmaps in Manim.

    Attributes
    ----------
    num_buckets : int
        Number of buckets in the hashmap.
    element_size : int
        Font size for hashmap elements.
    key_size : int
        Font size for keys.
    value_size : int
        Font size for values.
    line_spacing : float
        Spacing between elements in a bucket.
    bucket_spacing : float
        Spacing between buckets.
    hashmap : Optional[List[Tuple[str, int]]]
        Custom hashmap elements.
    element_color : str
        Color for the elements text.
    bucket_color : str
        Color for the bucket text.

    Methods
    -------
    create_buckets() -> VGroup
        Creates the buckets for the hashmap.
    create_elements() -> VGroup
        Creates the hashmap elements.
    create() -> VGroup
        Constructs the visual representation of the hashmap.

    Examples
    --------
    Basic usage:

    >>> hashmap = Hashmap(num_buckets=5)
    >>> hashmap.create()

    Custom hashmap and attributes:

    >>> custom_hashmap = [("key1", 1), ("key2", 2), ("key3", 3)]
    >>> hashmap = Hashmap(hashmap=custom_hashmap, element_size=48, bucket_color=GRAY_C)
    >>> hashmap.create()
    """

    def __init__(
        self,
        num_buckets: int = 5,
        element_size: int = 60,
        key_size: int = 48,
        value_size: int = 48,
        line_spacing: float = 0.5,
        bucket_spacing: float = 0.85,
        hashmap: Optional[List[Tuple[str, int]]] = None,
        element_color: str = WHITE,
        bucket_color: str = GRAY_C,
    ):
        """
        Initializes the Hashmap object with optional parameters.

        Parameters
        ----------
        `num_buckets` : int
            Number of buckets in the hashmap. Defaults to 5.
        `element_size` : int
            Font size for hashmap elements. Defaults to 60.
        `key_size` : int
            Font size for keys. Defaults to 48.
        `value_size` : int
            Font size for values. Defaults to 48.
        `line_spacing` : float, optional
            Spacing between elements in a bucket. Defaults to 0.5.
        `bucket_spacing` : float, optional
            Spacing between buckets. Defaults to 0.85.
        `hashmap` : Optional[List[Tuple[str, int]]], optional
            Custom hashmap elements. If None, an empty hashmap will be created.
        `element_color` : str
            Color for the elements text. Defaults to WHITE.
        `bucket_color` : str
            Color for the bucket text. Defaults to GRAY_C.
        """
        self.num_buckets = num_buckets
        self.element_size = element_size
        self.key_size = key_size
        self.value_size = value_size
        self.line_spacing = line_spacing
        self.bucket_spacing = bucket_spacing
        self.hashmap = hashmap or []
        self.element_color = element_color
        self.bucket_color = bucket_color
