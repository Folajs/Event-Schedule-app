from celery import shared_task
import time

@shared_task
def notify_event_created(title, location):
    # Simulate a notification or log
    print(f"[Celery] New Event Created: {title} at {location}")
    time.sleep(2)
    return f"Notification for event '{title}' sent."
