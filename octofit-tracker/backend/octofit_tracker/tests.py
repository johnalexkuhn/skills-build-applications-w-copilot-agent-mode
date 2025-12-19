from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(email='batman@dc.com', username='batman', team=team)
        self.assertEqual(str(user), 'batman')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(email='ironman@marvel.com', username='ironman', team=team)
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2025-12-19')
        self.assertEqual(str(activity), 'ironman - run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, week=1)
        self.assertEqual(str(leaderboard), 'Marvel - Week 1')
