from dao.swipe_dao import swipe_dao
from dao.match_dao import match_dao

class SwipeService:

    @staticmethod
    def process_swipe(swiper_id, swiped_id, swipe_type):
        swipe = swipe_dao.create_swipe(
            swiper_id=swiper_id,
            swiped_id=swiped_id,
            swipe_type=swipe_type
        )

        match = None
        if swipe_type == "like":
            match = match_dao.create_if_mutual_like(swiper_id, swiped_id)

        return {
            "swipe": swipe,
            "match": match
        }