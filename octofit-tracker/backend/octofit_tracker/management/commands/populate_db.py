from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name="Marvel")
        dc = Team.objects.create(name="DC")

        # Create Users (Superheroes)
        users = [
            {"username": "Spider-Man", "email": "spiderman@marvel.com", "team": marvel},
            {"username": "Iron Man", "email": "ironman@marvel.com", "team": marvel},
            {"username": "Wonder Woman", "email": "wonderwoman@dc.com", "team": dc},
            {"username": "Batman", "email": "batman@dc.com", "team": dc},
        ]
        user_objs = []
        for u in users:
            user_objs.append(User.objects.create(username=u["username"], email=u["email"], team=u["team"]))

        # Create Activities
        Activity.objects.create(user=user_objs[0], activity_type="Running", duration=30, date="2025-12-19")
        Activity.objects.create(user=user_objs[1], activity_type="Cycling", duration=45, date="2025-12-18")
        Activity.objects.create(user=user_objs[2], activity_type="Swimming", duration=60, date="2025-12-17")
        Activity.objects.create(user=user_objs[3], activity_type="Yoga", duration=40, date="2025-12-16")

        # Create Workouts
        w1 = Workout.objects.create(name="Morning Run", description="5km run in the park")
        w2 = Workout.objects.create(name="HIIT Session", description="High intensity interval training")
        w3 = Workout.objects.create(name="Swim Laps", description="20 laps freestyle")
        w4 = Workout.objects.create(name="Evening Yoga", description="Relaxing yoga routine")
        w1.suggested_for.set([user_objs[0]])
        w2.suggested_for.set([user_objs[1]])
        w3.suggested_for.set([user_objs[2]])
        w4.suggested_for.set([user_objs[3]])

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=1900, week=1)
        Leaderboard.objects.create(team=dc, total_points=2050, week=1)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
