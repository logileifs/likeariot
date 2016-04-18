from mezzanine.conf import register_setting

register_setting(
    name="AUTHORS_BOOKS_PER_PAGE",
    label="Authors books per page",
    description="The number of books to show per author page.",
    editable=True,
    default=10,
)