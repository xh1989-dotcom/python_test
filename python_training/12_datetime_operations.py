"""
Python Training - File 12: Date and Time Operations

This file covers:
- Working with datetime module
- Date and time formatting
- Timezone handling
- Date arithmetic
- Parsing and formatting dates
- Practical examples
"""

from datetime import datetime, date, time, timedelta
import time as time_module  # Avoid naming conflicts
import calendar

# Current date and time
print("Current date and time:")
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Current date: {date.today()}")
print(f"Current time: {datetime.now().time()}")

# Creating specific dates and times
print(f"\nCreating specific dates:")
specific_date = date(2023, 12, 25)
specific_time = time(14, 30, 45)
specific_datetime = datetime(2023, 12, 25, 14, 30, 45)

print(f"Specific date: {specific_date}")
print(f"Specific time: {specific_time}")
print(f"Specific datetime: {specific_datetime}")

# Accessing date and time components
print(f"\nAccessing components:")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print(f"Weekday: {now.weekday()} (Monday is 0)")
print(f"Iso weekday: {now.isoweekday()} (Monday is 1)")

# Formatting dates and times
print(f"\nFormatting examples:")
print(f"Default: {now}")
print(f"Format 1: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Format 2: {now.strftime('%B %d, %Y')}")
print(f"Format 3: {now.strftime('%A, %B %d, %Y at %I:%M %p')}")
print(f"Format 4: {now.strftime('%Y-%m-%d')}")

# Parsing dates from strings
print(f"\nParsing dates from strings:")
date_string = "2023-11-20"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d").date()
print(f"Parsed date: {parsed_date}")

datetime_string = "2023/12/25 14:30:45"
parsed_datetime = datetime.strptime(datetime_string, "%Y/%m/%d %H:%M:%S")
print(f"Parsed datetime: {parsed_datetime}")

# Time arithmetic with timedelta
print(f"\nTime arithmetic:")
future_date = now + timedelta(days=30)
past_date = now - timedelta(weeks=2)
next_hour = now + timedelta(hours=1)
last_month = now - timedelta(days=30)

print(f"Current time: {now}")
print(f"30 days from now: {future_date}")
print(f"2 weeks ago: {past_date}")
print(f"Next hour: {next_hour}")
print(f"Approximately last month: {last_month}")

# Calculating differences between dates
print(f"\nDate differences:")
birth_date = date(1990, 5, 15)
today = date.today()
age = today - birth_date
print(f"Birth date: {birth_date}")
print(f"Today: {today}")
print(f"Age in days: {age.days}")
print(f"Age in years: {age.days // 365}")

# Working with time
print(f"\nWorking with time module:")
print(f"Unix timestamp: {time_module.time()}")
print(f"Sleeping for 1 second...")
time_module.sleep(1)
print(f"Current time after sleep: {time_module.time()}")

# Creating a timestamp
timestamp = datetime.now().timestamp()
print(f"Current timestamp: {timestamp}")
print(f"From timestamp: {datetime.fromtimestamp(timestamp)}")

# Working with calendar
print(f"\nCalendar operations:")
print(f"Is 2024 a leap year? {calendar.isleap(2024)}")
print(f"Days in February 2024: {calendar.monthrange(2024, 2)[1]}")
print(f"Current month calendar:")
print(calendar.month(now.year, now.month))

# Timezone-naive vs timezone-aware operations
print(f"\nTimezone operations (naive):")
naive_datetime = datetime(2023, 12, 25, 15, 30, 0)
print(f"Naive datetime: {naive_datetime}")

# Using timedelta for more complex operations
print(f"\nComplex time operations:")
work_start = time(9, 0, 0)
work_end = time(17, 0, 0)
print(f"Work hours: {work_start.strftime('%H:%M')} to {work_end.strftime('%H:%M')}")

# Duration calculation
lunch_break = timedelta(hours=1)
work_duration = timedelta(hours=work_end.hour - work_start.hour) - lunch_break
print(f"Net work duration: {work_duration}")

# Date iteration example
print(f"\nIterating through dates:")
start_date = date.today()
dates = []
for i in range(5):
    dates.append(start_date + timedelta(days=i))
print(f"Next 5 days: {dates}")

# Practical example: Countdown timer
def countdown_timer(seconds):
    """Simple countdown timer"""
    print(f"Countdown: {seconds} seconds")
    for i in range(seconds, 0, -1):
        print(f"\rTime remaining: {i} seconds", end="", flush=True)
        time_module.sleep(1)
    print("\nTime's up!")

# Uncomment to run countdown (but we'll skip it to avoid blocking)
# countdown_timer(3)

# Practical example: Schedule management
class Schedule:
    def __init__(self):
        self.events = []
    
    def add_event(self, name, event_datetime):
        self.events.append({"name": name, "datetime": event_datetime})
    
    def get_upcoming_events(self, days_ahead=7):
        now = datetime.now()
        future_date = now + timedelta(days=days_ahead)
        upcoming = []
        
        for event in self.events:
            if now <= event["datetime"] <= future_date:
                upcoming.append(event)
        
        return sorted(upcoming, key=lambda x: x["datetime"])
    
    def time_until_event(self, event_name):
        for event in self.events:
            if event["name"] == event_name:
                time_diff = event["datetime"] - datetime.now()
                return time_diff
        return None

# Using the schedule class
schedule = Schedule()
schedule.add_event("Team Meeting", datetime.now() + timedelta(days=2, hours=3))
schedule.add_event("Project Deadline", datetime.now() + timedelta(days=5))
schedule.add_event("Birthday Party", datetime.now() + timedelta(days=1, hours=18))

print(f"\nUpcoming events:")
for event in schedule.get_upcoming_events():
    print(f"  {event['name']}: {event['datetime'].strftime('%Y-%m-%d %H:%M')}")

# Practical example: Date validation
def is_valid_date(year, month, day):
    """Validate if a date is valid"""
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

print(f"\nDate validation:")
test_dates = [
    (2023, 2, 29),  # Invalid - not a leap year
    (2024, 2, 29),  # Valid - leap year
    (2023, 4, 31),  # Invalid - April has 30 days
    (2023, 12, 25)  # Valid
]

for year, month, day in test_dates:
    valid = is_valid_date(year, month, day)
    print(f"Date {year}-{month:02d}-{day:02d} is {'valid' if valid else 'invalid'}")

# Working with business days (excluding weekends)
def add_business_days(start_date, business_days):
    """Add business days (excluding weekends) to a date"""
    current_date = start_date
    days_added = 0
    
    while days_added < business_days:
        current_date += timedelta(days=1)
        # Monday is 0, Sunday is 6, so 5 and 6 are weekend days
        if current_date.weekday() < 5:  # Monday to Friday
            days_added += 1
    
    return current_date

start_date = date.today()
business_date = add_business_days(start_date, 10)
print(f"\nAdding business days:")
print(f"Start date: {start_date}")
print(f"Date after 10 business days: {business_date}")

# Performance comparison for time operations
import timeit

def time_operation():
    return datetime.now()

# Time the operation
execution_time = timeit.timeit(time_operation, number=1000)
print(f"\nTime to execute datetime.now() 1000 times: {execution_time:.4f} seconds")

print("\nDate and time operations completed!")