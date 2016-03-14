__author__ = 'tpl'
import College
import Course

class Parent(object):
    def __init__(self, name, gender, college, course):
        self.name = name
        self.gender = gender
        self.college = college
        self.course = course
    def set_spouse_preference(self,gender,course,college):
        self.spouse_preference = SpousePreference(gender,course,college)
        self.spouse_preference.myself = self
    def set_child_preference(self, course, college):
        self.child_preference = ChildPreference(course, college)
        self.child_preference.myself = self
        pass
    def generate_spouse_ranks(self,parent_list):
        spouses = parent_list[:] # shallow copy
        spouses.remove(self)
        self.spouse_ranks = sorted(spouses, key=lambda p: self.spouse_preference.evaluate(p), reverse=True)
        return self.spouse_ranks

class SpousePreference(object):
    def __init__(self, gender='Random', course='Close', college = 'Close'):
        self.gender_preference = gender
        self.course_preference = course
        self.college_preference = college
        self.myself = None # to be assigned after creation
    def evaluate(self, parent):
        points = 0
        points = points + self._evaluate_gender(parent)
        # print( "Gender points" , self._evaluate_gender(parent),"to", parent.name)
        points = points + self._evaluate_course(parent)
        # print( "Course points" , self._evaluate_course(parent),"to", parent.name)
        points = points + self._evaluate_college(parent)
        # print( "College points" , self._evaluate_college(parent),"to", parent.name)
        return points
    def _evaluate_gender(self,parent):
        """
        If Random: 10 points (average)
        if Opposite: 20 points | 0 points
        if Same: 20 points | 0 points
        :param parent:
        :return:
        """
        if self.gender_preference == 'Random':
            return 10
        if self.gender_preference == 'Opposite':
            if self.myself.gender != parent.gender:
                return 20
            else:
                return 0
        if self.gender_preference == 'Same':
            if self.myself.gender == parent.gender:
                return 20
            else:
                return 0

    def _evaluate_college(self,parent):
        if self.college_preference == 'Different':
            return 10
        if self.college_preference == 'Same':
            if self.myself.college == parent.college:
                return 30
            else:
                return 0
        if self.college_preference == 'Close':
            """
            same college : 30 points
            colleges at threshold distance: 0 points
            colleges further than threshold distance : neg points
            """
            distance = College.distance2D(College.COORDINATES [self.myself.college],College.COORDINATES [parent.college])
            threshold = College.GIRTONTOHOMERTON / 4.0
            return (threshold - distance)/threshold * 30

    def _evaluate_course(self,parent):
        if self.course_preference == 'Different':
            return Course.AVERAGE/Course.MAX * 30
        if self.course_preference == 'Same':
            if self.myself.course == parent.course:
                return 30
            else:
                return 0
        if self.course_preference == 'Close':
            """
            Maximally Different Subject = 0
            Same subject = 30
            """
            distance = Course.distance3D(Course.C_COORDINATES[self.myself.course],Course.C_COORDINATES[parent.course])
            return abs(distance - Course.MAX)/Course.MAX * 30

class ChildPreference(object):
    def __init__(self, course='Close', college = 'Close'):
        self.course_preference = course
        self.college_preference = college
        self.myself = None # to be assigned after creation
    def evaluate(self, parent):
        points = 0
        points = points + self._evaluate_course(parent)
        # print( "Course points" , self._evaluate_course(parent),"to", parent.name)
        points = points + self._evaluate_college(parent)
        # print( "College points" , self._evaluate_college(parent),"to", parent.name)
        return points

    def _evaluate_college(self,child):
        if self.college_preference == 'Different':
            return 10
        if self.college_preference == 'Same':
            if self.myself.college == child.college:
                return 30
            else:
                return 0
        if self.college_preference == 'Close':
            """
            same college : 30 points
            colleges at threshold distance: 0 points
            colleges further than threshold distance : neg points
            """
            distance = College.distance2D(College.COORDINATES [self.myself.college],College.COORDINATES [child.college])
            threshold = College.GIRTONTOHOMERTON / 4.0
            return (threshold - distance)/threshold * 30

    def _evaluate_course(self,child):
        if self.course_preference == 'Different':
            return Course.AVERAGE/Course.MAX * 30
        if self.course_preference == 'Same':
            if self.myself.course == child.course:
                return 30
            else:
                return 0
        if self.course_preference == 'Close':
            """
            Maximally Different Subject = 0
            Same subject = 30
            """
            A = Course.C_COORDINATES[self.myself.course]
            Z = Course.C_COORDINATES
            B = Course.C_COORDINATES[child.course]
            distance = Course.distance3D(A,B)
            return abs(distance - Course.MAX)/Course.MAX * 30

class Couple(object):
    def __init__(self,par1, par2):
        self.par1 = par1
        self.par2 = par2
        self.name = par1.name + par2.name

    def _evaluate(self,child):
        points = 0
        points = points + self.par1.child_preference.evaluate(child)
        points = points + self.par2.child_preference.evaluate(child)
        return points

    def generate_child_ranks(self,child_list):
        children = child_list[:] # shallow copy
        self.child_ranks = sorted(children, key=lambda c: self._evaluate(c), reverse=True)
        return self.child_ranks