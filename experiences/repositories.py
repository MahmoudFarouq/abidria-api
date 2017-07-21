from abidria.entities import Picture
from .models import ORMExperience
from .entities import Experience


class ExperienceRepo(object):

    def _decode_db_experience(self, db_experience):
        if not db_experience.picture:
            picture = None
        else:
            picture = Picture(small=db_experience.picture.small.url,
                              medium=db_experience.picture.medium.url,
                              large=db_experience.picture.large.url)

        return Experience(id=db_experience.id,
                          title=db_experience.title,
                          description=db_experience.description,
                          picture=picture)

    def get_all_experiences(self):
        db_experiences = ORMExperience.objects.all()
        experiences = []
        for db_experience in db_experiences:
            experiences.append(self._decode_db_experience(db_experience))
        return experiences
