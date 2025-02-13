class Category:
    def __init__(self, category_id, name, description):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.subcategories = []


class Subcategory:
    def __init__(self, subcategory_id, category, name):
        self.subcategory_id = subcategory_id
        self.category = category
        self.name = name
        self.courses = []


class Course:
    def __init__(self, course_id, subcategory, title, description, duration_weeks, is_online):
        self.course_id = course_id
        self.subcategory = subcategory
        self.title = title
        self.description = description
        self.duration_weeks = duration_weeks
        self.is_online = is_online
        self.modules = []
        self.training_periods = []
        self.course_requirements = []


class Module:
    def __init__(self, module_id, course, name, duration_hours, course_part):
        self.module_id = module_id
        self.course = course
        self.name = name
        self.duration_hours = duration_hours
        self.course_part = course_part


class TrainingPeriod:
    def __init__(self, period_id, course, location, start_date, end_date, schedule_type, price, max_participants):
        self.period_id = period_id
        self.course = course
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.schedule_type = schedule_type
        self.price = price
        self.max_participants = max_participants
        self.enrollments = []


class User:
    def __init__(self, user_id, role, public_info, private_info, registration_date):
        self.user_id = user_id
        self.role = role
        self.public_info = public_info
        self.private_info = private_info
        self.registration_date = registration_date
        self.enrollments = []


class Role:
    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name
        self.users = []


class Enrollment:
    def __init__(self, enrollment_id, user, training_period, enrollment_date, payment_status):
        self.enrollment_id = enrollment_id
        self.user = user
        self.training_period = training_period
        self.enrollment_date = enrollment_date
        self.payment_status = payment_status
        self.attendance_records = []


class Attendance:
    def __init__(self, attendance_id, enrollment, module, date, status, notes):
        self.attendance_id = attendance_id
        self.enrollment = enrollment
        self.module = module
        self.date = date
        self.status = status
        self.notes = notes


class CourseRequirement:
    def __init__(self, requirement_id, course, description):
        self.requirement_id = requirement_id
        self.course = course
        self.description = description
