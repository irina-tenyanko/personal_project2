class Place:
    def __init__(
        self,
        name,
        country,
        description,
        image_url,
        visited=False,
    ):
        self.name = name
        self.country = country
        self.description = description
        self.image_url = image_url
        self.visited = visited

    def get_status(self):
        if self.visited:
            return "Вже відвідано"

        return "Хочу відвідати"

    def get_status_class(self):
        if self.visited:
            return "visited"

        return "planned"

    def get_description(self):
        return f"{self.name}, {self.country}: {self.description}"

    def to_html(self):
        return f"""
        <article class="place-card">
            <img
                class="place-image"
                src="{self.image_url}"
                alt="{self.name}"
            >

            <div class="place-content">
                <p class="country">{self.country}</p>
                <h2>{self.name}</h2>
                <p class="description">{self.description}</p>
                <span class="status {self.get_status_class()}">
                    {self.get_status()}
                </span>
            </div>
        </article>
        """